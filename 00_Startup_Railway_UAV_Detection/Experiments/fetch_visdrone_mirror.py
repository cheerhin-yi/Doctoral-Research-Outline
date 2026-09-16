"""Resumable public Ultralytics mirror transfer, with verified HTTP ranges.

This is a separate public mirror, not an original-author checksum attestation.
Does not run Ultralytics or alter annotations. Existing partials are retained.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '11_Datasets/processed/VisDrone/A0-05'
RAW = ROOT / '11_Datasets/raw/VisDrone/ultralytics'
CHUNK = 2 * 1024 * 1024


def request(url, start, end):
    req = urllib.request.Request(url, headers={'Range': f'bytes={start}-{end}'})
    with urllib.request.urlopen(req, timeout=45) as response:
        assert response.status == 206, 'Range ignored'
        cr = response.headers['Content-Range']
        assert cr.startswith(f'bytes {start}-{end}/'), cr
        data = response.read()
        assert len(data) == end - start + 1
        return data, int(cr.split('/')[-1])


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    manifests, jobs = [], []
    previous = OUT / 'mirror_range_sources.json'
    known = {x['split']: x for x in json.loads(previous.read_text())} if previous.exists() else {}
    for split in ['val', 'test-dev', 'train']:
        name = f'VisDrone2019-DET-{split}.zip'
        url = 'https://github.com/ultralytics/assets/releases/download/v0.0.0/' + name
        if split in known and known[split]['url'] == url:
            size = known[split]['bytes']
        else:
            _, size = request(url, 0, 0)
        chunks = OUT / ('chunks_' + split)
        chunks.mkdir(exist_ok=True)
        manifests.append(dict(split=split, url=url, bytes=size, chunks=str(chunks), name=name))
        for start in range(0, size, CHUNK):
            end = min(size, start + CHUNK) - 1
            jobs.append((url, start, end, chunks / str(start), size))
    (OUT / 'mirror_range_sources.json').write_text(json.dumps(manifests, indent=2), encoding='utf-8')

    def transfer(job):
        url, start, end, path, size = job
        if path.exists() and path.stat().st_size == end - start + 1:
            return
        for attempt in range(3):
            try:
                data, total = request(url, start, end)
                assert total == size, 'Remote file size changed'
                path.write_bytes(data)
                return
            except Exception:
                if attempt == 2:
                    raise

    last = time.monotonic()
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as pool:
        futures = {pool.submit(transfer, job): job for job in jobs}
        done = 0
        for future in concurrent.futures.as_completed(futures):
            done += 1
            try:
                future.result()
            except Exception as error:
                job = futures[future]
                errors.append({'url': job[0], 'start': job[1], 'error': str(error)})
            if time.monotonic() - last > 30:
                print('chunks complete', done, '/', len(jobs), 'errors', len(errors), flush=True)
                last = time.monotonic()
    logs = []
    for item in manifests:
        chunks = Path(item['chunks'])
        missing = [start for start in range(0, item['bytes'], CHUNK)
                   if not (chunks / str(start)).exists() or
                   (chunks / str(start)).stat().st_size != min(CHUNK, item['bytes'] - start)]
        if missing:
            logs.append(dict(**item, status='incomplete', missing=missing))
            continue
        target = RAW / item['name']
        if not target.exists():
            temporary = OUT / (item['name'] + '.assembled')
            with temporary.open('wb') as handle:
                for start in range(0, item['bytes'], CHUNK):
                    handle.write((chunks / str(start)).read_bytes())
            assert zipfile.is_zipfile(temporary)
            temporary.rename(target)
        with target.open('rb') as handle:
            sha = hashlib.file_digest(handle, 'sha256').hexdigest()
        logs.append(dict(**item, sha256=sha, status='downloaded; requires CRC/image audit'))
    (OUT / 'mirror_range_acquisition.json').write_text(json.dumps({'files': logs, 'errors': errors}, indent=2), encoding='utf-8')
    print(json.dumps(logs), flush=True)


if __name__ == '__main__':
    main()
