#!/usr/bin/env python3
"""P0 Stage B: cal48 x 5 methods x 3 timing reps on current GPU (no training)."""
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
sys.path.insert(0, str(EXP))
from diagnose_bt1 import BASE, RUNS, WEIGHT_SHA, axis_windows, nms, sha  # noqa: E402

RUN_ID = "P0-BENCH-B-TIMING-20260917-01"
METHODS = ["F640", "F1280", "DensK1", "UnifAll", "SAHI640"]
REPS = 3
CONF_KEEP = 0.25
IOU_NMS = 0.5
MAX_DET = 500
WEIGHT = BASE / RUNS[-1] / "train/weights/last.pt"
CAL_LIST = BASE / "full_data_v2/cal48.txt"
OUT = EXP / "P0_Benchmark" / "stage_b" / RUN_ID


def dump(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def boxes_from_result(r) -> np.ndarray:
    if r.boxes is None or len(r.boxes) == 0:
        return np.zeros((0, 6), dtype=np.float64)
    xyxy = r.boxes.xyxy.detach().float().cpu().numpy()
    conf = r.boxes.conf.detach().float().cpu().numpy()
    cls = r.boxes.cls.detach().float().cpu().numpy()
    return np.concatenate([xyxy, conf[:, None], cls[:, None]], axis=1).astype(np.float64)


def finalize(pred: np.ndarray) -> np.ndarray:
    pred = np.asarray(pred, dtype=np.float64).reshape(-1, 6)
    if not len(pred):
        return pred
    pred = pred[pred[:, 4] >= CONF_KEEP]
    return nms(pred, MAX_DET)


def build_windows(h: int, w: int):
    return [(x, y, min(w, x + 640), min(h, y + 640)) for y in axis_windows(h) for x in axis_windows(w)]


def density_top1(full: np.ndarray, windows):
    full = np.asarray(full, dtype=np.float64).reshape(-1, 6)
    keep = full[full[:, 4] >= 0.25]
    scores = []
    for x, y, x2, y2 in windows:
        if not len(keep):
            scores.append(0.0)
            continue
        cx = (keep[:, 0] + keep[:, 2]) * 0.5
        cy = (keep[:, 1] + keep[:, 3]) * 0.5
        scores.append(float(((cx >= x) & (cx < x2) & (cy >= y) & (cy < y2)).sum()))
    order = np.argsort(-np.asarray(scores), kind="stable")
    return int(order[0])


def map_local(pred: np.ndarray, x: int, y: int, x2: int, y2: int) -> np.ndarray:
    if not len(pred):
        return pred.reshape(0, 6)
    p = pred.copy()
    centers = (p[:, :2] + p[:, 2:4]) / 2
    p = p[(centers[:, 0] < (x2 - x)) & (centers[:, 1] < (y2 - y))].copy()
    if not len(p):
        return p.reshape(0, 6)
    p[:, [0, 2]] = np.clip(p[:, [0, 2]], 0, x2 - x) + x
    p[:, [1, 3]] = np.clip(p[:, [1, 3]], 0, y2 - y) + y
    return p[(p[:, 2] > p[:, 0]) & (p[:, 3] > p[:, 1])]


def infer_full(model, im_bgr, imgsz: int) -> np.ndarray:
    r = model.predict(
        im_bgr, imgsz=imgsz, rect=False, device=0, batch=1, half=False,
        conf=0.001, iou=IOU_NMS, max_det=1000, save=False, verbose=False,
    )[0]
    return boxes_from_result(r)


def infer_patch(model, patch_bgr) -> np.ndarray:
    r = model.predict(
        patch_bgr, imgsz=640, rect=False, device=0, batch=1, half=False,
        conf=0.001, iou=IOU_NMS, max_det=1000, save=False, verbose=False,
    )[0]
    return boxes_from_result(r)


def run_f_full(model, im, imgsz: int):
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    pred = finalize(infer_full(model, im, imgsz))
    torch.cuda.synchronize()
    t1 = time.perf_counter()
    return pred, {"total_ms": (t1 - t0) * 1000.0, "n_windows": 0, "selected": []}


def run_densk1(model, im):
    h, w = im.shape[:2]
    windows = build_windows(h, w)
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    full = infer_full(model, im, 640)
    torch.cuda.synchronize()
    t1 = time.perf_counter()
    j = density_top1(full, windows)
    x, y, x2, y2 = windows[j]
    patch = np.full((640, 640, 3), 114, dtype=np.uint8)
    patch[: y2 - y, : x2 - x] = im[y:y2, x:x2]
    local = map_local(infer_patch(model, patch), x, y, x2, y2)
    torch.cuda.synchronize()
    t2 = time.perf_counter()
    pred = finalize(np.concatenate([full, local], axis=0) if len(local) else full)
    torch.cuda.synchronize()
    t3 = time.perf_counter()
    return pred, {
        "total_ms": (t3 - t0) * 1000.0,
        "global_ms": (t1 - t0) * 1000.0,
        "local_ms": (t2 - t1) * 1000.0,
        "merge_ms": (t3 - t2) * 1000.0,
        "n_windows": 1,
        "selected": [j],
    }


def run_unifall(model, im):
    h, w = im.shape[:2]
    windows = build_windows(h, w)
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    full = infer_full(model, im, 640)
    locals_ = []
    for x, y, x2, y2 in windows:
        patch = np.full((640, 640, 3), 114, dtype=np.uint8)
        patch[: y2 - y, : x2 - x] = im[y:y2, x:x2]
        locals_.append(map_local(infer_patch(model, patch), x, y, x2, y2))
    parts = [full] + [p for p in locals_ if len(p)]
    pred = finalize(np.concatenate(parts, axis=0) if parts else full)
    torch.cuda.synchronize()
    t1 = time.perf_counter()
    return pred, {
        "total_ms": (t1 - t0) * 1000.0,
        "n_windows": len(windows),
        "selected": list(range(len(windows))),
    }


def run_sahi640(detection_model, im_bgr):
    from sahi.predict import get_sliced_prediction

    torch.cuda.synchronize()
    t0 = time.perf_counter()
    rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
    result = get_sliced_prediction(
        rgb,
        detection_model,
        slice_height=640,
        slice_width=640,
        overlap_height_ratio=0.25,
        overlap_width_ratio=0.25,
        verbose=0,
    )
    rows = []
    for pred in result.object_prediction_list:
        bb = pred.bbox
        rows.append([bb.minx, bb.miny, bb.maxx, bb.maxy, float(pred.score.value), float(pred.category.id)])
    arr = np.asarray(rows, dtype=np.float64).reshape(-1, 6)
    pred = finalize(arr)
    torch.cuda.synchronize()
    t1 = time.perf_counter()
    return pred, {
        "total_ms": (t1 - t0) * 1000.0,
        "n_windows": -1,
        "selected": [],
        "sahi_postprocess": "sahi_default_NMS",
    }


def save_pred(path: Path, pred: np.ndarray):
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, pred.astype(np.float64))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--methods", default=",".join(METHODS))
    ap.add_argument("--max-images", type=int, default=48)
    ap.add_argument("--skip-sahi", action="store_true")
    ap.add_argument("--run-id", default=RUN_ID)
    args = ap.parse_args()
    methods = [m.strip() for m in args.methods.split(",") if m.strip()]
    if args.skip_sahi and "SAHI640" in methods:
        methods = [m for m in methods if m != "SAHI640"]

    run_id = args.run_id or RUN_ID
    out = EXP / "P0_Benchmark" / "stage_b" / run_id
    # rebind module-level names used below
    globals()['RUN_ID'] = run_id
    globals()['OUT'] = out

    OUT.mkdir(parents=True, exist_ok=False)
    os.environ["YOLO_AUTOINSTALL"] = "false"
    os.environ["YOLO_CONFIG_DIR"] = str(OUT / "framework_config")
    (OUT / "framework_config").mkdir()
    (OUT / "preds").mkdir()

    assert sha(WEIGHT) == WEIGHT_SHA, (sha(WEIGHT), WEIGHT_SHA)
    paths = [Path(s.strip()) for s in CAL_LIST.read_text(encoding="utf-8").splitlines() if s.strip()]
    assert len(paths) == 48
    paths = paths[: args.max_images]

    dump(OUT / "status.json", dict(status="RUNNING", run_id=RUN_ID, methods=methods, reps=REPS, gpu=torch.cuda.get_device_name(0)))
    dump(
        OUT / "protocol.json",
        dict(
            run_id=RUN_ID,
            weight=str(WEIGHT),
            weight_sha256=WEIGHT_SHA,
            cal_list=str(CAL_LIST),
            cal_sha256=sha(CAL_LIST),
            conf_keep=CONF_KEEP,
            iou_nms=IOU_NMS,
            max_det=MAX_DET,
            methods=methods,
            reps=REPS,
            timing_boundary="decoded_image_to_final_eval_ready_dets_with_cuda_sync",
            hardware_role="pipeline_bringup_on_local_GPU; formal 4090 table later",
        ),
    )

    from ultralytics import YOLO

    model = YOLO(str(WEIGHT))
    warm = cv2.imread(str(paths[0]))
    assert warm is not None
    for _ in range(3):
        run_f_full(model, warm, 640)
        run_f_full(model, warm, 1280)

    sahi_model = None
    if "SAHI640" in methods:
        from sahi import AutoDetectionModel

        sahi_model = AutoDetectionModel.from_pretrained(
            model_type="ultralytics",
            model_path=str(WEIGHT),
            confidence_threshold=0.001,
            device="cuda:0",
        )

    rows = []
    try:
        for i, path in enumerate(paths):
            im = cv2.imread(str(path))
            assert im is not None, path
            image_id = path.name
            for rep in range(REPS):
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
                    if rep == 0:
                        save_pred(OUT / "preds" / f"{i:02d}_{method}_r0.npy", pred)
                    else:
                        ref = np.load(OUT / "preds" / f"{i:02d}_{method}_r0.npy")
                        close = pred.shape == ref.shape and (
                            np.allclose(pred, ref, atol=1e-5, rtol=0) if pred.size else True
                        )
                        meta["consistent_with_rep0"] = bool(close)
                        if not close:
                            save_pred(OUT / "preds" / f"{i:02d}_{method}_r{rep}_MISMATCH.npy", pred)
                    row = dict(
                        image=image_id,
                        index=i,
                        method=method,
                        rep=rep,
                        n_dets=int(len(pred)),
                        total_ms=float(meta["total_ms"]),
                        n_windows=int(meta.get("n_windows", 0)),
                        selected=json.dumps(meta.get("selected", [])),
                        consistent_with_rep0=meta.get("consistent_with_rep0", ""),
                        global_ms=float(meta.get("global_ms", "") or "nan") if "global_ms" in meta else "",
                        local_ms=float(meta.get("local_ms", "") or "nan") if "local_ms" in meta else "",
                        merge_ms=float(meta.get("merge_ms", "") or "nan") if "merge_ms" in meta else "",
                    )
                    rows.append(row)
                    with (OUT / "timings_partial.csv").open("w", newline="", encoding="utf-8-sig") as f:
                        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                        w.writeheader()
                        w.writerows(rows)
            print(f"{i+1}/{len(paths)} {image_id} done", flush=True)

        summary = dict(
            status="PASS",
            run_id=RUN_ID,
            n_images=len(paths),
            reps=REPS,
            methods=methods,
            gpu=torch.cuda.get_device_name(0),
        )
        budget = [10, 15, 20, 25, 30, 40, 50, 75, 100]
        by = {}
        for m in methods:
            vals = np.array([r["total_ms"] for r in rows if r["method"] == m], dtype=float)
            img_med = []
            for i in range(len(paths)):
                v = [r["total_ms"] for r in rows if r["method"] == m and r["index"] == i]
                img_med.append(float(np.median(v)))
            img_med = np.asarray(img_med, dtype=float)
            by[m] = dict(
                n=int(len(vals)),
                mean_ms=float(vals.mean()),
                median_ms=float(np.median(vals)),
                std_ms=float(vals.std(ddof=1)) if len(vals) > 1 else 0.0,
                p90_ms=float(np.percentile(vals, 90)),
                p95_ms=float(np.percentile(vals, 95)),
                p99_ms=float(np.percentile(vals, 99)),
                min_ms=float(vals.min()),
                max_ms=float(vals.max()),
                image_median_mean_ms=float(img_med.mean()),
                image_median_p95_ms=float(np.percentile(img_med, 95)),
                budget_violation_rate={str(t): float(np.mean(img_med > t)) for t in budget},
                inconsistent_reps=int(
                    sum(1 for r in rows if r["method"] == m and r.get("consistent_with_rep0") is False)
                ),
            )
        summary["timing"] = by
        summary["peak_vram_bytes"] = int(torch.cuda.max_memory_allocated())
        dump(OUT / "summary.json", summary)
        with (OUT / "timings.csv").open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        dump(OUT / "status.json", dict(status="PASS", run_id=RUN_ID, out=str(OUT)))
        print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    except Exception:
        (OUT / "failure.txt").write_text(traceback.format_exc(), encoding="utf-8")
        dump(OUT / "status.json", dict(status="FAILED", run_id=RUN_ID))
        raise


if __name__ == "__main__":
    main()
