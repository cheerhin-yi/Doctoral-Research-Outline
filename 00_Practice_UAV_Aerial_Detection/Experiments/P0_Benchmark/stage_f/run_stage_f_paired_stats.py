#!/usr/bin/env python3
"""P0 Stage F: image-level paired stats on Stage D test-dev metrics."""
from __future__ import annotations

import csv
import json
import math
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

RUN_ID = "P0-BENCH-F-TESTDEV-20260917-01"
STAGE_D_CSV = Path(
    "00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_d/"
    "P0-BENCH-D-TESTDEV-20260917-01/per_image_metrics.csv"
)
OUT = Path("00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_f") / RUN_ID
N_BOOT = 10000
SEED = 20260917
PRIMARY = ("F1280", "DensK1")
SECONDARY = [
    ("F640", "F1280"),
    ("F1280", "UnifAll"),
    ("F1280", "SAHI640"),
    ("DensK1", "UnifAll"),
    ("DensK1", "SAHI640"),
]
ALL_PAIRS = [PRIMARY] + SECONDARY


def load_by_image(path: Path):
    by = defaultdict(dict)
    with path.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            by[r["image"]][r["method"]] = {
                "index": int(r["index"]),
                "tp": int(float(r["tp"])),
                "fp": int(float(r["fp"])),
                "small_gt": int(float(r["small_gt"])),
                "small_tp": int(float(r["small_tp"])),
                "total_ms": float(r["total_ms"]),
            }
    return by


def paired(by, m_a, m_b, metric: str):
    imgs, xa, xb = [], [], []
    for img, methods in by.items():
        if m_a not in methods or m_b not in methods:
            continue
        ra, rb = methods[m_a], methods[m_b]
        if metric == "recall_small":
            if ra["small_gt"] <= 0:
                continue
            va = ra["small_tp"] / ra["small_gt"]
            vb = rb["small_tp"] / rb["small_gt"]
        elif metric == "total_ms":
            va, vb = ra["total_ms"], rb["total_ms"]
        else:
            raise ValueError(metric)
        imgs.append(img)
        xa.append(va)
        xb.append(vb)
    return imgs, np.asarray(xa, float), np.asarray(xb, float)


def wilcoxon_signed_rank(x, y):
    diff = x - y
    median_diff = float(np.median(diff))
    mean_diff = float(np.mean(diff))
    d = diff[diff != 0]
    n = int(len(d))
    if n < 1:
        return {
            "statistic": float("nan"),
            "pvalue": float("nan"),
            "n_nonzero": 0,
            "n_pairs": int(len(x)),
            "median_diff": median_diff,
            "mean_diff": mean_diff,
            "note": "all_zero_diff",
        }
    abs_d = np.abs(d)
    order = np.argsort(abs_d, kind="mergesort")
    ranks = np.empty(n, float)
    ranks[order] = np.arange(1, n + 1, dtype=float)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and abs_d[order[j + 1]] == abs_d[order[i]]:
            j += 1
        if j > i:
            avg = float(ranks[order[i : j + 1]].mean())
            ranks[order[i : j + 1]] = avg
        i = j + 1
    w_pos = float(ranks[d > 0].sum())
    w_neg = float(ranks[d < 0].sum())
    stat = min(w_pos, w_neg)
    mean = n * (n + 1) / 4.0
    tie_term = 0.0
    sorted_abs = abs_d[order]
    i = 0
    while i < n:
        j = i
        while j + 1 < n and sorted_abs[j + 1] == sorted_abs[i]:
            j += 1
        tlen = j - i + 1
        if tlen > 1:
            tie_term += tlen ** 3 - tlen
        i = j + 1
    var = n * (n + 1) * (2 * n + 1) / 24.0 - tie_term / 48.0
    if var <= 0:
        z = 0.0
    else:
        z = (stat - mean - 0.5 * np.sign(stat - mean)) / math.sqrt(var)
    p = float(math.erfc(abs(z) / math.sqrt(2.0)))
    return {
        "statistic": float(stat),
        "w_plus": w_pos,
        "w_minus": w_neg,
        "z": float(z),
        "pvalue": p,
        "n_nonzero": n,
        "n_pairs": int(len(x)),
        "median_diff": median_diff,
        "mean_diff": mean_diff,
    }


