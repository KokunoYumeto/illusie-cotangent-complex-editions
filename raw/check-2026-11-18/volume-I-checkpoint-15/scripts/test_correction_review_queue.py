"""Synthetic-only checks for the staged correction queue generator.

Run with: python3 -B tmp/infrastructure/test_correction_review_queue.py
This file never reads the active Illusie ledger, source trees, or evidence.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).with_name("correction_review_queue.py")
SPEC = importlib.util.spec_from_file_location("synthetic_queue_generator", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
GENERATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GENERATOR
SPEC.loader.exec_module(GENERATOR)

HEADERS = [
    "file", "layer", "printed_page", "line", "statement", "old", "new",
    "evidence", "kind", "confidence",
]
APPENDED = [
    "queue_index", "original_row_index", "original_row_sha256",
    "evidence_file_refs_json", "evidence_filenames_json",
]


def synthetic_row(page: str, tag: str = "sample") -> list[str]:
    return [
        "sources/synthetic.tex", "synthetic-layer", page, "1", tag,
        "old " + tag, "new " + tag, "evidence/nonexistent.png",
        "reading", "unmodified confidence",
    ]


def independent_digest(headers: list[str], values: list[str]) -> str:
    text = json.dumps(
        ["illusie-correction-row-v1", headers, values], ensure_ascii=False,
        separators=(",", ":"), allow_nan=False,
    )
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class QueueFixtures(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(
            prefix="synthetic-queue-check-", dir=SCRIPT.parent,
        )
        self.base = Path(self.temporary.name)
        self.inputs = self.base / "inputs"
        self.inputs.mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def ledger(
        self, rows: list[list[str]], headers: list[str] | None = None,
        name: str = "synthetic.tsv", bom: bool = False,
    ) -> Path:
        buffer = io.StringIO(newline="")
        writer = csv.writer(buffer, delimiter="\t", lineterminator="\r\n",
                            quoting=csv.QUOTE_ALL)
        writer.writerow(HEADERS if headers is None else headers)
        writer.writerows(rows)
        data = buffer.getvalue().encode("utf-8")
        if bom:
            data = b"\xef\xbb\xbf" + data
        path = self.inputs / name
        path.write_bytes(data)
        return path

    def invoke(self, ledger: Path, output: Path, success: bool = True) -> subprocess.CompletedProcess:
        before = ledger.read_bytes()
        result = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--ledger", str(ledger),
             "--output-dir", str(output)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(ledger.read_bytes(), before, "Generator changed its input bytes")
        self.assertEqual(result.returncode, 0 if success else 2,
                         msg=result.stderr or result.stdout)
        self.assertNotIn("Traceback", result.stderr)
        return result

    def output(self, directory: Path) -> tuple[list[str], list[list[str]], dict]:
        csv.field_size_limit(1_000_000)
        with (directory / "correction_review_queue.tsv").open(
            encoding="utf-8", newline="",
        ) as stream:
            parsed = list(csv.reader(stream, delimiter="\t", strict=True))
        manifest = json.loads((directory / "correction_review_manifest.json").read_text())
        return parsed[0], parsed[1:], manifest

    def assert_original_cells(
        self, original_headers: list[str], originals: list[list[str]],
        output_headers: list[str], output_rows: list[list[str]],
    ) -> None:
        self.assertEqual(output_headers, original_headers + APPENDED)
        n = len(original_headers)
        self.assertEqual(len(output_rows), len(originals))
        self.assertEqual([int(row[n]) for row in output_rows], list(range(1, len(originals) + 1)))
        self.assertEqual(sorted(int(row[n + 1]) for row in output_rows),
                         list(range(1, len(originals) + 1)))
        for row in output_rows:
            original_index = int(row[n + 1])
            self.assertEqual(row[:n], originals[original_index - 1])
            self.assertEqual(row[n + 2], independent_digest(original_headers, row[:n]))

    def test_sorting_ties_duplicates_and_both_explicit_runs(self) -> None:
        headers = HEADERS + ["audit_run"]
        labels = ["X", "10", "III", "2", "IX", "02", " 2 ", "2", "iii"]
        rows = [synthetic_row(page, str(i)) + ["earlier" if i % 2 else "later"]
                for i, page in enumerate(labels, 1)]
        rows[7] = rows[3].copy()
        ledger = self.ledger(rows, headers)
        output = self.base / "ordered"
        self.invoke(ledger, output)
        names, data, manifest = self.output(output)
        self.assert_original_cells(headers, rows, names, data)
        n = len(headers)
        self.assertEqual([int(row[n + 1]) for row in data], [3, 9, 5, 1, 4, 6, 7, 8, 2])
        self.assertEqual(manifest["coverage"]["input_rows"], 9)
        self.assertEqual(manifest["coverage"]["output_rows"], 9)
        self.assertEqual(manifest["coverage"]["duplicate_content_row_instances"], 1)
        self.assertEqual(sum(manifest["coverage"]["by_audit_run"].values()), 9)
        by_original = {int(row[n + 1]): row for row in data}
        self.assertEqual(by_original[4][n + 2], by_original[8][n + 2])

    def test_exact_cells_bom_newlines_unicode_extra_columns(self) -> None:
        headers = HEADERS + ["extra", "empty_extra"]
        unusual = ' leading\t"quoted"\nLF\r\nCRLF\rCR e\u0301 Ω 😀 trailing '
        row = synthetic_row(" iii ") + ['=synthetic_formula_text', ""]
        for name in ["old", "new", "evidence", "kind", "confidence"]:
            row[headers.index(name)] = unusual + " " + name
        row[headers.index("line")] = ""
        row[headers.index("statement")] = " leading and trailing "
        ledger = self.ledger([row], headers, bom=True)
        raw = ledger.read_bytes()
        output = self.base / "exact"
        self.invoke(ledger, output)
        names, data, manifest = self.output(output)
        self.assert_original_cells(headers, [row], names, data)
        self.assertTrue(manifest["input"]["utf8_bom_present"])
        self.assertEqual(manifest["input"]["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(manifest["input"]["columns"], headers)
        self.assertEqual(manifest["coverage"]["by_confidence"], {row[9]: 1})
        self.assertEqual(set(names) - set(headers), set(APPENDED))
        queue = (output / "correction_review_queue.tsv").read_bytes()
        self.assertEqual(manifest["queue"]["bytes"], len(queue))
        self.assertEqual(manifest["queue"]["sha256"], hashlib.sha256(queue).hexdigest())
        self.assertNotIn("by_run", manifest["coverage"])

    def test_independent_known_digest_vector(self) -> None:
        headers = ["printed_page", "old", "new", "evidence", "kind", "confidence"]
        values = ["2", "a", "b", "", "reading", "high"]
        expected = "f80282f16cf74ced452c0f39d536407df1a8dc036cc0df8c4b0205a10978f817"
        self.assertEqual(independent_digest(headers, values), expected)
        self.assertEqual(GENERATOR.original_row_digest(headers, values), expected)
        changed = values.copy()
        changed[2] = "B"
        self.assertNotEqual(GENERATOR.original_row_digest(headers, changed), expected)
        self.assertNotEqual(GENERATOR.original_row_digest(headers[::-1], values[::-1]), expected)

    def test_digest_mutation_reordering_and_repeatability(self) -> None:
        rows = [synthetic_row("2", "first"), synthetic_row("2", "second"), synthetic_row("1", "third")]
        ledger = self.ledger(rows)
        self.invoke(ledger, self.base / "first")
        self.invoke(ledger, self.base / "repeat")
        self.assertEqual((self.base / "first/correction_review_queue.tsv").read_bytes(),
                         (self.base / "repeat/correction_review_queue.tsv").read_bytes())
        _, original, first_manifest = self.output(self.base / "first")
        reversed_ledger = self.ledger(rows[::-1], name="reordered.tsv")
        self.invoke(reversed_ledger, self.base / "reordered")
        _, reordered, reordered_manifest = self.output(self.base / "reordered")
        n = len(HEADERS)
        self.assertEqual(sorted(row[n + 2] for row in original), sorted(row[n + 2] for row in reordered))
        self.assertNotEqual(first_manifest["input"]["sha256"], reordered_manifest["input"]["sha256"])
        mutated = [row.copy() for row in rows]
        mutated[1][6] += " modified"
        changed_ledger = self.ledger(mutated, name="changed.tsv")
        self.invoke(changed_ledger, self.base / "changed")
        _, changed, _ = self.output(self.base / "changed")
        old_by_index = {row[n + 1]: row[n + 2] for row in original}
        new_by_index = {row[n + 1]: row[n + 2] for row in changed}
        self.assertEqual([index for index in old_by_index if old_by_index[index] != new_by_index[index]], ["2"])

    def test_evidence_plain_quoted_markdown_spaces_queries(self) -> None:
        evidence = (
            'evidence/plain.png; `evidence/crop space (one).PNG` '
            '[link](evidence/linked.pdf?download=1#page=2) evidence/plain.png '
            '"evidence/quoted space.jpg" [wide](<evidence/angle space.png>) '
            'https://example.test/view.png?download=other.pdf#crop'
        )
        row = synthetic_row("1")
        row[7] = evidence
        ledger = self.ledger([row])
        self.invoke(ledger, self.base / "refs")
        names, rows, manifest = self.output(self.base / "refs")
        expected = [
            "evidence/plain.png", "evidence/crop space (one).PNG", "evidence/linked.pdf",
            "evidence/quoted space.jpg", "evidence/angle space.png", "https://example.test/view.png",
        ]
        self.assertEqual(rows[0][7], evidence)
        self.assertEqual(json.loads(rows[0][names.index("evidence_file_refs_json")]), expected)
        self.assertEqual(json.loads(rows[0][names.index("evidence_filenames_json")]),
                         ["plain.png", "crop space (one).PNG", "linked.pdf", "quoted space.jpg", "angle space.png", "view.png"])
        self.assertFalse(manifest["evidence_extraction"]["references_resolved_or_opened"])
        self.assertEqual(manifest["evidence_extraction"]["unique_reference_candidates"], 6)

    def test_schema_and_label_failures_publish_nothing(self) -> None:
        cases = [
            ("duplicate", HEADERS + ["old"], synthetic_row("1") + ["duplicate"]),
            ("empty_header", HEADERS + [""], synthetic_row("1") + ["empty header"]),
            ("missing", [name for name in HEADERS if name != "confidence"], synthetic_row("1")[:-1]),
            ("collision", HEADERS + ["queue_index"], synthetic_row("1") + ["1"]),
            ("short", HEADERS, synthetic_row("1")[:-1]),
            ("long", HEADERS, synthetic_row("1") + ["extra"]),
            ("roman_noncanonical", HEADERS, synthetic_row("IVI")),
            ("range", HEADERS, synthetic_row("1-2")),
            ("empty_page", HEADERS, synthetic_row("")),
            ("global", HEADERS, synthetic_row("global")),
        ]
        for name, headers, row in cases:
            with self.subTest(name=name):
                ledger = self.ledger([row], headers, name=name + ".tsv")
                output = self.base / ("out_" + name)
                self.invoke(ledger, output, success=False)
                self.assertFalse(output.exists())

    def test_invalid_utf8_malformed_tsv_blank_record_and_empty_input(self) -> None:
        valid = self.ledger([synthetic_row("1")]).read_bytes()
        header_only = self.ledger([], name="header.tsv").read_bytes()
        samples = {
            "utf8": header_only + b"\xff\r\n",
            "malformed": header_only + b'"unterminated\r\n',
            "blank_record": valid + b"\r\n",
            "empty": b"",
        }
        for name, raw in samples.items():
            with self.subTest(name=name):
                ledger = self.inputs / (name + ".tsv")
                ledger.write_bytes(raw)
                output = self.base / ("reject_" + name)
                self.invoke(ledger, output, success=False)
                self.assertFalse(output.exists())

    def test_no_overwrite_or_output_inside_input_tree(self) -> None:
        ledger = self.ledger([synthetic_row("1")])
        existing = self.base / "existing"
        existing.mkdir()
        sentinel = existing / "keep.txt"
        sentinel.write_text("unchanged synthetic sentinel")
        self.invoke(ledger, existing, success=False)
        self.assertEqual(sentinel.read_text(), "unchanged synthetic sentinel")
        self.assertEqual(sorted(path.name for path in existing.iterdir()), ["keep.txt"])
        inside = self.inputs / "queue"
        self.invoke(ledger, inside, success=False)
        self.assertFalse(inside.exists())
        self.invoke(ledger, self.inputs, success=False)
        self.invoke(ledger, ledger, success=False)
        missing_parent = self.base / "absent" / "queue"
        self.invoke(ledger, missing_parent, success=False)
        self.assertFalse(missing_parent.parent.exists())

    def test_header_only_coverage_and_large_field(self) -> None:
        empty = self.ledger([], name="zero.tsv")
        self.invoke(empty, self.base / "zero")
        names, rows, manifest = self.output(self.base / "zero")
        self.assertEqual(names, HEADERS + APPENDED)
        self.assertEqual(rows, [])
        self.assertEqual(manifest["coverage"]["input_rows"], 0)
        self.assertEqual(manifest["coverage"]["output_rows"], 0)
        self.assertEqual(manifest["coverage"]["printed_page_rows"], [])
        row = synthetic_row("1")
        row[5] = "x" * 200_000
        large = self.ledger([row], name="large.tsv")
        self.invoke(large, self.base / "large")
        names, rows, _ = self.output(self.base / "large")
        self.assert_original_cells(HEADERS, [row], names, rows)

    def test_detected_input_change_and_write_failure_leave_no_output(self) -> None:
        ledger = self.ledger([synthetic_row("1")])
        raw = ledger.read_bytes()
        fingerprint = GENERATOR.fingerprint(ledger)
        changed = (*fingerprint[:-1], fingerprint[-1] + 1)
        output = self.base / "changed_during_read"
        with mock.patch.object(GENERATOR, "fingerprint", side_effect=[fingerprint, changed]):
            with self.assertRaises(GENERATOR.QueueError):
                GENERATOR.generate(ledger, output)
        self.assertFalse(output.exists())
        original_open = Path.open

        def fail_manifest(path: Path, mode: str = "r", *args, **kwargs):
            if path.name == "correction_review_manifest.json" and mode == "xb":
                raise OSError(5, "synthetic I/O failure")
            return original_open(path, mode, *args, **kwargs)

        output = self.base / "failed_publication"
        with mock.patch.object(Path, "open", fail_manifest):
            with self.assertRaises(OSError):
                GENERATOR.generate(ledger, output)
        self.assertFalse(output.exists())
        self.assertEqual(ledger.read_bytes(), raw)


if __name__ == "__main__":
    unittest.main(verbosity=2)
