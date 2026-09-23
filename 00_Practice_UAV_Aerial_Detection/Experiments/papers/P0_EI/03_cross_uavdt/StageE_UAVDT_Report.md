# P0 Benchmark Stage E Report — UAVDT External Transfer (Frozen Weights)

- **Date:** 2026-09-20 (Asia/Shanghai); run finished 2026-09-18
- **Run ID:** `P0-BENCH-E-UAVDT-20260918-FULL`
- **Status:** **DONE / PASS**
- **Claim under test:** On a **frozen** VisDrone-trained detector, changing the **inference protocol** systematically moves aerial small-object recall–precision–cost trade-offs; Stage E checks whether the coarse trend transfers to UAVDT (not UAVDT SOTA / not official MATLAB AP).

---

## 1. Gates (frozen before scores)

| Gate | Result |
|---|---|
| UAVDT DET layout | PASS — 50 sequences / **40735** frames / 50 `*_gt_whole.txt` |
| Class mapping | `class_mapping_preregister.json` **FROZEN_PRE_RESULTS** (VisDrone→UAVDT vehicle subset) |
| Weight | frozen VisDrone `last.pt`, SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` — **no** UAVDT fine-tune |
| Ignore masks | official `*_gt_ignore.txt` **not** applied (do not invent VisDrone-style ignore) |
| Evaluator | VisDrone-compatible `prepare_gt` / `match_gt` after pred remap — transfer trend check only |

Config freeze: `stage_e/config_freeze.json` · Channel: `stage_e/channel_decision.md`

---

## 2. Setup

| Item | Value |
|---|---|
| Methods (one-shot) | `F640`, `F1280`, `DensK1`, `UnifAll`, `SAHI640` |
| conf / IoU / small | 0.25 / 0.5 / `0 < w·h < 1024` (original pixels, score>0 GT) |
| GPU | NVIDIA GeForce GTX 1660 SUPER |
| Wall time | **17149.2 s** (~4.76 h) |
| Artifacts | `stage_e/P0-BENCH-E-UAVDT-20260918-FULL/` (`summary.json`, `per_image_metrics.csv`, `status.json`) |
| Smoke | `P0-BENCH-E-UAVDT-20260918-01` (24 images) PASS before full |

---

## 3. Full-run results (n = 40735)

| Method | small_recall | precision | mean_ms | small_tp / small_gt | tp / fp |
|---|---:|---:|---:|---:|---:|
| **F1280** | **0.793** | 0.372 | 33.1 | 391579 / 493861 | 671489 / 1134085 |
| UnifAll | 0.782 | 0.332 | 47.2 | 386393 / 493861 | 668237 / 1346758 |
| DensK1 | 0.767 | 0.347 | 33.0 | 378871 / 493861 | 658280 / 1236148 |
| SAHI640 | 0.760 | 0.353 | 164.0 | 375203 / 493861 | 648364 / 1188553 |
| F640 | 0.708 | **0.430** | **16.7** | 349664 / 493861 | 623956 / 826262 |

Ranking by small_recall: **F1280 > UnifAll > DensK1 > SAHI640 > F640**.

---

## 4. Cross-set read vs Stage D (VisDrone test-dev)

Stage D (n=1610) small_recall order was roughly **UnifAll > F1280 > DensK1 > F640 > SAHI640**.

| Pattern | VisDrone D | UAVDT E | Read |
|---|---|---|---|
| F640 weakest small_recall | yes | yes | **consistent** |
| Higher-res / tiling lifts small_recall vs F640 | yes | yes | **consistent** |
| Precision often falls as recall rises | yes (esp. UnifAll/SAHI) | yes | **consistent trade-off story** |
| Method rank order | UnifAll tops | F1280 tops | **not fully stable** |
| SAHI position | bottom | mid | **dataset-sensitive** |

**Allowed claim:** inference protocol systematically changes small-object recall–precision–cost on both sets.

**Disallowed / overclaim:** a single universal five-method ranking across datasets.

---

## 5. Publication gate (recorded)

- **EI (default):** D+F+E dual-set table is enough to tell the transfer story; still add protocol appendix + failure cases for a stronger EI.
- **JCR Q4:** needs thickness (neighbor-protocol comparison table, thick cross-set/failure analysis, optional formal 4090 timing). Do **not** rush a homogeneous third dataset.
- **Still frozen:** no training; no class-mapping edit.

---

## 6. Next sole checkable task (after this report lands)

Optional / EI packaging: formal **4090** timing table (1660 latency stays pipeline-validation only) + neighbor-protocol comparison table + failure/boundary examples. Accuracy tables keep D/E numbers; do not mix 1660+4090 in one latency column.

---

## 7. Non-claims

- Not official UAVDT MATLAB AP / not leaderboard SOTA.
- Not a new detector or training recipe.
- 1660 `mean_ms` is on-device wall for this run, not the formal paper latency table.
