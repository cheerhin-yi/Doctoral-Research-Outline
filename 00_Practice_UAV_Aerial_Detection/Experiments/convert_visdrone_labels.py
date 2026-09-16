"""Single-file VisDrone label adapter; no images, model imports or bulk conversion.

Dropping positive labels does NOT implement region-neutral training ignore.
The CLI requires an unused output directory under this repository's processed
VisDrone directory. Original annotations are read only. See Label_Adapter_Check.md.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation, localcontext
import hashlib
import json
import math
from pathlib import Path

VERSION = "label-adapter-0.2"
REPO = Path(__file__).resolve().parents[2]
OUTPUT_ROOT = REPO / "11_Datasets/processed/VisDrone"
NAMES = (
    "pedestrian", "people", "bicycle", "car", "van", "truck", "tricycle",
    "awning-tricycle", "bus", "motor",
)


class AnnotationError(ValueError):
    """Input cannot be converted without an unapproved repair."""


def convert_text(text: str, width: int, height: int) -> tuple[str, list[dict]]:
    """Validate all rows before returning labels and a complete row audit.

    Blank files are valid; blank rows inside a nonblank file are malformed.
    Flags must be integers; score is restricted to 0/1 and category to 0..11.
    Occlusion/truncation values are preserved, not used to filter positives.
    """
    if any(type(v) is not int or v <= 0 for v in (width, height)):
        raise AnnotationError("Image dimensions must be positive integers")
    if not text.strip():
        return "", []
    rows, output = [], []
    with localcontext() as ctx:
        ctx.prec = 50
        W, H = Decimal(width), Decimal(height)
        for number, raw in enumerate(text.splitlines(), 1):
            fields = raw.split(",")
            # Match the existing dataset auditor's optional terminal delimiter rule.
            # Original raw text remains in the row audit; no numeric field is discarded.
            if len(fields) == 9 and not fields[-1].strip():
                fields.pop()
            if len(fields) != 8 or any(not v.strip() for v in fields):
                raise AnnotationError(f"Line {number}: expected eight nonempty fields")
            try:
                values = [Decimal(v.strip()) for v in fields]
            except InvalidOperation as exc:
                raise AnnotationError(f"Line {number}: invalid numeric field") from exc
            if not all(v.is_finite() for v in values):
                raise AnnotationError(f"Line {number}: nonfinite value")
            if any(v != v.to_integral_value() for v in values[4:]):
                raise AnnotationError(f"Line {number}: noninteger category/flag")
            x, y, w, h = values[:4]
            score, category, truncation, occlusion = map(int, values[4:])
            if score not in (0, 1) or not 0 <= category <= 11:
                raise AnnotationError(f"Line {number}: score/category outside allowed range")
            if (x < 0 or y < 0 or x > W or y > H
                    or (w > 0 and x + w > W) or (h > 0 and y + h > H)):
                raise AnnotationError(f"Line {number}: geometry outside image bounds")
            reasons = []
            if score == 0:
                reasons.append("score_zero")
            if category == 0:
                reasons.append("ignore_category")
            if category == 11:
                reasons.append("others_category")
            if w <= 0 or h <= 0:
                reasons.append("nonpositive_size")
            row = dict(line=number, raw=raw, score=score, category=category,
                       truncation=truncation, occlusion=occlusion,
                       reasons=reasons, action="excluded" if reasons else "kept")
            if not reasons:
                normalized = ((x + w / 2) / W, (y + h / 2) / H, w / W, h / H)
                tokens = [format(float(v), ".17g") for v in normalized]
                parsed = [float(v) for v in tokens]
                if not all(math.isfinite(v) and 0 < v <= 1 for v in parsed):
                    raise AnnotationError(f"Line {number}: normalization underflow/range error")
                label = f"{category - 1} " + " ".join(tokens)
                output.append(label)
                row.update(output_line=len(output), label=label)
            rows.append(row)
    return "".join(line + "\n" for line in output), rows


def convert_file(source: Path, width: int, height: int, destination: Path) -> dict:
    """Create labels.txt + audit.json in a fresh derived directory.

    Input errors create no destination. I/O failures may leave an incomplete
    directory, which is retained and cannot be overwritten by a retry.
    audit.json with status=complete is written last.
    """
    source, destination = Path(source).resolve(), Path(destination).resolve()
    allowed = OUTPUT_ROOT.resolve()
    if destination == allowed or not destination.is_relative_to(allowed):
        raise ValueError("Output must be a new subdirectory of processed/VisDrone")
    if destination.exists():
        raise FileExistsError(f"Refusing existing output: {destination}")
    if source.is_relative_to(destination):
        raise ValueError("Output cannot contain the input")
    original = source.read_bytes()  # Missing annotations are errors, never empty labels.
    labels, rows = convert_text(original.decode("utf-8"), width, height)
    digest = hashlib.sha256(original).hexdigest()
    if source.read_bytes() != original:
        raise RuntimeError("Source changed during conversion; no output written")
    encoded = labels.encode("utf-8")
    report = dict(
        status="complete", adapter_version=VERSION,
        adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        source=str(source), source_sha256=digest, width=width, height=height,
        names=list(NAMES), input_rows=len(rows), kept_rows=sum(r["action"] == "kept" for r in rows),
        empty_origin=("source_empty" if not rows else "all_excluded" if not labels else None),
        training_region_ignore=False, output_sha256=hashlib.sha256(encoded).hexdigest(),
        coordinate_rule="xywh pixels -> normalized center xywh; no +/-1; float .17g",
        rows=rows,
    )
    destination.mkdir(parents=True, exist_ok=False)
    with (destination / "labels.txt").open("xb") as handle:
        handle.write(encoded)
    with (destination / "audit.json").open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = convert_file(args.source, args.width, args.height, args.output)
    except (ValueError, OSError, RuntimeError) as exc:
        parser.exit(2, f"Conversion stopped: {exc}\n")
    print(json.dumps({key: report[key] for key in ("status", "input_rows", "kept_rows", "empty_origin")}))


if __name__ == "__main__":
    main()
