# Stage E — External validation channel decision

- **Date:** 2026-09-18 Asia/Shanghai
- **E_STATUS: READY**
- **Unblocked by:** Author UAVDT pack on `G:\Schloar Data\UAVDT\` layout PASS (50 sequences / 40735 frames / 50 `*_gt_whole.txt`).
- **Weight:** frozen VisDrone `last.pt` SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` — **no** UAVDT fine-tune.
- **Mapping:** `class_mapping_preregister.json` FROZEN before any Stage E scores.
- **Ignore policy (frozen):** do **not** invent VisDrone-style ignore masks; official `*_gt_ignore.txt` not applied.
- **Evaluator:** VisDrone-compatible `prepare_gt`/`match_gt` on mapped vehicle subset — **not** official UAVDT MATLAB AP / not SOTA.

## READY gates (checked 2026-09-18)

1. Local UAVDT DET images + whole GT — PASS
2. Frozen VisDrone→UAVDT class mapping before predictions — PASS
3. Same frozen last.pt, five methods one-shot — authorized; runner `run_stage_e_oneshot.py`

## Smoke (2026-09-18)
- PASS P0-BENCH-E-UAVDT-20260918-01 max-images=24 wall≈58s
- Methods F640/F1280/DensK1/UnifAll/SAHI640 all produced metrics

