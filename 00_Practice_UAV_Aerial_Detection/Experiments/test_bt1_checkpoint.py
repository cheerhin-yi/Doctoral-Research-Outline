"""Recovery serialization checks only: no YOLO training or dataset access."""
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
import zipfile


class RecoveryTests(unittest.TestCase):
    def test_roundtrip_and_rejections(self):
        with tempfile.TemporaryDirectory() as root:
            root = Path(root)
            (root/'config/Ultralytics').mkdir(parents=True)
            os.environ['YOLO_CONFIG_DIR'] = str(root/'config')
            import torch
            from bt1_checkpoint import write_recovery, read_recovery
            model = torch.nn.Linear(2, 1)
            ema = torch.nn.Linear(2, 1)
            optimizer = torch.optim.SGD(model.parameters(), lr=.01, momentum=.9)
            # Create known optimizer state directly; no training step is run.
            for parameter in model.parameters():
                optimizer.state[parameter]['momentum_buffer'] = torch.ones_like(parameter)*.125
            scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lambda _:1.)
            identity = {'args':{'epochs':100,'batch':4},'source':'unit fixture'}
            trainer = SimpleNamespace(epoch=4, best_fitness=0., model=model,
                ema=SimpleNamespace(ema=ema, updates=9), optimizer=optimizer,
                scaler=SimpleNamespace(state_dict=lambda:{}), scheduler=scheduler,
                args=SimpleNamespace(epochs=100), save_dir=root)
            meta = write_recovery(trainer, root/'recovery', identity)
            ckpt, restored = read_recovery(root/'recovery/latest_recovery.zip',root/'restored',identity)
            self.assertEqual(restored['completed_epochs'],5)
            self.assertEqual(ckpt['epoch'],4)
            self.assertEqual(ckpt['updates'],9)
            for key, value in model.state_dict().items():
                self.assertTrue(torch.equal(value,ckpt['bt1_live'][key]))
            for key, value in ema.state_dict().items():
                self.assertTrue(torch.equal(value,ckpt['ema'].state_dict()[key]))
            resumed_model = torch.nn.Linear(2,1)
            resumed_opt = torch.optim.SGD(resumed_model.parameters(),lr=.8,momentum=.9)
            resumed_opt.load_state_dict(ckpt['optimizer'])
            self.assertEqual(resumed_opt.param_groups[0]['lr'],.01)
            self.assertTrue(all(torch.allclose(v['momentum_buffer'],torch.full_like(v['momentum_buffer'],.125)) for v in resumed_opt.state.values()))
            self.assertTrue((root/'recovery/epoch_005_recovery.zip').is_file())
            with self.assertRaises(ValueError):
                read_recovery(root/'recovery/latest_recovery.zip',root/'wrong',{'args':{'epochs':100,'batch':1}})
            with zipfile.ZipFile(root/'bad.zip','w') as z:
                z.writestr('../escape','bad')
            with self.assertRaises(ValueError):
                read_recovery(root/'bad.zip',root/'unsafe',identity)
            with zipfile.ZipFile(root/'corrupt.zip','w') as z:
                z.writestr('manifest.json', json.dumps(meta))
                z.writestr('resume.pt',b'broken')
            with self.assertRaises(ValueError):
                read_recovery(root/'corrupt.zip',root/'corrupt',identity)
            trainer.epoch=99
            write_recovery(trainer,root/'complete',identity)
            with self.assertRaises(ValueError):
                read_recovery(root/'complete/latest_recovery.zip',root/'already_done',identity)


if __name__ == '__main__':
    unittest.main()
