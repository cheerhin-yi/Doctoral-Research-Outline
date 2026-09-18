#!/usr/bin/env python3
"""P0 Stage E: one-shot five-method frozen-weight transfer eval on UAVDT DET."""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import traceback
from pathlib import Path

import cv2
import numpy as np
import torch

EXP = Path(__file__).resolve().parents[2]
STAGE_B = Path(__file__).resolve().parents[1] / "stage_b"
sys.path.insert(0, str(EXP))
sys.path.insert(0, str(STAGE_B))

from diagnose_bt1 import WEIGHT_SHA, match_gt, prepare_gt, sha  # noqa: E402
from run_stage_b_timing import (  # noqa: E402
    METHODS,
    WEIGHT,
    run_densk1,
    run_f_full,
    run_sahi640,
    run_unifall,
    save_pred,
)

RUN_ID = "P0-BENCH-E-UAVDT-20260918-01"
UAVDT_M = Path(r"G:\Schloar Data\UAVDT\UAV-benchmark-M")
UAVDT_GT = Path(r"G:\Schloar Data\UAVDT\UAV-benchmark-MOTD_v1.0\GT")
LABEL = (
    "VisDrone-compatible matcher on UAVDT DET with frozen VisDrone->UAVDT mapping "
    "(transfer trend check; not UAVDT SOTA / not official MATLAB AP)"
)
CONF_KEEP = 0.25
IOU_MATCH = 0.5
# VisDrone YOLO id -> UAVDT eval id (0=car,1=truck,2=bus); matches preregister JSON.
# Official UAVDT GT cats stay 1/2/3 so match_gt(pred_cls+1) aligns after remap to 0/1/2.
VD2UAV = {3: 0, 4: 0, 5: 1, 8: 2}
EXPECTED_SEQS = 50
EXPECTED_FRAMES = 40735
EXPECTED_GT = 50


def dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def remap_pred(pred: np.ndarray) -> np.ndarray:
    if pred is None or len(pred) == 0:
        return np.zeros((0, 6), dtype=np.float64)
    out = []
    for d in pred:
        c = int(d[5])
        if c in VD2UAV:
            e = d.astype(np.float64).copy()
            e[5] = float(VD2UAV[c])
            out.append(e)
    if not out:
        return np.zeros((0, 6), dtype=np.float64)
    return np.asarray(out, dtype=np.float64).reshape(-1, 6)


def frame_index_from_name(name: str) -> int:
    stem = Path(name).stem
    digits = "".join(ch for ch in stem if ch.isdigit())
    if not digits:
        raise ValueError(f"cannot parse frame index from {name}")
    return int(digits)


def load_uavdt_gt_by_frame(gt_path: Path) -> dict[int, np.ndarray]:
    """Return {frame: VisDrone-like raw Nx8 [x,y,w,h,score,cat,trunc,occ]}."""
    by: dict[int, list] = {}
    if not gt_path.exists():
        return {}
    for line in gt_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [float(v) for v in line.split(",")]
        if len(parts) < 9:
            continue
        frame = int(parts[0])
        left, top, bw, bh = parts[2], parts[3], parts[4], parts[5]
        occ = parts[7]
        cat = int(parts[8])
        if cat not in (1, 2, 3):
            continue
        if bw <= 0 or bh <= 0:
            continue
        row = [left, top, bw, bh, 1.0, float(cat), 0.0, float(occ)]
        by.setdefault(frame, []).append(row)
    return {f: np.asarray(rows, dtype=np.float64) for f, rows in by.items()}


