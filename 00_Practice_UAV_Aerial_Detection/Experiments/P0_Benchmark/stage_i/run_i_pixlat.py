#!/usr/bin/env python
"""P0 Stage I: pixel-latency normalised table (CPU only, no inference).

Counts the network-input pixels each frozen protocol feeds to the detector per image,
using the frozen Stage B geometry (axis_windows / build_windows imported unchanged) and
the installed sahi slicer + ultralytics LetterBox (the code paths SAHI640 actually used),
then joins with existing per-image metrics:
  VisDrone test-dev: Stage D (GTX 1660 SUPER / UAV_BT1) and Run G (RTX 5060 Ti / UAV_BT2)
  UAVDT:             Stage E (GTX 1660 SUPER / UAV_BT1)
Latencies from different GPUs are kept in separate columns and never pooled.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from PIL import Image

EXP = Path(__file__).resolve().parents[2]
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(EXP))
sys.path.insert(0, str(EXP / "P0_Benchmark" / "stage_b"))
from diagnose_bt1 import axis_windows  # noqa: E402  (frozen)
from run_stage_b_timing import build_windows  # noqa: E402  (frozen)

import sahi  # noqa: E402
import ultralytics  # noqa: E402
from sahi.slicing import get_slice_bboxes  # noqa: E402
from ultralytics.data.augment import LetterBox  # noqa: E402

PAPERS = EXP / "papers" / "P0_EI"
D_CSV = PAPERS / "01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv"
G_CSV = PAPERS / "04_timing/data/G_TESTDEV_per_image_metrics.csv"
E_CSV = PAPERS / "03_cross_uavdt/data/E_FULL_per_image_metrics.csv"
VIS_IMG = ROOT / "11_Datasets/processed/VisDrone/P0_Benchmark/test-dev"
UAVDT_M = Path(r"G:\Schloar Data\P0\dataset\UAVDT\UAV-benchmark-M")
METHODS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
SAHI_SLICE, SAHI_OVL = 640, 0.25  # stage_b run_sahi640 arguments
SAHI_IMGSZ = 640  # no image_size passed -> ultralytics uses ckpt arg imgsz (train args.yaml: 640)
STRIDE = 32


def lb_shape(h, w, imgsz, auto):
    """Exact ultralytics LetterBox output shape (applied to a dummy array)."""
    out = LetterBox((imgsz, imgsz), auto=auto, stride=STRIDE)(image=np.zeros((h, w, 3), np.uint8))
    return out.shape[0], out.shape[1]


def content_px(h, w, imgsz):
    r = min(imgsz / h, imgsz / w)
    return round(w * r) * round(h * r)


_cache = {}


def geometry(h, w):
    if (h, w) in _cache:
        return _cache[(h, w)]
    g = {}
    for m, s in (("F640", 640), ("F1280", 1280)):
        H, W = lb_shape(h, w, s, auto=False)  # infer_full: rect=False -> square letterbox
        g[m] = dict(passes=1, input_px=H * W, content_px=content_px(h, w, s), local_scale=min(s / h, s / w))
    wins = build_windows(h, w)
    full = g["F640"]
    win_content = [(x2 - x) * (y2 - y) for x, y, x2, y2 in wins]
    # DensK1: F640 + 1 window (640x640 patch, pad 114, rect=False imgsz 640 -> 640x640, scale 1.0)
    g["DensK1"] = dict(passes=2, input_px=full["input_px"] + 640 * 640,
                       content_px=full["content_px"] + float(np.mean(win_content)),  # selected window varies; mean over grid
                       local_scale=1.0)
    g["UnifAll"] = dict(passes=1 + len(wins), input_px=full["input_px"] + len(wins) * 640 * 640,
                        content_px=full["content_px"] + sum(win_content), local_scale=1.0, n_windows=len(wins))
    sl = get_slice_bboxes(h, w, SAHI_SLICE, SAHI_SLICE, False, SAHI_OVL, SAHI_OVL)
    inp = cont = 0
    for x1, y1, x2, y2 in sl:  # predict() default rect=True -> minimal stride-32 letterbox
        H, W = lb_shape(y2 - y1, x2 - x1, SAHI_IMGSZ, auto=True)
        inp += H * W
        cont += content_px(y2 - y1, x2 - x1, SAHI_IMGSZ)
    std = len(sl) > 1  # sahi: standard full-image pred only if num_slices > 1 (perform_standard_pred=True)
    if std:
        H, W = lb_shape(h, w, SAHI_IMGSZ, auto=True)
        inp += H * W
        cont += content_px(h, w, SAHI_IMGSZ)
    g["SAHI640"] = dict(passes=len(sl) + int(std), input_px=inp, content_px=cont,
                        local_scale=min(SAHI_IMGSZ / min(SAHI_SLICE, h), SAHI_IMGSZ / min(SAHI_SLICE, w), 1e9),
                        n_slices=len(sl), standard_pred=std)
    _cache[(h, w)] = g
    return g


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def aggregate(rows_by_method, sizes, lat_cols):
    """rows_by_method[m] = list of dict rows; lat_cols = {label: {(image,m): ms}}"""
    out = {}
    for m in METHODS:
        rows = rows_by_method[m]
        geo = [geometry(*sizes[r["image"]])[m] for r in rows]
        stp = sum(int(r["small_tp"]) for r in rows)
        sgt = sum(int(r["small_gt"]) for r in rows)
        tp = sum(int(r["tp"]) for r in rows)
        fp = sum(int(r["fp"]) for r in rows)
        rec = {
            "n_images": len(rows),
            "mean_passes": float(np.mean([g["passes"] for g in geo])),
            "mean_input_mpx": float(np.mean([g["input_px"] for g in geo])) / 1e6,
            "mean_content_mpx": float(np.mean([g["content_px"] for g in geo])) / 1e6,
            "mean_local_scale": float(np.mean([g["local_scale"] for g in geo])),
            "small_recall": stp / sgt,
            "precision": tp / (tp + fp),
        }
        rec["small_recall_per_input_mpx"] = rec["small_recall"] / rec["mean_input_mpx"]
        for lab, lat in lat_cols.items():
            ms = [lat[(r["image"], m)] for r in rows]
            rec[f"mean_ms_{lab}"] = float(np.mean(ms))
            rec[f"ms_per_input_mpx_{lab}"] = rec[f"mean_ms_{lab}"] / rec["mean_input_mpx"]
        out[m] = rec
    base = out["F640"]
    for m in METHODS:
        r = out[m]
        dm = r["mean_input_mpx"] - base["mean_input_mpx"]
        r["delta_mpx_vs_F640"] = dm
        r["delta_small_recall_vs_F640"] = r["small_recall"] - base["small_recall"]
        r["marginal_recall_per_added_mpx"] = (r["delta_small_recall_vs_F640"] / dm) if dm > 0 else None
        for lab in lat_cols:
            d = r[f"mean_ms_{lab}"] - base[f"mean_ms_{lab}"]
            r[f"delta_ms_vs_F640_{lab}"] = d
            r[f"marginal_ms_per_added_mpx_{lab}"] = (d / dm) if dm > 0 else None
            r[f"marginal_recall_per_added_10ms_{lab}"] = (r["delta_small_recall_vs_F640"] / d * 10) if d > 0 else None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    a = ap.parse_args()
    out_dir = Path(__file__).resolve().parent / a.run_id
    out_dir.mkdir(parents=True, exist_ok=False)

    # ---- VisDrone test-dev
    img_dir = next(p for p in [VIS_IMG / "images", VIS_IMG / "VisDrone2019-DET-test-dev" / "images",
                               VIS_IMG / "test-dev" / "images"] if p.is_dir())
    D = read_rows(D_CSV)
    G = read_rows(G_CSV)
    vis_sizes = {}
    for name in sorted({r["image"] for r in D}):
        with Image.open(img_dir / name) as im:
            w, h = im.size
        vis_sizes[name] = (h, w)
    byD = defaultdict(list)
    for r in D:
        byD[r["method"]].append(r)
    lat_vis = {"1660_UAV_BT1": {(r["image"], r["method"]): float(r["total_ms"]) for r in D},
               "5060Ti_UAV_BT2": {(r["image"], r["method"]): float(r["total_ms"]) for r in G}}
    assert set(lat_vis["1660_UAV_BT1"]) == set(lat_vis["5060Ti_UAV_BT2"])
    vis = aggregate(byD, vis_sizes, lat_vis)
    # same accuracy computed on Run G rows for reference (should match within Run G consistency note)
    byG = defaultdict(list)
    for r in G:
        byG[r["method"]].append(r)
    for m in METHODS:
        s = sum(int(r["small_tp"]) for r in byG[m]) / sum(int(r["small_gt"]) for r in byG[m])
        vis[m]["small_recall_runG_rows"] = s

    # ---- UAVDT
    E = read_rows(E_CSV)
    ua_sizes = {}
    for name in sorted({r["image"] for r in E}):
        seq, fn = name.split("/")
        with Image.open(UAVDT_M / seq / "img1" / fn) as im:
            w, h = im.size
        ua_sizes[name] = (h, w)
    byE = defaultdict(list)
    for r in E:
        byE[r["method"]].append(r)
    ua = aggregate(byE, ua_sizes, {"1660_UAV_BT1": {(r["image"], r["method"]): float(r["total_ms"]) for r in E}})

    size_hist = lambda s: {f"{w}x{h}": c for (h, w), c in sorted(
        {k: sum(1 for v in s.values() if v == k) for k in set(s.values())}.items(), key=lambda kv: -kv[1])}
    geo_by_size = {f"{w}x{h}": geometry(h, w) for (h, w) in sorted(set(vis_sizes.values()) | set(ua_sizes.values()))}
    summary = {
        "status": "PASS",
        "run_id": a.run_id,
        "env": {"python": platform.python_version(), "numpy": np.__version__, "sahi": sahi.__version__,
                "ultralytics": ultralytics.__version__},
        "definitions": {
            "input_px": "pixels of the tensor(s) fed to the network per image, incl. letterbox padding, summed over all forward passes",
            "content_px": "same but excluding padding (resized image content)",
            "local_scale": "resize factor applied to image content in the highest-resolution pass (1.0 = native)",
            "F640/F1280": "model.predict(imgsz, rect=False) -> square imgsz^2",
            "DensK1": "F640 + 1 window; window 640x640 patch padded with 114, predicted at imgsz 640 rect=False",
            "UnifAll": "F640 + all build_windows() windows (axis_windows: range(0, max(1,L-640+1), 512) + [max(0,L-640)])",
            "SAHI640": "sahi.slicing.get_slice_bboxes(slice 640, overlap 0.25) crops, each predicted with ultralytics "
                       "default rect=True at ckpt imgsz 640 (stride-32 minimal letterbox); + one standard full-image "
                       "pred when num_slices>1 (sahi perform_standard_pred=True default)",
            "small_recall_per_input_mpx": "pooled small recall / mean input Mpx per image",
            "marginal_recall_per_added_mpx": "(small recall - F640 small recall) / (input Mpx - F640 input Mpx)",
        },
        "visdrone_testdev": {"image_sizes": size_hist(vis_sizes), "methods": vis},
        "uavdt": {"image_sizes": size_hist(ua_sizes), "methods": ua},
        "geometry_by_size": geo_by_size,
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    with open(out_dir / "pixel_latency_table.csv", "w", newline="", encoding="utf-8") as f:
        cols = ["dataset", "method", "n_images", "mean_passes", "mean_input_mpx", "mean_content_mpx",
                "mean_local_scale", "small_recall", "precision", "small_recall_per_input_mpx",
                "delta_mpx_vs_F640", "delta_small_recall_vs_F640", "marginal_recall_per_added_mpx",
                "mean_ms_1660_UAV_BT1", "ms_per_input_mpx_1660_UAV_BT1", "marginal_ms_per_added_mpx_1660_UAV_BT1",
                "mean_ms_5060Ti_UAV_BT2", "ms_per_input_mpx_5060Ti_UAV_BT2", "marginal_ms_per_added_mpx_5060Ti_UAV_BT2"]
        wr = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        wr.writeheader()
        for ds, res in (("VisDrone_testdev", vis), ("UAVDT", ua)):
            for m in METHODS:
                wr.writerow({"dataset": ds, "method": m, **res[m]})
    print(json.dumps({k: summary[k] for k in ("env",)}, indent=1))
    print(json.dumps(summary["visdrone_testdev"]["image_sizes"]), json.dumps(summary["uavdt"]["image_sizes"]))
    print(open(out_dir / "pixel_latency_table.csv", encoding="utf-8").read())


if __name__ == "__main__":
    main()
