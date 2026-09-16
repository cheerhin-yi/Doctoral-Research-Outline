"""BTD7 frozen-cache audit. GT counterfactuals are diagnostics, never a selector."""
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
from compare_dedup_density import choose


def json_ready(value):
    """Normalize NumPy scalar values before JSON artifact serialization."""
    if isinstance(value,np.generic):return value.item()
    if isinstance(value,dict):return {k:json_ready(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [json_ready(v) for v in value]
    return value


def unexplained_local(local, full):
    """Fixed prediction-to-prediction relation, no GT or unseen-window predictions."""
    local=local[local[:,4]>=.25];full=full[full[:,4]>=.25]
    result=[]
    for d in local:
        other=full[full[:,5]==d[5]]
        wh=np.maximum(0,np.minimum(d[2:4],other[:,2:4])-np.maximum(d[:2],other[:,:2]))
        inter=wh.prod(1);area=(d[2]-d[0])*(d[3]-d[1])
        union=area+(other[:,2:4]-other[:,:2]).prod(1)-inter
        if not np.any(inter/np.maximum(union,1e-12)>=.5):result.append(d)
    return np.array(result,dtype=float).reshape(-1,6)


def main():
    out=BASE/'BTD7-RESIDUAL-20260914-01';out.mkdir(exist_ok=False)
    dump(out/'status.json',dict(status='RUNNING',model_loaded=False,inference_calls=0))
    started=time.monotonic();hashes={};resources=[];process=psutil.Process()
    try:
        src=BASE/'BTD1-CAL48-20260913-01';ded=BASE/'BTD3-DEDUP-20260913-01'
        manifest=json.loads((src/'diagnostic_manifest.json').read_text())
        for name,info in manifest.items():
            if name.startswith(('image_','predictions_')) or name=='summary.json':
                hashes[str(src/name)]=sha(src/name);assert hashes[str(src/name)]==info['sha256']
        for p in [ded/'summary.json',ded/'per_image.csv']+sorted(ded.glob('predictions_*.npy')):hashes[str(p)]=sha(p)
        prior=list(csv.DictReader((ded/'per_image.csv').open(encoding='utf-8-sig')))
        original=json.loads((ded/'summary.json').read_text())['counts']
        for name in ['analyze_conditional_recovery.py','diagnose_bt1.py','compare_dedup_density.py','analyze_density_residuals.py','BTD7_Residual_Protocol.md']:
            shutil.copy2(Path(__file__).with_name(name),out/name)
        cases=[];winrows=[];frames=[];signals=['density','new_coarse','low001','p3','candidate','first_prediction_centers','first_unexplained_centers']
        pair_counts={s:Counter() for s in signals}
        for i,p in enumerate(sorted(src.glob('image_*.json'))):
            mem=process.memory_info();available=psutil.virtual_memory().available
            sample=dict(image_index=i,elapsed_seconds=time.monotonic()-started,rss_bytes=mem.rss,available_bytes=available);resources.append(sample)
            if sample['elapsed_seconds']>900 or mem.rss>2*(1<<30) or available<256*(1<<20) or shutil.disk_usage(out).free<2*(1<<30):
                dump(out/'resource_failure.json',sample);raise RuntimeError('Resource guard')
            r=json.loads(p.read_text());assert prior[i]['image']==r['image']
            with np.load(src/f'predictions_{i:02d}.npz') as d:
                full=d['F640'].copy();locals_=[d[f'local_{j}'].copy() for j in range(len(r['windows']))]
            windows=r['windows'];sel,new=choose(full,windows);f,second=sel
            assert sel==json.loads(prior[i]['new_selected'])
            ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt')
            hashes[str(ann)]=sha(ann);assert hashes[str(ann)]==r['annotation_sha256']
            raw=np.array([[float(v) for v in line.rstrip(',').split(',')] for line in ann.read_text().splitlines() if line.strip()])
            gt,ids,integral=prepare_gt(raw,r['height'],r['width'])
            def match(pred):return match_gt(gt,ids,pred,integral,r['height'],r['width'])
            small={d['id'] for d in r['small_gt_details']};rec={d['id'] for d in r['small_gt_details'] if d['recoverable']}
            fullmatch,fullfp,_=match(full)
            assert len(fullmatch&small)==r['metrics']['F640']['small_tp']
            localmatch=[match(nms(a))[0] for a in locals_]
            assert (set().union(*localmatch)&small)-fullmatch==rec
            for detail in r['small_gt_details']:
                assert [j for j,m in enumerate(localmatch) if detail['id'] in m]==detail['local_recovery_views']
            firstpred=nms(np.concatenate([full,locals_[f]]));first,firstfp,_=match(firstpred)
            coarse=full[full[:,4]>=.25];centers=(coarse[:,:2]+coarse[:,2:4])/2
            visible=firstpred[firstpred[:,4]>=.25];vcenters=(visible[:,:2]+visible[:,2:4])/2
            unexplained=unexplained_local(locals_[f],full);ucenters=(unexplained[:,:2]+unexplained[:,2:4])/2
            pairs={};preds={};fps={};frame_windows=[]
            for j,b in enumerate(windows):
                prediction=firstpred if j==f else nms(np.concatenate([full,locals_[f],locals_[j]]))
                found,fp,_=match(prediction);pairs[j]=found;preds[j]=prediction;fps[j]=fp
                gain=(found-first)&small;loss=(first-found)&small
                wr=dict(image=r['image'],window=j,box=b,first=j==f,dedup_second=j==second,
                    density=sum(inside(c,b) for c in centers),new_coarse=new[j],
                    low001=r['scores']['low001'][j],p3=r['scores']['p3_only'][j],candidate=r['scores']['candidate'][j],
                    first_prediction_centers=sum(inside(c,b) for c in vcenters),first_unexplained_centers=sum(inside(c,b) for c in ucenters),
                    small_tp=len(found&small),recoverable_tp=len(found&rec),fp=fp,fp_delta=fp-firstfp,
                    gained_ids=sorted(gain),lost_ids=sorted(loss),gained=len(gain),lost=len(loss),net=len(gain)-len(loss),
                    individual_new_recoverable=len((localmatch[j]-localmatch[f])&rec),individual_repeated_recoverable=len(localmatch[j]&localmatch[f]&rec))
                assert wr['net']==wr['small_tp']-len(first&small)
                winrows.append(wr);frame_windows.append(wr)
            assert np.array_equal(preds[second],np.load(ded/f'predictions_{i:02d}.npy'))
            actual=pairs[second];assert len(actual&small)==int(prior[i]['dedup_small_tp']) and fps[second]==int(prior[i]['dedup_fp'])
            remaining=rec-actual;concat=np.concatenate([full,locals_[f],locals_[second]])
            pre=match(concat)[0];uncapped=match(nms(concat,cap=len(concat)))[0]
            alternatives=[j for j in range(len(windows)) if j!=f]
            oracle=min(alternatives,key=lambda j:(-len(pairs[j]&small),j))
            stop_oracle=f if len(first&small)>=len(pairs[oracle]&small) else oracle
            for d in r['small_gt_details']:
                if d['id'] not in remaining:continue
                gid=d['id'];x,y,w,h=d['box'];point=[x+w/2,y+h/2]
                cover=[j for j in sel if inside(point,windows[j])]
                complete=[j for j in sel if windows[j][0]<=x and windows[j][1]<=y and windows[j][2]>=x+w and windows[j][3]>=y+h]
                chosen=sorted(set(sel)&set(d['local_recovery_views']))
                if chosen:
                    kind='fusion_or_matching';subtype='final_500_cap' if gid in uncapped else 'nms_or_assignment_change' if gid in pre else 'pre_nms_assignment_competition'
                elif cover:kind='covered_nonrecovering_view';subtype='full_box_covered' if complete else 'center_only_truncated'
                else:kind='center_not_selected';subtype='no_selected_center_cover'
                fixing=[j for j in alternatives if gid in pairs[j]]
                cases.append(dict(image=r['image'],gt_row=gid,category=d['category'],box=d['box'],failure=kind,subtype=subtype,selected=sel,
                    center_views=cover,full_box_views=complete,local_recovery_views=d['local_recovery_views'],selected_recovery_views=chosen,
                    detected_after_first=gid in first,fixing_second_windows=fixing,oracle_second_recovers=gid in pairs[oracle],
                    fixing_window_new_coarse=[new[j] for j in fixing],dedup_second_new_coarse=new[second],
                    max_fixing_unexplained_first_centers=max((frame_windows[j]['first_unexplained_centers'] for j in fixing),default=None),
                    p3_peak_inside=d['p3_peak_inside'],candidate_peak_inside=d['candidate_peak_inside']))
            for a,b in combinations(alternatives,2):
                target=frame_windows[a]['net']-frame_windows[b]['net']
                for s in signals:
                    diff=frame_windows[a][s]-frame_windows[b][s]
                    key='both_tied' if target==0 and diff==0 else 'target_tied' if target==0 else 'signal_tied' if diff==0 else 'concordant' if target*diff>0 else 'discordant'
                    pair_counts[s][key]+=1
            fr=dict(image=r['image'],small_gt=len(small),recoverable=len(rec),residual=len(remaining),first=f,second=second,
                full_small_tp=len(fullmatch&small),first_small_tp=len(first&small),dedup_small_tp=len(actual&small),
                first_recovered=len(first&rec),dedup_recovered=len(actual&rec),first_fp=firstfp,dedup_fp=fps[second],
                second_gain=len((actual-first)&small),second_loss=len((first-actual)&small),second_net=len(actual&small)-len(first&small),
                oracle_second=oracle,oracle_small_tp=len(pairs[oracle]&small),oracle_fp=fps[oracle],oracle_recovered=len(pairs[oracle]&rec),
                oracle_gain_vs_dedup=len((pairs[oracle]-actual)&small),oracle_loss_vs_dedup=len((actual-pairs[oracle])&small),
                oracle_rec_gain_vs_dedup=len((pairs[oracle]-actual)&rec),oracle_rec_loss_vs_dedup=len((actual-pairs[oracle])&rec),
                stop_oracle=stop_oracle,stop_oracle_small_tp=len(pairs[stop_oracle]&small),
                individually_fixable_residual=len(remaining&set().union(*(pairs[j] for j in alternatives))))
            frames.append(fr)
            dump(out/f'frame_{i:02d}.json',dict(frame=fr,first_match_ids=sorted(first),pair_match_ids={str(j):sorted(m) for j,m in pairs.items()}))
            if sum(p.stat().st_size for p in out.rglob('*') if p.is_file())>256*(1<<20):raise RuntimeError('Output guard')
            print(f'{i+1}/48 cache frames checked',flush=True)
        assert len(cases)==105 and len(winrows)==240 and len(frames)==48
        totals={k:sum(f[k] for f in frames) for k in ['small_gt','recoverable','residual','full_small_tp','first_small_tp','dedup_small_tp','first_recovered','dedup_recovered','first_fp','dedup_fp','second_gain','second_loss','second_net','oracle_small_tp','oracle_fp','oracle_recovered','oracle_gain_vs_dedup','oracle_loss_vs_dedup','oracle_rec_gain_vs_dedup','oracle_rec_loss_vs_dedup','stop_oracle_small_tp','individually_fixable_residual']}
        assert totals['small_gt']==2720 and totals['recoverable']==558 and totals['dedup_recovered']==453 and totals['dedup_small_tp']==1282
        assert totals['oracle_gain_vs_dedup']-totals['oracle_loss_vs_dedup']==totals['oracle_small_tp']-1282
        assert all(sha(name)==h for name,h in hashes.items())
        selectable=[r for r in winrows if not r['first']];zero=[r for r in selectable if r['new_coarse']==0]
        def outcomes(rows):return dict(n=len(rows),positive=sum(r['net']>0 for r in rows),zero=sum(r['net']==0 for r in rows),negative=sum(r['net']<0 for r in rows))
        summary=dict(status='PASS',totals=totals,residual_images=sum(f['residual']>0 for f in frames),failures=dict(Counter(c['failure'] for c in cases)),subtypes=dict(Counter(c['subtype'] for c in cases)),
            selectable_outcomes=outcomes(selectable),zero_new_coarse_outcomes=outcomes(zero),selected_second_outcomes=outcomes([r for r in selectable if r['dedup_second']]),
            selected_second_below_best=sum(f['dedup_small_tp']<f['oracle_small_tp'] for f in frames),oracle_prefers_stop=sum(f['stop_oracle']==f['first'] for f in frames),
            pairwise_signal_counts={s:dict(v) for s,v in pair_counts.items()},unfixable_residual=sum(not c['fixing_second_windows'] for c in cases),first_detected_residual=sum(c['detected_after_first'] for c in cases),
            resource_samples=resources,elapsed_seconds=time.monotonic()-started,model_loaded=False,inference_calls=0,
            caveat='All GT-best choices and new/lost target IDs are diagnostic only. Pair comparisons correlated within images, no fitted selector or inference-time claim.')
        cases=json_ready(cases);summary=json_ready(summary)
        write_csv(out/'all_105_cases.csv',cases);dump(out/'cases.json',cases)
        write_csv(out/'all_240_windows.csv',winrows);write_csv(out/'all_48_frames.csv',frames)
        dump(out/'input_hashes.json',hashes);dump(out/'summary.json',summary)
        dump(out/'status.json',dict(status='PASS',images=48,cases=105,model_loaded=False,inference_calls=0,script_sha256=sha(__file__)))
        dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file()})
        print(json.dumps({k:v for k,v in summary.items() if k!='resource_samples'},ensure_ascii=False,indent=2),flush=True)
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED',model_loaded=False,inference_calls=0));raise


if __name__=='__main__':main()
