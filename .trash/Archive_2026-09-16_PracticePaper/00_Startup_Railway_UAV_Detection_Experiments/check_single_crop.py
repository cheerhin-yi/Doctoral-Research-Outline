"""BTD8 cache upper bound and actual K1 timing; phases never silently restart."""
import argparse
import json
import os
from pathlib import Path
import shutil
import time
import traceback
import numpy as np
import psutil
from diagnose_bt1 import BASE, RUNS, WEIGHT_SHA, sha, dump, nms, axis_windows, prepare_gt, match_gt
from analyze_density_residuals import inside, write_csv

OUT=BASE/'BTD8-SINGLE-20260914-01'
SRC=BASE/'BTD1-CAL48-20260913-01'


def save(path,value):
    def convert(v):
        if isinstance(v,np.generic):return v.item()
        if isinstance(v,dict):return {k:convert(x) for k,x in v.items()}
        if isinstance(v,(list,tuple)):return [convert(x) for x in v]
        return v
    dump(path,convert(value))


def guard(started,phase):
    mem=psutil.Process().memory_info();vm=psutil.virtual_memory()
    r=dict(phase=phase,elapsed_seconds=time.monotonic()-started,rss=mem.rss,private=mem.private,available=vm.available)
    with (OUT/'resources.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(r)+'\n')
    if r['elapsed_seconds']>900 or mem.rss>3*(1<<30) or mem.private>4*(1<<30) or vm.available<256*(1<<20) or shutil.disk_usage(OUT).free<5*(1<<30):raise RuntimeError('Resource guard')


def output_guard():
    if sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())>256*(1<<20):raise RuntimeError('Output size guard')


def cache_phase():
    OUT.mkdir(exist_ok=False);started=time.monotonic()
    save(OUT/'status.json',dict(status='RUNNING',phase='cache',training_calls=0,inference_calls=0))
    hashes={}
    for name,info in json.loads((SRC/'diagnostic_manifest.json').read_text()).items():
        if name.startswith(('image_','predictions_')) or name=='summary.json':
            hashes[str(SRC/name)]=sha(SRC/name);assert hashes[str(SRC/name)]==info['sha256']
    prev=BASE/'BTD7-RESIDUAL-20260914-02'
    frames=[];windows=[];classes={c:dict(small_gt=0,density_tp=0,oracle_tp=0) for c in range(1,11)}
    for name in ['check_single_crop.py','diagnose_bt1.py','fast_stable_nms.py','analyze_density_residuals.py','BTD8_Single_Crop_Protocol.md']:
        shutil.copy2(Path(__file__).with_name(name),OUT/name)
    records=[json.loads(p.read_text()) for p in sorted(SRC.glob('image_*.json'))]
    names=[Path(s).name for s in (BASE/'full_data_v2/cal48.txt').read_text().splitlines()]
    assert [r['image'] for r in records]==names and len(names)==48
    for i,r in enumerate(records):
        guard(started,'cache')
        ip=BASE/'full_data_v2/images/cal48'/r['image'];ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt')
        for path,key in [(ip,'image_sha256'),(ann,'annotation_sha256')]:
            hashes[str(path)]=sha(path);assert hashes[str(path)]==r[key]
        with np.load(SRC/f'predictions_{i:02d}.npz') as d:full=d['F640'];local=[d[f'local_{j}'] for j in range(len(r['windows']))]
        raw=np.array([[float(v) for v in line.rstrip(',').split(',')] for line in ann.read_text().splitlines() if line.strip()])
        gt,ids,integral=prepare_gt(raw,r['height'],r['width'])
        def match(pred):return match_gt(gt,ids,pred,integral,r['height'],r['width'])
        small={x['id'] for x in r['small_gt_details']};rec={x['id'] for x in r['small_gt_details'] if x['recoverable']}
        first=r['selected']['density'][0];matches={};preds={};fps={}
        for j,a in enumerate(local):preds[j]=nms(np.concatenate([full,a]));matches[j],fps[j],_=match(preds[j])
        prior=prev/f'frame_{i:02d}.json';hashes[str(prior)]=sha(prior);pf=json.loads(prior.read_text())
        assert first==pf['frame']['first'] and matches[first]==set(pf['first_match_ids']) and fps[first]==pf['frame']['first_fp']
        best=min(matches,key=lambda j:(-len(matches[j]&small),j));fullmatch,fullfp,_=match(full)
        for j in matches:
            windows.append(dict(image=r['image'],window=j,box=r['windows'][j],density_selected=j==first,gt_best=j==best,
                small_tp=len(matches[j]&small),fp=fps[j],recovered=len(matches[j]&rec),
                gained_ids=sorted((matches[j]-matches[first])&small),lost_ids=sorted((matches[first]-matches[j])&small)))
        for detail in r['small_gt_details']:
            cc=classes[detail['category']];cc['small_gt']+=1;cc['density_tp']+=detail['id'] in matches[first];cc['oracle_tp']+=detail['id'] in matches[best]
        row=dict(image=r['image'],small_gt=len(small),first=first,best=best,full_small_tp=len(fullmatch&small),
            density_small_tp=len(matches[first]&small),oracle_small_tp=len(matches[best]&small),density_fp=fps[first],oracle_fp=fps[best],
            density_recovered=len(matches[first]&rec),oracle_recovered=len(matches[best]&rec),
            gained=len((matches[best]-matches[first])&small),lost=len((matches[first]-matches[best])&small),
            full_gain=len((matches[first]-fullmatch)&small),full_loss=len((fullmatch-matches[first])&small),
            stop_oracle_small_tp=max(len(fullmatch&small),len(matches[best]&small)))
        frames.append(row);save(OUT/f'cache_{i:02d}.json',dict(frame=row,match_ids={str(j):sorted(v) for j,v in matches.items()}))
        np.save(OUT/f'expected_k1_{i:02d}.npy',preds[first]);output_guard()
    fields=['small_gt','full_small_tp','density_small_tp','oracle_small_tp','density_fp','oracle_fp','density_recovered','oracle_recovered','gained','lost','full_gain','full_loss','stop_oracle_small_tp']
    totals={k:sum(r[k] for r in frames) for k in fields}
    assert totals['small_gt']==2720 and totals['density_small_tp']==1172 and totals['density_fp']==1051
    assert totals['gained']-totals['lost']==totals['oracle_small_tp']-1172
    assert all(sha(p)==h for p,h in hashes.items())
    write_csv(OUT/'all_240_single_windows.csv',windows);write_csv(OUT/'all_48_frames.csv',frames)
    save(OUT/'input_hashes.json',hashes)
    save(OUT/'cache_summary.json',dict(status='PASS',images=48,windows=240,totals=totals,classes=classes,
        better_images=sum(r['oracle_small_tp']>r['density_small_tp'] for r in frames),elapsed_seconds=time.monotonic()-started,model_loaded=False,inference_calls=0))
    save(OUT/'status.json',dict(status='CACHE_PASS',phase='timing_pending',inference_calls=0,training_calls=0))
    print(json.dumps(totals),flush=True)


