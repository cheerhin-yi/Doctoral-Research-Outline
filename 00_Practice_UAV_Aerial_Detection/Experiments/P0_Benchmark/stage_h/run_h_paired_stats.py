#!/usr/bin/env python3
"""P0 Stage H: parametrised copy of Stage F paired statistics (CPU only, no inference).

* Imports the FROZEN Stage F module (stage_f/run_stage_f_paired_stats.py) and calls its
  functions unchanged: load_by_image, paired, wilcoxon_signed_rank, holm, wilson,
  bootstrap_pair (used directly on VisDrone; see below), constants PRIMARY/SECONDARY/
  ALL_PAIRS/N_BOOT/SEED.
* main() of Stage F is NOT called (it writes fixed 1660 report / tracker paths); its
  orchestration is re-created here with parametrised input/output paths, same order of
  RNG consumption, same output keys.
* bootstrap: the frozen bootstrap_pair loops in pure Python (fine for 1610 images,
  ~hours for 40 735 UAVDT frames). `bootstrap_pair_fast` consumes the SAME rng draws
  (rng.integers(0, n, size=n) once per replicate, same image order) and computes the
  same aggregates with bincount weights. It is verified against the frozen function on
  VisDrone (mode --check-f) before being used on UAVDT.
* UAVDT extra: cluster bootstrap over sequences (resample the 50 sequences with
  replacement, B=10000, seed 20260917, separate rng) and a sequence-level Wilcoxon on
  per-sequence small recall (frozen wilcoxon_signed_rank, n = #sequences).
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import platform
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve()
P0B = HERE.parents[1]
EXP = HERE.parents[2]
ROOT = HERE.parents[4]
PAPER = EXP / "papers" / "P0_EI"

_spec = importlib.util.spec_from_file_location("stage_f_frozen", P0B / "stage_f" / "run_stage_f_paired_stats.py")
SF = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(SF)


def bootstrap_pair_fast(by, m_a, m_b, rng, n_boot):
    images = sorted([im for im in by if m_a in by[im] and m_b in by[im]], key=lambda im: by[im][m_a]["index"])
    n = len(images)
    cols = np.array([[by[im][m_a]["tp"], by[im][m_a]["fp"], by[im][m_b]["tp"], by[im][m_b]["fp"],
                      by[im][m_a]["small_gt"], by[im][m_a]["small_tp"], by[im][m_b]["small_tp"]] for im in images], dtype=np.int64)
    ms = np.array([[by[im][m_a]["total_ms"], by[im][m_b]["total_ms"]] for im in images], dtype=np.float64)

    def agg_from(c_int, c_ms, k):
        tp_a, fp_a, tp_b, fp_b, sgt, stp_a, stp_b = (int(v) for v in c_int)
        pa = (tp_a / (tp_a + fp_a)) if (tp_a + fp_a) else float("nan")
        pb = (tp_b / (tp_b + fp_b)) if (tp_b + fp_b) else float("nan")
        return {
            "small_gt": int(sgt),
            "small_recall_a": (stp_a / sgt) if sgt else float("nan"),
            "small_recall_b": (stp_b / sgt) if sgt else float("nan"),
            "delta_small_recall": ((stp_a - stp_b) / sgt) if sgt else float("nan"),
            "precision_a": pa, "precision_b": pb, "delta_precision": pa - pb,
            "mean_ms_a": c_ms[0] / k, "mean_ms_b": c_ms[1] / k, "delta_mean_ms": (c_ms[0] - c_ms[1]) / k,
        }

    point = agg_from(cols.sum(0), ms.sum(0), n)
    d_rec = np.empty(n_boot); d_prec = np.empty(n_boot); d_ms = np.empty(n_boot)
    for b in range(n_boot):
        w = np.bincount(rng.integers(0, n, size=n), minlength=n)
        ci = w @ cols
        cm = w.astype(np.float64) @ ms
        a = agg_from(ci, cm, n)
        d_rec[b] = a["delta_small_recall"]; d_prec[b] = a["delta_precision"]; d_ms[b] = a["delta_mean_ms"]

    def q(a):
        return [float(np.quantile(a, 0.025)), float(np.quantile(a, 0.975))]

    return {"n_images": n, "point": point,
            "bootstrap": {"B": n_boot, "seed": SF.SEED, "delta_small_recall_ci95": q(d_rec),
                          "delta_precision_ci95": q(d_prec), "delta_mean_ms_ci95": q(d_ms)}}


def stage_f_like(by, boot_fn):
    """Re-creation of frozen Stage F main() computations (same order of rng use)."""
    t0 = time.perf_counter()
    methods = sorted({m for d in by.values() for m in d})
    rng = np.random.default_rng(SF.SEED)
    wilcox_recall = {}
    for a, b in SF.ALL_PAIRS:
        imgs, xa, xb = SF.paired(by, a, b, "recall_small")
        w = SF.wilcoxon_signed_rank(xa, xb)
        w.update(pair=f"{a}_vs_{b}", metric="recall_small", n_images_with_small_gt=len(imgs))
        wilcox_recall[f"{a}_vs_{b}"] = w
    sec_keys = [f"{a}_vs_{b}" for a, b in SF.SECONDARY]
    for k, padj in zip(sec_keys, SF.holm([wilcox_recall[k]["pvalue"] for k in sec_keys])):
        wilcox_recall[k]["pvalue_holm"] = padj
    pk = f"{SF.PRIMARY[0]}_vs_{SF.PRIMARY[1]}"
    wilcox_recall[pk]["pvalue_holm"] = None
    wilcox_lat = {}
    for a, b in SF.ALL_PAIRS:
        imgs, xa, xb = SF.paired(by, a, b, "total_ms")
        w = SF.wilcoxon_signed_rank(xa, xb)
        w.update(pair=f"{a}_vs_{b}", metric="total_ms_oneshot", n_images=len(imgs), caveat="Stage D one-shot timing")
        wilcox_lat[f"{a}_vs_{b}"] = w
    boots = {f"{a}_vs_{b}": boot_fn(by, a, b, rng, SF.N_BOOT) for a, b in SF.ALL_PAIRS}
    binary = {}
    for a, b in SF.ALL_PAIRS:
        imgs, xa, xb = SF.paired(by, a, b, "recall_small")
        ba, bb = int(np.sum(xa > xb)), int(np.sum(xb > xa))
        tie = int(np.sum(xa == xb)); disc = ba + bb
        if disc > 0:
            chi2 = (abs(ba - bb) - 1) ** 2 / disc; p_mc = math.erfc(math.sqrt(chi2 / 2.0))
        else:
            chi2 = p_mc = float("nan")
        binary[f"{a}_vs_{b}"] = {"n": len(imgs), "a_strictly_better": ba, "b_strictly_better": bb, "tie": tie,
                                 "wilson_a_better": SF.wilson(ba, len(imgs)), "mcnemar_chi2_continuity": chi2, "mcnemar_pvalue": p_mc}
    agg = {}
    for m in methods:
        tp = fp = sgt = stp = 0; ms = []
        for md in by.values():
            if m not in md:
                continue
            r = md[m]; tp += r["tp"]; fp += r["fp"]; sgt += r["small_gt"]; stp += r["small_tp"]; ms.append(r["total_ms"])
        agg[m] = {"tp": tp, "fp": fp, "precision": (tp / (tp + fp)) if (tp + fp) else float("nan"), "small_gt": sgt,
                  "small_tp": stp, "small_recall": (stp / sgt) if sgt else float("nan"), "mean_ms": float(np.mean(ms)),
                  "median_ms": float(np.median(ms)), "n_images": len(ms)}
    ci = boots[pk]["bootstrap"]["delta_small_recall_ci95"]
    interp = ("95% CI for delta small-recall crosses 0: current sample does not establish a stable difference."
              if ci[0] <= 0 <= ci[1] else "95% CI for delta small-recall does not cross 0.")
    return {"unit_of_analysis": "image", "n_images": len(by), "B": SF.N_BOOT, "seed": SF.SEED, "primary_pair": pk,
            "primary_wilcoxon_recall_small": wilcox_recall[pk], "primary_bootstrap": boots[pk], "primary_interpretation": interp,
            "secondary_wilcoxon_recall_small": {k: wilcox_recall[k] for k in sec_keys}, "wilcoxon_latency_oneshot": wilcox_lat,
            "bootstrap_all": boots, "binary_win_counts": binary, "method_aggregates": agg, "wall_seconds": time.perf_counter() - t0}


def compare_tree(a, b, path="", out=None, tol=0.0):
    out = [] if out is None else out
    if isinstance(b, dict):
        for k in b:
            if k in ("wall_seconds", "run_id", "stage_d_csv", "status"):
                continue
            if not isinstance(a, dict) or k not in a:
                out.append((path + "/" + k, "missing", None)); continue
            compare_tree(a[k], b[k], path + "/" + k, out, tol)
    elif isinstance(b, list):
        for i, (x, y) in enumerate(zip(a, b)):
            compare_tree(x, y, f"{path}[{i}]", out, tol)
    elif isinstance(b, float) or isinstance(a, float):
        if not ((a is None and b is None) or (isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b))):
            d = abs(float(a) - float(b))
            if d > tol * max(1.0, abs(float(b))):
                out.append((path, a, b))
    elif a != b:
        out.append((path, a, b))
    return out


def max_reldiff(a, b, acc=None):
    acc = [0.0] if acc is None else acc
    if isinstance(b, dict):
        for k in b:
            if k in ("wall_seconds",) or not isinstance(a, dict) or k not in a:
                continue
            max_reldiff(a[k], b[k], acc)
    elif isinstance(b, list):
        for x, y in zip(a, b):
            max_reldiff(x, y, acc)
    elif isinstance(b, float) and isinstance(a, (int, float)) and not math.isnan(b):
        acc[0] = max(acc[0], abs(a - b) / max(1.0, abs(b)))
    return acc[0]


def cluster_bootstrap(rows_by_seq, pairs, n_boot, seed):
    seqs = sorted(rows_by_seq)
    S = len(seqs)
    res = {}
    rng = np.random.default_rng(seed)
    draws = [rng.integers(0, S, size=S) for _ in range(n_boot)]
    for a, b in pairs:
        # per-sequence sums: tp_a fp_a tp_b fp_b sgt stp_a stp_b ms_a ms_b n
        M = np.array([[sum(r[a]["tp"] for r in rows_by_seq[s]), sum(r[a]["fp"] for r in rows_by_seq[s]),
                       sum(r[b]["tp"] for r in rows_by_seq[s]), sum(r[b]["fp"] for r in rows_by_seq[s]),
                       sum(r[a]["small_gt"] for r in rows_by_seq[s]), sum(r[a]["small_tp"] for r in rows_by_seq[s]),
                       sum(r[b]["small_tp"] for r in rows_by_seq[s]), sum(r[a]["total_ms"] for r in rows_by_seq[s]),
                       sum(r[b]["total_ms"] for r in rows_by_seq[s]), len(rows_by_seq[s])] for s in seqs], dtype=np.float64)

        def stat(v):
            tpa, fpa, tpb, fpb, sgt, sa, sb, ma, mb, n = v
            return ((sa - sb) / sgt, tpa / (tpa + fpa) - tpb / (tpb + fpb), (ma - mb) / n, sa / sgt, sb / sgt)

        pt = stat(M.sum(0))
        boot = np.array([stat(np.bincount(d, minlength=S) @ M) for d in draws])
        q = lambda c: [float(np.quantile(boot[:, c], 0.025)), float(np.quantile(boot[:, c], 0.975))]
        # sequence-level Wilcoxon on per-sequence small recall (frozen function)
        has = M[:, 4] > 0  # like Stage F: units without small GT are excluded from recall tests
        ra = M[has, 5] / M[has, 4]; rb = M[has, 6] / M[has, 4]
        w = SF.wilcoxon_signed_rank(ra, rb)
        w["n_sequences_with_small_gt"] = int(has.sum())
        res[f"{a}_vs_{b}"] = {
            "n_sequences": S, "point": {"delta_small_recall": pt[0], "delta_precision": pt[1], "delta_mean_ms": pt[2],
                                        "small_recall_a": pt[3], "small_recall_b": pt[4]},
            "cluster_bootstrap": {"B": n_boot, "seed": seed, "unit": "sequence", "delta_small_recall_ci95": q(0),
                                  "delta_precision_ci95": q(1), "delta_mean_ms_ci95": q(2)},
            "sequence_level_wilcoxon_small_recall": w,
            "sequences_a_better": int(np.sum(ra > rb)), "sequences_b_better": int(np.sum(rb > ra)), "sequences_tie": int(np.sum(ra == rb)),
        }
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--mode", choices=["check-f", "uavdt"], required=True)
    a = ap.parse_args()
    out = P0B / "stage_h" / a.run_id / a.mode
    out.mkdir(parents=True, exist_ok=False)
    import scipy  # noqa: F401  (only to record the env; Stage F code does not use scipy)
    env = {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}
    if a.mode == "check-f":
        src = PAPER / "01_visdrone_main" / "data" / "D_TESTDEV_per_image_metrics.csv"
        ref = json.loads((PAPER / "02_paired_stats" / "data" / "F_summary.json").read_text(encoding="utf-8"))
        by = SF.load_by_image(src)
        s_frozen = stage_f_like(by, SF.bootstrap_pair)
        s_fast = stage_f_like(by, bootstrap_pair_fast)
        diffs_frozen = compare_tree(s_frozen, ref)
        diffs_fast_exact = compare_tree(s_fast, ref)
        res = {"run_id": a.run_id, "mode": a.mode, "env": env, "source_csv": str(src.relative_to(ROOT)).replace("\\", "/"),
               "reference": "papers/P0_EI/02_paired_stats/data/F_summary.json (UAV_BT1, 2026-09-17)",
               "frozen_functions_vs_F_summary": {"n_mismatch_exact": len(diffs_frozen), "mismatches": diffs_frozen[:50],
                                                 "max_rel_diff": max_reldiff(s_frozen, ref)},
               "fast_bootstrap_vs_F_summary": {"n_mismatch_exact": len(diffs_fast_exact), "mismatches_sample": diffs_fast_exact[:20],
                                               "max_rel_diff": max_reldiff(s_fast, ref)},
               "fast_vs_frozen_bootstrap_max_rel_diff": max_reldiff(s_fast["bootstrap_all"], s_frozen["bootstrap_all"]),
               "wall_seconds_frozen": s_frozen["wall_seconds"], "wall_seconds_fast": s_fast["wall_seconds"]}
        (out / "check_f_reproduction.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        (out / "summary_frozen_functions.json").write_text(json.dumps(s_frozen, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in res.items() if k not in ("frozen_functions_vs_F_summary", "fast_bootstrap_vs_F_summary")}, indent=1))
        print("frozen exact mismatches:", len(diffs_frozen), "max rel", res["frozen_functions_vs_F_summary"]["max_rel_diff"])
        print("fast exact mismatches:", len(diffs_fast_exact), "max rel", res["fast_bootstrap_vs_F_summary"]["max_rel_diff"])
        return
    src = PAPER / "03_cross_uavdt" / "data" / "E_FULL_per_image_metrics.csv"
    by = SF.load_by_image(src)
    s = stage_f_like(by, bootstrap_pair_fast)
    seq_of = {}
    with src.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            seq_of[r["image"]] = r["seq"]
    rows_by_seq = defaultdict(list)
    for im, md in by.items():
        rows_by_seq[seq_of[im]].append(md)
    cl = cluster_bootstrap(rows_by_seq, SF.ALL_PAIRS, SF.N_BOOT, SF.SEED)
    sec = [f"{x}_vs_{y}" for x, y in SF.SECONDARY]
    for k, padj in zip(sec, SF.holm([cl[k]["sequence_level_wilcoxon_small_recall"]["pvalue"] for k in sec])):
        cl[k]["sequence_level_wilcoxon_small_recall"]["pvalue_holm"] = padj
    summary = {"status": "PASS", "run_id": a.run_id, "source_csv": str(src.relative_to(ROOT)).replace("\\", "/"), "env": env,
               "note": "Stage F functions (frozen) on UAVDT frames; frame-level tests treat ~40k autocorrelated video frames as independent and overstate significance -> use the sequence cluster bootstrap / sequence-level Wilcoxon for inference.",
               "image_level": s, "sequence_cluster": cl, "n_sequences": len(rows_by_seq)}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (out / "paired_table.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["pair", "delta_small_recall", "img_ci_lo", "img_ci_hi", "seq_ci_lo", "seq_ci_hi", "delta_precision", "img_p_ci_lo", "img_p_ci_hi",
                    "seq_p_ci_lo", "seq_p_ci_hi", "delta_mean_ms_1660", "img_ms_ci_lo", "img_ms_ci_hi", "seq_ms_ci_lo", "seq_ms_ci_hi",
                    "img_wilcoxon_p_recall", "seq_wilcoxon_p_recall", "seq_a_better", "seq_b_better", "seq_tie", "img_wilcoxon_p_latency"])
        for x, y in SF.ALL_PAIRS:
            k = f"{x}_vs_{y}"; ib = s["bootstrap_all"][k]; c = cl[k]
            wr = s["primary_wilcoxon_recall_small"] if k == s["primary_pair"] else s["secondary_wilcoxon_recall_small"][k]
            w.writerow([k, ib["point"]["delta_small_recall"], *ib["bootstrap"]["delta_small_recall_ci95"], *c["cluster_bootstrap"]["delta_small_recall_ci95"],
                        ib["point"]["delta_precision"], *ib["bootstrap"]["delta_precision_ci95"], *c["cluster_bootstrap"]["delta_precision_ci95"],
                        ib["point"]["delta_mean_ms"], *ib["bootstrap"]["delta_mean_ms_ci95"], *c["cluster_bootstrap"]["delta_mean_ms_ci95"],
                        wr["pvalue"], c["sequence_level_wilcoxon_small_recall"]["pvalue"], c["sequences_a_better"], c["sequences_b_better"],
                        c["sequences_tie"], s["wilcoxon_latency_oneshot"][k]["pvalue"]])
    print(open(out / "paired_table.csv", encoding="utf-8-sig").read())


if __name__ == "__main__":
    main()
