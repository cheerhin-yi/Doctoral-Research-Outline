#!/usr/bin/env python
"""P0 Run J (optional part): failure-case crops from SAVED Run G predictions (CPU only, no inference).

Source preds: stage_d/P0-BENCH-G-5060TI-TESTDEV-20261001-01/preds (RTX 5060 Ti / UAV_BT2, VisDrone test-dev).
Evaluator: frozen diagnose_bt1.prepare_gt + match_gt via frozen stage_d.eval_one semantics (re-implemented
call order only; per-image small_tp is asserted equal to G_TESTDEV_per_image_metrics.csv).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import cv2
import numpy as np

EXP = Path(__file__).resolve().parents[2]
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(EXP))
sys.path.insert(0, str(EXP / "P0_Benchmark" / "stage_b"))
sys.path.insert(0, str(EXP / "P0_Benchmark" / "stage_d"))
from diagnose_bt1 import match_gt, prepare_gt  # noqa: E402  (frozen)
from run_stage_b_timing import build_windows, density_top1  # noqa: E402  (frozen)
from run_stage_d_oneshot import load_ann  # noqa: E402  (frozen)

PREDS = EXP / "P0_Benchmark/stage_d/P0-BENCH-G-5060TI-TESTDEV-20261001-01/preds"
G_CSV = EXP / "papers/P0_EI/04_timing/data/G_TESTDEV_per_image_metrics.csv"
IMG = ROOT / "11_Datasets/processed/VisDrone/P0_Benchmark/test-dev/VisDrone2019-DET-test-dev"


def small_sets(im, ann, pred):
    h, w = im.shape[:2]
    raw = load_ann(ann)
    gt, ids, integral = prepare_gt(raw, h, w)
    small = {int(ids[i]) for i, g in enumerate(gt) if g[4] > 0 and 0 < g[2] * g[3] < 1024}
    matched, fp, _ = match_gt(gt, ids, pred, integral, h, w)
    return raw, small, matched & small


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    a = ap.parse_args()
    out = Path(__file__).resolve().parent / a.run_id / "failure_crops"
    out.mkdir(parents=True, exist_ok=False)
    rows = {}
    with open(G_CSV, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows[(r["image"], r["method"])] = r
    imgs = sorted({k[0] for k in rows})
    st = lambda i, m: int(rows[(i, m)]["small_tp"])
    sg = lambda i: int(rows[(i, "F640")]["small_gt"])
    gap = sorted(imgs, key=lambda i: (st(i, "F1280") - st(i, "DensK1"), i))
    sahi_gap = sorted(imgs, key=lambda i: (st(i, "UnifAll") - st(i, "SAHI640"), i))
    hard = sorted([i for i in imgs if sg(i) >= 50],
                  key=lambda i: (max(st(i, "F1280"), st(i, "DensK1"), st(i, "UnifAll")) / sg(i), i))
    cases = [("F1280_wins", gap[-1], "F1280", "DensK1"), ("F1280_wins", gap[-2], "F1280", "DensK1"),
             ("DensK1_wins", gap[0], "F1280", "DensK1"), ("DensK1_wins", gap[1], "F1280", "DensK1"),
             ("SAHI640_loses_same_pixels", sahi_gap[-1], "UnifAll", "SAHI640"),
             ("all_miss", hard[0], "F1280", "UnifAll")]
    meta = []
    for k, (tag, name, ma, mb) in enumerate(cases, 1):
        im = cv2.imread(str(IMG / "images" / name))
        ann = IMG / "annotations" / (Path(name).stem + ".txt")
        h, w = im.shape[:2]
        P = {m: np.load(PREDS / f"{Path(name).stem}__{m}.npy") for m in ("F640", ma, mb)}
        raw, small, hit_a = small_sets(im, ann, P[ma])
        _, _, hit_b = small_sets(im, ann, P[mb])
        assert len(hit_a) == st(name, ma) and len(hit_b) == st(name, mb), (name, len(hit_a), len(hit_b))
        wins = build_windows(h, w)
        assert len(P["F640"]) < 500  # finalize cap not hit -> density window recomputation is exact
        dens_win = wins[density_top1(P["F640"], wins)]
        # crop = grid window with the largest symmetric difference of matched small GT
        cen = {i: (raw[i, 0] + raw[i, 2] / 2, raw[i, 1] + raw[i, 3] / 2) for i in small}
        def score(win):
            x, y, x2, y2 = win
            return sum(1 for i in (hit_a ^ hit_b) | (small - hit_a - hit_b) if x <= cen[i][0] < x2 and y <= cen[i][1] < y2)
        cx, cy, cx2, cy2 = max(wins, key=lambda wv: (score(wv), -wins.index(wv)))
        panels = []
        for m, hit in ((ma, hit_a), (mb, hit_b)):
            c = im[cy:cy2, cx:cx2].copy()
            for i in small:
                x, y, bw, bh = raw[i, :4].astype(int)
                col = (0, 200, 0) if i in hit else (0, 0, 255)
                cv2.rectangle(c, (x - cx, y - cy), (x - cx + bw, y - cy + bh), col, 1)
            if "DensK1" == m:
                x, y, x2, y2 = dens_win
                cv2.rectangle(c, (x - cx, y - cy), (x2 - cx - 1, y2 - cy - 1), (0, 220, 255), 2)
            ins = [i for i in small if cx <= cen[i][0] < cx2 and cy <= cen[i][1] < cy2]
            txt = f"{m}  crop small {sum(i in hit for i in ins)}/{len(ins)}  image small {len(hit)}/{len(small)}"
            cv2.rectangle(c, (0, 0), (c.shape[1], 22), (0, 0, 0), -1)
            cv2.putText(c, txt, (4, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            panels.append(c)
        gapcol = np.full((panels[0].shape[0], 8, 3), 255, np.uint8)
        fn = f"case{k}_{tag}_{Path(name).stem}.jpg"
        cv2.imwrite(str(out / fn), np.concatenate([panels[0], gapcol, panels[1]], 1), [cv2.IMWRITE_JPEG_QUALITY, 92])
        meta.append(dict(case=k, tag=tag, image=name, size=f"{w}x{h}", methods=[ma, mb], crop_xyxy=[cx, cy, cx2, cy2],
                         small_gt=len(small), small_tp={ma: len(hit_a), mb: len(hit_b)},
                         densk1_window_xyxy=list(dens_win) if "DensK1" in (ma, mb) else None, file=fn))
    (out / "cases.json").write_text(json.dumps(dict(run_id=a.run_id, preds_source=str(PREDS.relative_to(ROOT)),
        gpu_env="RTX 5060 Ti / UAV_BT2 (Run G saved preds)",
        legend="green = small GT matched by this method; red = small GT missed; yellow = DensK1 selected window",
        selection="max/min (F1280-DensK1) small_tp; max (UnifAll-SAHI640) small_tp; lowest best-of-3 small recall among images with >=50 small GT; ties by name",
        cases=meta), indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
