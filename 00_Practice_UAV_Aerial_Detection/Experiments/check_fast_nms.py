"""Validate exact NMS rows on synthetic inputs and frozen caches; CPU benchmark."""
import csv
import json
from pathlib import Path
import shutil
import time
import traceback
import numpy as np
from diagnose_bt1 import BASE, nms as reference, sha, dump


def main():
    out=BASE/'BTD5-NMS-20260913-01';out.mkdir(exist_ok=False)
    dump(out/'status.json',dict(status='RUNNING',phase='import',model_loaded=False))
    started=time.monotonic()
    try:
        print('Loading installed CPU operator; no detector or CUDA invocation',flush=True)
        from fast_stable_nms import nms as fast
        import torch,torchvision
        dump(out/'environment.json',dict(torch=torch.__version__,torchvision=torchvision.__version__,numpy=np.__version__,
             threads=torch.get_num_threads(),device='CPU',script_sha256=sha(__file__),implementation_sha256=sha(Path(__file__).with_name('fast_stable_nms.py'))))
        for n in ['check_fast_nms.py','fast_stable_nms.py','diagnose_bt1.py','BTD5_NMS_Protocol.md']:
            shutil.copy2(Path(__file__).with_name(n),out/n)
        fixtures=[('empty',np.empty((0,6)),500),
          ('ties',np.array([[0,0,10,10,.8,0],[0,0,10,10,.8,1],[0,0,10,10,.8,0]],float),500),
          ('chain',np.array([[0,0,10,10,.9,0],[2,0,12,10,.8,0],[4,0,14,10,.7,0]],float),500),
          ('zero_area',np.array([[0,0,0,10,.9,0],[0,0,0,10,.8,0]],float),500),
          ('tiny_floor',np.array([[0,0,1e-7,1e-7,.9,0],[0,0,1e-7,1e-7,.8,0]],float),500)]
        for edge in [np.nextafter(1.,0.),1.,np.nextafter(1.,2.)]:
            fixtures.append((f'iou_boundary_{edge!r}',np.array([[0,0,2,2,.9,0],[0,0,edge,2,.8,0]],float),500))
        for cap in [0,1,2,3,500,-1,1.5]:fixtures.append((f'cap_{cap}',fixtures[1][1],cap))
        rng=np.random.default_rng(20260913)
        for i in range(100):
            xy=rng.integers(0,500,(256,2)).astype(float);wh=rng.integers(1,100,(256,2)).astype(float)
            p=np.column_stack([xy,xy+wh,rng.choice([.1,.2,.5,.9],256),rng.integers(0,10,256)])
            p[10:20]=p[:10];fixtures.append((f'random_{i}',p,[1,20,500][i%3]))
        checked=[]
        for name,p,cap in fixtures:
            expected=reference(p,cap);actual=fast(p,cap)
            assert np.array_equal(expected,actual),name
            checked.append(dict(name=name,input_rows=len(p),output_rows=len(actual),cap=cap,exact=True))
        dump(out/'synthetic_checks.json',checked)
        print(f'{len(checked)} synthetic cases exact PASS',flush=True)
        src=BASE/'BTD1-CAL48-20260913-01';manifest=json.loads((src/'diagnostic_manifest.json').read_text())
        hashes={}
        for n,v in manifest.items():
            if n.startswith(('image_','predictions_')):
                hashes[n]=sha(src/n);assert hashes[n]==v['sha256']
        dedup=list(csv.DictReader((BASE/'BTD3-DEDUP-20260913-01/per_image.csv').open(encoding='utf-8-sig')))
        workloads=[]
        for i,p in enumerate(sorted(src.glob('image_*.json'))):
            r=json.loads(p.read_text());d=np.load(src/f'predictions_{i:02d}.npz')
            assert dedup[i]['image']==r['image']
            local=[d[f'local_{j}'] for j in range(len(r['windows']))];full=d['F640']
            workloads.append((r['image'],'full',full))
            workloads.extend((r['image'],f'local_{j}',a) for j,a in enumerate(local))
            for method,sel in [('density',r['selected']['density']),('dedup',json.loads(dedup[i]['new_selected']))]:
                combined=np.concatenate([full]+[local[j] for j in sel])
                old=reference(combined)
                saved=d['density'] if method=='density' else np.load(BASE/f'BTD3-DEDUP-20260913-01/predictions_{i:02d}.npy')
                assert np.array_equal(old,saved)
                workloads.append((r['image'],method,combined))
            workloads.append((r['image'],'Tall',np.concatenate([full]+local)))
        assert len(workloads)==432
        for name,kind,p in workloads:
            assert np.array_equal(reference(p),fast(p)),(name,kind)
        print('432 real cached arrays exact PASS; timing starts',flush=True)
        stats=[];timings=[]
        for i,(name,kind,p) in enumerate(workloads):
            if time.monotonic()-started>600:raise RuntimeError('10 minute guard')
            expected=reference(p);fast(p)
            samples={'reference':[],'compiled':[]}
            for rep in range(11):
                order=['reference','compiled'] if (i+rep)%2==0 else ['compiled','reference']
                for key in order:
                    func=reference if key=='reference' else fast
                    start=time.perf_counter();result=func(p);ms=(time.perf_counter()-start)*1000
                    assert np.array_equal(expected,result),(name,kind,rep,key)
                    samples[key].append(ms)
                    timings.append(dict(image=name,workload=kind,repeat=rep,implementation=key,ms=ms))
            stat=dict(image=name,workload=kind,input_rows=len(p),output_rows=len(expected),
                      reference_median_ms=float(np.median(samples['reference'])),compiled_median_ms=float(np.median(samples['compiled'])))
            stat['speedup']=stat['reference_median_ms']/stat['compiled_median_ms'];stats.append(stat)
            if (i+1)%100==0:print(f'{i+1}/432 benchmark arrays complete',flush=True)
        for filename,rows in [('workloads.csv',stats),('timings.csv',timings)]:
            with (out/filename).open('w',encoding='utf-8-sig',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        groups={}
        for kind in ['full','local','density','dedup','Tall']:
            part=[r for r in stats if r['workload']==kind or kind=='local' and r['workload'].startswith('local_')]
            groups[kind]=dict(arrays=len(part))
            for method in ['reference','compiled']:
                vals=[r[method+'_median_ms'] for r in part]
                groups[kind][method]=dict(mean_of_medians_ms=float(np.mean(vals)),median_ms=float(np.median(vals)),p95_ms=float(np.percentile(vals,95)))
            groups[kind]['ratio_of_mean_medians']=groups[kind]['reference']['mean_of_medians_ms']/groups[kind]['compiled']['mean_of_medians_ms']
        assert all(sha(src/n)==v for n,v in hashes.items())
        dump(out/'input_hashes.json',hashes)
        summary=dict(status='PASS',synthetic_cases=len(fixtures),real_arrays=432,repeats_per_impl=11,total_timing_calls=len(timings),
                     exact_output_mismatches=0,groups=groups,elapsed_seconds=time.monotonic()-started,
                     use='eligible for subsequent shared-pipeline validation; not E2E FPS or innovation',model_loaded=False,inference_calls=0)
        dump(out/'summary.json',summary);dump(out/'status.json',summary)
        print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED',elapsed_seconds=time.monotonic()-started));raise


if __name__=='__main__':main()
