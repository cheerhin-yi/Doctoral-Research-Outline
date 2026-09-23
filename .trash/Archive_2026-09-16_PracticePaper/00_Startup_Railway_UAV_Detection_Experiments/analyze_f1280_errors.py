"""BTD11: bounded CPU analysis of frozen final detections, never a detector run."""
from collections import Counter, defaultdict
import json
from pathlib import Path
import shutil
import time
import traceback

import numpy as np
import psutil
from diagnose_bt1 import BASE, dump, sha, prepare_gt, ignore_keep, match_gt
from analyze_density_residuals import write_csv

OUT = BASE / 'BTD11-ERROR-20260914-01'
THRESHOLDS = [.25, .10, .05, .01, .001]
FLAGS = ['high_same_good', 'low_same_good', 'high_same_near', 'high_other_good',
         'high_other_near', 'low_same_near', 'low_other_good', 'low_other_near']
GROUPS = ['competition', 'low_score', 'localization', 'classification', 'mixed',
          'low_score_localization', 'low_score_classification', 'low_score_mixed']


def overlaps(pred, gt):
    """Ordinary geometric IoU, not reusable-ignore IOA."""
    wh = np.maximum(0, np.minimum(pred[:, None, 2:4], gt[None, :, :2] + gt[None, :, 2:4])
                    - np.maximum(pred[:, None, :2], gt[None, :, :2]))
    inter = wh.prod(2)
    pa = ((pred[:, 2] - pred[:, 0]) * (pred[:, 3] - pred[:, 1]))[:, None]
    ga = (gt[:, 2] * gt[:, 3])[None, :]
    return inter / np.maximum(1e-12, pa + ga - inter)


def region_kept(pred, integral, h, w):
    rows = pred.copy()
    rows[:, 2:4] -= rows[:, :2]
    return ignore_keep(rows, integral, h, w)


def trace_match(gt, gids, pred, integral, h, w, threshold=.25):
    """Same semantics as match_gt, retaining original prediction IDs."""
    pids = np.flatnonzero((pred[:, 4] >= threshold) & region_kept(pred, integral, h, w))
    pids = pids[np.argsort(-pred[pids, 4], kind='stable')]
    matched, trace = set(), []
    for pid in pids:
        d = pred[pid]
        eligible = np.flatnonzero((gt[:, 5] == int(d[5]) + 1) & ~np.isin(gids, list(matched)))
        g = gt[eligible]
        ignored = g[:, 4] == 0
        inter = np.maximum(0, np.minimum(d[2:4], g[:, :2] + g[:, 2:4])
                           - np.maximum(d[:2], g[:, :2])).prod(1)
        da = (d[2] - d[0]) * (d[3] - d[1])
        ov = inter / np.maximum(1e-12, np.where(ignored, da, da + g[:, 2] * g[:, 3] - inter))
        choices = np.flatnonzero((ov >= .5) & ~ignored)
        if not len(choices):
            choices = np.flatnonzero((ov >= .5) & ignored)
        gid, state = None, 'FP'
        if len(choices):
            j = choices[np.flatnonzero(ov[choices] == ov[choices].max())[-1]]
            gid = int(gids[eligible[j]])
            state = 'IGNORED' if ignored[j] else 'TP'
            if state == 'TP':
                matched.add(gid)
        trace.append(dict(pred_id=int(pid), gt_row=gid, state=state))
    return matched, sum(x['state'] == 'FP' for x in trace), sum(x['state'] == 'IGNORED' for x in trace), trace


def maximum_pairs(edges):
    """Maximum cardinality matching; deterministic neighbor and target order."""
    owner = {}

    def augment(gid, seen):
        for pid in edges[gid]:
            if pid in seen:
                continue
            seen.add(pid)
            if pid not in owner or augment(owner[pid], seen):
                owner[pid] = gid
                return True
        return False

    for gid in sorted(edges, key=lambda g: (len(edges[g]), g)):
        augment(gid, set())
    return sorted((gid, pid) for pid, gid in owner.items())


