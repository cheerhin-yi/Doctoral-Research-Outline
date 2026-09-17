from pathlib import Path

prac = Path('00_Practice_UAV_Aerial_Detection')
stage = prac / 'Experiments' / 'P0_Benchmark' / 'stage_a'
report = prac / 'Experiments' / 'P0_Benchmark_Environment_Freeze.md'
tracker = prac / 'Experiments' / 'Experiment_Tracker.md'
run_id = 'P0-BENCH-A-ENV-20260917-01'

# tolerate alternate snapshot filenames
def read_first(names):
    for n in names:
        p = stage / n
        if p.exists():
            return p.read_text(encoding='utf-8')
    raise FileNotFoundError(names)

w = read_first(['weight_sha_reverify.txt','weight_sha256.txt'])
c = read_first(['cal48_identity.txt','cal48_id.txt'])
g = read_first(['gpu_snapshot.txt','gpu.txt'])
git = read_first(['git_snapshot.txt','git.txt'])
env = read_first(['env_snapshot.txt','env.txt'])
sahi = read_first(['sahi_status.txt','sahi.txt'])

w_paths = [ln.split('=',1)[1] for ln in w.splitlines() if ln.startswith('path=')]
disk_sha = [ln.split('=',1)[1] for ln in w.splitlines() if ln.startswith('sha256=')][0]
cal_path = [ln.split('=',1)[1] for ln in c.splitlines() if ln.startswith('path=')][0]
cal_sha = [ln.split('=',1)[1] for ln in c.splitlines() if ln.startswith('sha256=')][0]
expected = 'bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533'
assert disk_sha == expected, (disk_sha, expected)

def slash(p):
    return p.replace('\\','/')

md = f"""# P0 Benchmark — Stage A Environment & SHA Freeze

- **Run ID:** `{run_id}`
- **Date:** 2026-09-17 Asia/Shanghai
- **Scope:** Stage A only (no training, no Stage B)
- **A_STATUS: PASS**

## Weight

| Item | Value |
|---|---|
| Primary | `{slash(w_paths[0])}` |
| Archive twin | `{slash(w_paths[1])}` |
| Expected SHA256 | `{expected}` |
| Actual SHA256 | `{disk_sha}` |
| Match | **YES** |
| Bytes | 5457882 |

Evidence: `Experiments/P0_Benchmark/stage_a/weight_sha_reverify.txt`

## Dataset identity (cal48)

| Item | Value |
|---|---|
| Manifest | `{slash(cal_path)}` |
| Manifest SHA256 | `{cal_sha}` |
| Counts | lines=48, images=48, labels=48, annotations=48 |
| Resampled? | **No** |

Evidence: `Experiments/P0_Benchmark/stage_a/cal48_identity.txt`

## Git

```
{git.strip()}
```

## Hardware (this host)

```
{g.strip()}
```

### Known limitation for Stage B–D

This host has **GTX 1660 SUPER ×1**, not RTX 4090. Historical BT1/BTD latency on 1660 remains historical-only. Formal unified 4090 timing table is **blocked on this machine** until a pinned 4090 UUID is used. Do not mix 1660 and 4090 numbers in one fairness table.

## Software

Reuse conda env: `H:/Conda/envs/UAV_BT1` (base `E:/miniconda3`). No reinstall.

```
{env.strip()}
```

pip freeze: `Experiments/P0_Benchmark/stage_a/pip_freeze.txt`

### SAHI

```
{sahi.strip()}
```

Stage B **M5-only** blocker. Stage A PASS still holds.

## Five methods (definitions frozen; not executed)

| ID | Method | Note |
|---|---|---|
| M1 | F640 | full-frame 640 |
| M2 | F1280 | full-frame 1280; P0-EI-C1 strong simple baseline |
| M3 | DensK1 | recover from BTD8 only |
| M4 | UnifAll | same grid as DensK1, all windows |
| M5 | SAHI640 | 640 / overlap 0.25; needs sahi |

DensK1 extract: `Experiments/P0_Benchmark/stage_a/densk1_definition_extract.md`  
Locked summary: window 640; candidate grid yields 240 windows; density from coarse dets conf≥0.25; Top-1; BTD5 CPU NMS class-wise IoU>0.5 max500; eval conf=.25 IoU=.5; small area <1024 original px.

## Evaluation gates

- conf=0.25, IoU=0.50, batch=1
- small: 0 < w*h < 1024 original pixels
- VisDrone ignore/class/match: A0-07 / Label Adapter (`stage_a/evaluator_notes.md`)
- Name Ultralytics-native AP separately from VisDrone-compatible evaluator

## Timing boundary (registered for B; not run)

Decoded image → final evaluable dets; include preprocess/select/crop/resize/infer/restore/merge/NMS; sync CUDA; disk I/O separate. Budget grid: 10/15/20/25/30/40/50/75/100 ms.

## Statistical unit (registered for F; not run)

Unit = **image**. Primary pair F1280 vs DensK1.

## Script SHA256

`Experiments/P0_Benchmark/stage_a/script_sha256.txt`

## Risks / blockers

1. `sahi` missing → M5 blocked until install without stack upgrade.
2. No 4090 on this host → B–D unified 4090 latency blocked here.
3. No P0 five-method orchestrator / UnifAll runner yet.
4. Hard bans remain: no train, no net change, no BTD13, no test-dev tuning.

## Next

**Stage B — waiting for user continuation** (do not auto-start).
"""
report.write_text(md, encoding='utf-8')
print('report', report, report.stat().st_size)

entry = f"""
## P0 Benchmark Stage A ({run_id})

| Run ID | Stage | Goal | Hardware | Env | Status | Artifacts |
|---|---|---|---|---|---|---|
| {run_id} | A | Env & SHA freeze for P0 five-method benchmark | GTX 1660 SUPER | H:/Conda/envs/UAV_BT1 | DONE / PASS | [Freeze report](P0_Benchmark_Environment_Freeze.md); `P0_Benchmark/stage_a/` |

Notes: weight SHA match; cal48 n=48 frozen; sahi missing (M5 blocker); 4090 not present (B–D unified latency blocker on this host). No training. Stage B not started.

---
"""
old = tracker.read_text(encoding='utf-8')
if run_id not in old:
    parts = old.splitlines(True)
    if parts and parts[0].startswith('#'):
        new = parts[0] + '\n' + entry + ''.join(parts[1:])
    else:
        new = entry + old
    tracker.write_text(new, encoding='utf-8')
    print('tracker updated')
else:
    print('tracker already has run id')