def list_uavdt_images(max_images: int = 0):
    seqs = sorted([p for p in UAVDT_M.iterdir() if p.is_dir()])
    if len(seqs) != EXPECTED_SEQS:
        raise AssertionError(f"seqs={len(seqs)} expected {EXPECTED_SEQS}")
    items = []
    for seq in seqs:
        img_dir = seq / "img1"
        if not img_dir.is_dir():
            raise FileNotFoundError(img_dir)
        gt_path = UAVDT_GT / f"{seq.name}_gt_whole.txt"
        if not gt_path.is_file():
            raise FileNotFoundError(gt_path)
        gt_by = load_uavdt_gt_by_frame(gt_path)
        for im_path in sorted(img_dir.glob("*.jpg")):
            fr = frame_index_from_name(im_path.name)
            items.append(
                (
                    im_path,
                    seq.name,
                    fr,
                    gt_by.get(fr, np.zeros((0, 8), dtype=np.float64)),
                )
            )
            if max_images and len(items) >= max_images:
                return items
    return items


def eval_one(im_bgr, raw: np.ndarray, pred: np.ndarray):
    h, w = im_bgr.shape[:2]
    if raw.size == 0:
        gt = np.zeros((0, 8), dtype=np.float64)
        ids = np.zeros(0, dtype=int)
        integral = np.zeros((h + 1, w + 1), dtype=np.int32)
        small: set[int] = set()
        valid: set[int] = set()
    else:
        gt, ids, integral = prepare_gt(raw, h, w)
        small = {
            int(ids[i])
            for i, g in enumerate(gt)
            if g[4] > 0 and 0 < (g[2] * g[3]) < 1024
        }
        valid = {int(ids[i]) for i, g in enumerate(gt) if g[4] > 0}
    matched, fp, ignored = match_gt(gt, ids, pred, integral, h, w)
    tp = len(matched)
    small_tp = len(matched & small)
    return dict(
        tp=tp,
        fp=int(fp),
        ignored=int(ignored),
        valid_gt=len(valid),
        small_gt=len(small),
        small_tp=small_tp,
        recall_small=(small_tp / len(small)) if small else float("nan"),
        precision=(tp / max(1, tp + fp)),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default=RUN_ID)
    ap.add_argument("--methods", default=",".join(METHODS))
    ap.add_argument("--max-images", type=int, default=0, help="0 = all frames")
    ap.add_argument(
        "--save-preds", action="store_true", help="save per-image npy (disk heavy)"
    )
    args = ap.parse_args()

    run_id = args.run_id
    methods = [m.strip() for m in args.methods.split(",") if m.strip()]
    out = EXP / "P0_Benchmark" / "stage_e" / run_id
    out.mkdir(parents=True, exist_ok=True)
    (out / "preds").mkdir(exist_ok=True)
    (out / "framework_config").mkdir(exist_ok=True)
    os.environ["YOLO_AUTOINSTALL"] = "false"
    os.environ["YOLO_CONFIG_DIR"] = str(out / "framework_config")

    log_path = out / "progress.log"

    def log(msg: str) -> None:
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
        print(line, flush=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    t_wall0 = time.perf_counter()
    dump(out / "status.json", dict(status="RUNNING", run_id=run_id, label=LABEL))

    try:
        wsha = sha(WEIGHT)
        assert wsha == WEIGHT_SHA, (wsha, WEIGHT_SHA)
        n_gt = len(list(UAVDT_GT.glob("*_gt_whole.txt")))
        n_seq = len([p for p in UAVDT_M.iterdir() if p.is_dir()])
        assert n_seq == EXPECTED_SEQS and n_gt == EXPECTED_GT, (n_seq, n_gt)
        log(f"SHA OK weight={wsha} seqs={n_seq} gt_whole={n_gt}")

        items = list_uavdt_images(args.max_images)
        n_images = len(items)
        if not args.max_images:
            assert n_images == EXPECTED_FRAMES, f"expected {EXPECTED_FRAMES} got {n_images}"
        log(f"n_images={n_images} methods={methods}")

        from ultralytics import YOLO

        model = YOLO(str(WEIGHT))
        warm = cv2.imread(str(items[0][0]))
        assert warm is not None
        for _ in range(2):
            run_f_full(model, warm, 640)

        sahi_model = None
        if "SAHI640" in methods:
            from sahi import AutoDetectionModel

            sahi_model = AutoDetectionModel.from_pretrained(
                model_type="ultralytics",
                model_path=str(WEIGHT),
                confidence_threshold=0.001,
                device="cuda:0",
            )

        per_image = []
        for i, (path, seq, fr, raw) in enumerate(items):
            im = cv2.imread(str(path))
            assert im is not None, path
            for method in methods:
                if method == "F640":
                    pred, meta = run_f_full(model, im, 640)
                elif method == "F1280":
                    pred, meta = run_f_full(model, im, 1280)
                elif method == "DensK1":
                    pred, meta = run_densk1(model, im)
                elif method == "UnifAll":
                    pred, meta = run_unifall(model, im)
                elif method == "SAHI640":
                    pred, meta = run_sahi640(sahi_model, im)
                else:
                    raise ValueError(method)
                pred = remap_pred(pred)
                if args.save_preds:
                    save_pred(out / "preds" / f"{seq}_{path.stem}__{method}.npy", pred)
                m = eval_one(im, raw, pred)
                ms = float(meta.get("total_ms", float("nan")))
                row = dict(
                    image=f"{seq}/{path.name}",
                    seq=seq,
                    frame=fr,
                    index=i,
                    method=method,
                    n_dets=int(len(pred)),
                    total_ms=ms,
                    **m,
                )
                per_image.append(row)
            if (i + 1) % 10 == 0 or i == 0:
                log(f"{i+1}/{n_images} {seq}/{path.name}")
                with (out / "per_image_metrics_partial.csv").open(
                    "w", newline="", encoding="utf-8-sig"
                ) as f:
                    w = csv.DictWriter(f, fieldnames=list(per_image[0].keys()))
                    w.writeheader()
                    w.writerows(per_image)

        summary_methods = {}
        for method in methods:
            rows = [r for r in per_image if r["method"] == method]
            tp = sum(r["tp"] for r in rows)
            fp = sum(r["fp"] for r in rows)
            small_gt = sum(r["small_gt"] for r in rows)
            small_tp = sum(r["small_tp"] for r in rows)
            summary_methods[method] = dict(
                tp=tp,
                fp=fp,
                precision=tp / max(1, tp + fp),
                small_gt=small_gt,
                small_tp=small_tp,
                small_recall=small_tp / max(1, small_gt),
                n_images=len(rows),
                mean_ms=float(np.nanmean([r["total_ms"] for r in rows])),
            )

        wall = time.perf_counter() - t_wall0
        summary = dict(
            status="PASS",
            run_id=run_id,
            label=LABEL,
            evaluator=(
                "diagnose_bt1.prepare_gt+match_gt after VisDrone->UAVDT pred remap; "
                "official *_gt_ignore.txt not applied "
                "(frozen matching_rules: do not invent ignore masks)"
            ),
            n_images=n_images,
            conf=CONF_KEEP,
            iou=IOU_MATCH,
            small_def="0<w*h<1024 original image space; score>0 GT",
            weight_sha256=wsha,
            mapping="class_mapping_preregister.json FROZEN",
            methods=summary_methods,
            wall_seconds=wall,
            gpu=torch.cuda.get_device_name(0),
            python=sys.version,
            max_images=args.max_images,
            save_preds=bool(args.save_preds),
        )
        dump(out / "summary.json", summary)
        with (out / "per_image_metrics.csv").open(
            "w", newline="", encoding="utf-8-sig"
        ) as f:
            w = csv.DictWriter(f, fieldnames=list(per_image[0].keys()))
            w.writeheader()
            w.writerows(per_image)
        dump(out / "status.json", dict(status="PASS", run_id=run_id, wall_seconds=wall))
        log(json.dumps(summary_methods, ensure_ascii=False, indent=2))
        log(f"DONE wall_seconds={wall:.1f}")
    except Exception:
        (out / "failure.txt").write_text(traceback.format_exc(), encoding="utf-8")
        dump(out / "status.json", dict(status="FAILED", run_id=run_id))
        raise


if __name__ == "__main__":
    main()
