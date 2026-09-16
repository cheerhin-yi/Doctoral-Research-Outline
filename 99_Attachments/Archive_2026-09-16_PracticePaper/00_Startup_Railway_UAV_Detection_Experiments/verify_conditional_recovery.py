"""Audit BTD7 identities and set algebra from saved match IDs, no inference."""
import csv
import json
from pathlib import Path
from collections import Counter
from diagnose_bt1 import BASE, sha, dump

out=BASE/'BTD7-RESIDUAL-20260914-02';src=BASE/'BTD1-CAL48-20260913-01'
summary=json.loads((out/'summary.json').read_text())
assert summary['status']=='PASS'
for name,h in json.loads((out/'input_hashes.json').read_text()).items():assert sha(name)==h
cases=json.loads((out/'cases.json').read_text())
windows=list(csv.DictReader((out/'all_240_windows.csv').open(encoding='utf-8-sig')))
frames=list(csv.DictReader((out/'all_48_frames.csv').open(encoding='utf-8-sig')))
assert len(cases)==len({(c['image'],c['gt_row']) for c in cases})==105
assert len(windows)==240 and len(frames)==48
for i,frame in enumerate(frames):
    record=json.loads((src/f'image_{i:02d}.json').read_text())
    saved=json.loads((out/f'frame_{i:02d}.json').read_text())
    f=saved['frame'];first=set(saved['first_match_ids']);pairs={int(j):set(ids) for j,ids in saved['pair_match_ids'].items()}
    small={d['id'] for d in record['small_gt_details']};rec={d['id'] for d in record['small_gt_details'] if d['recoverable']}
    residual=rec-pairs[f['second']]
    assert residual=={c['gt_row'] for c in cases if c['image']==record['image']}
    assert f['first_small_tp']==len(first&small) and first==pairs[f['first']]
    rows=[r for r in windows if r['image']==record['image']]
    assert len(rows)==len(pairs)
    for r in rows:
        pair=pairs[int(r['window'])];gain=(pair-first)&small;loss=(first-pair)&small
        assert set(json.loads(r['gained_ids']))==gain and set(json.loads(r['lost_ids']))==loss
        assert len(gain)-len(loss)==int(r['net'])
    alternatives=[j for j in pairs if j!=f['first']]
    best=min(alternatives,key=lambda j:(-len(pairs[j]&small),j));assert best==f['oracle_second']
    for c in [c for c in cases if c['image']==record['image']]:
        assert c['fixing_second_windows']==[j for j in alternatives if c['gt_row'] in pairs[j]]
assert Counter(c['failure'] for c in cases)==summary['failures']
assert summary['totals']['second_gain']-summary['totals']['second_loss']==summary['totals']['second_net']
assert summary['totals']['dedup_small_tp']-summary['totals']['first_small_tp']==summary['totals']['second_net']
status=json.loads((out/'status.json').read_text())
assert sha(out/status['script_entry'])==status['script_sha256']
checks=dict(status='PASS',cases=105,windows=240,frames=48,input_hashes_unchanged=True,case_ids_exact=True,gain_loss_sets_exact=True,oracle_tie_rule_verified=True,script_snapshot_matches=True,model_loaded=False,inference_calls=0)
dump(out/'verification.json',checks)
dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
print(json.dumps(checks))
