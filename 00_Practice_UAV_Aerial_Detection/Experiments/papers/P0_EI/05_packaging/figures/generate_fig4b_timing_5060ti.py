#!/usr/bin/env python3
"""Fig 4b: Run G timing on RTX 5060 Ti (UAV_BT2). Separate figure; fig4_timing_1660.png is untouched.

Reads ../../04_timing/data/G_TIMING_stats.json (written by
Experiments/P0_Benchmark/stage_g/summarize_g_timing.py). 5060 Ti numbers only.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11,
    "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 9, "figure.dpi": 150,
    "savefig.dpi": 200, "savefig.bbox": "tight", "axes.spines.top": False, "axes.spines.right": False,
})
HERE = Path(__file__).resolve().parent
STATS = HERE.parent.parent / "04_timing" / "data" / "G_TIMING_stats.json"
PROTOCOLS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]


def main():
    s = json.loads(STATS.read_text(encoding="utf-8"))["rtx5060ti_uav_bt2"]
    panels = [("CAL48_stageB_3reps", "cal48 (48 img x 3 reps)"), ("TESTDEV_stageD_oneshot", "VisDrone test-dev (1610 img, one-shot)")]
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.6), sharey=True)
    x = np.arange(len(PROTOCOLS)); w = 0.38
    for ax, (key, label) in zip(axes, panels):
        t = s[key]["timing"]
        mean_ms = [t[p]["mean_ms"] for p in PROTOCOLS]
        med_ms = [t[p]["median_ms"] for p in PROTOCOLS]
        b0 = ax.bar(x - w / 2, mean_ms, w, label="Mean ms/img", color="#55A868", edgecolor="white")
        b1 = ax.bar(x + w / 2, med_ms, w, label="Median ms/img", color="#8C8C8C", edgecolor="white")
        ax.set_xticks(x); ax.set_xticklabels(PROTOCOLS)
        ax.set_yscale("log")
        ax.set_title(label)
        ax.yaxis.grid(True, linestyle="--", alpha=0.35); ax.set_axisbelow(True)
        for bars in (b0, b1):
            for bar in bars:
                h = bar.get_height()
                ax.annotate(f"{h:.1f}", xy=(bar.get_x() + bar.get_width() / 2, h), xytext=(0, 2),
                            textcoords="offset points", ha="center", va="bottom", fontsize=8)
    axes[0].set_ylabel("Latency (ms/img, log scale)")
    axes[0].legend(loc="upper left", frameon=False)
    fig.suptitle("Run G timing — RTX 5060 Ti 16GB, env UAV_BT2 (frozen weights/protocols; not comparable cell-by-cell with 1660)", fontsize=11)
    fig.tight_layout()
    out = HERE / "fig4b_timing_5060ti.png"
    fig.savefig(out); plt.close(fig)
    print("wrote", out)


if __name__ == "__main__":
    main()
