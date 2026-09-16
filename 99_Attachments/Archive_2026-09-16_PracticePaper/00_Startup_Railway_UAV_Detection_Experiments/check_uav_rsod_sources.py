"""A0-02: capture public metadata and inspect provenance, without model execution.

Snapshots go to a new ignored directory; existing packages are read-only.
Remote code is inspected as text, never imported or executed.
"""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / '11_Datasets/raw/UAV-RSOD'
BASE = ROOT / '11_Datasets/processed/UAV-RSOD/A0-02'
SOURCES = {
    'record': 'https://zenodo.org/api/records/12606374',
    'versions': 'https://zenodo.org/api/records/12606374/versions',
    'media': 'https://zenodo.org/api/records/12606374/media-files',
    'gist': 'https://api.github.com/gists/782fdb7b10bc4ac1424845662892120e',
}


def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out = BASE / stamp
    out.mkdir(parents=True, exist_ok=False)

    def capture(item):
        name, url = item
        result = {'url': url}
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'UAV-RSOD-research-audit'})
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read()
                result.update(status=response.status, final_url=response.url)
            (out / (name + '.json')).write_bytes(data)
            result.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            obj = json.loads(data)
            if name == 'record':
                result.update(id=obj['id'], updated=obj.get('updated'),
                              files=[{'name': f['key'], 'checksum': f['checksum']} for f in obj['files']],
                              related=obj['metadata'].get('related_identifiers', []),
                              version=obj['metadata'].get('version'))
            elif name == 'gist':
                result.update(files=[{'name': k, 'truncated': v.get('truncated', False),
                                      'raw_url': v['raw_url']} for k, v in obj['files'].items()],
                              revisions=[h['version'] for h in obj.get('history', [])],
                              updated=obj.get('updated_at'))
            else:
                result['response'] = obj
        except Exception as error:
            result['error'] = str(error)
        return name, result

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = dict(pool.map(capture, SOURCES.items()))

    provenance = {}
    for package in sorted(RAW.glob('*.zip')):
        with zipfile.ZipFile(package) as archive:
            names = [n for n in archive.namelist() if not n.endswith('/')]
            other = [n for n in names if Path(n).suffix.lower() not in {'.jpg', '.xml', '.csv'}]
            sources, paths = set(), set()
            for name in names:
                if name.lower().endswith('.xml'):
                    root = ET.fromstring(archive.read(name))
                    sources.add(ET.tostring(root.find('source'), encoding='unicode') if root.find('source') is not None else 'Missing')
                    paths.add(root.findtext('path', 'Missing'))
            provenance[package.name] = {'other_files': other, 'xml_source_values': sorted(sources),
                                        'xml_unique_path_count': len(paths), 'xml_path_examples': sorted(paths)[:3]}
    results['package_provenance'] = provenance
    result_path = out / 'results.json'
    result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(str(result_path))
    for name, value in results.items():
        print(name, json.dumps(value, ensure_ascii=True)[:2200])


if __name__ == '__main__':
    main()
