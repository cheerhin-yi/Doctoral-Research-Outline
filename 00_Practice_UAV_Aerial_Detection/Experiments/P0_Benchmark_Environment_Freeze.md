# P0 Benchmark — Stage A Environment & SHA Freeze

- **Run ID:** `P0-BENCH-A-ENV-20260917-01`
- **Date:** 2026-09-17 Asia/Shanghai
- **Scope:** Stage A only (no training, no Stage B)
- **A_STATUS: PASS**

## Weight

| Item | Value |
|---|---|
| Primary | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt` |
| Archive twin | `11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01/baseline_archive/BT1-LOCAL-20260913-01/train/weights/last.pt` |
| Expected SHA256 | `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` |
| Actual SHA256 | `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` |
| Match | **YES** |
| Bytes | 5457882 |

Evidence: `Experiments/P0_Benchmark/stage_a/weight_sha_reverify.txt`

## Dataset identity (cal48)

| Item | Value |
|---|---|
| Manifest | `11_Datasets/processed/VisDrone/BT1/full_data_v2/cal48.txt` |
| Manifest SHA256 | `b0e27b1dc10d952a927597022a1fe0cfa52714d45a89e4c3f36880c2a4a68e7f` |
| Counts | lines=48, images=48, labels=48, annotations=48 |
| Resampled? | **No** |

Evidence: `Experiments/P0_Benchmark/stage_a/cal48_identity.txt`

## Git

```
HEAD=604aeec623f2b9483906bb0bc06c317ad07a026a
short=604aeec
branch=main
--- status -sb ---
## main...origin/main
?? 00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/
--- porcelain ---
?? 00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/
```

## Hardware (this host)

```
timestamp=2026-09-17T12:44:05.6609022+08:00
GPU 0: NVIDIA GeForce GTX 1660 SUPER (UUID: GPU-43b14c17-b685-e8ad-ab90-abc0d70fca06)
--- query ---
index, name, uuid, memory.total [MiB], driver_version, power.limit [W], clocks.current.sm [MHz], mig.mode.current
0, NVIDIA GeForce GTX 1660 SUPER, GPU-43b14c17-b685-e8ad-ab90-abc0d70fca06, 6144 MiB, 591.86, 125.00 W, 300 MHz, [N/A]
```

### Known limitation for Stage B–D

This host has **GTX 1660 SUPER ×1**, not RTX 4090. Historical BT1/BTD latency on 1660 remains historical-only. Formal unified 4090 timing table is **blocked on this machine** until a pinned 4090 UUID is used. Do not mix 1660 and 4090 numbers in one fairness table.

## Software

Reuse conda env: `H:/Conda/envs/UAV_BT1` (base `E:/miniconda3`). No reinstall.

```
python 3.12.14 | packaged by conda-forge | (main, Sep  2 2026, 23:18:20) [MSC v.1944 64 bit (AMD64)]
executable H:\Conda\envs\UAV_BT1\python.exe
torch 2.7.1+cu126
torchvision 0.22.1+cu126
Creating new Ultralytics Settings v0.0.6 file  
View Ultralytics Settings with 'yolo settings' or at 'C:\Users\ChHao\AppData\Roaming\Ultralytics\settings.json'
Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/quickstart/#ultralytics-settings.
ultralytics 8.4.90
cv2 5.0.0
numpy 2.5.2
sahi MISSING ModuleNotFoundError No module named 'sahi'
PIL 12.3.0
cuda_available True
torch_cuda 12.6
cudnn 90701
device_count 1
device0 NVIDIA GeForce GTX 1660 SUPER
platform Windows-11-10.0.26200-SP0
```

pip freeze: `Experiments/P0_Benchmark/stage_a/pip_freeze.txt`

### SAHI

```
sahi_installed=False
note=Stage B M5-only blocker; Stage A can PASS with disclosure
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
