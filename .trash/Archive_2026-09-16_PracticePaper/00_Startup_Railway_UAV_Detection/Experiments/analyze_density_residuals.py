"""CPU-only analysis of existing BTD1 caches; never loads a detector."""
import csv
from collections import Counter
import json
from pathlib import Path
import traceback
import numpy as np
from diagnose_bt1 import BASE, sha, dump, nms, prepare_gt, match_gt


def inside(point, box):
    return box[0]<=point[0]<box[2] and box[1]<=point[1]<box[3]


def write_csv(path, rows):
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader()
        for r in rows:
            writer.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})


def main():
    src=BASE/'BTD1-CAL48-20260913-01';out=BASE/'BTD2-DENSITY-20260913-01'
    out.mkdir(exist_ok=False)
    dump(out/'status.json',dict(status='RUNNING',analysis_only=True))
    try:
        manifest=json.loads((src/'diagnostic_manifest.json').read_text())
        hashes={}
        for name in manifest:
            if name.startswith(('image_','predictions_')) or name=='summary.json':
                hashes[name]=sha(src/name)
                assert hashes[name]==manifest[name]['sha256'],name
        rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(src.glob('image_*.json'))]
        assert len(rows)==48
        cases=[];window_rows=[];frame_rows=[];controls={}
        all_recoverable=[]
        for index,r in enumerate(rows):
            data=np.load(src/f'predictions_{index:02d}.npz')
            full=data['F640'];sel=r['selected']['density'];windows=r['windows']
            assert len(sel)==2
            coarse=full[full[:,4]>=.25];centers=(coarse[:,:2]+coarse[:,2:4])/2
            ids=[set(j for j,p in enumerate(centers) if inside(p,b)) for b in windows]
            density=[len(x) for x in ids]
            assert density==r['scores']['density']
            unique=[len(s-ids[sel[0]]) for s in ids]
            density_rank={j:rank+1 for rank,j in enumerate(np.argsort(-np.array(density),kind='stable'))}
            shared=len(ids[sel[0]]&ids[sel[1]])
            recoverable=[d for d in r['small_gt_details'] if d['recoverable']]
            all_recoverable.extend(recoverable)
            missed=[d for d in recoverable if 'density' not in d['detected_by']]
            concat=np.concatenate([full]+[data[f'local_{j}'] for j in sel])
            assert np.array_equal(nms(concat),data['density'])
            ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt')
            assert sha(ann)==r['annotation_sha256']
            raw=np.array([[float(v) for v in s.rstrip(',').split(',')] for s in ann.read_text().splitlines() if s.strip()])
            gt,gids,integral=prepare_gt(raw,r['height'],r['width'])
            def matched(pred):return match_gt(gt,gids,pred,integral,r['height'],r['width'])[0]
            # Pair interventions affect only cached fusion, not detector inference.
            pre=matched(concat);uncapped=matched(nms(concat,cap=len(concat)))
            for j,b in enumerate(windows):
                recovered_ids=[d['id'] for d in recoverable if j in d['local_recovery_views']]
                window_rows.append(dict(image=r['image'],window=j,box=b,selected=j in sel,
                  density=density[j],density_rank=int(density_rank[j]),new_coarse_after_first=unique[j],
                  local_recoverable_gt=len(recovered_ids),recoverable_ids=recovered_ids,
                  low001=r['scores']['low001'][j],p3_score=r['scores']['p3_only'][j],candidate_score=r['scores']['candidate'][j]))
            frame_rows.append(dict(image=r['image'],recoverable=len(recoverable),density_missed=len(missed),
                first=sel[0],second=sel[1],first_density=density[sel[0]],second_density=density[sel[1]],
                shared_coarse=shared,second_new_coarse=unique[sel[1]],
                second_redundant_fraction=shared/density[sel[1]] if density[sel[1]] else None))
            for d in missed:
                gid=d['id'];x,y,w,h=d['box'];point=[x+w/2,y+h/2]
                center_views=[j for j in sel if inside(point,windows[j])]
                complete_views=[j for j in sel if windows[j][0]<=x and windows[j][1]<=y and windows[j][2]>=x+w and windows[j][3]>=y+h]
                chosen_recovery=sorted(set(sel)&set(d['local_recovery_views']))
                if chosen_recovery:
                    kind='fusion_or_matching'
                    subtype='final_500_cap' if gid in uncapped else 'nms_or_assignment_change' if gid in pre else 'pre_nms_assignment_competition'
                elif center_views:
                    kind='covered_nonrecovering_view';subtype='full_box_covered' if complete_views else 'center_only_truncated'
                else:
                    kind='center_not_selected';subtype='no_selected_center_cover'
                recovery_views=d['local_recovery_views']
                unselected=[j for j in recovery_views if j not in sel]
                better_new=[j for j in unselected if unique[j]>unique[sel[1]]]
                # This uses GT to name recovering windows, and is ONLY an explanatory statistic.
                case=dict(image=r['image'],gt_row=gid,category=d['category'],box=d['box'],
                    failure=kind,subtype=subtype,selected=sel,center_views=center_views,full_box_views=complete_views,
                    recovering_views=recovery_views,selected_recovering_views=chosen_recovery,
                    best_recovering_density_rank=min(int(density_rank[j]) for j in recovery_views),
                    max_recovering_density=max(density[j] for j in recovery_views),
                    all_recovering_windows_zero_coarse=all(density[j]==0 for j in recovery_views),
                    second_density=density[sel[1]],second_shared_coarse=shared,second_new_coarse=unique[sel[1]],
                    unselected_recovering_with_more_new_coarse=better_new,
                    p3_peak_inside=d['p3_peak_inside'],candidate_peak_inside=d['candidate_peak_inside'],
                    existing_strategies_recovering=[k for k in d['detected_by'] if k not in ['F640','Tall','density']],
                    input_short_side=d['input_short_side'])
                cases.append(case)
        assert len(all_recoverable)==558 and len(cases)==129
        kinds=Counter(c['failure'] for c in cases);subtypes=Counter(c['subtype'] for c in cases)
        for method in ['low025','low005','low001','low0001','raw_top_m','p3_only','raw_product','shift_p4','candidate']:
            gained=sum(method in d['detected_by'] and 'density' not in d['detected_by'] for d in all_recoverable)
            lost=sum(method not in d['detected_by'] and 'density' in d['detected_by'] for d in all_recoverable)
            controls[method]=dict(gained_from_129=gained,lost_from_429=lost,net_vs_density=gained-lost)
        subsets={k:[c for c in cases if c['failure']==k] for k in kinds}
        signatures={k:dict(n=len(cs),zero_coarse=sum(c['all_recovering_windows_zero_coarse'] for c in cs),
            better_new_coarse=sum(bool(c['unselected_recovering_with_more_new_coarse']) for c in cs),
            p3_peak_inside=sum(c['p3_peak_inside'] for c in cs),candidate_peak_inside=sum(c['candidate_peak_inside'] for c in cs)) for k,cs in subsets.items()}
        missed_frames=[r for r in frame_rows if r['density_missed']]
        summary=dict(status='PASS',images=48,residual_images=len(missed_frames),total=129,
            failures=dict(kinds),subtypes=dict(subtypes),signatures=signatures,controls=controls,
            affected_frames_with_shared_coarse=sum(r['shared_coarse']>0 for r in missed_frames),
            all_frames_second_redundant_fraction_median=float(np.median([r['second_redundant_fraction'] for r in frame_rows if r['second_redundant_fraction'] is not None])),
            case_categories=dict(Counter(c['category'] for c in cases)),
            examples={k:next(c for c in cases if c['failure']==k) for k in kinds},
            caution='Ground truth names recovering windows only for explanation. No alternative score is run; no novel-method or budget claim.')
        dump(out/'summary.json',summary);write_csv(out/'all_129_cases.csv',cases)
        write_csv(out/'all_240_windows.csv',window_rows);write_csv(out/'all_48_frames.csv',frame_rows)
        dump(out/'cases.json',cases);dump(out/'input_hashes.json',hashes)
        dump(out/'status.json',dict(status='PASS',model_loaded=False,inference_calls=0,cases=129,cache_identity=True,
                                   script_sha256=sha(__file__)))
        print(json.dumps(summary,ensure_ascii=False,indent=2))
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8')
        dump(out/'status.json',dict(status='FAILED',model_loaded=False));raise


if __name__=='__main__':main()