def holm(pvals):
    m = len(pvals)
    order = list(np.argsort(pvals))
    adj = [0.0] * m
    running = 0.0
    for rank, idx in enumerate(order):
        running = max(running, (m - rank) * pvals[idx])
        adj[idx] = min(1.0, running)
    for rank in range(1, m):
        i0, i1 = order[rank - 1], order[rank]
        if adj[i1] < adj[i0]:
            adj[i1] = adj[i0]
    return adj


def wilson(successes, n, z=1.96):
    if n <= 0:
        return {"p": float("nan"), "lo": float("nan"), "hi": float("nan"), "n": 0}
    phat = successes / n
    den = 1 + z * z / n
    centre = phat + z * z / (2 * n)
    margin = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return {
        "p": phat,
        "lo": (centre - margin) / den,
        "hi": (centre + margin) / den,
        "n": n,
        "successes": successes,
    }


def bootstrap_pair(by, m_a, m_b, rng, n_boot=N_BOOT):
    images = sorted(
        [im for im in by if m_a in by[im] and m_b in by[im]],
        key=lambda im: by[im][m_a]["index"],
    )
    n = len(images)

    def agg(idxs):
        tp_a = fp_a = tp_b = fp_b = sgt = stp_a = stp_b = 0
        ms_a = ms_b = 0.0
        for i in idxs:
            ra = by[images[i]][m_a]
            rb = by[images[i]][m_b]
            tp_a += ra["tp"]; fp_a += ra["fp"]
            tp_b += rb["tp"]; fp_b += rb["fp"]
            sgt += ra["small_gt"]; stp_a += ra["small_tp"]; stp_b += rb["small_tp"]
            ms_a += ra["total_ms"]; ms_b += rb["total_ms"]
        return {
            "small_gt": int(sgt),
            "small_recall_a": (stp_a / sgt) if sgt else float("nan"),
            "small_recall_b": (stp_b / sgt) if sgt else float("nan"),
            "delta_small_recall": ((stp_a - stp_b) / sgt) if sgt else float("nan"),
            "precision_a": (tp_a / (tp_a + fp_a)) if (tp_a + fp_a) else float("nan"),
            "precision_b": (tp_b / (tp_b + fp_b)) if (tp_b + fp_b) else float("nan"),
            "delta_precision": (
                ((tp_a / (tp_a + fp_a)) if (tp_a + fp_a) else float("nan"))
                - ((tp_b / (tp_b + fp_b)) if (tp_b + fp_b) else float("nan"))
            ),
            "mean_ms_a": ms_a / len(idxs),
            "mean_ms_b": ms_b / len(idxs),
            "delta_mean_ms": (ms_a - ms_b) / len(idxs),
        }

    point = agg(np.arange(n))
    d_rec = np.empty(n_boot)
    d_prec = np.empty(n_boot)
    d_ms = np.empty(n_boot)
    for b in range(n_boot):
        boot = agg(rng.integers(0, n, size=n))
        d_rec[b] = boot["delta_small_recall"]
        d_prec[b] = boot["delta_precision"]
        d_ms[b] = boot["delta_mean_ms"]

    def ci(a):
        return [float(np.quantile(a, 0.025)), float(np.quantile(a, 0.975))]

    return {
        "n_images": n,
        "point": point,
        "bootstrap": {
            "B": n_boot,
            "seed": SEED,
            "delta_small_recall_ci95": ci(d_rec),
            "delta_precision_ci95": ci(d_prec),
            "delta_mean_ms_ci95": ci(d_ms),
        },
    }


def fmt_p(p):
    if p is None or (isinstance(p, float) and math.isnan(p)):
        return "NA"
    return f"{p:.4g}"


