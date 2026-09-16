"""BTD6 output audit, no detector invocation."""
import csv
import json
from pathlib import Path
import numpy as np
from diagnose_bt1 import BASE, sha, dump

out=BASE/'BTD6-PIPELINE-20260913-01'
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
env=json.loads((out/'environment.json').read_text());assert sha(out/'run_fast_pipeline.py')==env['script_sha256']
checks=dict(status='PASS',images=500,timing_frames=3000,stage_sums_match=True,counts_reconciled=True,
            finite_sorted_in_bounds=True,first_window_equal=True,repeated_output_mismatches=summary['repeat_output_mismatches'],script_snapshot_matches=True)
dump(out/'verification.json',checks)
print(json.dumps(checks));print(json.dumps(concentration))

old=BASE/'BTD4-DIAG500-20260913-01'
old_s=json.loads((old/'summary.json').read_text())
for field in ['metrics','small_gt','valid_gt','gained_small','lost_small','classes']:
    assert summary[field]==old_s[field]
for name,h in json.loads((out/'prior_input_hashes.json').read_text()).items():assert sha(old/name)==h
assert summary['old_output_comparisons']==3000 and summary['max_old_absolute_difference']<=1e-5
nms_checks=json.loads((out/'actual_input_nms_checks.json').read_text())
assert len(nms_checks)==240 and all(r['exact'] for r in nms_checks)
cal_times=list(csv.DictReader((out/'calibration_times.csv').open(encoding='utf-8-sig')))
assert len(cal_times)==432 and len({(r['image'],r['method'],r['repeat']) for r in cal_times})==432
ref=[np.median([float(r['total_ms']) for r in cal_times if r['image']==n and r['method']=='F1280']) for n in identity['cal48']]
assert summary['T_ms']==int(np.ceil(np.percentile(ref,95)))
resources=list(csv.DictReader((out/'resource_samples.csv').open(encoding='utf-8-sig')))
assert len(resources)==3636
assert all(int(r['rss_bytes'])<=3*(1<<30) and int(r['private_bytes'])<=4*(1<<30) and int(r['system_available_bytes'])>=256*(1<<20) for r in resources)
checks.update(actual_input_nms_checks=len(nms_checks),prior_input_hashes_unchanged=True,prior_metrics_unchanged=True,old_output_comparisons=3000,exact_old_outputs=summary['exact_old_outputs'],max_old_absolute_difference=summary['max_old_absolute_difference'],recalibrated_T_ms=summary['T_ms'],resource_samples=len(resources),sampled_resource_limits_pass=True)
dump(out/'verification.json',checks)
dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
print(json.dumps(checks))
