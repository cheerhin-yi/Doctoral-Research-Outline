"""Read-only provenance acquisition for A0-01. Never runs dataset code or models.

Downloads only after the record's research-compatible license is verified.
Raw responses and packages remain under ignored raw/, outputs under processed/.
"""
import argparse
import hashlib
import json
import pathlib
import urllib.request
import xml.etree.ElementTree as ET
import concurrent.futures
import time
import zipfile
import io

ROOT = pathlib.Path(__file__).resolve().parents[2]
RAW = ROOT / '11_Datasets/raw/UAV-RSOD'
OUT = ROOT / '11_Datasets/processed/UAV-RSOD/A0-01'


def fetch(url, path, timeout=40):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path.read_bytes()
    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read()
    path.write_bytes(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['sources', 'download', 'inventory', 'remote-inventory'])
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.action == 'download':
        record = json.loads(fetch('https://zenodo.org/api/records/12606374', RAW / 'zenodo_record.json'))
        assert record['metadata']['access_right'] == 'open'
        assert record['metadata']['license']['id'] == 'cc-by-4.0'
        def download(entry):
            target = RAW / entry['key']
            partial = OUT / (entry['key'] + '.part')
            if not target.exists():
                with urllib.request.urlopen(entry['links']['self'], timeout=60) as response, partial.open('wb') as handle:
                    size = 0
                    last = time.monotonic()
                    while block := response.read(4 * 1024 * 1024):
                        handle.write(block)
                        size += len(block)
                        if time.monotonic() - last > 30:
                            print(entry['key'], size, '/', entry['size'], flush=True)
                            last = time.monotonic()
                assert partial.stat().st_size == entry['size'], 'incomplete package'
                with partial.open('rb') as handle:
                    digest = hashlib.file_digest(handle, 'md5').hexdigest()
                assert 'md5:' + digest == entry['checksum'], 'checksum mismatch'
                partial.rename(target)
            with target.open('rb') as handle:
                md5 = hashlib.file_digest(handle, 'md5').hexdigest()
            with target.open('rb') as handle:
                sha = hashlib.file_digest(handle, 'sha256').hexdigest()
            result = dict(file=target.name, bytes=target.stat().st_size, md5=md5, sha256=sha, url=entry['links']['self'], expected=entry['checksum'])
            assert 'md5:' + md5 == entry['checksum']
            print(json.dumps(result), flush=True)
            return result
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(download, record['files']))
        (OUT / 'package_checksums.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
        return
    if args.action == 'remote-inventory':
        record = json.loads((RAW / 'zenodo_record.json').read_bytes())
        class RemoteFile(io.RawIOBase):
            def __init__(self, entry):
                self.entry = entry
                self.pos = 0
            def seekable(self): return True
            def readable(self): return True
            def tell(self): return self.pos
            def seek(self, offset, whence=0):
                self.pos = offset + (0 if whence == 0 else self.pos if whence == 1 else self.entry['size'])
                return self.pos
            def read(self, size=-1):
                end = self.entry['size'] - 1 if size < 0 else min(self.pos + size, self.entry['size']) - 1
                if end < self.pos: return b''
                req = urllib.request.Request(self.entry['links']['self'], headers={'Range': f'bytes={self.pos}-{end}'})
                with urllib.request.urlopen(req, timeout=60) as response:
                    assert response.status == 206
                    assert response.headers['Content-Range'].startswith(f'bytes {self.pos}-{end}/')
                    data = response.read()
                self.pos += len(data)
                return data
        for entry in record['files']:
            with zipfile.ZipFile(RemoteFile(entry)) as archive:
                names = archive.namelist()
                (OUT / (entry['key'] + '.remote-inventory.txt')).write_text('\n'.join(names), encoding='utf-8')
                from collections import Counter
                print(entry['key'], len(names), Counter(pathlib.PurePosixPath(n).suffix.lower() for n in names), flush=True)
                print('\n'.join(names[:12]), flush=True)
                labels = [n for n in names if n.endswith(('.xml', '.txt', '.json', '.csv', '.py'))]
                print('label samples:', labels[:8], flush=True)
                for name in labels[:2]:
                    print(name, archive.read(name)[:3500].decode(errors='replace'), flush=True)
        return
    if args.action == 'inventory':
        from collections import Counter
        for package in sorted(RAW.glob('*.zip')):
            with zipfile.ZipFile(package) as archive:
                names = archive.namelist()
                (OUT / (package.name + '.inventory.txt')).write_text('\n'.join(names), encoding='utf-8')
                print(package.name, len(names), Counter(pathlib.PurePosixPath(n).suffix.lower() for n in names), flush=True)
                print('\n'.join(names[:20]), flush=True)
                labels = [n for n in names if n.endswith(('.xml', '.txt', '.json', '.csv', '.py'))]
                for name in labels[:4]:
                    print(name, archive.read(name)[:3500].decode(errors='replace'), flush=True)
        return
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11612275/fullTextXML'
    data = fetch(url, RAW / 'paper_fulltext.xml')
    article = ET.fromstring(data)
    lines = []
    for item in article.iter():
        if item.tag in ['article-title', 'title', 'p', 'table-wrap']:
            lines.append('[' + item.attrib.get('id', item.tag) + '] ' + ''.join(item.itertext()))
    (OUT / 'paper_fulltext.txt').write_text('\n\n'.join(lines), encoding='utf-8')
    print(json.dumps({'source': url, 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}))


if __name__ == '__main__':
    main()
