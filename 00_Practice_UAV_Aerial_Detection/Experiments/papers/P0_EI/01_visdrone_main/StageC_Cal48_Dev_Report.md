# P0 Benchmark Stage C — cal48 accuracy (development evidence)

- Run ID: P0-BENCH-C-CAL48-20260917-01
- Status: **PASS**
- Split: cal48 (**not** independent test)
- Predictions: Stage B rep0

| Method | TP | FP | Precision | small TP | small GT | small Recall |
|---|---:|---:|---:|---:|---:|---:|
| F640 | 1492 | 576 | 0.721 | 840 | 2720 | 0.309 |
| F1280 | 2010 | 839 | 0.706 | 1312 | 2720 | 0.482 |
| DensK1 | 1857 | 1051 | 0.639 | 1172 | 2720 | 0.431 |
| UnifAll | 2110 | 1572 | 0.573 | 1367 | 2720 | 0.503 |
| SAHI640 | 1345 | 1928 | 0.411 | 749 | 2720 | 0.275 |

## Notes
- DensK1 small_tp=1172 matches historical BTD8 density_small_tp lock.
- F1280 leads DensK1 on small recall on this bring-up GPU; interpret with Stage B latency.
- Do not call cal48 an independent test set.
