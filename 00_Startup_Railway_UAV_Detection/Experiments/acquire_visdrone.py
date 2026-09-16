"""Download public DET archives linked by VisDrone; no dataset/model code runs."""
import concurrent.futures
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import time
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / '11_Datasets/raw/VisDrone'
OUT = ROOT / '11_Datasets/processed/VisDrone/A0-05'
IDS = {'train': '1a2oHjcEcwXP8oUF95qiwrqzACb2YlUhn',
       'val': '1bxK5zgLn0_L8x276eKkuYA_FzwCIjb59',
       'test-dev': '1PFdW_VFSCfZ_sTSZAGjQdifF_Xd5mf0V'}
PROVIDER = 'official'


def download(item):
    split, file_id = item
    url = f'https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t'
    target = RAW / f'VisDrone2019-DET-{split}.zip'
    if PROVIDER == 'ultralytics':
        target = RAW / 'ultralytics' / target.name
        target.parent.mkdir(parents=True, exist_ok=True)
        url = 'https://github.com/ultralytics/assets/releases/download/v0.0.0/' + target.name
    log = {'split': split, 'official_index': 'https://github.com/VisDrone/VisDrone-Dataset',
           'drive_id': file_id, 'url': url, 'date_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    log['provider'] = PROVIDER
    log['original_byte_identity'] = 'not checked' if PROVIDER != 'official' else 'direct official download'
    try:
        if not target.exists():
            part = OUT / (PROVIDER + '_' + target.name + '.part')
            if part.exists():
                raise FileExistsError(f'Partial file preserved; inspect before retry: {part}')
            with urllib.request.urlopen(url, timeout=45) as response:
                assert 'text/html' not in response.headers.get('Content-Type', ''), 'HTML instead of ZIP'
                expected = response.headers.get('Content-Length')
                log['content_length'] = expected
                log['content_disposition'] = response.headers.get('Content-Disposition')
                log['last_modified'] = response.headers.get('Last-Modified')
                with part.open('xb') as handle:
                    size, last = 0, time.monotonic()
                    while block := response.read(4 * 1024 * 1024):
                        handle.write(block)
                        size += len(block)
                        if time.monotonic() - last > 30:
                            print(split, size, 'bytes', flush=True)
                            last = time.monotonic()
                if expected:
                    assert size == int(expected), 'Incomplete response'
            assert zipfile.is_zipfile(part), 'Invalid ZIP'
            part.rename(target)
        log['bytes'] = target.stat().st_size
        for algorithm in ['md5', 'sha256']:
            with target.open('rb') as handle:
                log[algorithm] = hashlib.file_digest(handle, algorithm).hexdigest()
        log['status'] = 'downloaded; CRC and images require audit'
    except Exception as error:
        log['status'] = 'error'
        log['error'] = str(error)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    (OUT / f'acquisition_{PROVIDER}_{split}_{stamp}.json').write_text(json.dumps(log, indent=2), encoding='utf-8')
    print(json.dumps(log), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--provider', choices=['official', 'ultralytics'], default='official')
    parser.add_argument('--splits', nargs='+', choices=list(IDS), default=list(IDS))
    args = parser.parse_args()
    PROVIDER = args.provider
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(download, [(s, IDS[s]) for s in args.splits]))
