#!/usr/bin/env python3
"""Regenerate P0_EI comparison plots from Stage D/E/F/B JSON summaries on disk."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

HERE = Path(__file__).resolve().parent
P0 = HERE.parent.parent  # .../papers/P0_EI
OUT = HERE
PROTOCOLS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
COLORS = {
    "precision": "#4C72B0",
    "small_recall": "#DD8452",
    "mean_ms": "#55A868",
    "visdrone": "#4C72B0",
    "uavdt": "#DD8452",
}


def load_json(rel: str) -> dict:
    path = P0 / rel
    return json.loads(path.read_text(encoding="utf-8"))


def methods_metrics(summary: dict) -> dict:
    methods = summary["methods"]
    return {
        name: {
            "precision": methods[name]["precision"],
            "small_recall": methods[name]["small_recall"],
            "mean_ms": methods[name]["mean_ms"],
        }
        for name in PROTOCOLS
    }


def timing_metrics(summary: dict) -> dict:
    timing = summary.get("timing") or summary["methods"]
    return {
        name: {
            "mean_ms": timing[name]["mean_ms"],
            "median_ms": timing[name]["median_ms"],
        }
        for name in PROTOCOLS
    }


def flip_pair(name: str) -> tuple[str, bool]:
    """Return (bootstrap_key, flip_sign). Display is always left - right."""
    # Keys stored as A_vs_B meaning delta = A - B
    mapping = {
        "F1280 − DensK1\n(primary)": ("F1280_vs_DensK1", False),
        "F1280 − F640": ("F640_vs_F1280", True),
        "UnifAll − DensK1": ("DensK1_vs_UnifAll", True),
        "F1280 − UnifAll": ("F1280_vs_UnifAll", False),
        "F1280 − SAHI640": ("F1280_vs_SAHI640", False),
    }
    return mapping[name]


def stage_f_deltas(summary: dict):
    labels = [
        "F1280 − DensK1\n(primary)",
        "F1280 − F640",
        "UnifAll − DensK1",
        "F1280 − UnifAll",
        "F1280 − SAHI640",
    ]
    rows = []
    for label in labels:
        key, flip = flip_pair(label)
        entry = summary["bootstrap_all"][key]
        point = entry["point"]
        ci = entry["bootstrap"]["delta_small_recall_ci95"]
        d = point["delta_small_recall"]
        dp = point["delta_precision"]
        lo, hi = ci
        if flip:
            d, lo, hi, dp = -d, -hi, -lo, -dp
        rows.append((label, d, lo, hi, dp))
    return rows


def grouped_bars_dataset(data, title, outfile, include_latency=True):
    x = np.arange(len(PROTOCOLS))
    if include_latency:
        fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1.35, 1.0]})
        ax0, ax1 = axes
    else:
        fig, ax0 = plt.subplots(figsize=(7.5, 4.2))
        ax1 = None

    w = 0.35
    prec = [data[p]["precision"] for p in PROTOCOLS]
    sr = [data[p]["small_recall"] for p in PROTOCOLS]
    b0 = ax0.bar(x - w / 2, prec, w, label="Precision", color=COLORS["precision"], edgecolor="white", linewidth=0.5)
    b1 = ax0.bar(x + w / 2, sr, w, label="Small-object recall", color=COLORS["small_recall"], edgecolor="white", linewidth=0.5)
    ax0.set_xticks(x)
    ax0.set_xticklabels(PROTOCOLS)
    ax0.set_ylabel("Score")
    ax0.set_ylim(0, 1.05)
    ax0.set_title(title)
    ax0.legend(loc="upper right", frameon=False)
    ax0.yaxis.grid(True, linestyle="--", alpha=0.35)
    ax0.set_axisbelow(True)
    for bars in (b0, b1):
        for bar in bars:
            h = bar.get_height()
            ax0.annotate(
                f"{h:.3f}",
                xy=(bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 2),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=7.5,
                rotation=90,
            )

    if ax1 is not None:
        ms = [data[p]["mean_ms"] for p in PROTOCOLS]
        bars = ax1.bar(x, ms, 0.55, color=COLORS["mean_ms"], edgecolor="white", linewidth=0.5)
        ax1.set_xticks(x)
        ax1.set_xticklabels(PROTOCOLS)
        ax1.set_ylabel("Mean latency (ms/img)")
        ax1.set_title("One-shot latency (same run)")
        ax1.yaxis.grid(True, linestyle="--", alpha=0.35)
        ax1.set_axisbelow(True)
        for bar in bars:
            h = bar.get_height()
            ax1.annotate(
                f"{h:.1f}",
                xy=(bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 2),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)
    print("wrote", outfile)


def fig3_dual_small_recall(D, E):
    outfile = OUT / "fig3_dual_set_small_recall.png"
    x = np.arange(len(PROTOCOLS))
    w = 0.38
    d_sr = [D[p]["small_recall"] for p in PROTOCOLS]
    e_sr = [E[p]["small_recall"] for p in PROTOCOLS]
    fig, ax = plt.subplots(figsize=(9.0, 4.4))
    b0 = ax.bar(x - w / 2, d_sr, w, label="VisDrone test-dev (Stage D)", color=COLORS["visdrone"], edgecolor="white")
    b1 = ax.bar(x + w / 2, e_sr, w, label="UAVDT DET FULL (Stage E)", color=COLORS["uavdt"], edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(PROTOCOLS)
    ax.set_ylabel("Small-object recall")
    ax.set_ylim(0, 1.05)
    ax.set_title("Dual-set small-object recall (do not pool D+E)")
    ax.legend(loc="upper left", frameon=False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    for bars in (b0, b1):
        for bar in bars:
            h = bar.get_height()
            ax.annotate(
                f"{h:.3f}",
                xy=(bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 2),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=7.5,
                rotation=90,
            )
    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)
    print("wrote", outfile)


def fig4_timing(B):
    outfile = OUT / "fig4_timing_1660.png"
    x = np.arange(len(PROTOCOLS))
    mean_ms = [B[p]["mean_ms"] for p in PROTOCOLS]
    med_ms = [B[p]["median_ms"] for p in PROTOCOLS]
    fig, ax = plt.subplots(figsize=(8.5, 4.4))
    w = 0.38
    b0 = ax.bar(x - w / 2, mean_ms, w, label="Mean ms/img", color="#4C72B0", edgecolor="white")
    b1 = ax.bar(x + w / 2, med_ms, w, label="Median ms/img", color="#8172B3", edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(PROTOCOLS)
    ax.set_ylabel("Latency (ms/img)")
    ax.set_title("Stage B timing — GTX 1660 SUPER (cal48, 3 reps; 4090 N/A)")
    ax.legend(loc="upper left", frameon=False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    for bars in (b0, b1):
        for bar in bars:
            h = bar.get_height()
            ax.annotate(
                f"{h:.1f}",
                xy=(bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 2),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
            )
    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)
    print("wrote", outfile)


def fig5_stageF(rows):
    outfile = OUT / "fig5_stageF_deltas.png"
    labels = [t[0] for t in rows]
    deltas = [t[1] for t in rows]
    lo = [t[2] for t in rows]
    hi = [t[3] for t in rows]
    err_lo = [d - l for d, l in zip(deltas, lo)]
    err_hi = [h - d for d, h in zip(deltas, hi)]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    colors = ["#55A868" if d >= 0 else "#C44E52" for d in deltas]
    ax.barh(
        y,
        deltas,
        xerr=[err_lo, err_hi],
        color=colors,
        edgecolor="white",
        height=0.62,
        capsize=3,
        error_kw={"elinewidth": 1.2, "ecolor": "#333333"},
    )
    ax.axvline(0, color="#333333", linewidth=0.9)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel(r"$\Delta$ small-object recall (95% bootstrap CI)")
    ax.set_title("Stage F paired deltas on VisDrone test-dev (image-level)")
    ax.xaxis.grid(True, linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    for yi, d in zip(y, deltas):
        ax.annotate(
            f"{d:+.4f}",
            xy=(d, yi),
            xytext=(4 if d >= 0 else -4, 0),
            textcoords="offset points",
            ha="left" if d >= 0 else "right",
            va="center",
            fontsize=8,
        )
    fig.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)
    print("wrote", outfile)


def main():
    d_sum = load_json("01_visdrone_main/data/D_TESTDEV_summary.json")
    e_sum = load_json("03_cross_uavdt/data/E_FULL_summary.json")
    b_sum = load_json("04_timing/data/B_TIMING_summary.json")
    f_sum = load_json("02_paired_stats/data/F_summary.json")

    D = methods_metrics(d_sum)
    E = methods_metrics(e_sum)
    B = timing_metrics(b_sum)
    F_rows = stage_f_deltas(f_sum)

    OUT.mkdir(parents=True, exist_ok=True)
    grouped_bars_dataset(
        D,
        "VisDrone test-dev (Stage D) — precision & small-object recall",
        OUT / "fig1_visdrone_metrics.png",
        include_latency=True,
    )
    grouped_bars_dataset(
        E,
        "UAVDT DET FULL (Stage E) — precision & small-object recall",
        OUT / "fig2_uavdt_metrics.png",
        include_latency=True,
    )
    fig3_dual_small_recall(D, E)
    fig4_timing(B)
    fig5_stageF(F_rows)
    print("done; sources:")
    print(" D", d_sum.get("run_id"))
    print(" E", e_sum.get("run_id"))
    print(" B", b_sum.get("run_id"))
    print(" F", f_sum.get("run_id"))


if __name__ == "__main__":
    main()