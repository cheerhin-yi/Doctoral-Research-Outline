# P0 Benchmark Stage D — VisDrone test-dev one-shot (local mirror GT)

- **Run ID:** P0-BENCH-D-TESTDEV-20260917-01
- **Status:** **PASS** (protocol completed; not a quality claim)
- **Finished:** 2026-09-17 14:33 Asia/Shanghai
- **Wall time:** 1128.1 s (~18.8 min)
- **GPU:** NVIDIA GeForce GTX 1660 SUPER (pipeline host; formal 4090 timing still deferred)
- **Images:** 1610 (full test-dev)
- **Frozen conf / IoU:** 0.25 / 0.5
- **Small def:** 0<w*h<1024 original image space; score>0 GT
- **Weight SHA256:** bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533
- **ZIP SHA256:** b28a94b06dfd9e36ce77ff8155fb82b9d2c030f198a76105933bd56c6ea6a68d

## Evaluation channel

**READY — Case 1 + Case 3**

VisDrone-compatible evaluator on Ultralytics-mirror test-dev local GT (not official leaderboard AP)

Evaluator: diagnose_bt1.prepare_gt+match_gt (VisDrone-compatible; not official server)

Do **not** treat these numbers as official VisDrone challenge leaderboard AP.

## Aggregate (image-pooled counts; primary unit for inference remains image)

| Method | TP | FP | Precision | small TP | small GT | small Recall | mean ms/img |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 28346 | 13911 | 0.6708 | 12042 | 50431 | 0.2388 | 17.4 |
| F1280 | 37767 | 18160 | 0.6753 | 20194 | 50431 | 0.4004 | 33.7 |
| DensK1 | 35662 | 23075 | 0.6071 | 18133 | 50431 | 0.3596 | 34.1 |
| UnifAll | 41705 | 39695 | 0.5123 | 22751 | 50431 | 0.4511 | 112.2 |
| SAHI640 | 26086 | 46632 | 0.3587 | 11016 | 50431 | 0.2184 | 373.2 |

## One-shot discipline

- Config frozen before opening results (stage_d/config_freeze.json, channel_decision.md).
- Five methods each predicted once; no retune after seeing scores.
- Bad or surprising outcomes retained as-is.
- Predictions: stage_d/P0-BENCH-D-TESTDEV-20260917-01/preds/ (8050 .npy = 1610×5).
- Per-image metrics: per_image_metrics.csv (for Stage F paired tests).

## Rough ranking on this host (small recall)

1. UnifAll (0.451) — highest small recall, lowest precision, ~112 ms
2. F1280 (0.400) — strong simple baseline, best precision among top recall methods, ~34 ms
3. DensK1 (0.360) — below F1280 on small recall here (same direction as cal48 Stage C)
4. F640 (0.239) — fastest, weakest small recall among full-frame/density set
5. SAHI640 (0.218) — slowest and weakest small recall on this frozen setup

## Not done in Stage D

- Stage F image-level Wilcoxon / bootstrap (use per_image_metrics.csv)
- Formal 4090 latency table
- Stage E external dataset (optional; needs separate go-ahead)
- Git push of artifacts

## Artifacts

- 00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_d/P0-BENCH-D-TESTDEV-20260917-01/summary.json
- 00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_d/P0-BENCH-D-TESTDEV-20260917-01/per_image_metrics.csv
- 00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_d/P0-BENCH-D-TESTDEV-20260917-01/status.json
- Experiments/P0_Benchmark/stage_d/channel_decision.md
- Experiments/P0_Benchmark/stage_d/config_freeze.json
