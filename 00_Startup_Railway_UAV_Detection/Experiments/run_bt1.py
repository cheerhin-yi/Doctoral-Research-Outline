"""BT-1 controlled ordinary training. Smoke checkpoints are never baselines."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time
import traceback


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=Path, required=True)
    p.add_argument("--weights", type=Path, required=True)
    p.add_argument("--spec", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--smoke", action="store_true")
    p.add_argument("--batch", type=int, default=None)
    p.add_argument("--resume-bundle", type=Path)
    p.add_argument("--segment-minutes", type=float, default=60)
    p.add_argument("--stop-after-epoch", type=int)
    p.add_argument("--continuous", action="store_true", help="Disable planned segment pauses; retain failure/resource guards")
    a = p.parse_args()
    if a.continuous and (a.stop_after_epoch is not None or a.smoke):
        raise ValueError('Continuous mode cannot be combined with an epoch stop or smoke run')
    out = a.output.resolve()
    if out.exists():
        raise FileExistsError(f"Refusing existing run directory: {out}")
    out.mkdir(parents=True)
    config_root = out / "framework_config"
    (config_root / "Ultralytics").mkdir(parents=True)
    os.environ["YOLO_CONFIG_DIR"] = str(config_root)
    os.environ["WANDB_MODE"] = "disabled"
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    start = time.monotonic()
    state = dict(status="RUNNING", purpose="SMOKE_ONLY" if a.smoke else "ORDINARY_BASELINE",
                 started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 data=str(a.data.resolve()), input_weight=str(a.weights.resolve()))
    dump = lambda name, value: (out / name).write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    dump("run_status.json", state)
    try:
        import torch
        import torchvision
        import ultralytics
        from ultralytics import YOLO, settings
        from ultralytics.models.yolo.detect import DetectionTrainer
        settings.update({"sync": False, "wandb": False, "mlflow": False, "clearml": False,
                         "comet": False, "dvc": False, "neptune": False, "raytune": False,
                         "tensorboard": False, "hub": False})
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA unavailable; CPU fallback not allowed")
        if ultralytics.__version__ != "8.4.90":
            raise RuntimeError("Unexpected Ultralytics version")
        torchvision.ops.nms(torch.tensor([[0., 0., 2., 2.]], device="cuda"), torch.tensor([.9], device="cuda"), .5)
        spec = json.loads(a.spec.read_text(encoding="utf-8"))
        args = spec["train_args"].copy()
        args.pop("task", None); args.pop("mode", None)
        args.update(data=str(a.data.resolve()), project=str(out), name="train", pretrained=True)
        if a.batch is not None:
            if a.batch < 1:
                raise ValueError("Explicit positive batch required")
            args["batch"] = a.batch
        if a.smoke:
            args.update(epochs=1, batch=1, close_mosaic=0, save_period=-1)
            data = json.loads(a.data.read_text(encoding="utf-8"))
            train = Path(data["train"]).read_text(encoding="utf-8").splitlines()
            if len(train) != 4:
                raise ValueError("Smoke run requires exactly four train images")
            cal = Path(data["val"]).read_text(encoding="utf-8").splitlines()
            (out / "smoke_val.txt").write_text("\n".join(cal[:4]) + "\n", encoding="utf-8")
            data["val"] = str(out / "smoke_val.txt")
            dump("smoke_data.yaml", data)
            args["data"] = str(out / "smoke_data.yaml")
        batch = args["batch"]
        if a.segment_minutes <= 0 or (a.smoke and a.resume_bundle):
            raise ValueError('Invalid segment limit or smoke resume')
        from bt1_checkpoint import contract, write_recovery, read_recovery
        identity = None if a.smoke else contract(spec, batch, a.data.parent/'preparation.json')
        recovery = None
        input_model = a.weights.resolve()
        if a.resume_bundle:
            recovery, parent_meta = read_recovery(a.resume_bundle, out/'parent_recovery', identity)
            # Relocate runtime paths without changing the preserved source bundle.
            recovery['train_args'].update(data=args['data'], project=str(out), name='train',
                                           save_dir=str(out/'train'), device='0', resume=True)
            input_model = out/'relocated_resume.pt'
            torch.save(recovery, input_model)
            args['resume'] = str(input_model)
            state.update(parent_checkpoint_sha256=parent_meta['checkpoint_sha256'],
                         resumed_after_epoch=parent_meta['completed_epochs'], bitwise_equivalence=False)
        limit = 600 if a.smoke else 86400
        prior_elapsed = 0 if recovery is None else recovery.get('bt1_elapsed_seconds', 0)
        if a.stop_after_epoch is not None and not (int(recovery['epoch'])+1 if recovery else 0) < a.stop_after_epoch <= args['epochs']:
            raise ValueError('Stop epoch must be after the checkpoint and within the unchanged schedule')
        if prior_elapsed >= limit:
            raise RuntimeError('Cumulative BT-1 wall-clock budget exhausted')
        dump("resolved_args.json", args)
        dump("environment.json", dict(python=sys.version, torch=torch.__version__, torchvision=torchvision.__version__,
            ultralytics=ultralytics.__version__, cuda=torch.version.cuda, gpu=torch.cuda.get_device_name(0),
            input_weight_sha256=hashlib.sha256(a.weights.read_bytes()).hexdigest()))

        class StrictTrainer(DetectionTrainer):
            def setup_model(self):
                ckpt = super().setup_model()
                if recovery is not None:
                    self.model.load_state_dict(recovery['bt1_live'], strict=True)
                return ckpt

            def final_eval(self):
                if self.epoch + 1 < self.args.epochs:
                    return  # Preserve optimizer state when intentionally pausing a segment.
                return super().final_eval()

            def _build_train_pipeline(self):
                if getattr(self, "_bt1_pipeline_built", False):
                    raise RuntimeError("BT1_STOP: framework attempted OOM batch recovery; retry forbidden")
                self._bt1_pipeline_built = True
                return super()._build_train_pipeline()

            def _handle_nan_recovery(self, epoch):
                if self.loss is not None and not bool(torch.isfinite(self.loss).all()):
                    raise FloatingPointError("Nonfinite training loss")
                if self.fitness is not None and not __import__("math").isfinite(float(self.fitness)):
                    raise FloatingPointError("Nonfinite validation fitness")
                return False

            def optimizer_step(self):
                flags = [torch.isfinite(x.grad).all() for x in self.model.parameters() if x.grad is not None]
                if flags and not bool(torch.stack(flags).all()):
                    raise FloatingPointError("Nonfinite gradient")
                return super().optimizer_step()

        def guard(trainer):
            if trainer.batch_size != batch or trainer.args.batch != batch:
                raise RuntimeError("Batch changed during training")
            if prior_elapsed + time.monotonic() - start > limit:
                raise TimeoutError("BT-1 wall-clock budget exhausted")
            if shutil.disk_usage(out).free < 5 * 1024**3:
                raise OSError("Less than 5 GiB free space")
            if getattr(trainer, "loss", None) is not None and not bool(torch.isfinite(trainer.loss).all()):
                raise FloatingPointError("Nonfinite loss")

        def save_original(trainer):
            if not a.smoke:
                trainer._bt1_elapsed_seconds = prior_elapsed + time.monotonic()-start
                meta = write_recovery(trainer, out/'recovery', identity)
                state.update(completed_epochs=meta['completed_epochs'], recovery_bundle=str(out/'recovery/latest_recovery.zip'))
                dump('run_status.json', state)
                if not a.continuous and time.monotonic()-start >= a.segment_minutes*60:
                    trainer.stop = True
                if a.stop_after_epoch is not None and trainer.epoch+1 >= a.stop_after_epoch:
                    trainer.stop = True
            if trainer.epoch + 1 == args["epochs"]:
                shutil.copy2(trainer.last, out / "last_pre_strip.pt")

        def restore_state(trainer):
            if recovery is None:
                return
            import random
            import numpy as np
            trainer.scheduler.load_state_dict(recovery['bt1_scheduler'])
            rng = recovery['bt1_rng']
            random.setstate(rng['python']); np.random.set_state(rng['numpy'])
            torch.set_rng_state(rng['torch'])
            torch.cuda.set_rng_state(rng['cuda'], 0)
            def same(x, y):
                if isinstance(x, torch.Tensor):
                    return isinstance(y, torch.Tensor) and x.dtype == y.dtype and torch.equal(x.detach().cpu(), y.detach().cpu())
                if isinstance(x, dict):
                    return isinstance(y, dict) and x.keys() == y.keys() and all(same(x[k], y[k]) for k in x)
                if isinstance(x, (tuple, list)):
                    return type(x) is type(y) and len(x) == len(y) and all(same(a,b) for a,b in zip(x,y))
                return x == y
            from ultralytics.utils.torch_utils import unwrap_model
            checks = dict(
                start_epoch=trainer.start_epoch == int(recovery['epoch'])+1,
                live_model=same(recovery['bt1_live'], unwrap_model(trainer.model).state_dict()),
                optimizer=same(recovery['optimizer'], trainer.optimizer.state_dict()),
                scheduler=same(recovery['bt1_scheduler'], trainer.scheduler.state_dict()),
                ema=same(recovery['ema'].state_dict(), trainer.ema.ema.state_dict()),
                ema_updates=trainer.ema.updates == recovery['updates'],
                scaler=same(recovery['scaler'], trainer.scaler.state_dict()),
                total_epochs=trainer.epochs == args['epochs'], batch=trainer.batch_size == batch)
            dump('resume_verification.json', dict(status='PASS' if all(checks.values()) else 'FAIL',
                checks=checks, start_epoch_zero_based=trainer.start_epoch,
                next_epoch_one_based=trainer.start_epoch+1, total_epochs=trainer.epochs,
                optimizer_lrs=[g['lr'] for g in trainer.optimizer.param_groups],
                scheduler=trainer.scheduler.state_dict(), ema_updates=trainer.ema.updates,
                data_loader_reconstructed=True, bitwise_equivalence=False))
            if not all(checks.values()):
                raise RuntimeError('Resume state mismatch; stopped before any resumed training batch')

        def verify_first_batch(trainer):
            if recovery is None or getattr(trainer, '_bt1_first_batch_verified', False):
                return
            expected = [g['initial_lr']*trainer.lf(trainer.epoch) for g in trainer.optimizer.param_groups]
            actual = [g['lr'] for g in trainer.optimizer.param_groups]
            # This explicit equality check applies after the configured warmup boundary.
            after_warmup = trainer.epoch >= trainer.args.warmup_epochs
            matched = all(abs(x-y) < 1e-12 for x,y in zip(expected,actual))
            dump('resume_first_batch.json', dict(epoch_one_based=trainer.epoch+1,
                scheduler_epoch=trainer.scheduler.last_epoch, expected_lrs=expected,
                actual_lrs=actual, after_warmup=after_warmup, lrs_match=matched,
                loss_finite=bool(torch.isfinite(trainer.loss).all())))
            if after_warmup and not matched:
                raise RuntimeError('Resumed learning rate does not match the original schedule')
            trainer._bt1_first_batch_verified = True

        model = YOLO(str(input_model))
        model.add_callback('on_pretrain_routine_end', restore_state)
        model.add_callback("on_train_batch_end", guard)
        model.add_callback('on_train_batch_end', verify_first_batch)
        model.add_callback("on_train_epoch_start", guard)
        model.add_callback("on_model_save", save_original)
        model.train(trainer=StrictTrainer, **args)
        if not a.smoke and state.get('completed_epochs', 0) < args['epochs']:
            if not state.get('completed_epochs'):
                raise RuntimeError('No epoch checkpoint was saved')
            state.update(status='PAUSED', baseline_eligible=False, reason='Epoch boundary segment completed; seal output before resuming')
            return
        last = out / "train" / "weights" / "last.pt"
        raw = torch.load(out / "last_pre_strip.pt", map_location="cpu", weights_only=False)
        completed_epoch = int(raw["epoch"]) + 1
        if completed_epoch != args["epochs"]:
            raise RuntimeError("Required final epoch was not completed")
        del raw
        reloaded = YOLO(str(last))
        if list(reloaded.names.values()) != spec["data"]["names"]:
            raise ValueError("Checkpoint class identity mismatch")
        data = json.loads(Path(args["data"]).read_text(encoding="utf-8"))
        sample = Path(data["val"]).read_text(encoding="utf-8").splitlines()[:1 if a.smoke else 10]
        predictions = reloaded.predict(source=sample, imgsz=640, device=0, batch=1,
                                       conf=.001, iou=.5, max_det=500, save=False, verbose=False)
        for result in predictions:
            if not bool(torch.isfinite(result.boxes.data).all()):
                raise FloatingPointError("Nonfinite reloaded prediction")
        # Read pre-sigmoid classification branch tensors; no network alteration.
        tensors = {}
        head = reloaded.model.model[-1]
        hooks = [head.cv3[i].register_forward_hook(lambda m, x, y, k=i: tensors.update({f"P{k+3}": dict(shape=list(y.shape), finite=bool(torch.isfinite(y).all()))})) for i in (0, 1)]
        try:
            reloaded.predict(source=sample[:1], imgsz=640, device=0, batch=1, save=False, verbose=False)
        finally:
            for h in hooks:
                h.remove()
        if set(tensors) != {"P3", "P4"} or not all(v["finite"] and v["shape"][1] == 10 for v in tensors.values()):
            raise RuntimeError("P3/P4 ten-class readout failed")
        state.update(status="PASS", completed_epochs=completed_epoch, checkpoint=str(last),
                     checkpoint_sha256=hashlib.sha256(last.read_bytes()).hexdigest(), responses=tensors,
                     output_images_checked=len(sample), baseline_eligible=not a.smoke,
                     max_cuda_allocated_bytes=torch.cuda.max_memory_allocated())
    except Exception as e:
        state.update(status="FAILED", error=f"{type(e).__name__}: {e}")
        (out / "failure.txt").write_text(traceback.format_exc(), encoding="utf-8")
        raise
    finally:
        state["elapsed_seconds"] = time.monotonic() - start
        dump("run_status.json", state)
        print(json.dumps(state, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
