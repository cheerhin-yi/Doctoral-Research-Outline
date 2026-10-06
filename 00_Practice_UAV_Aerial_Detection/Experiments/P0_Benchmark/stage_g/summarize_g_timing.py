#!/usr/bin/env python3
"""Summarise Run G timing into 04_timing/data/G_TIMING_stats.json (analysis only).

Metric definitions are copied from the frozen Stage B `finalize` (mean, median,
std ddof=1, np.percentile p90/p95/p99, budget violation = share of images whose
per-image latency > T, T in 10..100 ms). For the one-shot TESTDEV run the
per-image latency is the single Stage D measurement. "x_vs_F640" = mean(method) /
mean(F640) (relative cost); "speedup_vs_F640" = mean(F640) / mean(method).
The 1660 reference block is computed with the same code from the frozen 1660
records and is stored separately (never merged into the 5060 Ti numbers).
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve()
DATA = HERE.parents[2] / "papers" / "P0_EI" / "04_timing" / "data"
PAPER = DATA.parents[1]
M = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
BUDGET = [10, 15, 20, 25, 30, 40, 50, 75, 100]


def oneshot_stats(path: Path):
    by = {m: [] for m in M}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            by[r["method"]].append(float(r["total_ms"]))
    out = {}
    for m in M:
        a = np.asarray(by[m], float)
        out[m] = dict(n=int(len(a)), mean_ms=float(a.mean()), median_ms=float(np.median(a)), std_ms=float(a.std(ddof=1)),
                      p90_ms=float(np.percentile(a, 90)), p95_ms=float(np.percentile(a, 95)), p99_ms=float(np.percentile(a, 99)),
                      min_ms=float(a.min()), max_ms=float(a.max()),
                      budget_violation_rate={str(t): float(np.mean(a > t)) for t in BUDGET})
    return out


def add_ratios(block):
    base = block["F640"]["mean_ms"]
    base_med = block["F640"]["median_ms"]
    for m in M:
        block[m]["x_vs_F640_mean"] = block[m]["mean_ms"] / base
        block[m]["speedup_vs_F640_mean"] = base / block[m]["mean_ms"]
        block[m]["x_vs_F640_median"] = block[m]["median_ms"] / base_med
    return block


def main():
    cal = json.loads((DATA / "G_CAL48_summary.json").read_text(encoding="utf-8"))
    cal_t = {m: dict(cal["timing"][m]) for m in M}
    ref_b = json.loads((DATA / "B_TIMING_summary.json").read_text(encoding="utf-8"))
    ref_b_t = {m: dict(ref_b["timing"][m]) for m in M}
    out = {
        "definitions": __doc__.strip(),
        "rtx5060ti_uav_bt2": {
            "CAL48_stageB_3reps": {"run_id": cal["run_id"], "gpu": cal["gpu"], "n_images": cal["n_images"], "reps": cal["reps"],
                                    "peak_vram_bytes": cal["peak_vram_bytes"], "timing": add_ratios(cal_t)},
            "TESTDEV_stageD_oneshot": {"run_id": "P0-BENCH-G-5060TI-TESTDEV-20261001-01",
                                        "timing": add_ratios(oneshot_stats(DATA / "G_TESTDEV_per_image_metrics.csv"))},
        },
        "reference_gtx1660super_uav_bt1": {
            "CAL48_stageB_3reps": {"run_id": ref_b["run_id"], "gpu": ref_b["gpu"], "peak_vram_bytes": ref_b["peak_vram_bytes"],
                                    "timing": add_ratios(ref_b_t)},
            "TESTDEV_stageD_oneshot": {"run_id": "P0-BENCH-D-TESTDEV-20260917-01",
                                        "timing": add_ratios(oneshot_stats(PAPER / "01_visdrone_main" / "data" / "D_TESTDEV_per_image_metrics.csv"))},
        },
    }
    (DATA / "G_TIMING_stats.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    for k in ("CAL48_stageB_3reps", "TESTDEV_stageD_oneshot"):
        for m in M:
            t = out["rtx5060ti_uav_bt2"][k]["timing"][m]
            print(k, m, f"{t['mean_ms']:.2f} {t['median_ms']:.2f} {t['p90_ms']:.2f} x{t['x_vs_F640_mean']:.2f}")


if __name__ == "__main__":
    main()
