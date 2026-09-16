"""Reanalyse saved BTD1 outputs without inference; create audit tables and plot."""
import csv
import json
from pathlib import Path
import numpy as np
from diagnose_bt1 import BASE, RUNS, sha, dump, prepare_gt, match_gt
from check_visdrone_semantics import drop_ignored, match

OUT=BASE/'BTD1-CAL48-20260913-01'
rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(OUT.glob('image_*.json'))]
summary=json.loads((OUT/'summary.json').read_text())
assert len(rows)==48 and summary['images']==48
metrics=summary['metrics']
checks=[]
# Check the vectorized real-data adapter against the pre-existing literal evaluator
# on the first 3 fixed images (not a rerun of the historical synthetic suite).
for r in rows[:3]:
    raw=np.asarray([[float(v) for v in s.rstrip(',').split(',')] for s in
        (BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt')).read_text().splitlines() if s.strip()])
    p=np.load(OUT/f'predictions_{rows.index(r):02d}.npz')['F640']; p=p[p[:,4]>=.25]
    det=np.zeros((len(p),8));det[:,:4]=p[:,:4];det[:,2:4]-=det[:,:2];det[:,4]=p[:,4];det[:,5]=p[:,5]+1
    g,d=drop_ignored(raw.tolist(),det.tolist(),r['height'],r['width'])
    tp=fp=ign=0
    for c in range(1,11):
        gc=[x[:4]+[1-x[4]] for x in g if x[5]==c and x[2]>0 and x[3]>0]
        dc=[x[:5] for x in d if x[5]==c]
        gg,dd=match(gc,dc)
        tp+=sum(x[4]==1 for x in gg);fp+=sum(x[5]==0 for x in dd);ign+=sum(x[5]==-1 for x in dd)
    observed=r['metrics']['F640']
    assert (tp,fp,ign)==(observed['tp'],observed['fp'],observed['ignored'])
    checks.append(dict(image=r['image'],tp=tp,fp=fp,ignored=ign,literal_crosscheck='PASS'))

for i,r in enumerate(rows):
    data=np.load(OUT/f'predictions_{i:02d}.npz')
    assert all(np.isfinite(data[k]).all() for k in data.files)
    assert data['p3'].shape==(10,80,80) and data['p4'].shape==(10,40,40)
    assert len(r['small_gt_details'])==r['small_gt']
    assert sum(d['recoverable'] for d in r['small_gt_details'])==r['recoverable']
    assert all(len(v)<=2 for v in r['selected'].values())
    for k,v in r['selected'].items():
        expected=[int(j) for j in np.argsort(-np.array(r['scores'][k]),kind='stable')[:2]
                  if r['scores'][k][j]>0 or k=='density']
        assert v==expected
    for pred in [data[k] for k in metrics]:
        assert len(pred)<=500 and np.all(pred[:,4][:-1]>=pred[:,4][1:])
        assert np.all(pred[:,[0,2]]>=0) and np.all(pred[:,[0,2]]<=r['width']+.01)
        assert np.all(pred[:,[1,3]]>=0) and np.all(pred[:,[1,3]]<=r['height']+.01)

names={'F640':'全图640','Tall':'全部切片参考','density':'预测密度','low025':'低阈值0.25','low005':'低阈值0.05',
       'low001':'低阈值0.01','low0001':'低阈值0.001','raw_top_m':'匹配峰数原分数',
       'p3_only':'仅P3','raw_product':'原始跨层乘积','shift_p4':'移位P4','candidate':'完整候选'}
table=[]
for k,v in metrics.items():
    views=0 if k=='F640' else sum(len(r['windows']) if k=='Tall' else len(r['selected'][k]) for r in rows)
    table.append(dict(method=k,label=names[k],local_views=views,**v,
                      delta_small_recall_pp=100*(v['small_recall']-metrics['F640']['small_recall']),
                      relative_small_recall_gain_pct=100*(v['small_tp']/metrics['F640']['small_tp']-1)))
with (OUT/'comparison.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(table[0]));w.writeheader();w.writerows(table)
with (OUT/'per_image_comparison.csv').open('w',encoding='utf-8-sig',newline='') as f:
    fields=['image','small_gt','recoverable']+[k+'_recovered' for k in metrics]
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for r in rows: w.writerow(dict(image=r['image'],small_gt=r['small_gt'],recoverable=r['recoverable'],**{k+'_recovered':r['metrics'][k]['recovered'] for k in metrics}))

rng=np.random.default_rng(20260913)
sample=rng.integers(0,48,(10000,48)); denominator=np.array([r['recoverable'] for r in rows])[sample].sum(1)
paired={}
for k in ['density','low005','low001','raw_top_m','p3_only','shift_p4']:
    diff=np.array([r['metrics']['candidate']['recovered']-r['metrics'][k]['recovered'] for r in rows])
    ratio=100*diff[sample].sum(1)/denominator
    paired[k]=dict(delta_recovered=int(diff.sum()),win_tie_loss=[int(np.sum(diff>0)),int(np.sum(diff==0)),int(np.sum(diff<0))],
                   delta_recovery_rate_pp=100*diff.sum()/summary['recoverable'],
                   image_bootstrap_95_percentile_pp=np.percentile(ratio,[2.5,97.5]).tolist())
classes={}
for c in range(1,11):
    ds=[d for r in rows for d in r['small_gt_details'] if d['category']==c]
    classes[c]=dict(small_gt=len(ds),recoverable=sum(d['recoverable'] for d in ds),
       **{k+'_small_tp':sum(k in d['detected_by'] for d in ds) for k in ['F640','Tall','density','p3_only','candidate']})
recs=[d for r in rows for d in r['small_gt_details'] if d['recoverable']]
extra=dict(paired=paired,per_class=classes,
    candidate_center_covered_but_not_recovered=sum(d['candidate_center_covered'] and 'candidate' not in d['detected_by'] for d in recs),
    candidate_recovered_without_center_cover=sum(not d['candidate_center_covered'] and 'candidate' in d['detected_by'] for d in recs),
    recoverable_input_short_side_percentiles=np.percentile([d['input_short_side'] for d in recs],[10,50,90]).tolist(),
    all_control_scoring_ms_percentiles=np.percentile([r['all_control_scoring_seconds']*1000 for r in rows],[50,95]).tolist(),
    full_forward_with_hook_ms_percentiles=np.percentile([r['full_forward_with_hook_seconds']*1000 for r in rows],[50,95]).tolist(),
    total_windows=sum(len(r['windows']) for r in rows),
    cautions='Bootstrap resamples images, not independent source groups; exploratory stability only, not confirmatory CI. Cached accuracy has no E2E speed claim.')
dump(OUT/'analysis_details.json',extra)
dump(OUT/'verification.json',dict(status='PASS',images=48,finite_outputs=True,all_k_le_2=True,
     coordinate_and_sort_checks=True,literal_match_crosscheck=checks,
     executed_script_sha256=sha(OUT/'diagnose_bt1.py'),archive_check=json.loads((OUT/'archive_check.json').read_text())))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
keys=['F640','density','low001','raw_top_m','p3_only','candidate','shift_p4','Tall']
labels=['Full 640','Density (K=2)','Low threshold .01','Raw Top-M','P3 only','Candidate','Shifted P4','All tiles (reference)']
fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained')
values=[100*metrics[k]['small_recall'] for k in keys]
bars=ax.barh(labels,values,color=['#8197ad' if k not in ['candidate','Tall'] else '#c45d45' if k=='candidate' else '#aaaaaa' for k in keys])
ax.invert_yaxis();ax.set_xlim(0,60);ax.set_xlabel('Small-object recall (%) at confidence 0.25 / IoU 0.5')
ax.set_title('cal48 exploratory diagnosis | 2,720 valid small GT | same epoch-100 model')
ax.bar_label(bars,labels=[f'{v:.2f}%' for v in values],padding=4)
ax.spines[['top','right']].set_visible(False)
fig.savefig(OUT/'small_recall_comparison.png',dpi=170);fig.savefig(OUT/'small_recall_comparison.pdf');plt.close(fig)
print(json.dumps(extra,ensure_ascii=False,indent=2))
