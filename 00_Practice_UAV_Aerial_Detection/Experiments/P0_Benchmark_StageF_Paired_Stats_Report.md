# P0 Benchmark Stage F — Image-level paired statistics

- **Run ID:** `P0-BENCH-F-TESTDEV-20260917-01`
- **Status:** PASS (analysis completed)
- **Source:** Stage D `00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_d/P0-BENCH-D-TESTDEV-20260917-01/per_image_metrics.csv`
- **Unit:** image (N=1610)
- **Bootstrap:** B=10000, seed=20260917, paired image resampling
- **Primary:** F1280 vs DensK1

## Rules honored

- Analysis unit = image (not boxes).
- recall_small undefined when small_gt=0 (excluded from Wilcoxon recall).
- Secondary p-values Holm-corrected; primary reported raw.
- Latency = Stage D one-shot total_ms (not median-of-3).

## Method aggregates (pooled; context only)

| Method | small recall | precision | mean ms |
|---|---:|---:|---:|
| F640 | 0.2388 | 0.6708 | 17.4 |
| F1280 | 0.4004 | 0.6753 | 33.7 |
| DensK1 | 0.3596 | 0.6071 | 34.1 |
| UnifAll | 0.4511 | 0.5123 | 112.2 |
| SAHI640 | 0.2184 | 0.3587 | 373.2 |

## Primary: F1280 vs DensK1 (recall_small)

- N_images with small GT: **1499** (nonzero diffs: 1089)
- Median Δ (F1280 − DensK1): **0.0000**
- Mean Δ: **0.0345**
- Wilcoxon p (two-sided): **2.997e-28**
- Aggregate small recall: F1280=0.4004, DensK1=0.3596, Δ=0.0409
- Bootstrap 95% CI for Δ small recall: **[0.0355, 0.0462]**
- Interpretation: **95% CI for delta small-recall does not cross 0.**

## Secondary Wilcoxon (recall_small) + Holm

| Pair | N | median Δ | p raw | p Holm |
|---|---:|---:|---:|---:|
| F640 vs F1280 | 1499 | -0.1429 | 5.994e-172 | 2.398e-171 |
| F1280 vs UnifAll | 1499 | -0.0370 | 2.927e-86 | 2.927e-86 |
| F1280 vs SAHI640 | 1499 | 0.1778 | 4.06e-183 | 2.03e-182 |
| DensK1 vs UnifAll | 1499 | -0.0667 | 8.617e-161 | 2.585e-160 |
| DensK1 vs SAHI640 | 1499 | 0.1395 | 1.59e-155 | 3.18e-155 |

## Bootstrap Δ (A − B)

| Pair | Δ small recall [95% CI] | Δ precision [95% CI] | Δ mean ms [95% CI] |
|---|---|---|---|
| F1280 vs DensK1 | 0.0409 [0.0355, 0.0462] | 0.0681 [0.0631, 0.0731] | -0.3 [-0.7, -0.0] |
| F640 vs F1280 | -0.1616 [-0.1675, -0.1559] | -0.0045 [-0.0110, 0.0018] | -16.3 [-16.6, -16.1] |
| F1280 vs UnifAll | -0.0507 [-0.0551, -0.0464] | 0.1629 [0.1583, 0.1677] | -78.5 [-79.5, -77.5] |
| F1280 vs SAHI640 | 0.1820 [0.1735, 0.1908] | 0.3166 [0.3090, 0.3239] | -339.5 [-343.4, -335.6] |
| DensK1 vs UnifAll | -0.0916 [-0.0966, -0.0866] | 0.0948 [0.0906, 0.0993] | -78.1 [-79.1, -77.2] |
| DensK1 vs SAHI640 | 0.1411 [0.1311, 0.1512] | 0.2484 [0.2411, 0.2555] | -339.2 [-343.1, -335.3] |

## Image-level win counts (descriptive)

| Pair | A better | B better | tie | Wilson p(A better) |
|---|---:|---:|---:|---|
| F1280 vs DensK1 | 720 | 369 | 410 | 0.480 [0.455, 0.506] |
| F640 vs F1280 | 53 | 1161 | 285 | 0.035 [0.027, 0.046] |
| F1280 vs UnifAll | 193 | 899 | 407 | 0.129 [0.113, 0.147] |
| F1280 vs SAHI640 | 1201 | 81 | 217 | 0.801 [0.780, 0.821] |
| DensK1 vs UnifAll | 21 | 1008 | 470 | 0.014 [0.009, 0.021] |
| DensK1 vs SAHI640 | 1122 | 144 | 233 | 0.748 [0.726, 0.770] |

## Latency note

Stage D timings are one-shot on GTX 1660 SUPER. Formal 4090 multi-rep latency remains deferred.

## Artifacts

- `00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_f/P0-BENCH-F-TESTDEV-20260917-01/summary.json`
- `00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_f/P0-BENCH-F-TESTDEV-20260917-01/wilcoxon_recall_small.csv`
- `00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_f/P0-BENCH-F-TESTDEV-20260917-01/bootstrap_deltas.csv`