def self_checks():
    # One target must be reassigned to let another take its only candidate.
    assert len(maximum_pairs({10: [0, 1], 11: [0]})) == 2
    assert len(maximum_pairs({10: [0], 11: [0]})) == 1
    assert maximum_pairs({10: []}) == []
    h = w = 50
    integral = np.zeros((h + 1, w + 1), dtype=np.int64)
    raw = np.array([[5, 5, 10, 10, 1, 1, 0, 0],
                    [5, 5, 10, 10, 0, 1, 0, 0]], dtype=float)
    pred = np.array([[5, 5, 15, 15, .9, 0], [5, 5, 15, 15, .8, 0],
                     [5, 5, 15, 15, .7, 0], [30, 30, 32, 32, .1, 0]], dtype=float)
    found, fp, ignored, trace = trace_match(raw, np.array([0, 1]), pred, integral, h, w)
    assert found == {0} and fp == 0 and ignored == 2
    assert trace[0]['gt_row'] == 0 and [x['state'] for x in trace] == ['TP', 'IGNORED', 'IGNORED']
    equal_gt = raw.copy(); equal_gt[:, 4] = 1
    found, fp, ignored, trace = trace_match(equal_gt, np.array([0, 1]), pred[:1], integral, h, w)
    assert found == {1}  # later GT wins equal IoU
    integral[1:20, 1:20] = 1
    integral = integral.cumsum(0).cumsum(1)
    assert not region_kept(pred[:1], integral, h, w)[0]
    return dict(status='PASS',checks=['augmenting_path', 'one_to_one', 'empty_edges',
                'normal_before_ignore', 'reusable_ignore', 'later_gt_tie', 'region_ignore'])