def main():
    t0 = time.perf_counter()
    OUT.mkdir(parents=True, exist_ok=True)
    assert STAGE_D_CSV.exists(), STAGE_D_CSV
    by = load_by_image(STAGE_D_CSV)
    n_images = len(by)
    methods = sorted({m for d in by.values() for m in d})
    print(f"images={n_images} methods={methods}", flush=True)
    rng = np.random.default_rng(SEED)

    wilcox_recall = {}
    for a, b in ALL_PAIRS:
        imgs, xa, xb = paired(by, a, b, "recall_small")
        w = wilcoxon_signed_rank(xa, xb)
        w.update(pair=f"{a}_vs_{b}", metric="recall_small", n_images_with_small_gt=len(imgs))
        wilcox_recall[f"{a}_vs_{b}"] = w
        print(
            f"W recall {a} vs {b}: N={len(imgs)} nz={w['n_nonzero']} "
            f"p={w['pvalue']:.6g} med={w['median_diff']:.4f}",
            flush=True,
        )

    sec_keys = [f"{a}_vs_{b}" for a, b in SECONDARY]
    for k, padj in zip(sec_keys, holm([wilcox_recall[k]["pvalue"] for k in sec_keys])):
        wilcox_recall[k]["pvalue_holm"] = padj
    wilcox_recall[f"{PRIMARY[0]}_vs_{PRIMARY[1]}"]["pvalue_holm"] = None

    wilcox_lat = {}
    for a, b in ALL_PAIRS:
        imgs, xa, xb = paired(by, a, b, "total_ms")
        w = wilcoxon_signed_rank(xa, xb)
        w.update(
            pair=f"{a}_vs_{b}",
            metric="total_ms_oneshot",
            n_images=len(imgs),
            caveat="Stage D one-shot timing",
        )
        wilcox_lat[f"{a}_vs_{b}"] = w

    boots = {}
    for a, b in ALL_PAIRS:
        print(f"bootstrap {a} vs {b}", flush=True)
        boots[f"{a}_vs_{b}"] = bootstrap_pair(by, a, b, rng, N_BOOT)

    binary = {}
    for a, b in ALL_PAIRS:
        imgs, xa, xb = paired(by, a, b, "recall_small")
        better_a = int(np.sum(xa > xb))
        better_b = int(np.sum(xb > xa))
        tie = int(np.sum(xa == xb))
        disc = better_a + better_b
        if disc > 0:
            chi2 = (abs(better_a - better_b) - 1) ** 2 / disc
            p_mc = math.erfc(math.sqrt(chi2 / 2.0))
        else:
            chi2 = float("nan")
            p_mc = float("nan")
        binary[f"{a}_vs_{b}"] = {
            "n": len(imgs),
            "a_strictly_better": better_a,
            "b_strictly_better": better_b,
            "tie": tie,
            "wilson_a_better": wilson(better_a, len(imgs)),
            "mcnemar_chi2_continuity": chi2,
            "mcnemar_pvalue": p_mc,
        }

    agg = {}
    for m in methods:
        tp = fp = sgt = stp = 0
        ms = []
        for md in by.values():
            if m not in md:
                continue
            r = md[m]
            tp += r["tp"]; fp += r["fp"]; sgt += r["small_gt"]; stp += r["small_tp"]
            ms.append(r["total_ms"])
        agg[m] = {
            "tp": tp,
            "fp": fp,
            "precision": (tp / (tp + fp)) if (tp + fp) else float("nan"),
            "small_gt": sgt,
            "small_tp": stp,
            "small_recall": (stp / sgt) if sgt else float("nan"),
            "mean_ms": float(np.mean(ms)),
            "median_ms": float(np.median(ms)),
            "n_images": len(ms),
        }

    pk = f"{PRIMARY[0]}_vs_{PRIMARY[1]}"
    ci = boots[pk]["bootstrap"]["delta_small_recall_ci95"]
    crosses0 = ci[0] <= 0 <= ci[1]
    interpretation = (
        "95% CI for delta small-recall crosses 0: current sample does not establish a stable difference."
        if crosses0
        else "95% CI for delta small-recall does not cross 0."
    )

    summary = {
        "status": "PASS",
        "run_id": RUN_ID,
        "stage_d_csv": str(STAGE_D_CSV).replace("\\", "/"),
        "unit_of_analysis": "image",
        "n_images": n_images,
        "B": N_BOOT,
        "seed": SEED,
        "primary_pair": pk,
        "primary_wilcoxon_recall_small": wilcox_recall[pk],
        "primary_bootstrap": boots[pk],
        "primary_interpretation": interpretation,
        "secondary_wilcoxon_recall_small": {k: wilcox_recall[k] for k in sec_keys},
        "wilcoxon_latency_oneshot": wilcox_lat,
        "bootstrap_all": boots,
        "binary_win_counts": binary,
        "method_aggregates": agg,
        "wall_seconds": time.perf_counter() - t0,
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    with (OUT / "wilcoxon_recall_small.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["pair", "role", "n_images_with_small_gt", "n_nonzero", "median_diff_A_minus_B", "mean_diff", "statistic", "pvalue", "pvalue_holm"])
        for a, b in ALL_PAIRS:
            k = f"{a}_vs_{b}"
            r = wilcox_recall[k]
            w.writerow([k, "primary" if (a, b) == PRIMARY else "secondary", r["n_images_with_small_gt"], r["n_nonzero"], r["median_diff"], r["mean_diff"], r["statistic"], r["pvalue"], r.get("pvalue_holm")])

    with (OUT / "bootstrap_deltas.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["pair", "delta_small_recall", "ci95_lo", "ci95_hi", "delta_precision", "prec_ci_lo", "prec_ci_hi", "delta_mean_ms", "ms_ci_lo", "ms_ci_hi", "n_images"])
        for a, b in ALL_PAIRS:
            k = f"{a}_vs_{b}"
            bt = boots[k]; p = bt["point"]; bb = bt["bootstrap"]
            w.writerow([k, p["delta_small_recall"], *bb["delta_small_recall_ci95"], p["delta_precision"], *bb["delta_precision_ci95"], p["delta_mean_ms"], *bb["delta_mean_ms_ci95"], bt["n_images"]])

    pr = wilcox_recall[pk]
    pb = boots[pk]
    lines = [
        "# P0 Benchmark Stage F — Image-level paired statistics",
        "",
        f"- **Run ID:** `{RUN_ID}`",
        "- **Status:** PASS (analysis completed)",
        f"- **Source:** Stage D `{STAGE_D_CSV.as_posix()}`",
        f"- **Unit:** image (N={n_images})",
        f"- **Bootstrap:** B={N_BOOT}, seed={SEED}, paired image resampling",
        f"- **Primary:** {PRIMARY[0]} vs {PRIMARY[1]}",
        "",
        "## Rules honored",
        "",
        "- Analysis unit = image (not boxes).",
        "- recall_small undefined when small_gt=0 (excluded from Wilcoxon recall).",
        "- Secondary p-values Holm-corrected; primary reported raw.",
        "- Latency = Stage D one-shot total_ms (not median-of-3).",
        "",
        "## Method aggregates (pooled; context only)",
        "",
        "| Method | small recall | precision | mean ms |",
        "|---|---:|---:|---:|",
    ]
    for m in ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]:
        if m in agg:
            d = agg[m]
            lines.append(f"| {m} | {d['small_recall']:.4f} | {d['precision']:.4f} | {d['mean_ms']:.1f} |")
    lines += [
        "",
        "## Primary: F1280 vs DensK1 (recall_small)",
        "",
        f"- N_images with small GT: **{pr['n_images_with_small_gt']}** (nonzero diffs: {pr['n_nonzero']})",
        f"- Median Δ (F1280 − DensK1): **{pr['median_diff']:.4f}**",
        f"- Mean Δ: **{pr['mean_diff']:.4f}**",
        f"- Wilcoxon p (two-sided): **{fmt_p(pr['pvalue'])}**",
        f"- Aggregate small recall: F1280={pb['point']['small_recall_a']:.4f}, DensK1={pb['point']['small_recall_b']:.4f}, Δ={pb['point']['delta_small_recall']:.4f}",
        f"- Bootstrap 95% CI for Δ small recall: **[{ci[0]:.4f}, {ci[1]:.4f}]**",
        f"- Interpretation: **{interpretation}**",
        "",
        "## Secondary Wilcoxon (recall_small) + Holm",
        "",
        "| Pair | N | median Δ | p raw | p Holm |",
        "|---|---:|---:|---:|---:|",
    ]
    for a, b in SECONDARY:
        k = f"{a}_vs_{b}"
        r = wilcox_recall[k]
        lines.append(f"| {a} vs {b} | {r['n_images_with_small_gt']} | {r['median_diff']:.4f} | {fmt_p(r['pvalue'])} | {fmt_p(r.get('pvalue_holm'))} |")
    lines += [
        "",
        "## Bootstrap Δ (A − B)",
        "",
        "| Pair | Δ small recall [95% CI] | Δ precision [95% CI] | Δ mean ms [95% CI] |",
        "|---|---|---|---|",
    ]
    for a, b in ALL_PAIRS:
        k = f"{a}_vs_{b}"
        p = boots[k]["point"]; bb = boots[k]["bootstrap"]
        lines.append(
            f"| {a} vs {b} | {p['delta_small_recall']:.4f} [{bb['delta_small_recall_ci95'][0]:.4f}, {bb['delta_small_recall_ci95'][1]:.4f}] | "
            f"{p['delta_precision']:.4f} [{bb['delta_precision_ci95'][0]:.4f}, {bb['delta_precision_ci95'][1]:.4f}] | "
            f"{p['delta_mean_ms']:.1f} [{bb['delta_mean_ms_ci95'][0]:.1f}, {bb['delta_mean_ms_ci95'][1]:.1f}] |"
        )
    lines += [
        "",
        "## Image-level win counts (descriptive)",
        "",
        "| Pair | A better | B better | tie | Wilson p(A better) |",
        "|---|---:|---:|---:|---|",
    ]
    for a, b in ALL_PAIRS:
        k = f"{a}_vs_{b}"
        d = binary[k]; w = d["wilson_a_better"]
        lines.append(f"| {a} vs {b} | {d['a_strictly_better']} | {d['b_strictly_better']} | {d['tie']} | {w['p']:.3f} [{w['lo']:.3f}, {w['hi']:.3f}] |")
    lines += [
        "",
        "## Latency note",
        "",
        "Stage D timings are one-shot on GTX 1660 SUPER. Formal 4090 multi-rep latency remains deferred.",
        "",
        "## Artifacts",
        "",
        f"- `{OUT.as_posix()}/summary.json`",
        f"- `{OUT.as_posix()}/wilcoxon_recall_small.csv`",
        f"- `{OUT.as_posix()}/bootstrap_deltas.csv`",
        "",
    ]
    report = Path("00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark_StageF_Paired_Stats_Report.md")
    report.write_text("\n".join(lines), encoding="utf-8")
    (OUT / "status.json").write_text(json.dumps({"status": "PASS", "run_id": RUN_ID}, indent=2), encoding="utf-8")
    tr = Path("00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Tracker.md")
    line = (
        f"| {RUN_ID} | F | Image-level Wilcoxon+bootstrap+Holm on Stage D test-dev | "
        f"GTX 1660 SUPER (stats only) | H:/Conda/envs/UAV_BT1 | DONE / PASS | "
        f"Experiments/P0_Benchmark/stage_f/{RUN_ID}/; P0_Benchmark_StageF_Paired_Stats_Report.md |"
    )
    if tr.exists():
        t = tr.read_text(encoding="utf-8")
        if RUN_ID not in t:
            tr.write_text(t.rstrip() + "\n" + line + "\n", encoding="utf-8")
    print("wrote", report, "wall", summary["wall_seconds"], flush=True)


if __name__ == "__main__":
    main()
