"""Static ZIP/label/image audit. No model execution, conversion, or split changes.

Counts are label-level (score=1, category 1..10, valid half-open geometry),
before the evaluator's ignored-region overlap filter. Filename prefixes and
dHash candidates are clues only, never asserted to be source identities.
"""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import time
import zipfile

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / '11_Datasets/raw/VisDrone'
BASE = ROOT / '11_Datasets/processed/VisDrone/A0-05'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def run(packages, out):
    packages = [p.resolve(strict=True) for p in packages]
    assert all(zipfile.is_zipfile(p) for p in packages), 'Input must be a complete ZIP'
    out.mkdir(parents=True, exist_ok=False)
    frames, issues, inventories, package_info = [], [], [], []
    aggregates = defaultdict(Counter)
    dimensions = defaultdict(list)
    class_stats = defaultdict(Counter)
    bf = (out / 'boxes.csv').open('w', newline='', encoding='utf-8')
    bw = csv.writer(bf)
    bw.writerow(['image', 'split', 'row', 'x', 'y', 'w', 'h', 'score', 'category',
                 'truncation', 'occlusion', 'geometry_valid', 'eligible_pre_ignore', 'area',
                 'short_side', 'aspect', 'relative_area', 'area_long640'])
    last = time.monotonic()
    for package in packages:
        split = package.stem.removeprefix('VisDrone2019-DET-')
        counts = aggregates[split]
        with package.open('rb') as handle:
            digest = hashlib.file_digest(handle, 'sha256').hexdigest()
        pi = {'path': str(package.relative_to(ROOT)), 'split': split, 'bytes': package.stat().st_size,
              'sha256': digest, 'extra_files': [], 'crc_read_errors': 0}
        with zipfile.ZipFile(package) as archive:
            infos = [i for i in archive.infolist() if not i.is_dir()]
            names = [i.filename for i in infos]
            counts['duplicate_zip_names'] = len(names) - len(set(names))
            images = {Path(n).stem: n for n in names if '/images/' in n and n.lower().endswith(('.jpg', '.jpeg', '.png'))}
            labels = {Path(n).stem: n for n in names if '/annotations/' in n and n.endswith('.txt')}
            counts['images'], counts['annotation_files'] = len(images), len(labels)
            for key in sorted(images.keys() - labels.keys()):
                issues.append({'split': split, 'file': images[key], 'issue': 'missing_annotation'})
            for key in sorted(labels.keys() - images.keys()):
                issues.append({'split': split, 'file': labels[key], 'issue': 'orphan_annotation'})
            consumed = set()
            for info in infos:
                inventories.append({'split': split, 'path': info.filename, 'bytes': info.file_size, 'crc32': f'{info.CRC:08x}'})
            for key, name in sorted(images.items()):
                try:
                    data = archive.read(name)
                    consumed.add(name)
                    with Image.open(io.BytesIO(data)) as opened:
                        exif = bool(opened.getexif())
                        image = opened.convert('RGB')
                        image.load()
                    width, height = image.size
                    pixels = sha(f'{width},{height}:'.encode() + image.tobytes())
                    tiny = np.asarray(image.convert('L').resize((9, 8), Image.Resampling.BILINEAR))
                    dhash = int.from_bytes(np.packbits(tiny[:, 1:] > tiny[:, :-1]).tobytes(), 'big')
                except Exception as error:
                    issues.append({'split': split, 'file': name, 'issue': 'read_or_decode: ' + str(error)})
                    pi['crc_read_errors'] += 1
                    continue
                counts['decoded'] += 1
                counts['with_exif'] += int(exif)
                local_eligible, raw_rows, ignored_regions = 0, 0, 0
                if key in labels:
                    try:
                        raw = archive.read(labels[key])
                        consumed.add(labels[key])
                        text = raw.decode('utf-8-sig')
                    except Exception as error:
                        issues.append({'split': split, 'file': labels[key], 'issue': 'annotation_read: ' + str(error)})
                        pi['crc_read_errors'] += 1
                        text = ''
                    for row, line in enumerate(text.splitlines(), 1):
                        if not line.strip():
                            continue
                        raw_rows += 1
                        counts['annotation_rows'] += 1
                        try:
                            parts = [v.strip() for v in line.strip().split(',')]
                            if parts[-1] == '':
                                parts.pop()  # optional trailing delimiter, no field is discarded
                            assert len(parts) == 8, 'not eight fields'
                            vals = list(map(int, parts))
                            x, y, w, h, score, category, truncation, occlusion = vals
                        except Exception as error:
                            counts['malformed_rows'] += 1
                            issues.append({'split': split, 'file': labels[key], 'issue': f'row {row}: {error}'})
                            continue
                        geometry = x >= 0 and y >= 0 and w > 0 and h > 0 and x + w <= width and y + h <= height
                        attrs = score in [0, 1] and category in range(12) and truncation in [0, 1] and occlusion in [0, 1, 2]
                        eligible = geometry and score == 1 and 1 <= category <= 10
                        counts['invalid_geometry'] += int(not geometry)
                        counts['invalid_attributes'] += int(not attrs)
                        if not geometry or not attrs:
                            issues.append({'split': split, 'file': labels[key], 'issue': f'row {row}: geometry={geometry}, attributes={attrs}, values={vals}'})
                        counts[f'category_{category}'] += 1
                        counts['score_zero'] += int(score == 0)
                        counts['ignored_regions'] += int(category == 0)
                        ignored_regions += int(category == 0)
                        area = w * h
                        scaled = area * (640 / max(width, height)) ** 2
                        if eligible:
                            local_eligible += 1
                            counts['eligible_pre_ignore'] += 1
                            cs = class_stats[(split, category)]
                            for target in [counts, cs]:
                                target['small_area_lt1024'] += int(area < 1024)
                                target['short_lt32'] += int(min(w, h) < 32)
                                target['relative_lt1pct'] += int(area / (width * height) < .01)
                                target['small_long640_lt1024'] += int(scaled < 1024)
                            cs['eligible_pre_ignore'] += 1
                            dimensions[split].append([area, min(w, h), w / h, area / (width * height)])
                        bw.writerow([name, split, row, *vals, geometry, eligible, area, min(w, h),
                                     w / h if h else '', area / (width * height), scaled])
                counts['empty_annotation_images'] += int(raw_rows == 0)
                counts['no_eligible_images'] += int(local_eligible == 0)
                counts['images_with_ignore_region'] += int(ignored_regions > 0)
                frames.append({'split': split, 'path': name, 'key': key, 'prefix_candidate': key.split('_')[0],
                               'width': width, 'height': height, 'file_sha256': sha(data),
                               'rgb_sha256': pixels, 'dhash64': f'{dhash:016x}', 'exif_present': exif,
                               'eligible_pre_ignore': local_eligible})
                if time.monotonic() - last > 30:
                    print('decoded', len(frames), flush=True)
                    last = time.monotonic()
            for name in names:
                if name in consumed:
                    continue
                try:
                    data = archive.read(name)  # CRC for every other entry
                    if name not in images.values() and name not in labels.values():
                        pi['extra_files'].append({'path': name, 'bytes': len(data), 'sha256': sha(data),
                                                 'text': data.decode('utf-8', errors='replace')[:8000] if name.lower().endswith(('.txt', '.md')) else None})
                except Exception as error:
                    pi['crc_read_errors'] += 1
                    issues.append({'split': split, 'file': name, 'issue': 'CRC/read: ' + str(error)})
        package_info.append(pi)
    bf.close()
    duplicates = []
    for field in ['file_sha256', 'rgb_sha256']:
        groups = defaultdict(list)
        for frame in frames:
            groups[frame[field]].append(frame)
        for digest, members in groups.items():
            if len(members) > 1:
                duplicates.append({'hash_type': field, 'digest': digest,
                                   'cross_split': len({f['split'] for f in members}) > 1,
                                   'members': ';'.join(f['path'] for f in members)})
    near = []
    buckets = defaultdict(list)
    # Hamming <=4 implies one identical chunk in any five disjoint chunks.
    chunks = [(0, 13), (13, 13), (26, 13), (39, 13), (52, 12)]
    values = [int(f['dhash64'], 16) for f in frames]
    for i, frame in enumerate(frames):
        candidates = set()
        for offset, bits in chunks:
            bucket = (offset, (values[i] >> offset) & ((1 << bits) - 1))
            candidates.update(buckets[bucket])
            buckets[bucket].append(i)
        for j in sorted(candidates):
            if frames[j]['rgb_sha256'] == frame['rgb_sha256']:
                continue
            distance = (values[i] ^ values[j]).bit_count()
            if distance <= 4:
                near.append({'left': frames[j]['path'], 'right': frame['path'], 'distance': distance,
                             'cross_split': frames[j]['split'] != frame['split']})
    prefixes = defaultdict(set)
    for frame in frames:
        prefixes[frame['prefix_candidate']].add(frame['split'])
    summary = {'packages': package_info, 'splits': dict(aggregates),
               'geometry_summary': {s: {'columns': ['area', 'short', 'aspect', 'relative_area'],
                                        'min': np.min(v, axis=0).tolist(), 'median': np.median(v, axis=0).tolist(),
                                        'max': np.max(v, axis=0).tolist()} for s, v in dimensions.items()},
               'cross_split_exact_file_groups': sum(d['cross_split'] and d['hash_type'] == 'file_sha256' for d in duplicates),
               'cross_split_exact_pixel_groups': sum(d['cross_split'] and d['hash_type'] == 'rgb_sha256' for d in duplicates),
               'near_pairs': len(near), 'near_cross_split_pairs': sum(d['cross_split'] for d in near),
               'prefix_candidates': len(prefixes),
               'cross_split_prefix_candidates': {k: sorted(v) for k, v in prefixes.items() if len(v) > 1},
               'issue_count': len(issues), 'scope': 'label-level stats before evaluator ignore-overlap filtering; no inference'}
    (out / 'summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    write_csv(out / 'images.csv', frames, list(frames[0]) if frames else ['path'])
    write_csv(out / 'inventory.csv', inventories, ['split', 'path', 'bytes', 'crc32'])
    write_csv(out / 'issues.csv', issues, ['split', 'file', 'issue'])
    write_csv(out / 'exact_duplicates.csv', duplicates, ['hash_type', 'digest', 'cross_split', 'members'])
    write_csv(out / 'near_candidates.csv', near, ['left', 'right', 'distance', 'cross_split'])
    rows = [dict(split=s, category=c, **dict(v)) for (s, c), v in sorted(class_stats.items())]
    write_csv(out / 'classes.csv', rows, ['split', 'category', 'small_area_lt1024', 'short_lt32',
                                         'relative_lt1pct', 'small_long640_lt1024', 'eligible_pre_ignore'])
    print(json.dumps({k: v for k, v in summary.items() if k not in ['packages', 'cross_split_prefix_candidates']}, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--packages', nargs='+', required=True, type=Path)
    parser.add_argument('--output-name', required=True)
    args = parser.parse_args()
    out = (BASE / args.output_name).resolve()
    assert out.is_relative_to(BASE.resolve()), 'output outside audit directory'
    run(args.packages, out)
