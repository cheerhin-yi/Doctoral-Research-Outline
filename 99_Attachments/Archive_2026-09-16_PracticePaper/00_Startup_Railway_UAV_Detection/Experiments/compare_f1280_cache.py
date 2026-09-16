"""BTD9 compares saved predictions only; no detector or GPU imports."""
import json
from pathlib import Path
import shutil
import time
import traceback
import numpy as np
import psutil
from diagnose_bt1 import BASE, sha, dump, prepare_gt, match_gt
from analyze_density_residuals import write_csv


def main():
    out=BASE/'BTD9-F1280-20260914-01';out.mkdir(exist_ok=False);started=time.monotonic()
    dump(out/'status.json',dict(status='RUNNING',model_loaded=False,inference_calls=0))
    try:
        src=BASE/'BTD1-CAL48-20260913-01';b8=BASE/'BTD8-SINGLE-20260914-01';hashes={}
        for folder,manifest_name in [(src,'diagnostic_manifest.json'),(b8,'output_manifest.json')]:
            manifest=json.loads((folder/manifest_name).read_text())
            for name,info in manifest.items():
                if folder==src and not name.startswith(('image_','predictions_')):continue
                if folder==b8 and not (name.startswith(('cache_','reference_F1280_','actual_k1_')) or name in ['summary.json','cache_summary.json','all_48_frames.csv','verification.json']):continue
                hashes[str(folder/name)]=sha(folder/name);assert hashes[str(folder/name)]==info['sha256']
        for n in ['compare_f1280_cache.py','diagnose_bt1.py','analyze_density_residuals.py','BTD9_F1280_Protocol.md']:shutil.copy2(Path(__file__).with_name(n),out/n)
        methods=['F640','K1','GT_best_K1','F1280'];frames=[];changes=[];categories={c:{m:0 for m in methods}|{'small_gt':0} for c in range(1,11)}
        for i,p in enumerate(sorted(src.glob('image_*.json'))):
            mem=psutil.Process().memory_info();available=psutil.virtual_memory().available
            resource=dict(index=i,elapsed_seconds=time.monotonic()-started,rss=mem.rss,available=available)
            with (out/'resources.jsonl').open('a') as f:f.write(json.dumps(resource)+'\n')
            if resource['elapsed_seconds']>600 or mem.rss>2*(1<<30) or available<256*(1<<20) or shutil.disk_usage(out).free<2*(1<<30):raise RuntimeError('Resource guard')
            r=json.loads(p.read_text());old=json.loads((b8/f'cache_{i:02d}.json').read_text());assert old['frame']['image']==r['image']
            ann=BASE/'full_data_v2/annotations/cal48'/Path(r['image']).with_suffix('.txt');hashes[str(ann)]=sha(ann);assert hashes[str(ann)]==r['annotation_sha256']
            raw=np.array([[float(v) for v in s.rstrip(',').split(',')] for s in ann.read_text().splitlines() if s.strip()]);gt,ids,integral=prepare_gt(raw,r['height'],r['width'])
            small={d['id'] for d in r['small_gt_details']};valid={int(ids[j]) for j,g in enumerate(gt) if g[4]>0}
            assert len(valid)==r['valid_gt']
            with np.load(src/f'predictions_{i:02d}.npz') as a:full=a['F640'].copy()
            preds={'F640':full,'K1':np.load(b8/f'actual_k1_{i:02d}.npy'),'F1280':np.load(b8/f'reference_F1280_{i:02d}.npy')}
            matches={};metrics={}
            for name,a in preds.items():
                assert a.ndim==2 and a.shape[1]==6 and len(a)<=500 and np.isfinite(a).all()
                assert np.all(a[:-1,4]>=a[1:,4]) and np.all((a[:,5]>=0)&(a[:,5]<10))
                assert np.all(a[:,[0,2]]>=0) and np.all(a[:,[0,2]]<=r['width']+.01) and np.all(a[:,[1,3]]>=0) and np.all(a[:,[1,3]]<=r['height']+.01)
                found,fp,ignored=match_gt(gt,ids,a,integral,r['height'],r['width']);matches[name]=found
                metrics[name]=dict(tp=len(found),fp=fp,ignored=ignored,small_tp=len(found&small))
            best=old['frame']['best'];matches['GT_best_K1']=set(old['match_ids'][str(best)])
            metrics['GT_best_K1']=dict(tp=len(matches['GT_best_K1']),fp=old['frame']['oracle_fp'],ignored=None,small_tp=len(matches['GT_best_K1']&small))
            assert matches['K1']==set(old['match_ids'][str(old['frame']['first'])])
            assert metrics['K1']['small_tp']==old['frame']['density_small_tp'] and metrics['K1']['fp']==old['frame']['density_fp']
            assert metrics['F640']['small_tp']==r['metrics']['F640']['small_tp'] and metrics['F640']['tp']==r['metrics']['F640']['tp'] and metrics['F640']['fp']==r['metrics']['F640']['fp']
            assert metrics['GT_best_K1']['small_tp']==old['frame']['oracle_small_tp']
            pairs={}
            for other in methods[:-1]:
                gain=(matches['F1280']-matches[other])&small;loss=(matches[other]-matches['F1280'])&small
                pairs[other]=dict(gain=len(gain),loss=len(loss),net=len(gain)-len(loss),common=len(matches['F1280']&matches[other]&small))
                for kind,collection in [('F1280_only',gain),('other_only',loss)]:
                    for gid in sorted(collection):changes.append(dict(image=r['image'],comparison=other,kind=kind,gt_row=gid,category=int(raw[gid,5]),box=raw[gid,:4].tolist()))
            for d in r['small_gt_details']:
                categories[d['category']]['small_gt']+=1
                for m in methods:categories[d['category']][m]+=int(d['id'] in matches[m])
            row=dict(image=r['image'],small_gt=len(small),valid_gt=len(valid),metrics=metrics,pairs=pairs,
                image_GT_choice='GT_best_K1' if metrics['GT_best_K1']['small_tp']>metrics['F1280']['small_tp'] else 'F1280',
                image_GT_choice_small_tp=max(metrics['GT_best_K1']['small_tp'],metrics['F1280']['small_tp']))
            frames.append(row);dump(out/f'image_{i:02d}.json',row);dump(out/f'matches_{i:02d}.json',{m:sorted(matches[m]) for m in methods})
            if sum(p.stat().st_size for p in out.rglob('*') if p.is_file())>128*(1<<20):raise RuntimeError('Output guard')
        n=sum(r['small_gt'] for r in frames);valid=sum(r['valid_gt'] for r in frames);assert len(frames)==48 and n==2720 and valid==3619
        totals={m:{k:sum(r['metrics'][m][k] for r in frames) for k in ['tp','fp','small_tp']} for m in methods}
        for m,t in totals.items():t.update(small_recall=t['small_tp']/n,recall=t['tp']/valid,precision=t['tp']/(t['tp']+t['fp']))
        pairs={m:{k:sum(r['pairs'][m][k] for r in frames) for k in ['gain','loss','net','common']} for m in methods[:-1]}
        for m,v in pairs.items():
            assert v['net']==totals['F1280']['small_tp']-totals[m]['small_tp']
            v.update(delta_recall_pp=v['net']/n*100,relative_tp_change_pct=v['net']/totals[m]['small_tp']*100,
                image_win_tie_loss=[sum(r['pairs'][m]['net']>0 for r in frames),sum(r['pairs'][m]['net']==0 for r in frames),sum(r['pairs'][m]['net']<0 for r in frames)])
        assert totals['K1']['small_tp']==1172 and totals['GT_best_K1']['small_tp']==1223 and totals['F640']['small_tp']==840
        write_csv(out/'changed_small_gt.csv',changes);write_csv(out/'per_image.csv',[dict(image=r['image'],small_gt=r['small_gt'],**{m:r['metrics'][m]['small_tp'] for m in methods},**{m+'_fp':r['metrics'][m]['fp'] for m in methods},image_GT_choice=r['image_GT_choice'],image_GT_choice_small_tp=r['image_GT_choice_small_tp']) for r in frames])
        write_csv(out/'per_class.csv',[dict(category=c,**d) for c,d in categories.items()])
        timing=json.loads((b8/'summary.json').read_text())
        summary=dict(status='PASS',images=48,small_gt=n,valid_gt=valid,totals=totals,F1280_vs=pairs,classes=categories,
            image_GT_choice_small_tp=sum(r['image_GT_choice_small_tp'] for r in frames),image_GT_choice_uses_crop=sum(r['image_GT_choice']=='GT_best_K1' for r in frames),
            saved_timing=timing['timing'],T_ms=timing['T_ms'],elapsed_seconds=time.monotonic()-started,model_loaded=False,inference_calls=0,
            caveat='cal48 development, not AP or independent generalization. Set unions/GT choices are diagnostics, not deployable fusion or budget claims.')
        assert all(sha(p)==h for p,h in hashes.items())
        dump(out/'input_hashes.json',hashes);dump(out/'summary.json',summary);dump(out/'status.json',dict(status='PASS',model_loaded=False,inference_calls=0,script_sha256=sha(__file__)))
        dump(out/'output_manifest.json',{p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.iterdir()) if p.is_file()})
        print(json.dumps(summary,ensure_ascii=False,indent=2))
    except Exception:
        (out/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8');dump(out/'status.json',dict(status='FAILED',model_loaded=False,inference_calls=0));raise


if __name__=='__main__':main()
