#!/usr/bin/env python3
"""Run G accuracy-consistency gate (5060 Ti / UAV_BT2 vs frozen 1660 / UAV_BT1 records).

Read-only on frozen code: imports `eval_one` / `load_ann` from the frozen Stage D runner
(which itself uses diagnose_bt1.prepare_gt + match_gt). Nothing is re-tuned; this only
checks that the detections produced on the new GPU/env give the same per-image counts.

  --mode cal48   : evaluate stage_b/<run>/preds/{i:02d}_{m}_r0.npy on cal48 GT and compare
                   per (image, method) with papers/P0_EI/01_visdrone_main/data/C_cal48_metrics.csv
                   (Stage C = Stage B rep0 preds) and n_dets with 04_timing/data/B_TIMING_timings.csv.
  --mode testdev : compare stage_d/<run>/per_image_metrics.csv with
                   papers/P0_EI/01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv.
Writes stage_g/<run>/accuracy_consistency.json and accuracy_diff_rows.csv.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve()
P0B = HERE.parents[1]
EXP = HERE.parents[2]
ROOT = HERE.parents[4]
PAPER = EXP / "papers" / "P0_EI"
METHODS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
KEYS = ["n_dets", "tp", "fp", "ignored", "small_gt", "small_tp"]


def read_csv(p: Path):
    with p.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def to_int(v):
    return None if v in (None, "") else int(float(v))


def compare(new: dict, ref: dict, keys):
    """new/ref: {(image, method): {key: int}}"""
    diff_rows = []
    per_method = {m: {"pairs": 0, "pairs_with_any_diff": 0, "new_totals": defaultdict(int), "ref_totals": defaultdict(int),
                      "abs_diff_sum": defaultdict(int)} for m in METHODS}
    missing = sorted(set(ref) ^ set(new))
    for k in sorted(set(ref) & set(new)):
        img, m = k
        pm = per_method[m]
        pm["pairs"] += 1
        anyd = False
        row = {"image": img, "method": m}
        for key in keys:
            a, b = new[k].get(key), ref[k].get(key)
            if a is None or b is None:
                continue
            pm["new_totals"][key] += a
            pm["ref_totals"][key] += b
            pm["abs_diff_sum"][key] += abs(a - b)
            row[f"{key}_5060ti"] = a
            row[f"{key}_1660"] = b
            if a != b:
                anyd = True
        if anyd:
            pm["pairs_with_any_diff"] += 1
            diff_rows.append(row)
    out = {}
    for m, pm in per_method.items():
        out[m] = {"pairs": pm["pairs"], "pairs_with_any_diff": pm["pairs_with_any_diff"],
                  "totals_5060ti": dict(pm["new_totals"]), "totals_1660": dict(pm["ref_totals"]),
                  "delta_totals": {k: pm["new_totals"][k] - pm["ref_totals"][k] for k in pm["ref_totals"]},
                  "abs_diff_sum": dict(pm["abs_diff_sum"])}
        sg = pm["ref_totals"].get("small_gt")
        if sg:
            out[m]["small_recall_5060ti"] = pm["new_totals"]["small_tp"] / sg
            out[m]["small_recall_1660"] = pm["ref_totals"]["small_tp"] / sg
    return out, diff_rows, missing


def mode_cal48(run_id: str):
    import cv2
    sys.path.insert(0, str(P0B / "stage_d"))
    from run_stage_d_oneshot import eval_one  # frozen evaluator wrapper (diagnose_bt1)
    from diagnose_bt1 import BASE

    run_dir = P0B / "stage_b" / run_id
    paths = [Path(s.strip()) for s in (BASE / "full_data_v2/cal48.txt").read_text(encoding="utf-8").splitlines() if s.strip()]
    ann_dir = BASE / "full_data_v2/annotations/cal48"
    new = {}
    rep_consistency = defaultdict(lambda: {"checked": 0, "identical_to_r0": 0})
    for i, p in enumerate(paths):
        im = cv2.imread(str(p)); assert im is not None, p
        for m in METHODS:
            f = run_dir / "preds" / f"{i:02d}_{m}_r0.npy"
            assert f.exists(), f
            pred = np.load(f)
            r = eval_one(im, ann_dir / (p.stem + ".txt"), pred)
            new[(p.name, m)] = {"n_dets": int(len(pred)), **{k: int(r[k]) for k in ["tp", "fp", "ignored", "small_gt", "small_tp"]}}
            for rep in (1, 2):
                fr = run_dir / "preds" / f"{i:02d}_{m}_r{rep}.npy"
                if fr.exists():
                    rep_consistency[m]["checked"] += 1
                    o = np.load(fr)
                    rep_consistency[m]["identical_to_r0"] += int(o.shape == pred.shape and np.array_equal(o, pred))
    ref = {}
    for r in read_csv(PAPER / "01_visdrone_main/data/C_cal48_metrics.csv"):
        ref[(r["image"], r["method"])] = {k: to_int(r[k]) for k in ["tp", "fp", "ignored", "small_gt", "small_tp"]}
    for r in read_csv(PAPER / "04_timing/data/B_TIMING_timings.csv"):
        if r["rep"] == "0" and (r["image"], r["method"]) in ref:
            ref[(r["image"], r["method"])]["n_dets"] = to_int(r["n_dets"])
    res, diffs, missing = compare(new, ref, KEYS)
    # timings.csv consistency flags written by the frozen runner (rep vs rep0 n_dets)
    flags = defaultdict(lambda: {"rows": 0, "inconsistent": 0})
    tpath = run_dir / "timings.csv"
    if tpath.exists():
        for r in read_csv(tpath):
            if r.get("consistent_with_rep0") not in (None, ""):
                flags[r["method"]]["rows"] += 1
                flags[r["method"]]["inconsistent"] += int(r["consistent_with_rep0"] in ("False", "0", "false"))
    return dict(mode="cal48", run_id=run_id, reference="C_cal48_metrics.csv + B_TIMING_timings.csv (rep0 n_dets), GTX 1660 SUPER / UAV_BT1",
                n_pairs_compared=sum(v["pairs"] for v in res.values()), missing_pairs=missing,
                per_method=res, within_run_rep_identical=dict(rep_consistency), timings_rep_flags=dict(flags)), diffs, new


def mode_testdev(run_id: str):
    new = {}
    for r in read_csv(P0B / "stage_d" / run_id / "per_image_metrics.csv"):
        new[(r["image"], r["method"])] = {k: to_int(r[k]) for k in KEYS}
    ref = {}
    for r in read_csv(PAPER / "01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv"):
        ref[(r["image"], r["method"])] = {k: to_int(r[k]) for k in KEYS}
    res, diffs, missing = compare(new, ref, KEYS)
    return dict(mode="testdev", run_id=run_id, reference="D_TESTDEV_per_image_metrics.csv, GTX 1660 SUPER / UAV_BT1",
                n_pairs_compared=sum(v["pairs"] for v in res.values()), missing_pairs_count=len(missing),
                missing_pairs_sample=missing[:20], per_method=res), diffs, new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["cal48", "testdev"], required=True)
    ap.add_argument("--run-id", required=True)
    a = ap.parse_args()
    summary, diffs, new = (mode_cal48 if a.mode == "cal48" else mode_testdev)(a.run_id)
    out = P0B / "stage_g" / a.run_id
    out.mkdir(parents=True, exist_ok=True)
    summary["pairs_with_any_diff"] = len(diffs)
    (out / "accuracy_consistency.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (out / "accuracy_diff_rows.csv").open("w", newline="", encoding="utf-8-sig") as f:
        cols = sorted({c for r in diffs for c in r}, key=lambda c: (c not in ("image", "method"), c))
        w = csv.DictWriter(f, fieldnames=cols or ["image", "method"]); w.writeheader(); w.writerows(diffs)
    if a.mode == "cal48":
        with (out / "accuracy_cal48_metrics_5060ti.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["image", "method"] + KEYS); w.writeheader()
            for (img, m), v in new.items():
                w.writerow({"image": img, "method": m, **v})
    print(json.dumps({m: {"pairs_with_any_diff": v["pairs_with_any_diff"], "delta_totals": v["delta_totals"]}
                      for m, v in summary["per_method"].items()}, indent=1))
    print("pairs_with_any_diff", len(diffs), "of", summary["n_pairs_compared"])


if __name__ == "__main__":
    main()
