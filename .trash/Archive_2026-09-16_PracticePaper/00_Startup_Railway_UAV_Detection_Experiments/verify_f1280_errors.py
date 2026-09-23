"""BTD11 saved-set, single-attribute and maximum-matching certificate checks."""
from collections import Counter, defaultdict, deque
import csv
import json
from pathlib import Path
import shutil
import sys
import numpy as np
from diagnose_bt1 import BASE, sha, dump, prepare_gt, match_gt, ignore_keep

OUT = BASE/'BTD11-ERROR-20260914-01'


def read_csv(name):
    with (OUT/name).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))


def certify_maximum(edges, pairs):
    """No augmenting path exists: independent certificate, no matching solver reuse."""
    edges = {int(k):list(map(int,v)) for k,v in edges.items()}
    gp = {int(x['gt_row']):int(x['pred_id']) for x in pairs}
    pg = {p:g for g,p in gp.items()}
    assert len(gp)==len(pg)==len(pairs)
    for g,p in gp.items(): assert p in edges[g]
    reached_g = set(edges)-set(gp); reached_p=set(); queue=deque(reached_g)
    while queue:
        g=queue.popleft()
        for p in edges[g]:
            if gp.get(g)==p or p in reached_p: continue
            reached_p.add(p)
            assert p in pg, 'Unmatched prediction reached: matching is not maximum'
            other=pg[p]
            if other not in reached_g:
                reached_g.add(other);queue.append(other)
    # Minimum vertex cover constructed from alternating reachability has matching size.
    cover_g=set(edges)-reached_g
    assert len(cover_g)+len(reached_p)==len(pairs)
    assert all(g in cover_g or p in reached_p for g,ps in edges.items() for p in ps)


