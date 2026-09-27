#!/usr/bin/env python3
"""P0 Stage D: one-shot five-method eval on VisDrone2019-DET test-dev (local mirror GT)."""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import traceback
import zipfile
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
    finalize,
    run_densk1,
    run_f_full,
    run_sahi640,
    run_unifall,
    save_pred,
)

RUN_ID = "P0-BENCH-D-TESTDEV-20260917-01"
EXPECTED_ZIP_SHA = "b28a94b06dfd9e36ce77ff8155fb82b9d2c030f198a76105933bd56c6ea6a68d"
ROOT = Path(__file__).resolve().parents[4]  # Doctoral-Research-Outline
# parents: stage_d -> P0_Benchmark -> Experiments -> 00_Practice... -> ROOT
# __file__ = ROOT/00_Practice.../Experiments/P0_Benchmark/stage_d/run_....py
# parents[0]=stage_d [1]=P0_Benchmark [2]=Experiments [3]=00_Practice [4]=ROOT
ZIP_PATH = ROOT / "11_Datasets/raw/VisDrone/ultralytics/VisDrone2019-DET-test-dev.zip"
TESTDEV_ROOT = ROOT / "11_Datasets/processed/VisDrone/P0_Benchmark/test-dev"
LABEL = (
    "VisDrone-compatible evaluator on Ultralytics-mirror test-dev local GT "
    "(not official leaderboard AP)"
)
CONF_KEEP = 0.25
IOU_NMS = 0.5


def dump(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def ensure_extracted(zip_path: Path, dest: Path):
    if dest.exists() and any(dest.rglob("*.jpg")):
        return
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(dest)


def find_images_and_anns(root: Path):
    img_dirs = []
    for cand in [
        root / "images",
        root / "VisDrone2019-DET-test-dev" / "images",
        root / "test-dev" / "images",
    ]:
        if cand.is_dir():
            img_dirs.append(cand)
    if not img_dirs:
        img_dirs = [p for p in root.rglob("images") if p.is_dir()]
    if not img_dirs:
        raise FileNotFoundError(f"No images/ under {root}")
    img_dir = img_dirs[0]
    ann_dir = img_dir.parent / "annotations"
    if not ann_dir.is_dir():
        alts = list(root.rglob("annotations"))
        if not alts:
            raise FileNotFoundError(f"No annotations/ near {img_dir}")
        ann_dir = alts[0]
    images = sorted(
        [p for p in img_dir.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
    )
    return images, ann_dir


def load_ann(ann_path: Path) -> np.ndarray:
    if not ann_path.exists():
        return np.zeros((0, 8), dtype=np.float64)
    rows = []
    for line in ann_path.read_text(encoding="utf-8").splitlines():
        line = line.strip().rstrip(",")
        if not line:
            continue
        rows.append([float(v) for v in line.split(",")])
    return np.asarray(rows, dtype=np.float64)


def eval_one(im_bgr, ann_path: Path, pred: np.ndarray):
    h, w = im_bgr.shape[:2]
    raw = load_ann(ann_path)
    if raw.size == 0:
        gt = np.zeros((0, 8), dtype=np.float64)
        ids = np.zeros(0, dtype=int)
        integral = np.zeros((h + 1, w + 1), dtype=np.int32)
        small = set()
        valid = set()
    else:
        if raw.shape[1] < 6:
            raise ValueError(f"bad ann cols {raw.shape} {ann_path}")
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
    ap.add_argument("--max-images", type=int, default=0, help="0 = all")
    ap.add_argument("--skip-extract", action="store_true")
    ap.add_argument("--test-dev-root", type=Path, default=TESTDEV_ROOT)
    ap.add_argument("--zip-path", type=Path, default=ZIP_PATH)
    args = ap.parse_args()

    run_id = args.run_id
    methods = [m.strip() for m in args.methods.split(",") if m.strip()]
    out = EXP / "P0_Benchmark" / "stage_d" / run_id
    out.mkdir(parents=True, exist_ok=True)
    (out / "preds").mkdir(exist_ok=True)
    (out / "framework_config").mkdir(exist_ok=True)
    os.environ["YOLO_AUTOINSTALL"] = "false"
    os.environ["YOLO_CONFIG_DIR"] = str(out / "framework_config")

    log_path = out / "progress.log"

    def log(msg: str):
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
        print(line, flush=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    t_wall0 = time.perf_counter()
    dump(out / "status.json", dict(status="RUNNING", run_id=run_id, label=LABEL))

    try:
        wsha = sha(WEIGHT)
        assert wsha == WEIGHT_SHA, (wsha, WEIGHT_SHA)
        zsha = sha(args.zip_path)
        assert zsha == EXPECTED_ZIP_SHA, (zsha, EXPECTED_ZIP_SHA)
        log(f"SHA OK weight={wsha} zip={zsha}")

        if not args.skip_extract:
            log(f"extracting {args.zip_path} -> {args.test_dev_root}")
            ensure_extracted(args.zip_path, args.test_dev_root)
        images, ann_dir = find_images_and_anns(args.test_dev_root)
        if args.max_images and args.max_images > 0:
            images = images[: args.max_images]
        n_images = len(images)
        log(f"n_images={n_images} ann_dir={ann_dir}")
        if not args.max_images:
            assert n_images == 1610, f"expected 1610 got {n_images}"

        from ultralytics import YOLO

        model = YOLO(str(WEIGHT))
        warm = cv2.imread(str(images[0]))
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
        for i, path in enumerate(images):
            im = cv2.imread(str(path))
            assert im is not None, path
            ann_path = ann_dir / (path.stem + ".txt")
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
                save_pred(out / "preds" / f"{path.stem}__{method}.npy", pred)
                m = eval_one(im, ann_path, pred)
                row = dict(
                    image=path.name,
                    index=i,
                    method=method,
                    n_dets=int(len(pred)),
                    total_ms=float(meta.get("total_ms", float("nan"))),
                    **m,
                )
                per_image.append(row)
            if (i + 1) % 10 == 0 or i == 0:
                log(f"{i+1}/{n_images} {path.name}")
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
                mean_ms=float(np.mean([r["total_ms"] for r in rows])),
            )

        wall = time.perf_counter() - t_wall0
        summary = dict(
            status="PASS",
            run_id=run_id,
            label=LABEL,
            evaluator="diagnose_bt1.prepare_gt+match_gt (VisDrone-compatible; not official server)",
            n_images=n_images,
            conf=CONF_KEEP,
            iou=IOU_NMS,
            small_def="0<w*h<1024 original image space; score>0 GT",
            weight_sha256=wsha,
            zip_sha256=zsha,
            methods=summary_methods,
            wall_seconds=wall,
            gpu=torch.cuda.get_device_name(0),
            python=sys.version,
        )
        dump(out / "summary.json", summary)
        with (out / "per_image_metrics.csv").open("w", newline="", encoding="utf-8-sig") as f:
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