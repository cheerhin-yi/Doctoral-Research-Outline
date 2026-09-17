# Stage D — Evaluation channel decision (2026-09-17 Asia/Shanghai)

## Decision: READY (Case 1 + Case 3)

- **Case 1 (legal local GT):** Ultralytics assets mirror `VisDrone2019-DET-test-dev.zip` includes images + annotations (1610). Audited in A0-05; SHA registered there.
- **Case 3 (repo evaluator):** Same VisDrone-compatible path as Stage C (`diagnose_bt1.prepare_gt` + `match_gt`) + official toolkit archive present under `11_Datasets/processed/VisDrone/`.
- **Not Case 2:** Official challenge server / Drive package not used (historical acquisition error; no live submission).

## Label for all Stage D metrics

> VisDrone-compatible evaluator on Ultralytics-mirror test-dev **local GT** — **not** official VisDrone challenge leaderboard AP.

## Caveats (from A0-05)

- Ultralytics train/test-dev ZIPs may differ from original challenge packages; only val ZIP SHA matched the official verification package.
- Academic / internal benchmark use only; do not claim official challenge ranking.
