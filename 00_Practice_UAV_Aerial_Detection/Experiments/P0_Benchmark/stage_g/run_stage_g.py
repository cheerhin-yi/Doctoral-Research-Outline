#!/usr/bin/env python3
"""P0 Run G launcher (RTX 5060 Ti formal timing).

Invokes the FROZEN Stage B / Stage D runners *unchanged* as subprocesses with
Run-G parameters (--run-id / --max-images / --skip-extract). It never edits or
copies their code. Per-run evidence (config, preflight, child log, GPU monitor,
result) goes to stage_g/<run_id>/stage_<B|D>/; the frozen runners write their own outputs
to stage_b/<run_id>/ or stage_d/<run_id>/ as usual.

No training, no new mechanism, no protocol / evaluator / class-map change.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve()
P0B = HERE.parents[1]                 # Experiments/P0_Benchmark
EXP = HERE.parents[2]                 # Experiments
ROOT = HERE.parents[4]                # repo root
FROZEN = {
    "B": P0B / "stage_b" / "run_stage_b_timing.py",
    "D": P0B / "stage_d" / "run_stage_d_oneshot.py",
}
DIAG = EXP / "diagnose_bt1.py"
WEIGHT = ROOT / "11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt"
WEIGHT_SHA = "bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533"
EXPECTED_PY = r"F:\Conda\envs\UAV_BT2\python.exe"


def sha_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sha_lf(p: Path) -> str:
    """SHA-256 of the file with CRLF normalised to LF (== content in git)."""
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def git_blob(p: Path) -> str:
    data = p.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def run_text(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception as e:  # noqa: BLE001
        return f"ERROR {e!r}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--stage", choices=["B", "D"], required=True)
    ap.add_argument("--max-images", type=int, default=None)
    ap.add_argument("--skip-extract", action="store_true")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    assert a.run_id.startswith("P0-BENCH-G-5060TI-"), a.run_id

    out = P0B / "stage_g" / a.run_id / f"stage_{a.stage}"
    out.mkdir(parents=True, exist_ok=False)

    import torch  # preflight only; the child process does the real work

    gpu = torch.cuda.get_device_name(0) if torch.cuda.is_available() else None
    pre = {
        "run_id": a.run_id,
        "stage": a.stage,
        "started_local": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "python": sys.executable,
        "python_version": platform.python_version(),
        "expected_python": EXPECTED_PY,
        "torch": torch.__version__,
        "cuda_runtime": torch.version.cuda,
        "cudnn": torch.backends.cudnn.version(),
        "cuda_available": torch.cuda.is_available(),
        "gpu": gpu,
        "gpu_capability": list(torch.cuda.get_device_capability(0)) if gpu else None,
        "weight": str(WEIGHT),
        "weight_sha256": sha_file(WEIGHT),
        "weight_sha256_expected": WEIGHT_SHA,
        "frozen_scripts": {
            str(p.relative_to(ROOT)).replace("\\", "/"): {"sha256_lf": sha_lf(p), "git_blob": git_blob(p)}
            for p in [FROZEN["B"], FROZEN["D"], DIAG]
        },
        "git_head": run_text(["git", "-C", str(ROOT), "rev-parse", "HEAD"]),
        "nvidia_smi_gpu": run_text(["nvidia-smi", "--query-gpu=name,uuid,driver_version,utilization.gpu,memory.used,memory.total,temperature.gpu,pstate,clocks.sm,clocks.mem,power.draw,power.limit", "--format=csv"]),
        "nvidia_smi_compute_apps": run_text(["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv"]),
    }
    try:
        import numpy, ultralytics, sahi, cv2, scipy  # noqa: E401
        pre["packages"] = {"numpy": numpy.__version__, "ultralytics": ultralytics.__version__, "sahi": sahi.__version__,
                           "opencv": cv2.__version__, "scipy": scipy.__version__}
    except Exception as e:  # noqa: BLE001
        pre["packages_error"] = repr(e)

    checks = {
        "python_is_UAV_BT2": os.path.normcase(sys.executable) == os.path.normcase(EXPECTED_PY),
        "cuda_available": bool(pre["cuda_available"]),
        "gpu_is_5060ti": bool(gpu and "5060 Ti" in gpu),
        "weight_sha_matches_lock": pre["weight_sha256"] == WEIGHT_SHA,
        "ultralytics_8.4.90": pre.get("packages", {}).get("ultralytics") == "8.4.90",
    }
    pre["checks"] = checks
    cmd = [sys.executable, "-u", str(FROZEN[a.stage]), "--run-id", a.run_id]
    if a.max_images is not None:
        cmd += ["--max-images", str(a.max_images)]
    if a.skip_extract:
        if a.stage != "D":
            raise SystemExit("--skip-extract only applies to stage D")
        cmd += ["--skip-extract"]
    pre["child_cmd"] = cmd
    pre["child_output_dir"] = str((P0B / ("stage_b" if a.stage == "B" else "stage_d") / a.run_id).relative_to(ROOT)).replace("\\", "/")
    pre["note"] = a.note
    (out / "config.json").write_text(json.dumps(pre, ensure_ascii=False, indent=2), encoding="utf-8")
    if not all(checks.values()):
        (out / "result.json").write_text(json.dumps({"status": "PREFLIGHT_FAIL", "checks": checks}, indent=2), encoding="utf-8")
        print("PREFLIGHT FAIL", checks, flush=True)
        raise SystemExit(2)
    print("PREFLIGHT OK", json.dumps(checks), flush=True)
    del torch

    mon_f = (out / "gpu_monitor.csv").open("w", encoding="utf-8")
    mon = subprocess.Popen(
        ["nvidia-smi", "--query-gpu=timestamp,utilization.gpu,memory.used,temperature.gpu,clocks.sm,clocks.mem,power.draw,pstate",
         "--format=csv", "-l", "2"], stdout=mon_f, stderr=subprocess.STDOUT)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    t0 = time.perf_counter()
    with (out / "run.log").open("w", encoding="utf-8") as log:
        child = subprocess.Popen(cmd, cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True, encoding="utf-8", errors="replace")
        for line in child.stdout:
            sys.stdout.write(line); sys.stdout.flush()
            log.write(line); log.flush()
        rc = child.wait()
    wall = time.perf_counter() - t0
    mon.terminate()
    try:
        mon.wait(timeout=10)
    except Exception:  # noqa: BLE001
        mon.kill()
    mon_f.close()
    res = {"status": "PASS" if rc == 0 else "FAIL", "returncode": rc, "wall_seconds": wall,
           "finished_local": dt.datetime.now().astimezone().isoformat(timespec="seconds")}
    (out / "result.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print("RESULT", json.dumps(res), flush=True)
    raise SystemExit(rc)


if __name__ == "__main__":
    main()
