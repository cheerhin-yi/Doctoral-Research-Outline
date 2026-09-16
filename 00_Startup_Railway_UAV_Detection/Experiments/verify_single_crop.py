"""BTD8 saved-output identity, set algebra, timing, and resource audit."""
import csv
import json
import shutil
from pathlib import Path
import numpy as np
from diagnose_bt1 import BASE, sha, dump

out=BASE/'BTD8-SINGLE-20260914-01';src=BASE/'BTD1-CAL48-20260913-01'
summary=json.loads((out/'summary.json').read_text());cache=json.loads((out/'cache_summary.json').read_text())
assert summary['status']==cache['status']=='PASS'
for p,h in json.loads((out/'input_hashes.json').read_text()).items():assert sha(p)==h
rows=list(csv.DictReader((out/'all_240_single_windows.csv').open(encoding='utf-8-sig')))
frames=list(csv.DictReader((out/'all_48_frames.csv').open(encoding='utf-8-sig')))
assert len(rows)==240 and len(frames)==48
for i,f in enumerate(frames):
    s=json.loads((out/f'cache_{i:02d}.json').read_text());r=json.loads((src/f'image_{i:02d}.json').read_text());small={d['id'] for d in r['small_gt_details']}
    pairs={int(j):set(v) for j,v in s['match_ids'].items()};first=int(f['first']);best=min(pairs,key=lambda j:(-len(pairs[j]&small),j))
    assert best==int(f['best']) and first==r['selected']['density'][0]
    for row in [x for x in rows if x['image']==f['image']]:
        found=pairs[int(row['window'])]
        assert int(row['small_tp'])==len(found&small)
        assert set(json.loads(row['gained_ids']))==(found-pairs[first])&small
        assert set(json.loads(row['lost_ids']))==(pairs[first]-found)&small
    assert np.array_equal(np.load(out/f'actual_k1_{i:02d}.npy'),np.load(out/f'expected_k1_{i:02d}.npy'))
for key,total in cache['totals'].items():assert sum(int(f[key]) for f in frames)==total
times=list(csv.DictReader((out/'timings.csv').open(encoding='utf-8-sig')))
assert len(times)==len({(r['image'],r['method'],r['repeat']) for r in times})==288
assert len([r for r in times if r['method']=='K1'])==144
for t in times:
    assert abs(sum(float(t[k]) for k in ['convert_windows_ms','global_ms','selection_ms','local_ms','merge_ms'])-float(t['total_ms']))<1e-5
    assert float(t['total_ms'])>0 and np.isfinite(float(t['total_ms']))
ref=[np.median([float(t['total_ms']) for t in times if t['image']==f['image'] and t['method']=='F1280']) for f in frames]
assert int(np.ceil(np.percentile(ref,95)))==summary['T_ms']
for method in ['K1','F1280']:
    vals=np.array([float(t['total_ms']) for t in times if t['method']==method])
    assert abs(vals.mean()-summary['timing'][method]['mean_ms'])<1e-8
    assert np.mean(vals>summary['T_ms'])==summary['timing'][method]['over_T_fraction']
resources=[json.loads(line) for line in (out/'resources.jsonl').read_text().splitlines()]
assert len([r for r in resources if r['phase']=='cache'])==48
assert len([r for r in resources if r['phase']=='timing'])==334
assert all(r['rss']<=3*(1<<30) and r['private']<=4*(1<<30) and r['available']>=256*(1<<20) and r['elapsed_seconds']<=900 for r in resources)
assert summary['k1_exact_outputs']==144 and summary['k1_max_abs_diff']==0 and summary['F1280_exact_repeats']==96
assert sha(out/'check_single_crop.py')==json.loads((out/'environment.json').read_text())['script_sha256']
checks=dict(status='PASS',images=48,windows=240,timing_calls=288,k1_exact_outputs=144,reference_exact_repeats=96,input_hashes_unchanged=True,gain_loss_ids_reconciled=True,GT_best_tie_rule=True,budget_recomputed=True,
    resource_samples=len(resources),sampled_limits_pass=True,max_sampled_rss=max(r['rss'] for r in resources),max_sampled_private=max(r['private'] for r in resources),min_sampled_available=min(r['available'] for r in resources),script_snapshot_matches=True)
dump(out/'verification.json',checks);shutil.copy2(__file__,out/Path(__file__).name)
dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
print(json.dumps(checks))
