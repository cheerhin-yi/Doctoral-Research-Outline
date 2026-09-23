"""Preregistered two-view deduplicated-density control, cached predictions only."""
import json
import traceback
import numpy as np
from pathlib import Path
from diagnose_bt1 import BASE, sha, dump, nms, prepare_gt, match_gt
from analyze_density_residuals import inside, write_csv


def choose(full, windows):
    pred=full[full[:,4]>=.25]
    centers=(pred[:,:2]+pred[:,2:4])/2
    covered=[set(i for i,c in enumerate(centers) if inside(c,w)) for w in windows]
    first=min(range(len(windows)),key=lambda j:(-len(covered[j]),j))
    additional=[len(ids-covered[first]) for ids in covered]
    second=min((j for j in range(len(windows)) if j!=first),key=lambda j:(-additional[j],j))
    return [first,second],additional


def main():
    src=BASE/'BTD1-CAL48-20260913-01';out=BASE/'BTD3-DEDUP-20260913-01'
    out.mkdir(exist_ok=False);dump(out/'status.json',dict(status='RUNNING',model_loaded=False))
    try:
        # Actual selector boundary checks, including exclusion of first and zero-score ties.
        windows=[[0,0,10,10],[0,0,11,10],[10,0,20,10]]
        fake=np.array([[1,1,2,2,.8,0],[12,1,13,2,.8,0]],float)
        assert choose(fake,windows)[0]==[0,2]
        assert choose(np.empty((0,6)),windows)[0]==[0,1]
        original=json.loads((src/'diagnostic_manifest.json').read_text());hashes={}
        for n,m in original.items():
            if n.startswith(('image_','predictions_')) or n=='summary.json':
                hashes[n]=sha(src/n);assert hashes[n]==m['sha256'],n
        records=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(src.glob('image_*.json'))]
        assert len(records)==48
        rows=[];all_cases=[];class_counts={c:dict(small_gt=0,density_tp=0,dedup_tp=0) for c in range(1,11)}
        for index,r in enumerate(records):
            cache=np.load(src/f'predictions_{index:02d}.npz')
            selected,scores=choose(cache['F640'],r['windows'])
            assert selected[0]==r['selected']['density'][0] and len(set(selected))==2
            merged=nms(np.concatenate([cache['F640']]+[cache[f'local_{j}'] for j in selected]))
            assert np.isfinite(merged).all() and len(merged)<=500
            np.save(out/f'predictions_{index:02d}.npy',merged)
            ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt')
            assert sha(ann)==r['annotation_sha256']
            raw=np.array([[float(v) for v in s.rstrip(',').split(',')] for s in ann.read_text().splitlines() if s.strip()])
            gt,ids,integral=prepare_gt(raw,r['height'],r['width'])
            density,fp0,ig0=match_gt(gt,ids,cache['density'],integral,r['height'],r['width'])
            dedup,fp1,ig1=match_gt(gt,ids,merged,integral,r['height'],r['width'])
            assert len(density)==r['metrics']['density']['tp'] and fp0==r['metrics']['density']['fp']
            small=set(d['id'] for d in r['small_gt_details'])
            recoverable=set(d['id'] for d in r['small_gt_details'] if d['recoverable'])
            for d in r['small_gt_details']:
                c=d['category'];gid=d['id'];class_counts[c]['small_gt']+=1
                class_counts[c]['density_tp']+=gid in density;class_counts[c]['dedup_tp']+=gid in dedup
                if (gid in density)!=(gid in dedup):
                    all_cases.append(dict(image=r['image'],gt_row=gid,category=c,box=d['box'],recoverable=d['recoverable'],
                                          change='gain' if gid in dedup else 'loss',old_selected=r['selected']['density'],new_selected=selected))
            row=dict(image=r['image'],old_selected=r['selected']['density'],new_selected=selected,new_scores=scores,
               changed=selected!=r['selected']['density'],small_gt=len(small),valid_gt=r['valid_gt'],recoverable=len(recoverable),
               density_tp=len(density),dedup_tp=len(dedup),density_fp=fp0,dedup_fp=fp1,
               density_small_tp=len(density&small),dedup_small_tp=len(dedup&small),
               gained_small=len((dedup-density)&small),lost_small=len((density-dedup)&small),
               density_recovered=len(density&recoverable),dedup_recovered=len(dedup&recoverable),
               gained_recoverable=len((dedup-density)&recoverable),lost_recoverable=len((density-dedup)&recoverable),
               gained_gt_ids=sorted(dedup-density),lost_gt_ids=sorted(density-dedup))
            rows.append(row)
        fields=['small_gt','valid_gt','recoverable','density_tp','dedup_tp','density_fp','dedup_fp','density_small_tp','dedup_small_tp',
                'gained_small','lost_small','density_recovered','dedup_recovered','gained_recoverable','lost_recoverable']
        total={k:sum(r[k] for r in rows) for k in fields}
        assert total['small_gt']==2720 and total['recoverable']==558 and total['density_recovered']==429
        assert total['dedup_recovered']-429==total['gained_recoverable']-total['lost_recoverable']
        assert total['dedup_small_tp']-total['density_small_tp']==total['gained_small']-total['lost_small']
        delta=np.array([r['dedup_small_tp']-r['density_small_tp'] for r in rows])
        rng=np.random.default_rng(20260913);resamples=rng.integers(0,48,(10000,48))
        den=np.array([r['small_gt'] for r in rows]);ratios=100*delta[resamples].sum(1)/den[resamples].sum(1)
        summary=dict(status='PASS',images=48,local_views=96,changed_images=sum(r['changed'] for r in rows),counts=total,
            small_recall_density=total['density_small_tp']/2720,small_recall_dedup=total['dedup_small_tp']/2720,
            precision_density=total['density_tp']/(total['density_tp']+total['density_fp']),precision_dedup=total['dedup_tp']/(total['dedup_tp']+total['dedup_fp']),
            delta_small_recall_pp=100*delta.sum()/2720,relative_small_recall_change_pct=100*delta.sum()/total['density_small_tp'],
            paired_image_win_tie_loss=[int(sum(delta>0)),int(sum(delta==0)),int(sum(delta<0))],
            exploratory_image_bootstrap_95_percentile_pp=np.percentile(ratios,[2.5,97.5]).tolist(),classes=class_counts,
            caution='cal48 development only, no independent-source inference, AP or E2E timing; no new network or model invocation')
        dump(out/'summary.json',summary);write_csv(out/'per_image.csv',rows);write_csv(out/'changed_small_gt.csv',all_cases)
        dump(out/'input_hashes.json',hashes)
        assert all(sha(src/n)==v for n,v in hashes.items())
        dump(out/'status.json',dict(status='PASS',model_loaded=False,inference_calls=0,identity_pass=True,images=48,local_views=96,script_sha256=sha(__file__)))
        print(json.dumps(summary,ensure_ascii=False,indent=2))
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED'));raise


if __name__=='__main__':main()
