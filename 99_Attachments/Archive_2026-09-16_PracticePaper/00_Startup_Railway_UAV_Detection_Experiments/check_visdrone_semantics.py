"""A0-07 synthetic-only semantic probe, NOT an official evaluator replacement.

Reads only the pinned toolkit ZIP and writes a fresh audit output directory.
Hand expectations are independent constants in fixtures(); the Python translation
and the generated MATLAB runner use the same synthetic inputs and expectations.
No image, dataset label, model, framework, or network is used.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import sys
import zipfile

ARCHIVE_SHA = '30298f4e0b56dcb5a49ab4a0d790b2c3329da5fa4391757920b74294351ff3b6'
COMMIT = '005445782213e20cb91bc50a597db3dd949e749a'
METRICS = ['AP', 'AP50', 'AP75', 'AR1', 'AR10', 'AR100', 'AR500']


def row(x=1, y=1, w=10, h=10, score=1, category=1):
    return [x, y, w, h, score, category, 0, 0]


def drop_ignored(gt, det, height=128, width=128):
    """Literal integral-map semantics for these integer-region fixtures."""
    regions = [r for r in gt if r[5] == 0]
    kept_gt = [r[:] for r in gt if r[5] != 0]
    if not regions:
        return kept_gt, [r[:] for r in det]
    mask = [[0] * (width + 1) for _ in range(height + 1)]
    for r in regions:
        x, y, w, h = [max(1, v) for v in r[:4]]
        if any(int(v) != v for v in (x, y, w, h)):
            raise ValueError('Synthetic probe supports integer ignored regions only')
        for yy in range(int(y), min(height, int(y + h)) + 1):
            for xx in range(int(x), min(width, int(x + w)) + 1):
                mask[yy][xx] = 1
    integral = [[0] * (width + 1) for _ in range(height + 1)]
    for yy in range(1, height + 1):
        for xx in range(1, width + 1):
            integral[yy][xx] = (mask[yy][xx] + integral[yy - 1][xx]
                                + integral[yy][xx - 1] - integral[yy - 1][xx - 1])

    def keep(r):
        # MATLAB round uses halves away from zero; Python round does not.
        rounded = [math.copysign(math.floor(abs(v) + .5), v) for v in r[:4]]
        x, y, w, h = [max(1, int(v)) for v in rounded]
        x, y = min(width, x), min(height, y)
        right, bottom = min(width, x + w), min(height, y + h)
        covered = (integral[y][x] + integral[bottom][right]
                   - integral[y][right] - integral[bottom][x])
        return covered / (h * w) < .5
    return list(filter(keep, kept_gt)), list(filter(keep, [r[:] for r in det]))


def overlap(d, g, ignore):
    w = min(d[0] + d[2], g[0] + g[2]) - max(d[0], g[0])
    h = min(d[1] + d[3], g[1] + g[3]) - max(d[1], g[1])
    if w <= 0 or h <= 0:
        return 0.
    intersection = w * h
    denom = d[2] * d[3] if ignore else d[2] * d[3] + g[2] * g[3] - intersection
    return intersection / denom


def match(gt, det, threshold=.5):
    """Input gt=[x,y,w,h,ignore], dt=[x,y,w,h,confidence]."""
    g = sorted([r[:] for r in gt], key=lambda r: r[4])
    d = sorted([r[:] + [0] for r in det], key=lambda r: -r[4])
    for r in g:
        r[4] = -r[4]
    for dr in d:
        best_overlap, best_index, best_match = threshold, None, 0
        for i, gr in enumerate(g):
            if gr[4] == 1:
                continue
            if best_match != 0 and gr[4] == -1:
                break
            value = overlap(dr, gr, gr[4] == -1)
            if value < best_overlap:
                continue
            best_overlap, best_index = value, i
            best_match = 1 if gr[4] == 0 else -1
        if best_match == -1:
            dr[5] = -1
        elif best_match == 1:
            g[best_index][4], dr[5] = 1, 1
    return g, d


def voc_ap(rec, prec):
    r, p = [0.] + rec + [1.], [0.] + prec + [0.]
    for i in range(len(p) - 2, -1, -1):
        p[i] = max(p[i], p[i + 1])
    return sum((r[i] - r[i - 1]) * p[i] for i in range(1, len(r)) if r[i] != r[i - 1])


def prepare(images_gt, images_det):
    result = []
    for gt, det in zip(images_gt, images_det, strict=True):
        gt, det = drop_ignored(gt, det)
        for r in gt:
            r[4] = 1 - r[4]
        result.append((gt, det))
    return result


def evaluate(images_gt, images_det):
    prepared = prepare(images_gt, images_det)
    classes = [c for c in range(1, 11) for gt, _ in prepared if any(r[5] == c for r in gt)]
    ap, ar = {}, {}
    for c in range(1, 11):
        for ti in range(10):
            for cap in [1, 10, 100, 500]:
                gs, ds = [], []
                for gt, det in prepared:
                    # Intentional prefix truncation BEFORE class filtering and sort.
                    g, d = match([r[:5] for r in gt if r[5] == c],
                                 [r[:5] for r in det[:cap] if r[5] == c], .5 + ti * .05)
                    gs.extend(r[4] for r in g)
                    ds.extend((r[4], r[5]) for r in d)
                tp, fp, rec, prec = 0, 0, [], []
                for _, flag in sorted(ds, key=lambda r: -r[0]):
                    tp += flag == 1
                    fp += flag == 0
                    rec.append(tp / max(1, len(gs)))  # Includes ignored GT, as source does.
                    prec.append(tp / max(1, tp + fp))
                ar[c, ti, cap] = max(rec, default=0.) * 100
                if cap == 500:
                    ap[c, ti] = voc_ap(rec, prec) * 100
    def mean(values):
        return sum(values) / len(values) if values else None
    metrics = [mean([ap[c, t] for c in classes for t in range(10)]),
               mean([ap[c, 0] for c in classes]), mean([ap[c, 5] for c in classes])]
    metrics += [mean([ar[c, t, cap] for c in classes for t in range(10)]) for cap in [1, 10, 100, 500]]
    return metrics, classes


def small_recall(images_gt, images_det, tau=.0):
    """PROPOSED diagnostic, not official: global score sort, then cap=500.

    Matching includes all sizes. Denominator excludes ignored/invalid GT.
    Returns numerator/denominator, so an empty denominator remains explicit.
    """
    numerator, denominator = 0, 0
    for gt, det in prepare(images_gt, images_det):
        det = sorted([r for r in det if r[4] >= tau], key=lambda r: -r[4])[:500]
        for c in range(1, 11):
            g, _ = match([r[:5] for r in gt if r[5] == c], [r[:5] for r in det if r[5] == c])
            for r in g:
                if r[4] != -1 and r[2] > 0 and r[3] > 0 and 0 < r[2] * r[3] < 1024:
                    denominator += 1
                    numerator += r[4] == 1
    return [numerator, denominator]


def fixtures():
    cases = []
    def add(identifier, operation, gt, det, expected, **kwargs):
        cases.append(dict(id=identifier, operation=operation, gt=gt, det=det, expected=expected, **kwargs))
    all100 = [100.] * 7
    add('C01_perfect', 'metrics', [[row()]], [[row(score=.9)]], all100)
    add('C02_empty_predictions', 'metrics', [[row()]], [[]], [0.] * 7)
    add('C03_prefix_500_unsorted', 'metrics', [[row()]],
        [[row(x=60, score=.1)] * 500 + [row(score=.99)]], [0.] * 7)
    add('C04_prefix_500_sorted', 'metrics', [[row()]],
        [[row(score=.99)] + [row(x=60, score=.1)] * 500], all100)
    add('C05_global_not_per_class_cap', 'metrics', [[row(), row(x=30, category=2)]],
        [[row(score=.9), row(x=30, category=2, score=.8)]], [100, 100, 100, 50, 100, 100, 100])
    add('C06_repeated_class_weight', 'metrics', [[row(), row(x=30, category=2)], [row()]],
        [[row(score=.9)], [row(score=.8)]], [200 / 3] * 7)
    add('C07_ignore_in_denominator', 'metrics', [[row(x=30), row(score=0)]],
        [[row(score=.9), row(x=30, score=.8)]], [50, 50, 50, 0, 50, 50, 50])
    add('C08_others_not_spatial_ignore', 'metrics', [[row(category=11, score=0), row(x=30)]],
        [[row(score=.9), row(x=30, score=.8)]], [50, 50, 50, 0, 100, 100, 100])
    add('C09_iou_boundary', 'metrics', [[row()]], [[row(w=5, score=.9)]], [10, 100, 0, 10, 10, 10, 10])
    for identifier, w, expected in [('C10_ignore_40pct', 4, [1, 1]),
                                     ('C11_ignore_50pct', 5, [0, 0]),
                                     ('C12_ignore_60pct', 6, [0, 0])]:
        add(identifier, 'filter', [row(category=0, score=0, w=w), row()], [row(score=.9)], expected)
    add('C13_ignore_union', 'filter', [row(category=0, score=0, w=3),
        row(x=2, category=0, score=0, w=3), row()], [row(score=.9)], [1, 1])
    add('C14_zero_height_region_clamped', 'filter',
        [row(category=0, score=0, w=5, h=0), row(w=5, h=2)], [row(w=5, h=2, score=.9)], [0, 0])
    add('C15_right_bottom_pixel', 'filter', [row(x=128, y=128, w=1, h=1, category=0, score=0),
        row(x=128, y=128, w=1, h=1)], [row(x=128, y=128, w=1, h=1, score=.9)], [1, 1])
    add('C16_half_rounding', 'filter', [row(category=0, score=0, w=5), row(w=10.5)],
        [row(w=10.5, score=.9)], [1, 1])
    # Matching inputs use internal ignore flag in column five, not raw GT score.
    add('C17_normal_first_ignore_reusable', 'match', [row()[:4] + [1], row()[:4] + [0]],
        [row(score=.9)[:5], row(score=.8)[:5], row(score=.7)[:5]], [1, -1, -1])
    add('C18_duplicate_detection', 'match', [row()[:4] + [0]],
        [row(score=.9)[:5], row(score=.8)[:5]], [1, 0])
    add('C19_small_1023_vs_1024', 'small', [[row(w=31, h=33), row(x=50, w=32, h=32), row(y=70, score=0)]],
        [[row(w=31, h=33, score=.9), row(x=50, w=32, h=32, score=.8), row(y=70, score=.7)]], [1, 1])
    add('C20_no_small_NA', 'small', [[row(w=32, h=32)]], [[row(w=32, h=32, score=.9)]], [0, 0])
    add('C21_small_threshold', 'small', [[row()]], [[row(score=.4)]], [0, 1], tau=.5)
    add('C22_ignore_before_cap', 'metrics', [[row(category=0, score=0), row(x=50)]],
        [[row(score=.9), row(x=50, score=.8)]], all100)
    # An ignored region contains two smaller predictions: IoA=1, IoU<.5.
    add('C23_ignore_IoA', 'match', [row(w=30, h=30)[:4] + [1]],
        [row(score=.9)[:5], row(x=15, score=.8)[:5]], [-1, -1])
    add('C24_matching_all_sizes', 'small', [[row(w=31, h=33), row(w=32, h=32)]],
        [[row(w=32, h=32, score=.9)]], [0, 1])
    return cases


def matlab_matrix(rows, columns=8):
    if not rows:
        return f'zeros(0,{columns})'
    return '[' + ';'.join(' '.join(format(v, '.17g') for v in r) for r in rows) + ']'


def write_matlab_runner(cases, destination):
    """Generate original-function calls; no toolkit edits or replacement helpers."""
    lines = [
        'function results = run_a007_official(toolkitDir, outputFile)',
        '% Generated synthetic fixtures. Requires original utils plus mean2.',
        '% NOT RUN by Python. Output path must be new; original source unchanged.',
        "assert(exist(outputFile,'file') == 0, 'Output already exists');",
        "addpath(fullfile(toolkitDir,'utils'));",
        'results = struct();',
    ]
    for c in cases:
        op = c['operation']
        if op in ('metrics', 'small'):
            gt = '{' + ','.join(matlab_matrix(x) for x in c['gt']) + '}'
            dt = '{' + ','.join(matlab_matrix(x) for x in c['det']) + '}'
        else:
            gt = matlab_matrix(c['gt'], 5 if op == 'match' else 8)
            dt = matlab_matrix(c['det'], 5 if op == 'match' else 8)
        lines += [f'G={gt}; D={dt};']
        if op in ('metrics', 'small'):
            lines += ['for i=1:numel(G)', '[g,d]=dropObjectsInIgr(G{i},D{i},128,128);',
                      'oldScore=g(:,5); g(oldScore==0,5)=1; g(oldScore==1,5)=0;', 'G{i}=g; D{i}=d;', 'end']
        if op == 'metrics':
            lines += ['[a,b,c,d,e,f,g]=calcAccuracy(numel(G),G,D); actual=[a b c d e f g];']
        elif op == 'filter':
            lines += ['[g,d]=dropObjectsInIgr(G,D,128,128); actual=[size(g,1) size(d,1)];']
        elif op == 'match':
            lines += ['[g,d]=evalRes(G,D,.5); actual=d(:,6)\';']
        else:
            lines += ['num=0; den=0;', 'for i=1:numel(G)',
                      f'd=D{{i}}; d=d(d(:,5)>={c.get("tau",0):.17g},:);',
                      "[~,ord]=sort(d(:,5),'descend'); d=d(ord,:); d=d(1:min(500,size(d,1)),:);",
                      'for cls=1:10', '[g,~]=evalRes(G{i}(G{i}(:,6)==cls,1:5),d(d(:,6)==cls,1:5),.5);',
                      's=g(:,5)~=-1 & g(:,3)>0 & g(:,4)>0 & g(:,3).*g(:,4)<1024;',
                      'den=den+sum(s); num=num+sum(s & g(:,5)==1);', 'end', 'end', 'actual=[num den];']
        expected = matlab_matrix([c['expected']])
        lines += [f'expected={expected};',
                  f"assert(all(abs(actual-expected)<1e-8), '{c['id']} failed');",
                  f'results.{c["id"]}=actual;']
    lines += ["save(outputFile,'results');", 'end']
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--toolkit', type=Path, default=Path('11_Datasets/processed/VisDrone/A0-05/official_toolkit.zip'))
    parser.add_argument('--output', type=Path, default=Path('11_Datasets/processed/VisDrone/A0-07/probe_01'))
    args = parser.parse_args()
    archive = args.toolkit.read_bytes()
    if hashlib.sha256(archive).hexdigest() != ARCHIVE_SHA:
        raise ValueError('Pinned toolkit archive hash mismatch')
    args.output.mkdir(parents=True, exist_ok=False)
    manifest = {}
    with zipfile.ZipFile(args.toolkit) as z:
        for name in z.namelist():
            if name.endswith('.m'):
                manifest[name] = hashlib.sha256(z.read(name)).hexdigest()
    cases = fixtures()
    (args.output / 'fixtures.json').write_text(json.dumps(cases, indent=2), encoding='utf-8')
    write_matlab_runner(cases, args.output / 'run_a007_official.m')
    results = []
    for case in cases:
        metadata = {}
        if case['operation'] == 'metrics':
            actual, classes = evaluate(case['gt'], case['det'])
            metadata = dict(metric_order=METRICS, repeated_evalClass=classes)
        elif case['operation'] == 'filter':
            g, d = drop_ignored(case['gt'], case['det'])
            actual = [len(g), len(d)]
        elif case['operation'] == 'match':
            _, d = match(case['gt'], case['det'])
            actual = [r[5] for r in d]
        else:
            actual = small_recall(case['gt'], case['det'], case.get('tau', 0))
            metadata = dict(ratio=None if actual[1] == 0 else actual[0] / actual[1])
        passed = len(actual) == len(case['expected']) and all(
            a is not None and math.isclose(a, e, abs_tol=1e-8) for a, e in zip(actual, case['expected']))
        results.append(dict(id=case['id'], expected=case['expected'], actual=actual,
                            passed=passed, **metadata))
    record = dict(scope='SYNTHETIC_ONLY_PYTHON_TRANSLATION_NOT_OFFICIAL_EXECUTION',
                  toolkit_commit=COMMIT, toolkit_zip_sha256=ARCHIVE_SHA,
                  source_hashes=manifest, script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python=sys.version, platform=platform.platform(),
                  official_runtime_executed=False, results=results,
                  passed=sum(r['passed'] for r in results), total=len(results))
    (args.output / 'results.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps({k: record[k] for k in ['scope', 'passed', 'total', 'official_runtime_executed']}))
    for r in results:
        if not r['passed']:
            print(json.dumps(r))
    if record['passed'] != record['total']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
