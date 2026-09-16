"""Recover BTD7 artifacts from preserved frame sets; fill missing window FP only."""
import csv
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
import shutil
import time
import traceback
import numpy as np
import psutil
from diagnose_bt1 import BASE, sha, dump, nms, prepare_gt, match_gt
from analyze_density_residuals import inside, write_csv
from analyze_conditional_recovery import unexplained_local, json_ready
from compare_dedup_density import choose


def main():
    old=BASE/'BTD7-RESIDUAL-20260914-01';out=BASE/'BTD7-RESIDUAL-20260914-02'
    out.mkdir(exist_ok=False);dump(out/'status.json',dict(status='RUNNING',recovered_from=str(old),model_loaded=False))
    started=time.monotonic();resources=[];hashes={}
    try:
        assert json.loads((old/'status.json').read_text())['status']=='FAILED'
        src=BASE/'BTD1-CAL48-20260913-01';ded=BASE/'BTD3-DEDUP-20260913-01'
        for folder,files in [(old,list(old.glob('frame_*.json'))+[old/'all_105_cases.csv',old/'failure.txt',old/'analyze_conditional_recovery.py']),
                             (ded,list(ded.glob('predictions_*.npy'))+[ded/'summary.json',ded/'per_image.csv'])]:
            for p in files:hashes[str(p)]=sha(p)
        for name,info in json.loads((src/'diagnostic_manifest.json').read_text()).items():
            if name.startswith(('image_','predictions_')) or name=='summary.json':
                hashes[str(src/name)]=sha(src/name);assert hashes[str(src/name)]==info['sha256']
        for name in ['finalize_conditional_recovery.py','analyze_conditional_recovery.py','diagnose_bt1.py','compare_dedup_density.py','analyze_density_residuals.py','BTD7_Residual_Protocol.md']:
            shutil.copy2(Path(__file__).with_name(name),out/name)
        cases=list(csv.DictReader((old/'all_105_cases.csv').open(encoding='utf-8-sig')))
        text_fields={'image','failure','subtype'}
        for c in cases:
            for k,v in c.items():
                if k in text_fields:continue
                c[k]=None if v=='' else True if v=='True' else False if v=='False' else json.loads(v)
        assert len(cases)==105
        frames=[];winrows=[];signals=['density','new_coarse','low001','p3','candidate','first_prediction_centers','first_unexplained_centers']
        pair_counts={s:Counter() for s in signals}
        for i in range(48):
            mem=psutil.Process().memory_info();available=psutil.virtual_memory().available
            sample=dict(index=i,elapsed_seconds=time.monotonic()-started,rss_bytes=mem.rss,available_bytes=available);resources.append(sample)
            if sample['elapsed_seconds']>900 or mem.rss>2*(1<<30) or available<256*(1<<20) or shutil.disk_usage(out).free<2*(1<<30):raise RuntimeError('Resource guard')
            saved=json.loads((old/f'frame_{i:02d}.json').read_text());fr=saved['frame'];first=set(saved['first_match_ids']);pairs={int(j):set(v) for j,v in saved['pair_match_ids'].items()}
            r=json.loads((src/f'image_{i:02d}.json').read_text());assert r['image']==fr['image']
            small={d['id'] for d in r['small_gt_details']};rec={d['id'] for d in r['small_gt_details'] if d['recoverable']}
            with np.load(src/f'predictions_{i:02d}.npz') as cache:
                full=cache['F640'];local=[cache[f'local_{j}'] for j in range(len(r['windows']))]
            windows=r['windows'];sel,new=choose(full,windows);f,second=sel;assert f==fr['first'] and second==fr['second']
            firstpred=nms(np.concatenate([full,local[f]]));coarse=full[full[:,4]>=.25];centers=(coarse[:,:2]+coarse[:,2:4])/2
            visible=firstpred[firstpred[:,4]>=.25];vcenters=(visible[:,:2]+visible[:,2:4])/2
            unexplained=unexplained_local(local[f],full);ucenters=(unexplained[:,:2]+unexplained[:,2:4])/2
            ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt');hashes[str(ann)]=sha(ann);assert hashes[str(ann)]==r['annotation_sha256']
            raw=np.array([[float(v) for v in line.rstrip(',').split(',')] for line in ann.read_text().splitlines() if line.strip()])
            gt,ids,integral=prepare_gt(raw,r['height'],r['width'])
            localrec=[{d['id'] for d in r['small_gt_details'] if d['recoverable'] and j in d['local_recovery_views']} for j in range(len(windows))]
            fw=[]
            for j,b in enumerate(windows):
                if j==f:fp=fr['first_fp']
                elif j==second:fp=fr['dedup_fp']
                elif j==fr['oracle_second']:fp=fr['oracle_fp']
                else:
                    pred=nms(np.concatenate([full,local[f],local[j]]))
                    found,fp,_=match_gt(gt,ids,pred,integral,r['height'],r['width']);assert found==pairs[j]
                gain=(pairs[j]-first)&small;loss=(first-pairs[j])&small
                row=dict(image=r['image'],window=j,box=b,first=j==f,dedup_second=j==second,
                    density=int(sum(inside(c,b) for c in centers)),new_coarse=new[j],low001=r['scores']['low001'][j],p3=r['scores']['p3_only'][j],candidate=r['scores']['candidate'][j],
                    first_prediction_centers=int(sum(inside(c,b) for c in vcenters)),first_unexplained_centers=int(sum(inside(c,b) for c in ucenters)),
                    small_tp=len(pairs[j]&small),recoverable_tp=len(pairs[j]&rec),fp=fp,fp_delta=fp-fr['first_fp'],
                    gained_ids=sorted(gain),lost_ids=sorted(loss),gained=len(gain),lost=len(loss),net=len(gain)-len(loss),
                    individual_new_recoverable=len(localrec[j]-localrec[f]),individual_repeated_recoverable=len(localrec[j]&localrec[f]))
                fw.append(row);winrows.append(row)
            assert fr['oracle_small_tp']==max(row['small_tp'] for row in fw if not row['first'])
            for a,b in combinations([j for j in pairs if j!=f],2):
                target=fw[a]['net']-fw[b]['net']
                for s in signals:
                    diff=fw[a][s]-fw[b][s]
                    key='both_tied' if target==0 and diff==0 else 'target_tied' if target==0 else 'signal_tied' if diff==0 else 'concordant' if target*diff>0 else 'discordant'
                    pair_counts[s][key]+=1
            frames.append(fr);shutil.copy2(old/f'frame_{i:02d}.json',out/f'frame_{i:02d}.json')
            if sum(p.stat().st_size for p in out.rglob('*') if p.is_file())>256*(1<<20):raise RuntimeError('Output guard')
        totals={k:sum(f[k] for f in frames) for k in ['small_gt','recoverable','residual','full_small_tp','first_small_tp','dedup_small_tp','first_recovered','dedup_recovered','first_fp','dedup_fp','second_gain','second_loss','second_net','oracle_small_tp','oracle_fp','oracle_recovered','oracle_gain_vs_dedup','oracle_loss_vs_dedup','oracle_rec_gain_vs_dedup','oracle_rec_loss_vs_dedup','stop_oracle_small_tp','individually_fixable_residual']}
        selectable=[r for r in winrows if not r['first']];zero=[r for r in selectable if r['new_coarse']==0]
        def outcomes(rows):return dict(n=len(rows),positive=sum(r['net']>0 for r in rows),zero=sum(r['net']==0 for r in rows),negative=sum(r['net']<0 for r in rows))
        summary=dict(status='PASS',recovered_from=str(old),totals=totals,residual_images=sum(f['residual']>0 for f in frames),failures=dict(Counter(c['failure'] for c in cases)),subtypes=dict(Counter(c['subtype'] for c in cases)),
            selectable_outcomes=outcomes(selectable),zero_new_coarse_outcomes=outcomes(zero),selected_second_outcomes=outcomes([r for r in selectable if r['dedup_second']]),
            selected_second_below_best=sum(f['dedup_small_tp']<f['oracle_small_tp'] for f in frames),oracle_prefers_stop=sum(f['stop_oracle']==f['first'] for f in frames),pairwise_signal_counts={s:dict(v) for s,v in pair_counts.items()},
            unfixable_residual=sum(not c['fixing_second_windows'] for c in cases),first_detected_residual=sum(c['detected_after_first'] for c in cases),
            resource_samples=resources,elapsed_seconds=time.monotonic()-started,model_loaded=False,inference_calls=0,
            caveat='Original run failed during JSON serialization after all 48 frame sets and 105 cases were saved. This finalizer reuses them, fills missing FP/signal fields. Original continuous resource trace unavailable. GT oracles are not methods; no timing claim.')
        assert totals['small_gt']==2720 and totals['recoverable']==558 and totals['dedup_recovered']==453 and totals['residual']==105
        assert all(sha(p)==h for p,h in hashes.items())
        write_csv(out/'all_105_cases.csv',cases);dump(out/'cases.json',cases);write_csv(out/'all_240_windows.csv',winrows);write_csv(out/'all_48_frames.csv',frames)
        dump(out/'input_hashes.json',hashes);dump(out/'summary.json',json_ready(summary))
        dump(out/'status.json',dict(status='PASS',images=48,cases=105,model_loaded=False,inference_calls=0,script_entry=Path(__file__).name,script_sha256=sha(__file__),recovered_from=str(old)))
        dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file()})
        print(json.dumps({k:v for k,v in summary.items() if k!='resource_samples'},ensure_ascii=False,indent=2))
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED',model_loaded=False));raise


if __name__=='__main__':main()