def main():
    s=json.loads((OUT/'summary.json').read_text())
    assert s['status']=='PASS'
    original_manifest=json.loads((OUT/'output_manifest.json').read_text())
    for name,v in original_manifest.items():
        assert sha(OUT/name)==v['sha256'] and (OUT/name).stat().st_size==v['bytes']
    hashes=json.loads((OUT/'input_hashes.json').read_text())
    for p,v in hashes.items(): assert sha(p)==v
    cases=read_csv('missed_small_gt.csv');allgt=read_csv('all_small_gt.csv')
    fps=read_csv('false_positives.csv');pairs=read_csv('repair_pairs.csv')
    keys={(x['image'],int(x['gt_row'])) for x in cases}
    assert len(keys)==len(cases)==1408 and len(allgt)==2720 and len(fps)==839
    counts=Counter(x['group'] for x in cases);assert dict(counts)==s['missed_groups']
    assert dict(Counter(x['group'] for x in fps))==s['fp_groups']
    for flag in s['missed_flags']:
        assert sum(json.loads(x['flags'])[flag] for x in cases)==s['missed_flags'][flag]
    totals=defaultdict(Counter);expected_keys=set();class_gains=defaultdict(Counter)
    class_confusion=Counter();capacities=Counter();assignment_gaps=[]
    for i in range(48):
        frame=json.loads((OUT/f'frame_{i:02d}.json').read_text())
        saved={k:set(v) for k,v in json.loads((OUT/f'matches_{i:02d}.json').read_text()).items()}
        info=json.loads((BASE/'BTD1-CAL48-20260913-01'/f'image_{i:02d}.json').read_text())
        old=json.loads((BASE/'BTD9-F1280-20260914-01'/f'matches_{i:02d}.json').read_text())
        base=set(old['F1280']);small={d['id'] for d in info['small_gt_details']}
        assert saved['threshold_0.25']==base
        expected_keys.update((frame['image'],g) for g in small-base)
        assert frame['small_fn']==len(small-base)
        trace=json.loads((OUT/f'trace_{i:02d}.json').read_text())
        used={x['pred_id'] for x in trace if x['state']=='TP'}
        assert len(used)==len(base)
        pred=np.load(BASE/'BTD8-SINGLE-20260914-01'/f'reference_F1280_{i:02d}.npy')
        ann=BASE/'full_data_v2/annotations/cal48'/Path(info['image']).with_suffix('.txt')
        raw=np.loadtxt(ann,delimiter=',',ndmin=2)
        gt,gids,integral=prepare_gt(raw,info['height'],info['width'])
        edges=json.loads((OUT/f'edges_{i:02d}.json').read_text())
        for kind in ['score','localization','classification']:
            chosen=[x for x in pairs if x['image']==frame['image'] and x['kind']==kind]
            certify_maximum(edges[kind],chosen)
            modified=np.load(OUT/f'repair_{kind}_{i:02d}.npy')
            assert modified.shape==pred.shape
            pids={int(x['pred_id']) for x in chosen}
            assert not pids & used
            expected=pred.copy()
            for x in chosen:
                g=int(x['gt_row']);p=int(x['pred_id']);assert g in small-base
                a=pred[p];b=raw[g]
                inter=np.maximum(0,np.minimum(a[2:4],b[:2]+b[2:4])-np.maximum(a[:2],b[:2])).prod()
                iou=float(inter/max(1e-12,(a[2]-a[0])*(a[3]-a[1])+b[2]*b[3]-inter))
                assert abs(iou-float(x['original_iou']))<1e-12
                if kind=='score':
                    assert .001<=a[4]<.25 and a[5]==b[5]-1 and iou>=.5
                    expected[p,4]=.25
                elif kind=='localization':
                    assert a[4]>=.25 and a[5]==b[5]-1 and .1<=iou<.5
                    expected[p,:4]=[*b[:2],*(b[:2]+b[2:4])]
                else:
                    assert a[4]>=.25 and a[5]!=b[5]-1 and iou>=.5
                    expected[p,5]=b[5]-1
                    class_confusion[f'{int(a[5])+1}->{int(b[5])}']+=1
            assert np.array_equal(expected,modified)
            found,fp,ignored=match_gt(gt,gids,modified,integral,info['height'],info['width'])
            name='repair_'+kind
            assert found==saved[name] and fp==frame['metrics'][name]['fp']
            capacities[kind]+=len(chosen)
            expected_targets={int(x['gt_row']) for x in chosen}
            if not expected_targets<=found:
                assignment_gaps.append(dict(image=frame['image'],kind=kind,
                    assigned_targets_not_matched=sorted(expected_targets-found),
                    other_new_matched=sorted((found-base)-expected_targets)))
            for g in (found-base)&small: class_gains[kind][str(int(raw[g,5]))]+=1
        for name,metric in frame['metrics'].items():
            found=saved[name]
            assert metric['small_tp']==len(found & small) and metric['tp']==len(found)
            assert metric['gain']==len((found-base)&small) and metric['loss']==len((base-found)&small)
            assert metric['gain']-metric['loss']==metric['small_tp']-len(base & small)
            totals[name].update(metric)
    assert expected_keys==keys
    for name,vals in totals.items():
        for k,v in vals.items(): assert v==s['totals'][name][k],(name,k)
    for kind,v in capacities.items(): assert v==s['totals']['repair_'+kind]['capacity']
    for field in ['category','size_group','neighbor_group']:
        groups=defaultdict(Counter)
        for row in allgt:
            groups[row[field]].update(gt=1,tp=int(row['detected']=='True'),fn=int(row['detected']=='False'))
        assert dict(groups)==s['groups'][field]
    resources=[json.loads(x) for x in (OUT/'resources.jsonl').read_text().splitlines()]
    assert len(resources)==96
    assert all(x['rss']<=2*(1<<30) and x['available']>=256*(1<<20) and x['elapsed_seconds']<=600
               and x['free_disk']>=2*(1<<30) and x['output_bytes']<=128*(1<<20) for x in resources)
    assert sha(OUT/'analyze_f1280_errors.py')==json.loads((OUT/'status.json').read_text())['script_sha256']
    assert not any(x in sys.modules for x in ['torch','ultralytics'])
    checks=dict(status='PASS',images=48,small_gt=2720,unique_small_fn=1408,fp_rows=839,
                input_hashes=len(hashes),artifact_hashes=len(original_manifest),
                independent_maximum_certificates=144,single_attribute_repairs=True,
                repaired_evaluator_checks=144,matched_sets_and_groups_reconciled=True,
                sampled_resources=len(resources),sampled_peak_rss=max(x['rss'] for x in resources),
                model_loaded=False,inference_calls=0)
    dump(OUT/'verification.json',checks)
    dump(OUT/'repair_breakdown.json',dict(class_gains={k:dict(v) for k,v in class_gains.items()},
         class_confusion=dict(class_confusion),assignment_gaps=assignment_gaps))
    shutil.copy2(__file__,OUT/Path(__file__).name)
    dump(OUT/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p))
         for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
    print(json.dumps(checks));print(json.dumps(dict(class_gains=class_gains, class_confusion=class_confusion,
                                                   assignment_gaps=assignment_gaps)))


if __name__=='__main__': main()
