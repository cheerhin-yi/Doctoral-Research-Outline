"""BTD4 frozen paired real inference and synchronized complete-pipeline timing."""
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import time
import traceback
import zipfile
import numpy as np
from diagnose_bt1 import BASE, RUNS, WEIGHT_SHA, sha, dump, nms, axis_windows, prepare_gt, match_gt
from compare_dedup_density import choose
from analyze_density_residuals import inside, write_csv


def main():
    out=BASE/'BTD4-DIAG500-20260913-01';out.mkdir(exist_ok=False)
    (out/'framework_config').mkdir()
    os.environ['YOLO_CONFIG_DIR']=str(out/'framework_config');os.environ['YOLO_AUTOINSTALL']='false'
    dump(out/'status.json',dict(status='RUNNING',phase='identity',completed_images=0))
    started=time.monotonic()
    try:
        import torch
        import cv2
        import ultralytics
        from ultralytics import YOLO
        assert torch.cuda.is_available() and ultralytics.__version__=='8.4.90'
        torch.manual_seed(0);np.random.seed(0)
        weight=BASE/RUNS[-1]/'train/weights/last.pt';assert sha(weight)==WEIGHT_SHA
        archive=BASE.parents[2]/'raw/VisDrone/VisDrone2019-DET-val.zip'
        expected=json.loads((BASE/'full_data_v2/preparation.json').read_text())['source_sha256']['val']
        assert sha(archive)==expected
        z=zipfile.ZipFile(archive)
        images={Path(n).name:n for n in z.namelist() if n.lower().endswith('.jpg')}
        annotations={Path(n).name:n for n in z.namelist() if '/annotations/' in n and n.endswith('.txt')}
        assert len(images)==548 and len(images)==sum(n.lower().endswith('.jpg') for n in z.namelist())
        ordered=sorted(images,key=lambda n:(hashlib.sha256(('diag-v1:'+n).encode()).hexdigest(),n))
        cal=ordered[:48];diag=ordered[48:]
        assert diag==(BASE/'full_data_v2/diag500_names.txt').read_text().splitlines()
        assert cal==[Path(n).name for n in (BASE/'full_data_v2/cal48.txt').read_text().splitlines()]
        dump(out/'data_identity.json',dict(val_sha256=expected,cal48=cal,diag500=diag,source=str(archive)))
        model=YOLO(str(weight)); assert len(model.names)==10
        dump(out/'environment.json',dict(torch=torch.__version__,ultralytics=ultralytics.__version__,gpu=torch.cuda.get_device_name(0),
             numpy=np.__version__,opencv=cv2.__version__,torch_threads=torch.get_num_threads(),names=model.names,
             weight_sha256=WEIGHT_SHA,script_sha256=sha(__file__),protocol_sha256=sha(Path(__file__).with_name('BTD4_Diag500_Protocol.md'))))
        for name in ['run_diag500_pair.py','diagnose_bt1.py','compare_dedup_density.py','analyze_density_residuals.py','BTD4_Diag500_Protocol.md']:
            shutil.copy2(Path(__file__).with_name(name),out/name)
        def guard():
            if time.monotonic()-started>7200 or shutil.disk_usage(out).free<5*(1<<30):raise RuntimeError('Resource/time guard')
        def read_image(name):
            t=time.perf_counter();payload=z.read(images[name])
            bgr=cv2.imdecode(np.frombuffer(payload,np.uint8),cv2.IMREAD_COLOR)
            assert bgr is not None
            rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
            return rgb,1000*(time.perf_counter()-t),hashlib.sha256(payload).hexdigest()
        def infer(im,size=640):
            r=model.predict(im,imgsz=size,rect=False,device=0,batch=1,conf=.001,iou=.5,max_det=1000,save=False,verbose=False)[0]
            pred=r.boxes.data.detach().cpu().numpy().astype(float)
            assert np.isfinite(pred).all()
            return pred
        def pipeline(rgb,method):
            guard();torch.cuda.synchronize();t0=time.perf_counter()
            im=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR);h,w=im.shape[:2]
            windows=[(x,y,min(w,x+640),min(h,y+640)) for y in axis_windows(h) for x in axis_windows(w)]
            t1=time.perf_counter()
            full=nms(infer(im,1280 if method=='F1280' else 640))
            t2=time.perf_counter()
            if method=='F1280':selected=[]
            elif len(windows)==1:selected=[0]
            elif method=='dedup':selected,_=choose(full,windows)
            else:
                coarse=full[full[:,4]>=.25];centers=(coarse[:,:2]+coarse[:,2:4])/2
                scores=[sum(inside(p,b) for p in centers) for b in windows]
                selected=[int(j) for j in np.argsort(-np.array(scores),kind='stable')[:2]]
            t3=time.perf_counter();local=[]
            for j in selected:
                x,y,x2,y2=windows[j];patch=np.full((640,640,3),114,dtype=np.uint8)
                patch[:y2-y,:x2-x]=im[y:y2,x:x2]
                p=infer(patch);centers=(p[:,:2]+p[:,2:4])/2
                p=p[(centers[:,0]<x2-x)&(centers[:,1]<y2-y)].copy()
                p[:,[0,2]]=np.clip(p[:,[0,2]],0,x2-x)+x;p[:,[1,3]]=np.clip(p[:,[1,3]],0,y2-y)+y
                p=p[(p[:,2]>p[:,0])&(p[:,3]>p[:,1])];local.append(p)
            t4=time.perf_counter();result=nms(np.concatenate([full]+local)) if local else full
            torch.cuda.synchronize();t5=time.perf_counter()
            timings=dict(convert_windows_ms=(t1-t0)*1000,global_ms=(t2-t1)*1000,selection_ms=(t3-t2)*1000,
                         local_crop_detect_map_ms=(t4-t3)*1000,merge_ms=(t5-t4)*1000,total_ms=(t5-t0)*1000)
            assert np.isfinite(result).all() and len(result)<=500
            return result,selected,timings,full
        for name in cal[:10]:
            rgb,_,_=read_image(name)
            for m in ['density','dedup','F1280']:pipeline(rgb,m)
        assert next(model.model.parameters()).dtype==torch.float32
        rgb,_,_=read_image(cal[0])
        for m in ['density','dedup','F1280']:
            for _ in range(20):pipeline(rgb,m)
        print('Identity and cal10 precheck PASS; warmup completed',flush=True)
        cal_times=[]
        for i,name in enumerate(cal):
            rgb,dec,_=read_image(name)
            for rep in range(3):
                methods=['density','dedup'] if (i+rep)%2==0 else ['dedup','density']
                for m in methods+['F1280']:
                    _,sel,t,_=pipeline(rgb,m);cal_times.append(dict(image=name,repeat=rep,method=m,selected=sel,decode_ms=dec,**t))
        write_csv(out/'calibration_times.csv',cal_times)
        ref=[np.median([r['total_ms'] for r in cal_times if r['image']==n and r['method']=='F1280']) for n in cal]
        budget=math.ceil(float(np.percentile(ref,95)));dump(out/'budget.json',dict(T_ms=budget,source='ceil p95 of cal48 F1280 per-image median, relative reference only'))
        print(f'Calibration complete; frozen reference T={budget} ms',flush=True)
        times=[];records=[];changed=[];repeat_mismatches=0
        counts_by_class={c:dict(small_gt=0,density_small_tp=0,dedup_small_tp=0) for c in range(1,11)}
        for i,name in enumerate(diag):
            rgb,dec,image_sha=read_image(name);h,w=rgb.shape[:2];first={}
            for rep in range(3):
                methods=['density','dedup'] if (i+rep)%2==0 else ['dedup','density']
                for m in methods:
                    pred,sel,t,full=pipeline(rgb,m)
                    times.append(dict(image=name,repeat=rep,method=m,selected=sel,decode_ms=dec,**t))
                    if rep==0:first[m]=(pred,sel,full)
                    else:
                        prev=first[m]
                        stable=sel==prev[1] and pred.shape==prev[0].shape and np.allclose(pred,prev[0],atol=1e-5,rtol=0)
                        repeat_mismatches+=not stable
            payload=z.read(annotations[Path(name).with_suffix('.txt').name])
            raw=np.array([[float(v) for v in s.rstrip(',').split(',')] for s in payload.decode('utf-8-sig').splitlines() if s.strip()])
            gt,ids,integral=prepare_gt(raw,h,w);valid=set(int(ids[j]) for j,g in enumerate(gt) if g[4]>0)
            small=set(int(ids[j]) for j,g in enumerate(gt) if g[4]>0 and 0<g[2]*g[3]<1024)
            matches={};metrics={}
            for m in ['density','dedup']:
                matched,fp,ig=match_gt(gt,ids,first[m][0],integral,h,w);matches[m]=matched
                metrics[m]=dict(tp=len(matched),fp=fp,ignored=ig,small_tp=len(matched&small))
            for gid in small:
                c=int(raw[gid,5]);counts_by_class[c]['small_gt']+=1
                for m in ['density','dedup']:counts_by_class[c][m+'_small_tp']+=gid in matches[m]
                if (gid in matches['density'])!=(gid in matches['dedup']):
                    changed.append(dict(image=name,gt_row=gid,category=c,box=raw[gid,:4].tolist(),change='gain' if gid in matches['dedup'] else 'loss'))
            record=dict(image=name,image_sha256=image_sha,annotation_sha256=hashlib.sha256(payload).hexdigest(),
               width=w,height=h,small_gt=len(small),valid_gt=len(valid),metrics=metrics,
               selected={m:first[m][1] for m in first},
               gained_small=len((matches['dedup']-matches['density'])&small),lost_small=len((matches['density']-matches['dedup'])&small))
            dump(out/f'image_{i:03d}.json',record)
            np.savez_compressed(out/f'predictions_{i:03d}.npz',density=first['density'][0],dedup=first['dedup'][0])
            records.append(record)
            if (i+1)%25==0:
                write_csv(out/'timings_partial.csv',times)
                dump(out/'status.json',dict(status='RUNNING',phase='diag500',completed_images=i+1,elapsed_seconds=time.monotonic()-started))
                print(f'{i+1}/500 complete, elapsed {time.monotonic()-started:.1f}s',flush=True)
        assert len(records)==500 and len(times)==3000
        write_csv(out/'timings.csv',times);write_csv(out/'changed_small_gt.csv',changed)
        totals={m:{k:sum(r['metrics'][m][k] for r in records) for k in ['tp','fp','ignored','small_tp']} for m in ['density','dedup']}
        small_n=sum(r['small_gt'] for r in records);valid_n=sum(r['valid_gt'] for r in records)
        for m,t in totals.items():t.update(small_recall=t['small_tp']/small_n,recall=t['tp']/valid_n,precision=t['tp']/(t['tp']+t['fp']))
        delta=np.array([r['metrics']['dedup']['small_tp']-r['metrics']['density']['small_tp'] for r in records])
        rng=np.random.default_rng(20260913);resample=rng.integers(0,500,(10000,500));den=np.array([r['small_gt'] for r in records])
        ratios=100*delta[resample].sum(1)/den[resample].sum(1)
        timing={}
        for m in ['density','dedup']:
            ts=[r for r in times if r['method']==m];all_ms=np.array([r['total_ms'] for r in ts])
            med=np.array([np.median([r['total_ms'] for r in ts if r['image']==n]) for n in diag])
            timing[m]=dict(frames=len(ts),mean_ms=float(all_ms.mean()),median_ms=float(np.median(all_ms)),p95_ms=float(np.percentile(all_ms,95)),
               per_image_median_mean_ms=float(med.mean()),per_image_median_p95_ms=float(np.percentile(med,95)),
               all_frames_over_T_fraction=float(np.mean(all_ms>budget)),image_medians_over_T_fraction=float(np.mean(med>budget)),
               stage_means_ms={k:float(np.mean([r[k] for r in ts])) for k in ['convert_windows_ms','global_ms','selection_ms','local_crop_detect_map_ms','merge_ms']})
        gained=sum(r['gained_small'] for r in records);lost=sum(r['lost_small'] for r in records)
        assert gained-lost==delta.sum()
        summary=dict(status='PASS',images=500,small_gt=small_n,valid_gt=valid_n,metrics=totals,gained_small=gained,lost_small=lost,
            delta_small_recall_pp=float(delta.sum()*100/small_n),relative_small_recall_change_pct=float(delta.sum()*100/totals['density']['small_tp']),
            image_win_tie_loss=[int(sum(delta>0)),int(sum(delta==0)),int(sum(delta<0))],
            exploratory_image_bootstrap_95_percentile_pp=np.percentile(ratios,[2.5,97.5]).tolist(),
            changed_selection_images=sum(r['selected']['density']!=r['selected']['dedup'] for r in records),classes=counts_by_class,
            timing=timing,T_ms=budget,repeat_output_mismatches=repeat_mismatches,elapsed_seconds=time.monotonic()-started)
        dump(out/'summary.json',summary)
        dump(out/'status.json',dict(status='PASS',completed_images=500,actual_timing_calls=3000,training_calls=0,elapsed_seconds=time.monotonic()-started))
        print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED',elapsed_seconds=time.monotonic()-started));raise


if __name__=='__main__':main()
