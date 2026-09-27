"""Fixed cal48 exploratory diagnosis. No training, tuning, or test access.

Accuracy comparisons share cached views; timing is NOT an end-to-end benchmark.
See BT1_Baseline_Diagnostic_Protocol.md for the preregistered interpretation.
"""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
import traceback
import zipfile

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '11_Datasets/processed/VisDrone/BT1'
RUNS = ['BT1-LOCAL-20260912-01', 'BT1-LOCAL-20260912-02', 'BT1-LOCAL-20260913-01']
WEIGHT_SHA = 'bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533'


def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def dump(p, v):
    Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2), encoding='utf-8')


def archive(out):
    """Copy evidence; leave all original runs and source files intact."""
    dest = out / 'baseline_archive'
    dest.mkdir()
    rows = []
    copied = []
    for name in RUNS:
        r = BASE / name
        with (r/'train/results.csv').open(encoding='utf-8-sig') as f:
            rows.extend([{k.strip(): v.strip() for k, v in row.items()} for row in csv.DictReader(f)])
        files = ['run_status.json', 'resolved_args.json', 'environment.json',
                 'train/results.csv', 'train/args.yaml', 'resume_verification.json',
                 'resume_first_batch.json']
        if name == RUNS[-1]:
            files += ['train/weights/last.pt', 'last_pre_strip.pt', 'recovery/latest_recovery.zip']
        for rel in files:
            src = r/rel
            if not src.exists():
                continue
            target = dest/name/rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)
            assert sha(src) == sha(target)
            copied.append(dict(source=str(src), archived=str(target.relative_to(dest)),
                               bytes=src.stat().st_size, sha256=sha(target)))
        launch = BASE/(name+'-launch')
        if launch.exists():
            for src in launch.iterdir():
                if src.is_file():
                    target = dest/(name+'-launch')/src.name
                    target.parent.mkdir(exist_ok=True)
                    shutil.copy2(src, target)
                    copied.append(dict(source=str(src), archived=str(target.relative_to(dest)),
                                       bytes=src.stat().st_size, sha256=sha(target)))
    assert [int(r['epoch']) for r in rows] == list(range(1, 101))
    assert all(np.isfinite(float(v)) for r in rows for v in r.values())
    with (dest/'epochs_001_100.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    weight = BASE/RUNS[-1]/'train/weights/last.pt'
    assert sha(weight) == WEIGHT_SHA
    import torch
    raw = torch.load(BASE/RUNS[-1]/'last_pre_strip.pt', map_location='cpu', weights_only=False)
    assert raw['epoch'] == 99 and raw['optimizer'] is not None
    # Final stripped last is the final EMA, not best. Check every tensor.
    stripped = torch.load(weight, map_location='cpu', weights_only=False)
    a, b = raw['ema'].state_dict(), stripped['model'].state_dict()
    assert a.keys() == b.keys() and all(torch.equal(a[k].half(), b[k].half()) for k in a)
    bundle = BASE/RUNS[-1]/'recovery/latest_recovery.zip'
    with zipfile.ZipFile(bundle) as z:
        assert z.testzip() is None
        manifest = json.loads(z.read('manifest.json'))
        checkpoint_hash = hashlib.sha256(z.read('resume.pt')).hexdigest()
        assert manifest['completed_epochs'] == 100 and manifest['checkpoint_sha256'] == checkpoint_hash
    for src in [Path(__file__).parent/'baseline_training_spec.json', BASE/'execution_2026-09-12/pip_freeze.txt',BASE/RUNS[0]/'preview_environment_freeze.txt'] + [BASE/'full_data_v2'/n for n in ['train.txt','cal48.txt','preparation.json','data.yaml']]:
        target=dest/'configuration'/src.name; target.parent.mkdir(exist_ok=True)
        shutil.copy2(src,target)
        copied.append(dict(source=str(src),archived=str(target.relative_to(dest)),bytes=src.stat().st_size,sha256=sha(target)))
    checks = dict(epochs=list(range(1,101)), final_raw_epoch=99, optimizer_retained=True,
                  final_ema_equals_last=True, last_sha256=sha(weight),
                  recovery_zip_crc_pass=True, recovery_checkpoint_sha256=checkpoint_hash,
                  recovery_manifest=manifest, files=copied)
    dump(dest/'archive_manifest.json', checks)
    package = out/'BT1_100epochs_evidence.zip'
    with zipfile.ZipFile(package, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for p in dest.rglob('*'):
            if p.is_file(): z.write(p, p.relative_to(dest))
    with zipfile.ZipFile(package) as z: assert z.testzip() is None
    dump(out/'archive_check.json', dict(status='PASS', path=str(package), sha256=sha(package),
         bytes=package.stat().st_size, rows=100, final_ema_equals_last=True))
    print('Archive PASS: epochs 1-100, final EMA identity, evidence ZIP', flush=True)


def nms(pred, cap=500):
    """Stable class-aware CPU NMS; ties retain input view/index order."""
    pred = np.asarray(pred, dtype=np.float64).reshape(-1, 6)
    ids = np.argsort(-pred[:, 4], kind='stable')
    keep = []
    while len(ids) and len(keep) < cap:
        i = ids[0]; keep.append(i); ids = ids[1:]
        if not len(ids): break
        box = pred[i]; others = pred[ids]
        wh = np.maximum(0, np.minimum(box[2:4], others[:,2:4])-np.maximum(box[:2],others[:,:2]))
        inter = wh.prod(1)
        area = (box[2]-box[0])*(box[3]-box[1])
        other_area = (others[:,2]-others[:,0])*(others[:,3]-others[:,1])
        iou = inter/np.maximum(area+other_area-inter,1e-12)
        ids = ids[~((others[:,5] == box[5]) & (iou > .5))]
    return pred[keep]


def axis_windows(size):
    return sorted(set(list(range(0, max(1,size-640+1),512)) + [max(0,size-640)]))


def ignore_keep(rows, integral, h, w):
    if not len(rows): return np.zeros(0, dtype=bool)
    # Same positive integer clamp / MATLAB half-away rounding as the pinned probe.
    rounded = np.sign(rows[:,:4])*np.floor(np.abs(rows[:,:4])+.5)
    r = np.maximum(1, rounded).astype(int)
    x, y = np.minimum(w,r[:,0]), np.minimum(h,r[:,1])
    right, bottom = np.minimum(w,x+r[:,2]), np.minimum(h,y+r[:,3])
    covered = integral[y,x]+integral[bottom,right]-integral[y,right]-integral[bottom,x]
    return covered/(r[:,2]*r[:,3]) < .5


def prepare_gt(raw, h, w):
    integral = np.zeros((h+1,w+1), dtype=np.int32)
    for r in raw[raw[:,5] == 0]:
        x,y,rw,rh = np.maximum(1,r[:4]).astype(int)
        integral[y:min(h,y+rh)+1, x:min(w,x+rw)+1] = 1
    integral = integral.cumsum(0).cumsum(1)
    valid = (raw[:,5]>=1)&(raw[:,5]<=10)&(raw[:,2]>0)&(raw[:,3]>0)
    valid &= ignore_keep(raw, integral, h,w)
    ids = np.flatnonzero(valid)
    return raw[ids], ids, integral


def match_gt(gt, ids, pred, integral, h,w):
    """Return matched original-row IDs, false positives and valid predictions.

    Match all sizes, score-order greedily; normal GT before reusable score=0 GT.
    Equal overlaps prefer later GT, matching existing checked MATLAB semantics.
    """
    p = pred[pred[:,4]>=.25].copy()
    rows = p.copy(); rows[:,2:4] -= rows[:,:2]
    p = p[ignore_keep(rows,integral,h,w)]
    p = p[np.argsort(-p[:,4],kind='stable')]
    matched, fp, ignored = set(), 0, 0
    for d in p:
        eligible = np.flatnonzero((gt[:,5] == int(d[5])+1) & ~np.isin(ids,list(matched)))
        g=gt[eligible]; is_ignore=g[:,4]==0
        inter=np.maximum(0,np.minimum(d[2:4],g[:,:2]+g[:,2:4])-np.maximum(d[:2],g[:,:2])).prod(1)
        da=(d[2]-d[0])*(d[3]-d[1])
        overlap=inter/np.maximum(1e-12,np.where(is_ignore,da,da+g[:,2]*g[:,3]-inter))
        choices=np.flatnonzero((overlap>=.5)&~is_ignore)
        if not len(choices): choices=np.flatnonzero((overlap>=.5)&is_ignore)
        bi,flag=None,0
        if len(choices):
            best=choices[np.flatnonzero(overlap[choices]==overlap[choices].max())[-1]]
            bi=int(eligible[best]); flag=-1 if is_ignore[best] else 1
        if flag == 1: matched.add(int(ids[bi]))
        elif flag == -1: ignored += 1
        else: fp += 1
    return matched, fp, ignored


def local_z(values, c, y, x, valid, radius):
    ya,yb=max(0,y-radius),min(values.shape[1],y+radius+1)
    xa,xb=max(0,x-radius),min(values.shape[2],x+radius+1)
    mask=valid[ya:yb,xa:xb].copy(); mask[y-ya,x-xa]=False
    neighbors=values[c,ya:yb,xa:xb][mask]
    if not len(neighbors): return 0.
    median=np.median(neighbors); mad=np.median(np.abs(neighbors-median))
    return float(np.clip((values[c,y,x]-median)/max(float(mad),.1),0,6))


def response_scores(logits, h,w, full, windows):
    p3,p4=logits
    assert p3.shape == (10,80,80) and p4.shape == (10,40,40)
    gain=min(640/h,640/w)
    top=round((640-round(h*gain))/2-.1); left=round((640-round(w*gain))/2-.1)
    grids=[]
    for stride,size in [(8,80),(16,40)]:
        yy,xx=np.mgrid[:size,:size]
        x=((xx+.5)*stride-left)/gain; y=((yy+.5)*stride-top)/gain
        grids.append((x,y,(x>=0)&(x<w)&(y>=0)&(y<h)))
    x3,y3,v3=grids[0]; _,_,v4=grids[1]
    shifted=p4.copy()
    vys,vxs=np.where(v4); y0,y1=vys.min(),vys.max()+1; x0,x1=vxs.min(),vxs.max()+1
    shifted[:,y0:y1,x0:x1]=np.roll(p4[:,y0:y1,x0:x1],((y1-y0)//2,(x1-x0)//2),(1,2))
    classes=p3.argmax(0); cls4=p4.argmax(0); clss=shifted.argmax(0)
    peaks=[]
    for y,x in zip(*np.where(v3)):
        c=int(classes[y,x]); value=p3[c,y,x]
        ya,yb=max(0,y-1),min(80,y+2); xa,xb=max(0,x-1),min(80,x+2)
        local=p3[c,ya:yb,xa:xb]; mask=v3[ya:yb,xa:xb]
        maximum=np.max(local[mask])
        if value < maximum: continue
        ties=np.argwhere(mask & (local == maximum))
        if (int(ties[0,0])+ya,int(ties[0,1])+xa)!=(y,x): continue
        px,py=float(x3[y,x]),float(y3[y,x])
        explained=full[(full[:,4]>=.25)&(full[:,5]==c)]
        if any((d[0]<=px<=d[2] and d[1]<=py<=d[3]) for d in explained): continue
        qy,qx=y//2,x//2
        z3=local_z(p3,c,y,x,v3,4)
        qvalid=bool(v4[qy,qx])
        same=qvalid and cls4[qy,qx]==c
        z4=local_z(p4,c,qy,qx,v4,2) if same else 0.
        zs=local_z(shifted,c,qy,qx,v4,2) if qvalid and clss[qy,qx]==c else 0.
        prob=float(1/(1+np.exp(-float(value))))
        prob4=float(1/(1+np.exp(-float(p4[c,qy,qx])))) if same else 0.
        peaks.append([px,py,c,prob,z3,z3*z4,prob*prob4,z3*zs])
    peaks=np.asarray(peaks,dtype=float).reshape(-1,8)
    m=int(np.count_nonzero(peaks[:,5]>0))
    top_m=np.zeros(len(peaks)); top_m[np.argsort(-peaks[:,3],kind='stable')[:m]]=1
    scores={k:[] for k in ['density','low025','low005','low001','low0001','raw_top_m','p3_only','raw_product','shift_p4','candidate']}
    for x,y,x2,y2 in windows:
        pm=(peaks[:,0]>=x)&(peaks[:,0]<x2)&(peaks[:,1]>=y)&(peaks[:,1]<y2)
        centers=(full[:,:2]+full[:,2:4])/2
        dm=(full[:,4]>=.25)&(centers[:,0]>=x)&(centers[:,0]<x2)&(centers[:,1]>=y)&(centers[:,1]<y2)
        scores['density'].append(float(dm.sum()))
        for name,tau in [('low025',.25),('low005',.05),('low001',.01),('low0001',.001)]:
            scores[name].append(float(np.count_nonzero(pm & (peaks[:,3]>=tau))))
        for name,values in [('raw_top_m',peaks[:,3]*top_m),('p3_only',peaks[:,4]),
                            ('raw_product',peaks[:,6]),('shift_p4',peaks[:,7]),('candidate',peaks[:,5])]:
            scores[name].append(float(np.sort(values[pm])[-8:].sum()))
    chosen={k:[int(i) for i in np.argsort(-np.array(v),kind='stable')[:2]
               if v[i]>0 or k=='density'] for k,v in scores.items()}
    return peaks,scores,chosen


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    out=a.output.resolve(); out.mkdir(exist_ok=False,parents=True)
    (out/'framework_config').mkdir()
    os.environ['YOLO_AUTOINSTALL']='false'; os.environ['YOLO_CONFIG_DIR']=str(out/'framework_config')
    import torch
    import cv2
    import ultralytics
    from ultralytics import YOLO
    start=time.monotonic()
    dump(out/'status.json',dict(status='RUNNING',run_id=out.name))
    try:
        archive(out)
        source=BASE/'full_data_v2'
        paths=[Path(s) for s in (source/'cal48.txt').read_text(encoding='utf-8').splitlines()]
        assert len(paths)==48 and sha(source/'cal48.txt')=='b0e27b1dc10d952a927597022a1fe0cfa52714d45a89e4c3f36880c2a4a68e7f'
        assert ultralytics.__version__=='8.4.90' and torch.cuda.is_available()
        model=YOLO(str(BASE/RUNS[-1]/'train/weights/last.pt'))
        assert len(model.names)==10
        dump(out/'provenance.json',dict(weight_sha256=WEIGHT_SHA,script_sha256=sha(__file__),
             protocol_sha256=sha(Path(__file__).with_name('BT1_Baseline_Diagnostic_Protocol.md')),
             cal48_sha256=sha(source/'cal48.txt'),torch=torch.__version__,ultralytics=ultralytics.__version__,
             gpu=torch.cuda.get_device_name(0),names=model.names,scope='cal48 only; exploratory; cached accuracy, not E2E timing'))
        cache={}
        head=model.model.model[-1]
        hooks=[head.cv3[i].register_forward_hook(lambda m,x,y,k=i: cache.update({k:y.detach().float().cpu().numpy()[0].copy()})) for i in (0,1)]
        def infer(im):
            torch.cuda.synchronize(); t=time.perf_counter()
            r=model.predict(im,imgsz=640,rect=False,device=0,batch=1,half=False,conf=.001,iou=.5,max_det=1000,save=False,verbose=False)[0]
            a=r.boxes.data.cpu().numpy().astype(float)
            torch.cuda.synchronize(); elapsed=time.perf_counter()-t
            assert np.isfinite(a).all() and all(np.isfinite(v).all() for v in cache.values())
            return a,elapsed
        # Fixed prewarm, no metrics or thresholds selected.
        warm=cv2.imread(str(paths[0])); infer(warm)
        results=[]
        for index,path in enumerate(paths):
            if time.monotonic()-start>7200 or shutil.disk_usage(out).free<5*(1<<30):
                raise RuntimeError('Resource guard')
            im=cv2.imread(str(path)); assert im is not None
            h,w=im.shape[:2]
            full,tfull=infer(im); logits=[cache[i].copy() for i in (0,1)]
            full=nms(full)
            windows=[(x,y,min(w,x+640),min(h,y+640)) for y in axis_windows(h) for x in axis_windows(w)]
            t=time.perf_counter(); peaks,scores,chosen=response_scores(logits,h,w,full,windows); tscore=time.perf_counter()-t
            local=[]; tlocal=[]
            for x,y,x2,y2 in windows:
                patch=np.full((640,640,3),114,dtype=np.uint8); patch[:y2-y,:x2-x]=im[y:y2,x:x2]
                d,dt=infer(patch); centers=(d[:,:2]+d[:,2:4])/2
                d=d[(centers[:,0]<x2-x)&(centers[:,1]<y2-y)].copy()
                d[:,[0,2]]=np.clip(d[:,[0,2]],0,x2-x)+x
                d[:,[1,3]]=np.clip(d[:,[1,3]],0,y2-y)+y
                d=d[(d[:,2]>d[:,0])&(d[:,3]>d[:,1])]
                local.append(d); tlocal.append(dt)
            variants={'F640':full,'Tall':nms(np.concatenate([full]+local))}
            variants.update({k:nms(np.concatenate([full]+[local[j] for j in sel])) for k,sel in chosen.items()})
            ann=source/'annotations/cal48'/path.with_suffix('.txt').name
            raw=np.asarray([[float(v) for v in line.rstrip(',').split(',')] for line in ann.read_text().splitlines() if line.strip()])
            gt,ids,integral=prepare_gt(raw,h,w)
            small=set(int(ids[i]) for i,g in enumerate(gt) if g[4]>0 and 0<g[2]*g[3]<1024)
            valid=set(int(ids[i]) for i,g in enumerate(gt) if g[4]>0)
            matches={}; measurements={}
            for k,pred in variants.items():
                matched,fp,ignored=match_gt(gt,ids,pred,integral,h,w)
                matches[k]=matched
                measurements[k]=dict(tp=len(matched),fp=fp,ignored=ignored,small_tp=len(matched&small))
            local_matches=[match_gt(gt,ids,nms(d),integral,h,w)[0] for d in local]
            recoverable=(set().union(*local_matches)&small)-matches['F640']
            for k in measurements:
                measurements[k]['recovered']=len(matches[k]&recoverable)
            details=[]
            for gid in sorted(small):
                g=raw[gid]; cx,cy=g[0]+g[2]/2,g[1]+g[3]/2
                same=(peaks[:,2]==g[5]-1)&(peaks[:,0]>=g[0])&(peaks[:,0]<=g[0]+g[2])&(peaks[:,1]>=g[1])&(peaks[:,1]<=g[1]+g[3])
                details.append(dict(id=gid,category=int(g[5]),box=g[:4].tolist(),input_short_side=min(g[2:4])*min(640/h,640/w),
                  full_detected=gid in matches['F640'],recoverable=gid in recoverable,
                  p3_peak_inside=bool(np.any(same&(peaks[:,4]>0))),candidate_peak_inside=bool(np.any(same&(peaks[:,5]>0))),
                  detected_by=[k for k,v in matches.items() if gid in v],
                  candidate_center_covered=any(windows[j][0]<=cx<windows[j][2] and windows[j][1]<=cy<windows[j][3] for j in chosen['candidate']),
                  local_recovery_views=[j for j,m in enumerate(local_matches) if gid in m]))
            record=dict(image=path.name,width=w,height=h,image_sha256=sha(path),annotation_sha256=sha(ann),
                 valid_gt=len(valid),small_gt=len(small),recoverable=len(recoverable),metrics=measurements,
                 windows=windows,scores=scores,selected=chosen,small_gt_details=details,
                 full_forward_with_hook_seconds=tfull,all_control_scoring_seconds=tscore,local_seconds=tlocal)
            dump(out/f'image_{index:02d}.json',record)
            np.savez_compressed(out/f'predictions_{index:02d}.npz',peaks=peaks,p3=logits[0],p4=logits[1],**variants,
                                **{f'local_{i}':d for i,d in enumerate(local)})
            results.append(record)
            print(f'{index+1}/48 {path.name}: small={len(small)}, F640={measurements["F640"]["small_tp"]}, recoverable={len(recoverable)}',flush=True)
        for hook in hooks: hook.remove()
        totals={k:{metric:sum(r['metrics'][k][metric] for r in results) for metric in results[0]['metrics'][k]} for k in results[0]['metrics']}
        small_total=sum(r['small_gt'] for r in results); valid_total=sum(r['valid_gt'] for r in results); rec_total=sum(r['recoverable'] for r in results)
        for k,v in totals.items():
            v.update(small_recall=v['small_tp']/small_total, recall=v['tp']/valid_total,
                     precision=v['tp']/max(1,v['tp']+v['fp']), recoverable_recall=v['recovered']/rec_total if rec_total else None)
        recs=[d for r in results for d in r['small_gt_details'] if d['recoverable']]
        summary=dict(status='PASS',images=48,valid_gt=valid_total,small_gt=small_total,recoverable=rec_total,
             recoverable_images=sum(r['recoverable']>0 for r in results),metrics=totals,
             recoverable_with_p3_peak_inside=sum(d['p3_peak_inside'] for d in recs),
             recoverable_with_candidate_peak_inside=sum(d['candidate_peak_inside'] for d in recs),
             recoverable_candidate_center_covered=sum(d['candidate_center_covered'] for d in recs),
             elapsed_seconds=time.monotonic()-start)
        dump(out/'summary.json',summary); dump(out/'status.json',dict(status='PASS',images=48,elapsed_seconds=time.monotonic()-start))
        print(json.dumps(summary,ensure_ascii=False),flush=True)
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8')
        dump(out/'status.json',dict(status='FAILED',elapsed_seconds=time.monotonic()-start))
        raise


if __name__=='__main__': main()
