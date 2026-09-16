"""Prepare fresh BT-1 inputs from two fixed ZIPs; never reads test-dev."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import zipfile

from PIL import Image
from convert_visdrone_labels import convert_text, NAMES

SHA = {"train": "86a77eba93137bfc16e4993860de9245b0675c0dba0d3ab98fb458699e256f84",
       "val": "abeea063037e5d20398837deb11084e652402a34ddf4f207bdf541a6f2a35ef9"}


def digest(path):
    with Path(path).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def prepare(train_zip, val_zip, out, smoke=False):
    out = Path(out).resolve()
    if out.exists():
        raise FileExistsError(f"Refusing existing output: {out}")
    for split, path in [("train", train_zip), ("val", val_zip)]:
        if digest(path) != SHA[split]:
            raise ValueError(f"{split} ZIP identity differs from approved input")
    out.mkdir(parents=True)
    manifests, counts = {}, {}
    with (out / "conversion.jsonl").open("x", encoding="utf-8") as audit:
        for split, source in [("train", train_zip), ("val", val_zip)]:
            with zipfile.ZipFile(source) as z:
                names = z.namelist()
                if len(set(names)) != len(names):
                    raise ValueError("Duplicate ZIP members")
                for n in names:
                    pp = PurePosixPath(n)
                    if pp.is_absolute() or ".." in pp.parts or "\\" in n or ":" in n:
                        raise ValueError("Unsafe ZIP path")
                prefix = f"VisDrone2019-DET-{split}"
                images = sorted(n for n in names if n.startswith(prefix + "/images/") and n.endswith(".jpg"))
                expected = 6471 if split == "train" else 548
                if len(images) != expected:
                    raise ValueError(f"Unexpected {split} image count: {len(images)}")
                if split == "val":
                    images.sort(key=lambda n: (hashlib.sha256(("diag-v1:" + PurePosixPath(n).name).encode()).hexdigest(), PurePosixPath(n).name))
                    # The remaining 500 images are not decoded or labelled here.
                    (out / "diag500_names.txt").write_text("\n".join(PurePosixPath(n).name for n in images[48:]) + "\n", encoding="utf-8")
                    images = images[:48]
                elif smoke:
                    images = images[:4]
                tag = "train" if split == "train" else "cal48"
                paths = []
                total = kept = excluded = 0
                for sub in ["images", "labels", "annotations"]:
                    (out / sub / tag).mkdir(parents=True)
                for n in images:
                    stem = PurePosixPath(n).stem
                    ann = prefix + "/annotations/" + stem + ".txt"
                    raw = z.read(ann)  # Missing label is an error, not an empty label.
                    img = z.read(n)
                    with Image.open(io.BytesIO(img)) as im:
                        w, h = im.size
                        im.verify()
                    labels, rows = convert_text(raw.decode("utf-8"), w, h)
                    image_path = out / "images" / tag / (stem + ".jpg")
                    image_path.write_bytes(img)
                    (out / "annotations" / tag / (stem + ".txt")).write_bytes(raw)
                    (out / "labels" / tag / (stem + ".txt")).write_text(labels, encoding="utf-8", newline="\n")
                    paths.append(image_path.as_posix())
                    n_kept = sum(r["action"] == "kept" for r in rows)
                    total += len(rows); kept += n_kept; excluded += len(rows) - n_kept
                    audit.write(json.dumps(dict(split=tag, member=n, width=w, height=h,
                        image_sha256=hashlib.sha256(img).hexdigest(), annotation_sha256=hashlib.sha256(raw).hexdigest(),
                        label_sha256=hashlib.sha256(labels.encode()).hexdigest(), rows=rows), ensure_ascii=False) + "\n")
                manifest = out / (tag + ".txt")
                manifest.write_text("\n".join(paths) + "\n", encoding="utf-8")
                manifests[tag] = str(manifest)
                counts[tag] = dict(images=len(paths), input_rows=total, kept_rows=kept, excluded_rows=excluded)
                assert total == kept + excluded
        # JSON is valid YAML; extension chosen for the detection framework.
        data = dict(path=str(out), train=manifests["train"], val=manifests["cal48"], nc=10, names=list(NAMES))
        (out / "data.yaml").write_text(json.dumps(data, indent=2), encoding="utf-8")
    report = dict(status="COMPLETE", smoke=smoke, source_sha256=SHA, counts=counts,
                  training_region_ignore=False, manifest_hashes={k: digest(v) for k, v in manifests.items()},
                  adapter_sha256=digest(Path(__file__).with_name("convert_visdrone_labels.py")))
    (out / "preparation.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--train-zip", type=Path, required=True)
    p.add_argument("--val-zip", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--smoke", action="store_true")
    a = p.parse_args()
    prepare(a.train_zip, a.val_zip, a.output, a.smoke)
