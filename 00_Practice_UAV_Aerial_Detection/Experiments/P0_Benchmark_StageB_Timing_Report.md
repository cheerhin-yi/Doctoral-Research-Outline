# P0 Benchmark Stage B — Timing (local bring-up)

- Run ID: P0-BENCH-B-TIMING-20260917-01
- Status: **PASS**
- GPU: NVIDIA GeForce GTX 1660 SUPER (pipeline bring-up only; formal 4090 table later)
- Images: 48 (cal48) × reps=3
- Methods: F640, F1280, DensK1, UnifAll, SAHI640
- Peak VRAM: 159038464 bytes

## Timing summary (ms)

| Method | mean | median | p95 | image-median mean | inconsistent reps |
|---|---:|---:|---:|---:|---:|
| F640 | 18.62 | 18.23 | 23.09 | 18.44 | 0 |
| F1280 | 33.15 | 32.88 | 38.73 | 32.78 | 0 |
| DensK1 | 35.34 | 34.63 | 43.20 | 34.82 | 0 |
| UnifAll | 96.42 | 105.79 | 134.92 | 95.14 | 0 |
| SAHI640 | 317.45 | 363.90 | 493.61 | 308.68 | 0 |

## Notes
- No training; frozen last.pt SHA matched at Stage A.
- 40 ms is NOT treated as a 1660/4090 business deadline; budget grid reported in summary.json.
- Predictions for rep0 saved under preds/ for Stage C.
- Do not mix these 1660 numbers with future 4090 fairness tables.