def main():
    tests = self_checks()
    OUT.mkdir(exist_ok=False)
    start = time.monotonic()
    dump(OUT / 'status.json', dict(status='RUNNING', model_loaded=False, inference_calls=0))
    dump(OUT / 'self_checks.json', tests)
    hashes, frames, cases, small_rows, fp_rows, pair_rows = {}, [], [], [], [], []
    totals = defaultdict(Counter)

    def guard(index, when):
        rec = dict(index=index, when=when, elapsed_seconds=time.monotonic()-start,
                   rss=psutil.Process().memory_info().rss, available=psutil.virtual_memory().available,
                   output_bytes=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file()),
                   free_disk=shutil.disk_usage(OUT).free)
        with (OUT / 'resources.jsonl').open('a') as f:
            f.write(json.dumps(rec)+'\n')
        assert rec['elapsed_seconds'] <= 600 and rec['rss'] <= 2*(1 << 30)
        assert rec['available'] >= 256*(1 << 20) and rec['free_disk'] >= 2*(1 << 30)
        assert rec['output_bytes'] <= 128*(1 << 20)

    def checked(path, expected=None):
        digest = sha(path)
        if expected:
            assert digest == expected, str(path)
        hashes[str(path)] = digest
        return path

    try:
        for name in ['analyze_f1280_errors.py', 'diagnose_bt1.py', 'analyze_density_residuals.py',
                     'BTD11_Error_Structure_Protocol.md']:
            p = Path(__file__).with_name(name)
            checked(p); shutil.copy2(p, OUT / name)
        b1 = BASE / 'BTD1-CAL48-20260913-01'
        b8 = BASE / 'BTD8-SINGLE-20260914-01'
        b9 = BASE / 'BTD9-F1280-20260914-01'
        manifests = {str(p): json.loads(checked(p / n).read_text()) for p, n in
                     [(b1, 'diagnostic_manifest.json'), (b8, 'output_manifest.json'), (b9, 'output_manifest.json')]}

        def artifact(folder, name):
            return checked(folder / name, manifests[str(folder)][name]['sha256'])

        for i in range(48):
            guard(i, 'before')
            info = json.loads(artifact(b1, f'image_{i:02d}.json').read_text())
            old = json.loads(artifact(b9, f'image_{i:02d}.json').read_text())
            old_match = json.loads(artifact(b9, f'matches_{i:02d}.json').read_text())['F1280']
            assert info['image'] == old['image']
            ann = checked(BASE / 'full_data_v2/annotations/cal48' / Path(info['image']).with_suffix('.txt'),
                          info['annotation_sha256'])
            raw = np.loadtxt(ann, delimiter=',', ndmin=2)
            h, w = info['height'], info['width']
            gt, gids, integral = prepare_gt(raw, h, w)
            pred = np.load(artifact(b8, f'reference_F1280_{i:02d}.npy'))
            assert pred.ndim == 2 and pred.shape[1] == 6 and len(pred) <= 500 and np.isfinite(pred).all()
            assert np.all(pred[:, 4] >= .001) and np.all(pred[:-1, 4] >= pred[1:, 4])
            small = {d['id'] for d in info['small_gt_details']}
            normals = gids[gt[:, 4] > 0]
            assert small == {int(g) for g in normals if raw[g, 2]*raw[g, 3] < 1024}
            base, fp, ign, traces = trace_match(gt, gids, pred, integral, h, w)
            assert (base, fp, ign) == match_gt(gt, gids, pred, integral, h, w)
            assert base == set(old_match) and fp == old['metrics']['F1280']['fp']
            assert len(base & small) == old['metrics']['F1280']['small_tp']
            missing = small - base
            kept = region_kept(pred, integral, h, w)
            normal_boxes = raw[normals]
            ov = overlaps(pred, normal_boxes)
            col = {int(g): j for j, g in enumerate(normals)}
            gp = np.column_stack([normal_boxes[:, :2], normal_boxes[:, :2] + normal_boxes[:, 2:4],
                                  np.ones(len(normals)), normal_boxes[:, 5]-1])
            neighbor = overlaps(gp, normal_boxes)
            neighbor[normal_boxes[:, 5, None] != normal_boxes[None, :, 5]] = 0
            np.fill_diagonal(neighbor, 0)
            used = {t['pred_id'] for t in traces if t['state'] == 'TP'}
            free = np.array([j not in used for j in range(len(pred))]) & kept
            edge_maps = {kind: {} for kind in ['score', 'localization', 'classification']}
            frame_cases = []
            for gid in sorted(small):
                j = col[gid]; box = raw[gid]
                same = pred[:, 5] == box[5]-1
                good, near = ov[:, j] >= .5, (ov[:, j] >= .1) & (ov[:, j] < .5)
                high, low = kept & (pred[:, 4] >= .25), kept & (pred[:, 4] < .25)
                masks = [high & same & good, low & same & good, high & same & near,
                         high & ~same & good, high & ~same & near, low & same & near,
                         low & ~same & good, low & ~same & near]
                flags = {k: bool(a.any()) for k, a in zip(FLAGS, masks)}
                group = next((name for name, mask in zip(GROUPS, masks) if mask.any()), 'not_observed')
                max_neighbor = float(neighbor[j].max()) if len(normals) else 0.
                nb = 'overlap_ge_0.5' if max_neighbor >= .5 else 'overlap_0.1_0.5' if max_neighbor >= .1 else 'overlap_lt_0.1'
                short = float(min(box[2:4]))
                sb = 'short_lt_8' if short < 8 else 'short_8_16' if short < 16 else 'short_16_32' if short < 32 else 'short_ge_32'
                allrow = dict(image=info['image'], gt_row=gid, category=int(box[5]), detected=gid in base,
                              short_side=short, size_group=sb, neighbor_group=nb, max_same_gt_iou=max_neighbor)
                small_rows.append(allrow)
                if gid not in missing:
                    continue
                best = max(np.flatnonzero(kept), key=lambda k: (ov[k,j], pred[k,4], -k), default=None)
                counts = {k: int(a.sum()) for k, a in zip(FLAGS, masks)}
                row = dict(**allrow, box=box[:4].tolist(), group=group, flags=flags, counts=counts,
                           max_same_iou=float(ov[kept & same, j].max()) if (kept & same).any() else 0.,
                           max_any_iou=float(ov[kept,j].max()) if kept.any() else 0.,
                           best_pred_id=int(best) if best is not None else None,
                           best_pred=pred[best].tolist() if best is not None else None)
                cases.append(row); frame_cases.append(row)
                for kind, mask in [('score', masks[1]), ('localization', masks[2]), ('classification', masks[3])]:
                    candidates = np.flatnonzero(mask & free)
                    edge_maps[kind][gid] = sorted(map(int, candidates), key=lambda k: (-pred[k, 4], k))
            frame_fp = []
            for t in traces:
                if t['state'] != 'FP':
                    continue
                k = t['pred_id']; same = normal_boxes[:, 5] == pred[k, 5]+1
                good, near = ov[k] >= .5, (ov[k] >= .1) & (ov[k] < .5)
                masks = [same & good, same & near, ~same & good, ~same & near]
                kind = next((n for n, a in zip(['duplicate','localization','classification','mixed'], masks) if a.any()), 'background')
                row = dict(image=info['image'], pred_id=k, group=kind, score=float(pred[k, 4]), box=pred[k, :4].tolist())
                fp_rows.append(row); frame_fp.append(row)

            metrics, match_sets = {}, {}

            def evaluate(name, array, threshold=.25, capacity=None):
                found, fp2, ignored2, _ = trace_match(gt, gids, array, integral, h, w, threshold)
                metric = dict(small_tp=len(found & small), tp=len(found), fp=fp2, ignored=ignored2,
                              gain=len((found-base) & small), loss=len((base-found) & small),
                              all_gain=len(found-base), all_loss=len(base-found))
                if capacity is not None:
                    metric['capacity'] = capacity
                metrics[name] = metric; match_sets[name] = sorted(found)
                totals[name].update(metric)

            for threshold in THRESHOLDS:
                evaluate(f'threshold_{threshold:g}', pred, threshold)
            for kind, edges in edge_maps.items():
                pairs = maximum_pairs(edges)
                modified = pred.copy()
                for gid, k in pairs:
                    if kind == 'score': modified[k, 4] = .25
                    elif kind == 'localization': modified[k, :4] = [*raw[gid, :2], *(raw[gid, :2]+raw[gid, 2:4])]
                    else: modified[k, 5] = raw[gid, 5]-1
                    pair_rows.append(dict(image=info['image'], kind=kind, gt_row=gid, pred_id=k,
                                          original_iou=float(ov[k,col[gid]]), original_score=float(pred[k,4])))
                evaluate('repair_'+kind, modified, capacity=len(pairs))
                np.save(OUT / f'repair_{kind}_{i:02d}.npy', modified)
            frame = dict(index=i,image=info['image'], small_gt=len(small),small_fn=len(missing),
                         valid_gt=len(normals), cached_predictions=len(pred), capped=len(pred)==500,
                         minimum_saved_score=float(pred[:,4].min()) if len(pred) else None,
                         kept_predictions=int(kept.sum()), metrics=metrics,
                         missed_groups=dict(Counter(x['group'] for x in frame_cases)),
                         fp_groups=dict(Counter(x['group'] for x in frame_fp)))
            frames.append(frame)
            dump(OUT / f'frame_{i:02d}.json', frame)
            dump(OUT / f'matches_{i:02d}.json', match_sets)
            dump(OUT / f'trace_{i:02d}.json', traces)
            dump(OUT / f'cases_{i:02d}.json', frame_cases)
            dump(OUT / f'edges_{i:02d}.json', edge_maps)
            guard(i, 'after')

        assert len(cases) == 1408 and len(small_rows) == 2720 and len(fp_rows) == 839
        assert totals['threshold_0.25']['small_tp'] == 1312 and totals['threshold_0.25']['tp'] == 2010
        for name, t in totals.items():
            assert t['gain']-t['loss'] == t['small_tp']-1312
            t['recall_small'] = t['small_tp']/2720
            t['delta_recall_pp'] = (t['small_tp']-1312)/2720*100
            t['relative_small_tp_pct'] = (t['small_tp']-1312)/1312*100
            t['precision_all'] = t['tp']/(t['tp']+t['fp'])
        groups = {}
        for field in ['category', 'size_group', 'neighbor_group']:
            group_stats = defaultdict(Counter)
            for row in small_rows:
                group_stats[str(row[field])].update(gt=1, tp=int(row['detected']), fn=int(not row['detected']))
            groups[field] = dict(group_stats)
        contributions = {}
        for kind in ['score', 'localization', 'classification']:
            name = 'repair_'+kind
            positive = sorted([f['metrics'][name]['gain'] for f in frames], reverse=True)
            contributions[kind] = dict(images_positive=sum(v > 0 for v in positive),
                top5_gain=sum(positive[:5]), total_gain=sum(positive))
        representatives = {}
        for group in sorted({x['group'] for x in cases}):
            representatives[group] = next(x for x in cases if x['group'] == group)
        summary = dict(status='PASS', images=48, small_gt=2720, small_fn=1408, baseline_fp=839,
                       totals={k:dict(v) for k,v in totals.items()},
                       missed_groups=dict(Counter(x['group'] for x in cases)),
                       missed_flags={k:sum(x['flags'][k] for x in cases) for k in FLAGS},
                       fp_groups=dict(Counter(x['group'] for x in fp_rows)),
                       groups=groups, concentration=contributions,
                       capped_images=sum(f['capped'] for f in frames),
                       minimum_saved_score=min(f['minimum_saved_score'] for f in frames),
                       elapsed_seconds=time.monotonic()-start, model_loaded=False, inference_calls=0,
                       caveat='Post-NMS capped cal48 predictions only. Repairs use GT, not deployable. No network/NMS causal attribution or official TIDE/AP.')
        write_csv(OUT/'missed_small_gt.csv', cases)
        write_csv(OUT/'all_small_gt.csv', small_rows)
        write_csv(OUT/'false_positives.csv', fp_rows)
        write_csv(OUT/'repair_pairs.csv', pair_rows)
        write_csv(OUT/'per_image.csv', [dict(image=f['image'],small_gt=f['small_gt'],small_fn=f['small_fn'],
                  capped=f['capped'], **{k:v['small_tp'] for k,v in f['metrics'].items()}) for f in frames])
        dump(OUT/'representatives.json', representatives)
        assert all(sha(p)==digest for p,digest in hashes.items())
        dump(OUT/'input_hashes.json', hashes)
        dump(OUT/'summary.json', summary)
        dump(OUT/'status.json', dict(status='PASS', model_loaded=False, inference_calls=0, script_sha256=sha(__file__)))
        dump(OUT/'output_manifest.json', {p.name:dict(bytes=p.stat().st_size,sha256=sha(p))
             for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='output_manifest.json'})
        print(json.dumps(summary,ensure_ascii=False,indent=2))
    except Exception:
        (OUT/'failure.txt').write_text(traceback.format_exc(),encoding='utf-8')
        dump(OUT/'status.json',dict(status='FAILED',model_loaded=False,inference_calls=0))
        raise


if __name__ == '__main__':
    main()
