"""Portable epoch-boundary recovery; does not claim bitwise cross-GPU replay."""
import hashlib
import json
from pathlib import Path
import random
import shutil
import zipfile


def sha(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def contract(spec, batch, preparation):
    args = spec['train_args'].copy()
    args['batch'] = batch
    args['resume'] = False
    return dict(args=args, data=spec['data'], commit=spec['ultralytics_commit'],
                initialization=spec['initialization']['sha256'],
                conversion_sha256=sha(Path(preparation).parent/'conversion.jsonl'))


def write_recovery(trainer, output, identity):
    import numpy as np
    import torch
    from copy import deepcopy
    from ultralytics.utils.torch_utils import unwrap_model
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    epoch = trainer.epoch + 1
    # Native checkpoints contain half-precision EMA. Preserve live FP32 state separately.
    payload = dict(epoch=trainer.epoch, best_fitness=trainer.best_fitness,
        model=None, ema=deepcopy(unwrap_model(trainer.ema.ema)).cpu().float(),
        updates=trainer.ema.updates, optimizer=deepcopy(trainer.optimizer.state_dict()),
        scaler=trainer.scaler.state_dict(), train_args=vars(trainer.args).copy(),
        version='8.4.90', bt1_format=1, bt1_contract=identity,
        bt1_live={k:v.detach().cpu().clone() for k,v in unwrap_model(trainer.model).state_dict().items()},
        bt1_scheduler=trainer.scheduler.state_dict(),
        bt1_elapsed_seconds=getattr(trainer, '_bt1_elapsed_seconds', 0),
        bt1_rng=dict(python=random.getstate(), numpy=np.random.get_state(),
                     torch=torch.get_rng_state(), cuda=torch.cuda.get_rng_state(0)))
    tmp = output/'resume.pt.tmp'
    torch.save(payload, tmp)
    tmp.replace(output/'resume.pt')
    meta = dict(format=1, completed_epochs=epoch, total_epochs=trainer.args.epochs,
        checkpoint_sha256=sha(output/'resume.pt'), contract=identity,
        bitwise_equivalence=False, note='Epoch boundary resume; data loader is reconstructed.')
    (output/'manifest.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
    bundle = output/'latest_recovery.zip'
    temp_bundle = output/'latest_recovery.zip.tmp'
    with zipfile.ZipFile(temp_bundle, 'w', compression=zipfile.ZIP_STORED) as z:
        z.write(output/'resume.pt', 'resume.pt')
        z.write(output/'manifest.json', 'manifest.json')
        for name in ('results.csv', 'args.yaml'):
            p = Path(trainer.save_dir)/name
            if p.is_file():
                z.write(p, name)
    temp_bundle.replace(bundle)
    if epoch == 1 or epoch % 5 == 0 or epoch == trainer.args.epochs:
        named = output/f'epoch_{epoch:03d}_recovery.zip'
        if named.exists():
            raise FileExistsError(named)
        shutil.copy2(bundle, named)
    with (output/'checkpoint_history.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(dict(epoch=epoch, sha256=meta['checkpoint_sha256']))+'\n')
    print(f'BT1_RECOVERY_SAVED epoch={epoch} path={bundle}', flush=True)
    return meta


def read_recovery(bundle, destination, identity):
    import torch
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(bundle) as z:
        if len(z.namelist()) != len(set(z.namelist())) or set(z.namelist())-{'resume.pt','manifest.json','results.csv','args.yaml'}:
            raise ValueError('Unexpected recovery members')
        for name in z.namelist():
            if z.getinfo(name).file_size > 1024**3:
                raise ValueError('Oversized recovery member')
            (destination/name).write_bytes(z.read(name))
    meta = json.loads((destination/'manifest.json').read_text())
    if meta['contract'] != identity or sha(destination/'resume.pt') != meta['checkpoint_sha256']:
        raise ValueError('Recovery identity/hash mismatch')
    # Only use bundles produced by this project; a hash alone is not trust in a foreign pickle.
    ckpt = torch.load(destination/'resume.pt', map_location='cpu', weights_only=False)
    if (ckpt.get('bt1_format') != 1 or ckpt.get('bt1_contract') != identity
            or ckpt.get('optimizer') is None or 'bt1_live' not in ckpt
            or int(ckpt['epoch'])+1 != meta['completed_epochs']
            or not 0 < meta['completed_epochs'] < identity['args']['epochs']):
        raise ValueError('Recovery is incomplete, finished, or incompatible')
    return ckpt, meta
