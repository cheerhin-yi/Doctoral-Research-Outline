"""Synthetic-only checks for convert_visdrone_labels; no dataset/model access."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest

from convert_visdrone_labels import AnnotationError, OUTPUT_ROOT, convert_file, convert_text

WORK: Path


class AdapterChecks(unittest.TestCase):
    def test_ten_classes_and_attributes(self):
        raw = "\n".join(f"10,20,30,40,1,{c},1,2" for c in range(1, 11))
        labels, rows = convert_text(raw, 200, 100)
        self.assertEqual([int(v.split()[0]) for v in labels.splitlines()], list(range(10)))
        for row in rows:
            self.assertEqual((row["truncation"], row["occlusion"], row["action"]), (1, 2, "kept"))
        self.assertEqual([r["line"] for r in rows], list(range(1, 11)))

    def test_non_square_manual_coordinates(self):
        labels, _ = convert_text("10,20,30,40,1,4,0,0", 200, 100)
        cls, *box = map(float, labels.split())
        self.assertEqual(cls, 3)
        for actual, expected in zip(box, [.125, .4, .15, .4]):
            self.assertAlmostEqual(actual, expected, places=14)

    def test_full_frame_and_roundtrip(self):
        raw = "0,0,200,100,1,1,0,0\n199,99,1,1,1,10,0,0\n0.25,1.5,2.75,4.5,1,4,0,0"
        labels, _ = convert_text(raw, 200, 100)
        self.assertEqual(list(map(float, labels.splitlines()[0].split()[1:])), [.5, .5, 1., 1.])
        expected = [(0, 0, 200, 100), (199, 99, 1, 1), (.25, 1.5, 2.75, 4.5)]
        for line, truth in zip(labels.splitlines(), expected):
            _, xc, yc, w, h = map(float, line.split())
            reconstructed = ((xc - w / 2) * 200, (yc - h / 2) * 100, w * 200, h * 100)
            for actual, value in zip(reconstructed, truth):
                self.assertLessEqual(abs(actual - value), 1e-10)

    def test_tiny_positive_not_rounded_to_zero(self):
        labels, _ = convert_text("0,0,0.00000001,0.00000001,1,1,0,0", 10000, 10000)
        self.assertGreater(float(labels.split()[3]), 0)
        self.assertGreater(float(labels.split()[4]), 0)

    def test_ignore_overlap_does_not_delete_valid_positive(self):
        labels, rows = convert_text("0,0,100,100,1,0,0,0\n10,10,5,5,1,1,0,0", 100, 100)
        self.assertEqual(len(labels.splitlines()), 1)
        self.assertEqual(rows[0]["reasons"], ["ignore_category"])
        self.assertEqual(rows[1]["action"], "kept")

    def test_combined_exclusion_reasons(self):
        labels, rows = convert_text("0,0,10,0,0,0,0,0\n0,0,-1,2,1,4,0,0", 100, 100)
        self.assertEqual(labels, "")
        self.assertEqual(rows[0]["reasons"], ["score_zero", "ignore_category", "nonpositive_size"])
        self.assertEqual(rows[1]["reasons"], ["nonpositive_size"])

    def test_empty_and_all_excluded_distinct(self):
        for name, raw, expected in [("empty", " \r\n", "source_empty"),
                                    ("excluded", "0,0,1,1,0,1,0,0", "all_excluded")]:
            source = WORK / f"{name}.txt"
            source.write_text(raw, encoding="utf-8")
            result = convert_file(source, 100, 100, WORK / f"{name}_output")
            self.assertEqual(result["empty_origin"], expected)
            self.assertEqual((WORK / f"{name}_output/labels.txt").read_bytes(), b"")
            self.assertFalse(result["training_region_ignore"])

    def test_file_audit_hash_and_original_preservation(self):
        source = WORK / "original.txt"
        content = b"10,20,30,40,1,4,1,2\r\n0,0,1,1,0,11,0,0\r\n"
        source.write_bytes(content)
        dest = WORK / "audited"
        result = convert_file(source, 200, 100, dest)
        self.assertEqual(source.read_bytes(), content)
        self.assertEqual(result["source_sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(result["output_sha256"], hashlib.sha256((dest / "labels.txt").read_bytes()).hexdigest())
        self.assertEqual(json.loads((dest / "audit.json").read_text(encoding="utf-8")), result)
        self.assertEqual(result["rows"][1]["raw"], "0,0,1,1,0,11,0,0")
        self.assertEqual(result["rows"][0]["output_line"], 1)
        self.assertEqual((result["input_rows"], result["kept_rows"]), (2, 1))

    def test_invalid_late_row_creates_no_output(self):
        source, dest = WORK / "late_error.txt", WORK / "late_error_output"
        source.write_text("0,0,1,1,1,1,0,0\n0,0,1,1,1,12,0,0", encoding="utf-8")
        original = source.read_bytes()
        with self.assertRaisesRegex(AnnotationError, "Line 2"):
            convert_file(source, 100, 100, dest)
        self.assertFalse(dest.exists())
        self.assertEqual(source.read_bytes(), original)

    def test_missing_file_not_empty(self):
        dest = WORK / "missing_output"
        with self.assertRaises(FileNotFoundError):
            convert_file(WORK / "missing.txt", 100, 100, dest)
        self.assertFalse(dest.exists())

    def test_existing_results_and_retry_refused(self):
        source = WORK / "retry.txt"
        source.write_text("0,0,1,1,1,1,0,0", encoding="utf-8")
        dest = WORK / "retry_output"
        convert_file(source, 100, 100, dest)
        before = {p.name: p.read_bytes() for p in dest.iterdir()}
        with self.assertRaises(FileExistsError):
            convert_file(source, 100, 100, dest)
        self.assertEqual(before, {p.name: p.read_bytes() for p in dest.iterdir()})
        empty = WORK / "existing_empty"
        empty.mkdir()
        with self.assertRaises(FileExistsError):
            convert_file(source, 100, 100, empty)

    def test_output_boundary_and_traversal_refused(self):
        for dest in [OUTPUT_ROOT, OUTPUT_ROOT / "../../raw/forbidden_adapter_output",
                     OUTPUT_ROOT.parent / "outside_adapter_output"]:
            with self.assertRaises(ValueError):
                convert_file(WORK / "not_read.txt", 100, 100, dest)

    def test_cli_success_and_missing_input_error(self):
        source = WORK / "cli.txt"
        source.write_text("0,0,100,100,1,10,0,0", encoding="utf-8")
        script = Path(__file__).with_name("convert_visdrone_labels.py")
        base = [sys.executable, str(script)]
        success = subprocess.run(base + [str(source), "--width", "100", "--height", "100",
                                        "--output", str(WORK / "cli_output")], capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout)["kept_rows"], 1)
        failure = subprocess.run(base + [str(WORK / "absent.txt"), "--width", "100", "--height", "100",
                                        "--output", str(WORK / "cli_absent_output")], capture_output=True, text=True)
        self.assertEqual(failure.returncode, 2)
        self.assertFalse((WORK / "cli_absent_output").exists())


# Individually named checks make edge-case failures visible in the saved log.
INVALID_ROWS = {
    "field_count": "0,0,1,1,1,1,0",
    "extra_field": "0,0,1,1,1,1,0,0,9",
    "empty_field": "0,0,1,,1,1,0,0",
    "nonnumeric": "bad,0,1,1,1,1,0,0",
    "nan": "NaN,0,1,1,1,1,0,0",
    "infinity": "0,0,Infinity,1,1,1,0,0",
    "fractional_category": "0,0,1,1,1,1.5,0,0",
    "fractional_attribute": "0,0,1,1,1,1,0,0.5",
    "invalid_score": "0,0,1,1,2,1,0,0",
    "fractional_score": "0,0,1,1,0.5,1,0,0",
    "negative_category": "0,0,1,1,1,-1,0,0",
    "large_category": "0,0,1,1,1,12,0,0",
    "negative_x": "-1,0,1,1,1,1,0,0",
    "negative_y": "0,-1,1,1,1,1,0,0",
    "beyond_right": "99,0,2,1,1,1,0,0",
    "beyond_bottom": "0,99,1,2,1,1,0,0",
    "ignored_outside": "101,0,1,1,0,0,0,0",
    "blank_middle": "0,0,1,1,1,1,0,0\n\n0,0,1,1,1,1,0,0",
    "underflow": "0,0,1e-400,1e-400,1,1,0,0",
}


def invalid_check(raw):
    def test(self):
        with self.assertRaises(AnnotationError):
            convert_text(raw, 100, 100)
    return test


for name, row in INVALID_ROWS.items():
    setattr(AdapterChecks, "test_reject_" + name, invalid_check(row))


def excluded_check(category, score, reason):
    def test(self):
        labels, rows = convert_text(f"0,0,1,1,{score},{category},0,0", 100, 100)
        self.assertEqual(labels, "")
        self.assertIn(reason, rows[0]["reasons"])
    return test


for category in range(12):
    setattr(AdapterChecks, f"test_score_zero_category_{category:02d}", excluded_check(category, 0, "score_zero"))
for category, reason in [(0, "ignore_category"), (11, "others_category")]:
    setattr(AdapterChecks, f"test_score_one_non_target_{category}", excluded_check(category, 1, reason))


def dimension_check(width, height):
    def test(self):
        with self.assertRaises(AnnotationError):
            convert_text("", width, height)
    return test


for name, dims in {"zero": (0, 100), "negative": (100, -1), "float": (100.5, 100), "boolean": (True, 100)}.items():
    setattr(AdapterChecks, "test_dimensions_" + name, dimension_check(*dims))


def main():
    global WORK
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    WORK = args.output.resolve()
    allowed = OUTPUT_ROOT.resolve()
    if WORK == allowed or not WORK.is_relative_to(allowed):
        parser.error("Use a new output directory under processed/VisDrone")
    WORK.mkdir(parents=True, exist_ok=False)
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AdapterChecks)
    names = [test.id() for test in suite]
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    log = stream.getvalue()
    (WORK / "checks.log").write_text(log, encoding="utf-8")
    report = dict(scope="synthetic annotations and dimensions only", tests_run=result.testsRun,
                  passed=result.testsRun - len(result.failures) - len(result.errors),
                  failures=result.failures, errors=result.errors, test_names=names,
                  python=sys.version, dataset_reads=0, model_runs=0,
                  code_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                               (Path(__file__), Path(__file__).with_name("convert_visdrone_labels.py"))})
    # Failure objects are serialized as readable test identifiers plus traceback.
    for key in ("failures", "errors"):
        report[key] = [(str(test), trace) for test, trace in report[key]]
    (WORK / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(log)
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
