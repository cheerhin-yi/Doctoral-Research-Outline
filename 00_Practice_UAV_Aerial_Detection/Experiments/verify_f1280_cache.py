"""Independent saved-ID reconciliation for BTD9; no model invocation."""
import csv
import json
from pathlib import Path
import shutil
from diagnose_bt1 import BASE, sha, dump

out=BASE/'BTD9-F1280-20260914-01';src=BASE/'BTD1-CAL48-20260913-01'
s=json.loads((out/'summary.json').read_text());assert s['status']=='PASS'
for p,h in json.loads((out/'input_hashes.json').read_text()).items():assert sha(p)==h
totals={m:dict(tp=0,fp=0,small_tp=0) for m in s['totals']};expected_changes=set();n=0
for i in range(48):
    row=json.loads((out/f'image_{i:02d}.json').read_text());r=json.loads((src/f'image_{i:02d}.json').read_text())
    assert row['image']==r['image'];small={d['id'] for d in r['small_gt_details']};n+=len(small)
    matches={m:set(v) for m,v in json.loads((out/f'matches_{i:02d}.json').read_text()).items()}
    for m in matches:
        assert len(matches[m])==row['metrics'][m]['tp'] and len(matches[m]&small)==row['metrics'][m]['small_tp']
        for k in totals[m]:totals[m][k]+=row['metrics'][m][k]
    for other,pair in row['pairs'].items():
        a=matches['F1280']&small;b=matches[other]&small
        assert pair==dict(gain=len(a-b),loss=len(b-a),net=len(a)-len(b),common=len(a&b))
        expected_changes.update((row['image'],other,'F1280_only',gid) for gid in a-b)
        expected_changes.update((row['image'],other,'other_only',gid) for gid in b-a)
    assert row['image_GT_choice_small_tp']==max(row['metrics']['F1280']['small_tp'],row['metrics']['GT_best_K1']['small_tp'])
assert n==2720
for m,t in totals.items():
    for k,v in t.items():assert v==s['totals'][m][k]
changes=list(csv.DictReader((out/'changed_small_gt.csv').open(encoding='utf-8-sig')))
assert len(changes)==len(expected_changes) and {(r['image'],r['comparison'],r['kind'],int(r['gt_row'])) for r in changes}==expected_changes
for m in totals:assert sum(c[m] for c in s['classes'].values())==totals[m]['small_tp']
resources=[json.loads(line) for line in (out/'resources.jsonl').read_text().splitlines()]
assert len(resources)==48 and all(r['rss']<=2*(1<<30) and r['available']>=256*(1<<20) and r['elapsed_seconds']<=600 for r in resources)
assert sha(out/'compare_f1280_cache.py')==json.loads((out/'status.json').read_text())['script_sha256']
checks=dict(status='PASS',images=48,small_gt=n,methods=4,paired_changed_rows=len(changes),input_hashes_unchanged=True,target_sets_reconciled=True,classes_reconciled=True,sampled_resources_pass=True,script_snapshot_matches=True,model_loaded=False,inference_calls=0)
dump(out/'verification.json',checks);shutil.copy2(__file__,out/Path(__file__).name)
dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
print(json.dumps(checks))
