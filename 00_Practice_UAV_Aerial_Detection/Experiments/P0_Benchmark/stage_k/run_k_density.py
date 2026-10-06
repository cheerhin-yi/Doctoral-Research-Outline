#!/usr/bin/env python
"""P0 Run K: density attribute slices (CPU only, no inference).

Bins images by valid_gt and by small_gt (both are GT-only, method-independent attributes) using
quintile edges computed on the F640 rows of each dataset, then reports per bin x method pooled small
recall, precision and mean latency, plus paired F1280-vs-DensK1 / F1280-vs-UnifAll / DensK1-vs-UnifAll
deltas with bootstrap CIs:
  VisDrone test-dev (Stage D accuracy; latency 1660 = Stage D, 5060 Ti = Run G, separate columns):
      image-level paired bootstrap.
  UAVDT (Stage E; latency 1660 only): sequence-cluster bootstrap restricted to the bin's frames.
B = 10000, seed = 20260917 (same constants as frozen Stage F).
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
from collections import defaultdict
from pathlib import Path

import numpy as np

EXP = Path(__file__).resolve().parents[2]
PAPERS = EXP / "papers" / "P0_EI"
D_CSV = PAPERS / "01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv"
G_CSV = PAPERS / "04_timing/data/G_TESTDEV_per_image_metrics.csv"
E_CSV = PAPERS / "03_cross_uavdt/data/E_FULL_per_image_metrics.csv"
METHODS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
PAIRS = [("F1280", "DensK1"), ("F1280", "UnifAll"), ("DensK1", "UnifAll"), ("F1280", "SAHI640")]
B, SEED = 10000, 20260917
COLS = ["small_tp", "small_gt", "tp", "fp", "total_ms"]


def read(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def table(rows, key):
    """-> images (ordered), per-method matrix [n_img, len(COLS)], attrs."""
    by = defaultdict(dict)
    for r in rows:
        by[r[key]][r["method"]] = r
    imgs = sorted(by, key=lambda i: int(by[i]["F640"]["index"]))
    M = {m: np.array([[float(by[i][m][c]) for c in COLS] for i in imgs]) for m in METHODS}
    attrs = {a: np.array([int(by[i]["F640"][a]) for i in imgs]) for a in ("valid_gt", "small_gt")}
    seq = [by[i]["F640"].get("seq") for i in imgs]
    return imgs, M, attrs, seq


def quintile_bins(x):
    """Quintile edges on the attribute; zero gets its own bin for small_gt. Returns labels per image, bin defs."""
    pos = x[x > 0]
    qs = np.unique(np.quantile(pos, [0.2, 0.4, 0.6, 0.8]).round().astype(int))
    edges = [1] + [int(q) + 1 for q in qs] + [int(x.max()) + 1]
    edges = sorted(set(edges))
    defs = []
    if (x == 0).any():
        defs.append((0, 1))
    defs += [(edges[k], edges[k + 1]) for k in range(len(edges) - 1)]
    lab = np.full(len(x), -1)
    for b, (lo, hi) in enumerate(defs):
        lab[(x >= lo) & (x < hi)] = b
    assert (lab >= 0).all()
    return lab, defs


def pooled(Ms, w):
    """Ms: matrix, w: weights (counts per image). Returns sr, prec, mean_ms."""
    s = w @ Ms
    sr = s[0] / s[1] if s[1] > 0 else np.nan
    pr = s[2] / (s[2] + s[3]) if (s[2] + s[3]) > 0 else np.nan
    return sr, pr, s[4] / w.sum()


def boot_image(MA, MB, idx, rng):
    n = len(idx)
    A, Bm = MA[idx], MB[idx]
    W = np.stack([np.bincount(rng.integers(0, n, n), minlength=n) for _ in range(B)]).astype(float)
    SA, SB = W @ A, W @ Bm
    with np.errstate(invalid="ignore", divide="ignore"):
        dr = (SA[:, 0] - SB[:, 0]) / SA[:, 1]
        dp = SA[:, 2] / (SA[:, 2] + SA[:, 3]) - SB[:, 2] / (SB[:, 2] + SB[:, 3])
    return dr, dp


def boot_cluster(MA, MB, idx, seq_of, rng):
    seqs = sorted(set(seq_of[i] for i in idx))
    k = len(seqs)
    sid = {s: j for j, s in enumerate(seqs)}
    G = np.zeros((k, len(idx)))
    for c, i in enumerate(idx):
        G[sid[seq_of[i]], c] = 1
    A, Bm = G @ MA[idx], G @ MB[idx]  # per-sequence sums within bin
    W = np.stack([np.bincount(rng.integers(0, k, k), minlength=k) for _ in range(B)]).astype(float)
    SA, SB = W @ A, W @ Bm
    with np.errstate(invalid="ignore", divide="ignore"):
        dr = (SA[:, 0] - SB[:, 0]) / SA[:, 1]
        dp = SA[:, 2] / (SA[:, 2] + SA[:, 3]) - SB[:, 2] / (SB[:, 2] + SB[:, 3])
    return dr, dp, k


def ci(a):
    a = a[np.isfinite(a)]
    return [float(np.quantile(a, 0.025)), float(np.quantile(a, 0.975))] if len(a) else [None, None]


def analyse(name, M, attrs, seq, lat_extra, cluster):
    res = {}
    rng = np.random.default_rng(SEED)
    for attr in ("valid_gt", "small_gt"):
        lab, defs = quintile_bins(attrs[attr])
        bins = []
        for b, (lo, hi) in enumerate(defs):
            idx = np.flatnonzero(lab == b)
            w = np.zeros(len(lab)); w[idx] = 1
            row = {"bin": f"[{lo},{hi - 1}]", "lo": lo, "hi_incl": hi - 1, "n_images": int(len(idx)),
                   "sum_small_gt": int(M["F640"][idx, 1].sum()),
                   "mean_valid_gt": float(attrs["valid_gt"][idx].mean()), "mean_small_gt": float(attrs["small_gt"][idx].mean())}
            if cluster:
                row["n_sequences"] = len(set(seq[i] for i in idx))
            meth = {}
            for m in METHODS:
                sr, pr, ms = pooled(M[m], w)
                meth[m] = {"small_recall": None if np.isnan(sr) else float(sr), "precision": float(pr), "mean_ms_1660_UAV_BT1": float(ms)}
                for lab2, L in lat_extra.items():
                    meth[m][f"mean_ms_{lab2}"] = float(L[m][idx].mean())
            row["methods"] = meth
            valid = {m: v["small_recall"] for m, v in meth.items() if v["small_recall"] is not None}
            row["best_small_recall"] = max(valid, key=valid.get) if valid else None
            row["best_precision"] = max(meth, key=lambda m: meth[m]["precision"])
            pairs = {}
            for a, bb in PAIRS:
                if cluster:
                    dr, dp, k = boot_cluster(M[a], M[bb], idx, seq, rng)
                else:
                    dr, dp = boot_image(M[a], M[bb], idx, rng)
                pa, pb = meth[a], meth[bb]
                pairs[f"{a}_vs_{bb}"] = {
                    "delta_small_recall": None if pa["small_recall"] is None else pa["small_recall"] - pb["small_recall"],
                    "delta_small_recall_ci95": ci(dr) if pa["small_recall"] is not None else [None, None],
                    "delta_precision": pa["precision"] - pb["precision"], "delta_precision_ci95": ci(dp),
                    "delta_mean_ms_1660_UAV_BT1": pa["mean_ms_1660_UAV_BT1"] - pb["mean_ms_1660_UAV_BT1"],
                    **{f"delta_mean_ms_{l}": pa[f"mean_ms_{l}"] - pb[f"mean_ms_{l}"] for l in lat_extra},
                }
            row["pairs"] = pairs
            bins.append(row)
        res[attr] = {"bins": bins, "binning": "quintile edges of attribute>0 on this dataset (GT-only, method-independent); 0 own bin"}
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    a = ap.parse_args()
    out = Path(__file__).resolve().parent / a.run_id
    out.mkdir(parents=True, exist_ok=False)
    imgs, MD, attrD, _ = table(read(D_CSV), "image")
    gi, MG, _, _ = table(read(G_CSV), "image")
    assert gi == imgs
    vis = analyse("visdrone", MD, attrD, None, {"5060Ti_UAV_BT2": {m: MG[m][:, 4] for m in METHODS}}, cluster=False)
    _, ME, attrE, seqE = table(read(E_CSV), "image")
    ua = analyse("uavdt", ME, attrE, seqE, {}, cluster=True)
    summ = {"status": "PASS", "run_id": a.run_id,
            "env": {"python": platform.python_version(), "numpy": np.__version__},
            "B": B, "seed": SEED, "visdrone_testdev": vis, "uavdt": ua,
            "notes": ["VisDrone CIs: paired image bootstrap within bin; UAVDT CIs: sequence-cluster bootstrap within bin",
                      "latency columns are per GPU and never pooled; UAVDT has 1660 latency only",
                      "small recall undefined in small_gt=0 bins"]}
    (out / "summary.json").write_text(json.dumps(summ, indent=2), encoding="utf-8")
    with open(out / "density_slices.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["dataset", "attr", "bin", "n_images", "n_sequences", "sum_small_gt", "method", "small_recall",
                     "precision", "mean_ms_1660_UAV_BT1", "mean_ms_5060Ti_UAV_BT2"])
        for ds, R in (("VisDrone_testdev", vis), ("UAVDT", ua)):
            for attr, blk in R.items():
                for row in blk["bins"]:
                    for m in METHODS:
                        v = row["methods"][m]
                        wr.writerow([ds, attr, row["bin"], row["n_images"], row.get("n_sequences", ""), row["sum_small_gt"], m,
                                     v["small_recall"], v["precision"], v["mean_ms_1660_UAV_BT1"], v.get("mean_ms_5060Ti_UAV_BT2", "")])
    with open(out / "density_pairs.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["dataset", "attr", "bin", "n_images", "pair", "delta_small_recall", "ci_lo", "ci_hi",
                     "delta_precision", "p_ci_lo", "p_ci_hi", "delta_ms_1660_UAV_BT1", "delta_ms_5060Ti_UAV_BT2", "best_small_recall"])
        for ds, R in (("VisDrone_testdev", vis), ("UAVDT", ua)):
            for attr, blk in R.items():
                for row in blk["bins"]:
                    for k, p in row["pairs"].items():
                        wr.writerow([ds, attr, row["bin"], row["n_images"], k, p["delta_small_recall"], *p["delta_small_recall_ci95"],
                                     p["delta_precision"], *p["delta_precision_ci95"], p["delta_mean_ms_1660_UAV_BT1"],
                                     p.get("delta_mean_ms_5060Ti_UAV_BT2", ""), row["best_small_recall"]])
    print(open(out / "density_pairs.csv", encoding="utf-8").read())


if __name__ == "__main__":
    main()
