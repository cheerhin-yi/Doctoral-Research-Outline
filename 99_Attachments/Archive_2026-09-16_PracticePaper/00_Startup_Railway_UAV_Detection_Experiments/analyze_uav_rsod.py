"""A0-01 static dataset audit. Reads verified ZIPs; never imports/runs models.

Requires Pillow and numpy. No annotation is repaired, converted or generated.
VOC geometry uses raw xmax-xmin/ymax-ymin; origin convention remains unassumed.
Exact SHA/pixel matches are evidence; dHash matches are review candidates only.
"""
import csv
import hashlib
import io
import json
import pathlib
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

import numpy as np
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = ROOT / '11_Datasets/raw/UAV-RSOD'
OUT = ROOT / '11_Datasets/processed/UAV-RSOD/A0-01'


def write_csv(name, rows):
    if not rows:
        (OUT / name).write_text('none\n', encoding='utf-8')
        return
    with (OUT / name).open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def dhash(image):
    a = np.asarray(image.convert('L').resize((9, 8), Image.Resampling.LANCZOS))
    bits = a[:, 1:] > a[:, :-1]
    return int.from_bytes(np.packbits(bits).tobytes(), 'big')


def quantiles(values):
    if not values: return None
    return dict(zip(['min', 'p25', 'median', 'p75', 'p95', 'max'], map(float, np.quantile(values, [0, .25, .5, .75, .95, 1]))))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    inventory, images, boxes, issues, hashes, thumbs = [], [], [], [], {}, {}
    original_variants = {}
    exif_presence = Counter()
    masks = set()
    csv_labels = []
    archives = {}
    record = json.loads((RAW / 'zenodo_record.json').read_bytes())
    for entry in record['files']:
        path = RAW / entry['key']
        with path.open('rb') as handle:
            assert 'md5:' + hashlib.file_digest(handle, 'md5').hexdigest() == entry['checksum']
        version = path.name[:2]
        archive = zipfile.ZipFile(path)
        archives[version] = archive
        members = set(archive.namelist())
        bad_crc = archive.testzip()
        assert bad_crc is None, bad_crc
        for item in archive.infolist():
            name = item.filename
            inventory.append(dict(package=version, path=name, size=item.file_size, compressed=item.compress_size, crc32=f'{item.CRC:08x}', directory=item.is_dir()))
            if item.is_dir(): continue
            if name.endswith('_labels.csv'):
                for record_row in csv.DictReader(io.StringIO(archive.read(name).decode('utf-8-sig'))):
                    csv_labels.append(dict(source=name, **record_row))
            if version == 'V1' and '/2.2 Masking/' in name:
                masks.add(name)
            if not name.lower().endswith('.jpg'): continue
            # All files decoded, including segmentation renderings/masks.
            data = archive.read(name)
            try:
                with Image.open(io.BytesIO(data)) as source:
                    source.load()
                    exif_presence[version + ':' + ('present' if source.getexif() else 'absent')] += 1
                    im = source.convert('RGB')
            except Exception as error:
                issues.append(dict(path=name, kind='image_decode_error', detail=str(error)))
                continue
            if version == 'V1' and '/1 Images/' not in name: continue
            key = version + ':' + name
            split = 'original' if version == 'V1' else pathlib.PurePosixPath(name).parent.name
            row = dict(key=key, version=version, path=name, split=split, width=im.width, height=im.height, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pixel_sha256=hashlib.sha256(f'{im.size}:RGB:'.encode()+im.tobytes()).hexdigest(), dhash=f'{dhash(im):016x}')
            images.append(row)
            hashes[key] = int(row['dhash'], 16)
            thumbs[key] = im.resize((256,144), Image.Resampling.LANCZOS)
            if version == 'V1':
                variants = [im] + [im.transpose(op) for op in [Image.Transpose.FLIP_LEFT_RIGHT, Image.Transpose.FLIP_TOP_BOTTOM, Image.Transpose.ROTATE_90, Image.Transpose.ROTATE_180, Image.Transpose.ROTATE_270, Image.Transpose.TRANSPOSE, Image.Transpose.TRANSVERSE]]
                original_variants[key] = [dhash(v) for v in variants]
                continue
            xmlname = name[:-4] + '.xml'
            if xmlname not in members:
                issues.append(dict(path=name, kind='missing_xml', detail=xmlname))
                continue
            tree = ET.fromstring(archive.read(xmlname))
            declared = (int(tree.findtext('size/width')), int(tree.findtext('size/height')))
            if declared != im.size:
                issues.append(dict(path=name, kind='dimension_mismatch', detail=f'xml={declared}; image={im.size}'))
            if tree.findtext('filename') != pathlib.PurePosixPath(name).name:
                issues.append(dict(path=name, kind='filename_mismatch', detail=str(tree.findtext('filename'))))
            for j, obj in enumerate(tree.findall('object')):
                coords = [float(obj.findtext('bndbox/'+tag)) for tag in ['xmin','ymin','xmax','ymax']]
                x1,y1,x2,y2 = coords
                w,h=x2-x1,y2-y1
                valid = bool(np.isfinite(coords).all() and w>0 and h>0 and x1>=0 and y1>=0 and x2<=im.width and y2<=im.height)
                if not valid:
                    issues.append(dict(path=name, kind='invalid_box', detail=str(coords)))
                scale = 640/max(im.size)
                boxes.append(dict(key=key, index=j, split=split, label=obj.findtext('name'), xmin=x1,ymin=y1,xmax=x2,ymax=y2,width=w,height=h,area=w*h,short=min(w,h),aspect=w/h if h else None, relative_area=w*h/(im.width*im.height), area_letterbox640=w*h*scale*scale,valid=valid))
        for name in members:
            if name.endswith('.xml') and name[:-4]+'.jpg' not in members:
                issues.append(dict(path=name,kind='missing_image',detail=name[:-4]+'.jpg'))
        print(version, 'read complete', flush=True)
    write_csv('file_inventory.csv', inventory)
    write_csv('image_manifest.csv',images)
    write_csv('box_manifest.csv', boxes)
    write_csv('issues.csv',issues)
    bykey = {r['key']:r for r in images}
    exact = []
    for field in ['sha256', 'pixel_sha256']:
        groups = defaultdict(list)
        for row in images: groups[row[field]].append(row['key'])
        for digest, keys in groups.items():
            if len(keys)>1:
                exact.append(dict(kind=field, digest=digest, count=len(keys), splits=';'.join(sorted(set(bykey[k]['split'] for k in keys))), keys=';'.join(keys)))
    write_csv('exact_duplicate_groups.csv', exact)
    originals = [r for r in images if r['version']=='V1']
    detected = [r for r in images if r['version']=='V2']
    mappings = []
    for row in detected:
        key=row['key']; dh=hashes[key]
        nearest = sorted((min((dh^v).bit_count() for v in variants), orig) for orig,variants in original_variants.items())[:2]
        exact_orig = [r['key'] for r in originals if r['sha256']==row['sha256'] or r['pixel_sha256']==row['pixel_sha256']]
        mappings.append(dict(key=key, exact_original=';'.join(exact_orig), nearest_original=nearest[0][1], distance=nearest[0][0], runner_up_distance=nearest[1][0], relationship='Exact' if exact_orig else 'Unknown: perceptual candidate only'))
    write_csv('original_match_candidates.csv', mappings)
    near=[]
    all_primary = originals+detected
    for i,a in enumerate(all_primary):
        for b in all_primary[i+1:]:
            distance = (hashes[a['key']]^hashes[b['key']]).bit_count()
            if distance<=4 and a['pixel_sha256']!=b['pixel_sha256']:
                near.append(dict(left=a['key'],right=b['key'],distance=distance,cross_official_split={a['split'],b['split']}=={'train','test'},relationship='Unknown: visually inspect; no source ID inferred'))
    write_csv('near_duplicate_candidates.csv', near)
    valid_boxes=[r for r in boxes if r['valid']]
    class_stats=[]
    for label in sorted(set(r['label'] for r in boxes)):
        subset=[r for r in valid_boxes if r['label']==label]
        class_stats.append(dict(label=label,boxes=sum(r['label']==label for r in boxes),valid=len(subset),images=len(set(r['key'] for r in subset)),train=sum(r['split']=='train' for r in subset),test=sum(r['split']=='test' for r in subset),area_lt1024=sum(r['area']<1024 for r in subset),short_lt32=sum(r['short']<32 for r in subset),relative_area_lt01=sum(r['relative_area']<.01 for r in subset),small_letterbox640=sum(r['area_letterbox640']<1024 for r in subset)))
    write_csv('class_statistics.csv',class_stats)
    csv_keys=Counter()
    for r in csv_labels:
        csv_keys[(pathlib.PurePosixPath(r['source']).name.split('_')[0],r['filename'],r['class'],*(float(r[k]) for k in ['xmin','ymin','xmax','ymax']))]+=1
    xml_keys=Counter((r['split'],pathlib.PurePosixPath(bykey[r['key']]['path']).name,r['label'],r['xmin'],r['ymin'],r['xmax'],r['ymax']) for r in boxes)
    csv_comparison=dict(csv_rows=len(csv_labels), xml_boxes=len(boxes),csv_not_in_xml=sum((csv_keys-xml_keys).values()),xml_not_in_csv=sum((xml_keys-csv_keys).values()))
    boxed_keys=set(r['key'] for r in boxes)
    summary=dict(images_by_version_split=dict(Counter(r['version']+':'+r['split'] for r in images)),dimensions=dict(Counter(str((r['width'],r['height'])) for r in images)),class_statistics=class_stats,boxes=len(boxes),valid_boxes=len(valid_boxes),empty_images=sum(r['key'] not in boxed_keys for r in detected),issues=dict(Counter(r['kind'] for r in issues)),bbox_quantiles={field:quantiles([r[field] for r in valid_boxes]) for field in ['area','short','aspect','relative_area','area_letterbox640']},exif=dict(exif_presence),exact_group_count=len(exact),exact_cross_split_groups=sum('train' in r['splits'] and 'test' in r['splits'] for r in exact if r['kind']=='pixel_sha256'),v2_exact_matched_images=sum(bool(r['exact_original']) for r in mappings),v1_exact_matched_originals=len(set(k for r in mappings for k in r['exact_original'].split(';') if k)),perceptual_v2_to_v1_candidates_le4=sum(r['distance']<=4 for r in mappings),near_pair_count=len(near),near_cross_split_pairs=sum(r['cross_official_split'] for r in near),masks=len(masks),source_independence='Unknown; hashes do not establish independent flights/scenes')
    summary['csv_xml_comparison']=csv_comparison
    summary['original_mask_missing']=sum(not any(pathlib.PurePosixPath(m).name==pathlib.PurePosixPath(r['path']).name and '/Rail Inside/' in m for m in masks) for r in originals)
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    # Deterministic visual audit: 12 evenly spaced originals, then 8 closest cross-split pairs.
    selected=[originals[i]['key'] for i in np.linspace(0,len(originals)-1,12,dtype=int)]
    canvas=Image.new('RGB',(4*320,3*205),'white'); draw=ImageDraw.Draw(canvas)
    for i,key in enumerate(selected):
        x=(i%4)*320;y=(i//4)*205
        canvas.paste(thumbs[key].resize((320,180)),(x,y))
        draw.text((x+3,y+182),bykey[key]['version']+':'+pathlib.PurePosixPath(bykey[key]['path']).name,fill='black')
    canvas.save(OUT/'original_contact_sheet.jpg')
    pairs=sorted([r for r in near if r['cross_official_split']],key=lambda r:(r['distance'],r['left'],r['right']))[:8]
    if pairs:
        canvas=Image.new('RGB',(640,len(pairs)*205),'white'); draw=ImageDraw.Draw(canvas)
        for i,pair in enumerate(pairs):
            for j,key in enumerate([pair['left'],pair['right']]):
                canvas.paste(thumbs[key].resize((320,180)),(j*320,i*205))
                draw.text((j*320+3,i*205+182),bykey[key]['split']+':'+pathlib.PurePosixPath(bykey[key]['path']).name+f" d={pair['distance']}",fill='black')
        canvas.save(OUT/'cross_split_candidates.jpg')
    for a in archives.values(): a.close()
    print(json.dumps(summary,indent=2),flush=True)


if __name__ == '__main__': main()