def timing_phase():
    assert json.loads((OUT/'cache_summary.json').read_text())['status']=='PASS'
    assert not (OUT/'timing_started.json').exists(),'Timing already attempted; inspect saved state first'
    assert sha(__file__)==sha(OUT/'check_single_crop.py')
    for p,h in json.loads((OUT/'input_hashes.json').read_text()).items():assert sha(p)==h
    save(OUT/'timing_started.json',dict(started=True));started=time.monotonic()
    (OUT/'framework_config').mkdir(exist_ok=True);os.environ['YOLO_CONFIG_DIR']=str(OUT/'framework_config');os.environ['YOLO_AUTOINSTALL']='false'
    import torch
    import cv2
    import ultralytics
    from ultralytics import YOLO
    from fast_stable_nms import nms as fast
    weight=BASE/RUNS[-1]/'train/weights/last.pt';assert sha(weight)==WEIGHT_SHA and ultralytics.__version__=='8.4.90' and torch.cuda.is_available()
    model=YOLO(str(weight));torch.manual_seed(0);np.random.seed(0)
    save(OUT/'environment.json',dict(torch=torch.__version__,ultralytics=ultralytics.__version__,gpu=torch.cuda.get_device_name(0),threads=torch.get_num_threads(),weight_sha256=WEIGHT_SHA,script_sha256=sha(__file__)))
    records=[json.loads(p.read_text()) for p in sorted(SRC.glob('image_*.json'))]
    def read(i):
        t=time.perf_counter();im=cv2.imread(str(BASE/'full_data_v2/images/cal48'/records[i]['image']));assert im is not None
        return cv2.cvtColor(im,cv2.COLOR_BGR2RGB),(time.perf_counter()-t)*1000
    def infer(im,size):
        r=model.predict(im,imgsz=size,rect=False,device=0,batch=1,conf=.001,iou=.5,max_det=1000,save=False,verbose=False)[0]
        pred=r.boxes.data.detach().cpu().numpy().astype(float);assert np.isfinite(pred).all();return pred
    def pipeline(rgb,method):
        guard(started,'timing');torch.cuda.synchronize();t0=time.perf_counter()
        im=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR);h,w=im.shape[:2]
        windows=[(x,y,min(w,x+640),min(h,y+640)) for y in axis_windows(h) for x in axis_windows(w)];t1=time.perf_counter()
        full=fast(infer(im,1280 if method=='F1280' else 640));t2=time.perf_counter()
        selected=[]
        if method=='K1':
            coarse=full[full[:,4]>=.25];centers=(coarse[:,:2]+coarse[:,2:4])/2
            scores=[sum(inside(c,b) for c in centers) for b in windows]
            selected=[int(np.argsort(-np.array(scores),kind='stable')[0])]
        t3=time.perf_counter();local=[]
        for j in selected:
            x,y,x2,y2=windows[j];patch=np.full((640,640,3),114,dtype=np.uint8);patch[:y2-y,:x2-x]=im[y:y2,x:x2]
            p=infer(patch,640);centers=(p[:,:2]+p[:,2:4])/2;p=p[(centers[:,0]<x2-x)&(centers[:,1]<y2-y)].copy()
            p[:,[0,2]]=np.clip(p[:,[0,2]],0,x2-x)+x;p[:,[1,3]]=np.clip(p[:,[1,3]],0,y2-y)+y
            local.append(p[(p[:,2]>p[:,0])&(p[:,3]>p[:,1])])
        t4=time.perf_counter();result=fast(np.concatenate([full]+local)) if local else full
        torch.cuda.synchronize();t5=time.perf_counter()
        return result,selected,dict(convert_windows_ms=(t1-t0)*1000,global_ms=(t2-t1)*1000,selection_ms=(t3-t2)*1000,local_ms=(t4-t3)*1000,merge_ms=(t5-t4)*1000,total_ms=(t5-t0)*1000)
    def check(i,pred,sel):
        expected=np.load(OUT/f'expected_k1_{i:02d}.npy')
        ok=sel==[records[i]['selected']['density'][0]] and pred.shape==expected.shape and np.allclose(pred,expected,atol=1e-5,rtol=0)
        if not ok:np.savez_compressed(OUT/'mismatch.npz',actual=pred,expected=expected);raise RuntimeError('K1 cache mismatch')
        return bool(np.array_equal(pred,expected)),float(np.max(np.abs(pred-expected))) if pred.size else 0.
    for i in range(3):
        rgb,_=read(i);p,s,_=pipeline(rgb,'K1');check(i,p,s);pipeline(rgb,'F1280')
    assert next(model.model.parameters()).dtype==torch.float32
    rgb,_=read(0)
    for m in ['K1','F1280']:
        for _ in range(20):pipeline(rgb,m)
    torch.cuda.reset_peak_memory_stats();times=[];exact=0;maxdiff=0.;ref_exact=0
    for i,r in enumerate(records):
        rgb,decode=read(i);ref=None
        for rep in range(3):
            for method in (['K1','F1280'] if (i+rep)%2==0 else ['F1280','K1']):
                p,s,t=pipeline(rgb,method);times.append(dict(image=r['image'],repeat=rep,method=method,selected=s,decode_ms=decode,**t))
                if method=='K1':
                    same,diff=check(i,p,s);exact+=same;maxdiff=max(maxdiff,diff)
                    if rep==0:np.save(OUT/f'actual_k1_{i:02d}.npy',p)
                elif ref is None:ref=p.copy();np.save(OUT/f'reference_F1280_{i:02d}.npy',p)
                else:
                    assert p.shape==ref.shape and np.allclose(p,ref,atol=1e-5,rtol=0),'F1280 repeat mismatch'
                    ref_exact+=int(np.array_equal(p,ref))
        write_csv(OUT/'timings_partial.csv',times);output_guard()
    refmed=[np.median([x['total_ms'] for x in times if x['image']==r['image'] and x['method']=='F1280']) for r in records]
    T=int(np.ceil(np.percentile(refmed,95)));timing={}
    for m in ['K1','F1280']:
        rows=[x for x in times if x['method']==m];a=np.array([x['total_ms'] for x in rows]);med=np.array([np.median([x['total_ms'] for x in rows if x['image']==r['image']]) for r in records])
        timing[m]=dict(frames=len(a),mean_ms=float(a.mean()),median_ms=float(np.median(a)),p95_ms=float(np.percentile(a,95)),over_T_fraction=float(np.mean(a>T)),
            image_median_mean_ms=float(med.mean()),image_median_p95_ms=float(np.percentile(med,95)),image_median_over_T_fraction=float(np.mean(med>T)),
            stage_means={k:float(np.mean([x[k] for x in rows])) for k in ['convert_windows_ms','global_ms','selection_ms','local_ms','merge_ms']})
    for p,h in json.loads((OUT/'input_hashes.json').read_text()).items():assert sha(p)==h
    write_csv(OUT/'timings.csv',times)
    summary=dict(status='PASS',images=48,timing_calls=288,T_ms=T,timing=timing,k1_comparisons=144,k1_exact_outputs=exact,k1_max_abs_diff=maxdiff,F1280_repeat_comparisons=96,F1280_exact_repeats=ref_exact,
        elapsed_seconds=time.monotonic()-started,gpu_peak_allocated=torch.cuda.max_memory_allocated(),training_calls=0,cache_result='cache_summary.json',prior_inputs_unchanged=True)
    save(OUT/'summary.json',summary);save(OUT/'status.json',dict(status='PASS',phase='complete',training_calls=0,timing_calls=288));print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['cache','timing'],required=True);args=ap.parse_args()
    try:
        cache_phase() if args.phase=='cache' else timing_phase()
    except Exception:
        if OUT.exists():
            (OUT/f'failure_{args.phase}.txt').write_text(traceback.format_exc(),encoding='utf-8');save(OUT/'status.json',dict(status='FAILED',phase=args.phase,training_calls=0))
        raise
