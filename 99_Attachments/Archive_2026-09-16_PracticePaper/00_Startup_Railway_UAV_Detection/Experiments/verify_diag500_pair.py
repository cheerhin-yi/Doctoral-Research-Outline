"""Read-only BTD4 output audit, no detector invocation."""
import csv
import json
from pathlib import Path
import numpy as np
from diagnose_bt1 import BASE, sha, dump

out=BASE/'BTD4-DIAG500-20260913-01'
summary=json.loads((out/'summary.json').read_text());status=json.loads((out/'status.json').read_text())
assert status['status']=='PASS' and status['completed_images']==500
identity=json.loads((out/'data_identity.json').read_text());names=identity['diag500'];assert len(names)==len(set(names))==500
rows=[json.loads(p.read_text()) for p in sorted(out.glob('image_*.json'))]
assert [r['image'] for r in rows]==names
assert sum(r['small_gt'] for r in rows)==summary['small_gt']
assert sum(r['valid_gt'] for r in rows)==summary['valid_gt']
for i,r in enumerate(rows):
    p=np.load(out/f'predictions_{i:03d}.npz')
    assert r['selected']['density'][0]==r['selected']['dedup'][0]
    assert len(r['selected']['density'])==len(r['selected']['dedup'])<=2
    for m in ['density','dedup']:
        assert len(set(r['selected'][m]))==len(r['selected'][m])
        a=p[m];assert a.shape[1]==6 and len(a)<=500 and np.isfinite(a).all()
        assert np.all(a[:,4][:-1]>=a[:,4][1:]) and np.all((a[:,5]>=0)&(a[:,5]<10))
        assert np.all(a[:,[0,2]]>=0) and np.all(a[:,[0,2]]<=r['width']+.01)
        assert np.all(a[:,[1,3]]>=0) and np.all(a[:,[1,3]]<=r['height']+.01)
for m in ['density','dedup']:
    for k in ['tp','fp','small_tp']:
        assert sum(r['metrics'][m][k] for r in rows)==summary['metrics'][m][k]
times=list(csv.DictReader((out/'timings.csv').open(encoding='utf-8-sig')))
assert len(times)==3000 and len({(r['image'],r['method'],r['repeat']) for r in times})==3000
stages=['convert_windows_ms','global_ms','selection_ms','local_crop_detect_map_ms','merge_ms']
for r in times:
    assert r['image'] in names and r['method'] in ['density','dedup'] and r['repeat'] in ['0','1','2']
    assert abs(sum(float(r[k]) for k in stages)-float(r['total_ms']))<1e-5
    assert all(np.isfinite(float(r[k])) and float(r[k])>=0 for k in stages)
changes=list(csv.DictReader((out/'changed_small_gt.csv').open(encoding='utf-8-sig')))
assert len(changes)==summary['gained_small']+summary['lost_small']
assert summary['gained_small']-summary['lost_small']==summary['metrics']['dedup']['small_tp']-summary['metrics']['density']['small_tp']
rank=sorted(rows,key=lambda r:r['metrics']['dedup']['small_tp']-r['metrics']['density']['small_tp'],reverse=True)
concentration=dict(top5=[dict(image=r['image'],delta=r['metrics']['dedup']['small_tp']-r['metrics']['density']['small_tp']) for r in rank[:5]],
                    bottom5=[dict(image=r['image'],delta=r['metrics']['dedup']['small_tp']-r['metrics']['density']['small_tp']) for r in rank[-5:]])
flat=[dict(image=r['image'],small_gt=r['small_gt'],valid_gt=r['valid_gt'],
       density_small_tp=r['metrics']['density']['small_tp'],dedup_small_tp=r['metrics']['dedup']['small_tp'],
       gained=r['gained_small'],lost=r['lost_small']) for r in rows]
with (out/'per_image_summary.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=list(flat[0]));writer.writeheader();writer.writerows(flat)
dump(out/'concentration.json',concentration)
env=json.loads((out/'environment.json').read_text());assert sha(out/'run_diag500_pair.py')==env['script_sha256']
checks=dict(status='PASS',images=500,timing_frames=3000,stage_sums_match=True,counts_reconciled=True,
            finite_sorted_in_bounds=True,first_window_equal=True,repeated_output_mismatches=summary['repeat_output_mismatches'],script_snapshot_matches=True)
dump(out/'verification.json',checks)
print(json.dumps(checks));print(json.dumps(concentration))
