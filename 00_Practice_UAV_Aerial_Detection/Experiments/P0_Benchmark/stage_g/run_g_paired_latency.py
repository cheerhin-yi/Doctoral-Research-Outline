#!/usr/bin/env python3
"""Run G paired latency test on 5060 Ti Stage-D-style one-shot per-image timings.

Parametrised re-use of the FROZEN Stage F statistics: functions are imported from
stage_f/run_stage_f_paired_stats.py unchanged (its main() is NOT called, because it
writes fixed 1660 report/tracker paths). Same pairs, same Wilcoxon (normal approx.,
tie + continuity correction), same bootstrap (B=10000, seed 20260917), same Holm.
Unit of analysis: image.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve()
P0B = HERE.parents[1]
EXP = HERE.parents[2]
PAPER = EXP / "papers" / "P0_EI"

spec = importlib.util.spec_from_file_location("stage_f_frozen", P0B / "stage_f" / "run_stage_f_paired_stats.py")
SF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(SF)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--testdev-run-id", required=True)
    a = ap.parse_args()
    t0 = time.perf_counter()
    src = P0B / "stage_d" / a.testdev_run_id / "per_image_metrics.csv"
    out = P0B / "stage_g" / a.run_id
    out.mkdir(parents=True, exist_ok=False)
    by = SF.load_by_image(src)
    rng = np.random.default_rng(SF.SEED)

    lat = {}
    for x, y in SF.ALL_PAIRS:
        imgs, xa, xb = SF.paired(by, x, y, "total_ms")
        w = SF.wilcoxon_signed_rank(xa, xb)
        w.update(pair=f"{x}_vs_{y}", metric="total_ms_oneshot_5060ti", n_images=len(imgs))
        lat[f"{x}_vs_{y}"] = w
    sec = [f"{x}_vs_{y}" for x, y in SF.SECONDARY]
    for k, padj in zip(sec, SF.holm([lat[k]["pvalue"] for k in sec])):
        lat[k]["pvalue_holm"] = padj
    pk = f"{SF.PRIMARY[0]}_vs_{SF.PRIMARY[1]}"
    lat[pk]["pvalue_holm"] = None

    boots = {}
    for x, y in SF.ALL_PAIRS:
        b = SF.bootstrap_pair(by, x, y, rng, SF.N_BOOT)
        boots[f"{x}_vs_{y}"] = {"n_images": b["n_images"], "mean_ms_a": b["point"]["mean_ms_a"], "mean_ms_b": b["point"]["mean_ms_b"],
                                "delta_mean_ms": b["point"]["delta_mean_ms"], "delta_mean_ms_ci95": b["bootstrap"]["delta_mean_ms_ci95"]}

    ref = json.loads((PAPER / "02_paired_stats/data/F_summary.json").read_text(encoding="utf-8"))
    ref_lat = ref.get("wilcoxon_latency_oneshot", {})
    p = lat[pk]["pvalue"]
    summary = {
        "status": "PASS", "run_id": a.run_id, "source_csv": str(src.relative_to(EXP.parent.parent)).replace("\\", "/"),
        "gpu": "NVIDIA GeForce RTX 5060 Ti (UAV_BT2)", "unit_of_analysis": "image", "primary_pair": pk,
        "method": "frozen stage_f functions: wilcoxon_signed_rank (normal approx, tie+continuity), bootstrap_pair B=10000 seed=20260917, holm on secondary",
        "wilcoxon_latency_oneshot": lat, "bootstrap_latency": boots,
        "reference_1660_F": {k: {"pvalue": v.get("pvalue"), "median_diff": v.get("median_diff"), "mean_diff": v.get("mean_diff")} for k, v in ref_lat.items()},
        "primary_conclusion": ("F1280 vs DensK1 latency NOT significantly different at alpha=0.05 (two-sided)" if p >= 0.05
                               else "F1280 vs DensK1 latency significantly different at alpha=0.05 (two-sided)"),
        "wall_seconds": time.perf_counter() - t0,
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (out / "wilcoxon_latency.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["pair", "n", "median_diff_ms", "mean_diff_ms", "w_plus", "w_minus", "z", "p", "p_holm", "boot_delta_mean_ci95_lo", "boot_delta_mean_ci95_hi", "p_1660_ref"])
        for k, v in lat.items():
            ci = boots[k]["delta_mean_ms_ci95"]
            w.writerow([k, v["n_pairs"], v["median_diff"], v["mean_diff"], v.get("w_plus"), v.get("w_minus"), v.get("z"), v["pvalue"],
                        v.get("pvalue_holm"), ci[0], ci[1], ref_lat.get(k, {}).get("pvalue")])
    (out / "status.json").write_text(json.dumps({"status": "PASS", "run_id": a.run_id}, indent=2), encoding="utf-8")
    print(json.dumps({k: {"p": v["pvalue"], "median_diff": v["median_diff"], "mean_diff": v["mean_diff"]} for k, v in lat.items()}, indent=1))
    print(summary["primary_conclusion"])


if __name__ == "__main__":
    main()
