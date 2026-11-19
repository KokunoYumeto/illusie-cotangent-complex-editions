#!/usr/bin/env python3
"""Prepare an unreviewed, lossless correction queue from one frozen ledger.

Standard library only. The input is read-only. No evidence or source files are
opened. Run after the primary has completed the first reading of Volume I.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
from typing import Sequence


QUEUE_NAME = "correction_review_queue.tsv"
MANIFEST_NAME = "correction_review_manifest.json"
SCHEMA_VERSION = "correction-review-queue/v1"
ROW_DIGEST_DOMAIN = "illusie-correction-row-v1"
REQUIRED_COLUMNS = {"printed_page", "old", "new", "evidence", "kind", "confidence"}
ADDED_COLUMNS = [
    "queue_index",
    "original_row_index",
    "original_row_sha256",
    "evidence_file_refs_json",
    "evidence_filenames_json",
]
EVIDENCE_EXTENSIONS = (
    "png", "jpg", "jpeg", "tif", "tiff", "webp", "bmp", "gif", "svg",
    "pdf", "tex", "txt", "md", "tsv", "csv", "json", "jsonl", "log", "zip",
)
_EXT = "(?:" + "|".join(sorted(EVIDENCE_EXTENSIONS, key=len, reverse=True)) + ")"
_ROMAN = re.compile(r"M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})\Z")
_QUOTED_OR_BARE = re.compile(
    r"(?P<quoted>`[^`\r\n]*`|\"[^\"\r\n]*\"|'[^'\r\n]*'|<[^>\r\n]*>)"
    r"|(?<![^\s<>\"'`\[\]{}(),;|=*])(?P<bare>[^\s<>\"'`\[\]{}(),;|=*]+?\." + _EXT + r")"
    r"(?:[?#][^\s<>\"'`\[\]{}()*]*)?"
    r"(?=$|[\s<>\"'`\[\]{}(),;|?#:=*]|[.!](?=\s|$))",
    re.IGNORECASE,
)
_QUOTED_REFERENCE = re.compile(
    r"(?P<reference>[^\r\n<>]+?\." + _EXT + r")(?:[?#][^\r\n]*)?\Z",
    re.IGNORECASE,
)


class QueueError(Exception):
    """A validation failure with a deliberately path-free message."""


@dataclass(frozen=True)
class LedgerRow:
    original_index: int
    values: tuple[str, ...]
    page_key: tuple[int, int]
    digest: str
    references: tuple[str, ...]
    filenames: tuple[str, ...]


def compact_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def original_row_digest(headers: Sequence[str], values: Sequence[str]) -> str:
    """Hash schema plus exact cells, independent of index and TSV quoting."""
    canonical = compact_json([ROW_DIGEST_DOMAIN, list(headers), list(values)])
    return sha256_bytes(canonical.encode("utf-8"))


def printed_page_key(label: str, row_index: int) -> tuple[int, int]:
    """Sort canonical Roman labels before decimal labels; preserve raw cells."""
    value = label.strip()
    if re.fullmatch(r"[0-9]+", value):
        return 1, int(value)
    roman = value.upper()
    if roman and _ROMAN.fullmatch(roman):
        numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        previous = 0
        for char in reversed(roman):
            current = numbers[char]
            result += -current if current < previous else current
            previous = max(previous, current)
        return 0, result
    raise QueueError(
        f"Unsupported printed_page label at original row {row_index}; "
        "expected a canonical Roman or decimal label. No rows were omitted."
    )


def ordered_unique(values: Sequence[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def extract_evidence_references(value: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Extract filename-like spans only; never resolve or open a reference.

    Backticks/quotes/angle brackets permit spaces and parentheses. Plain
    references and Markdown link targets use the same token matcher. Query/fragment suffixes
    are omitted from extracted references, but the original evidence cell is
    retained exactly in the output. These are mechanical candidates, not an
    evidence-validity finding.
    """
    candidates: list[str] = []
    for match in _QUOTED_OR_BARE.finditer(value):
        quoted = match.group("quoted")
        if quoted is not None:
            interior = quoted[1:-1].strip()
            reference = _QUOTED_REFERENCE.fullmatch(interior)
            if reference:
                candidates.append(reference.group("reference"))
            else:
                nested, _ = extract_evidence_references(interior)
                candidates.extend(nested)
        else:
            candidates.append(match.group("bare"))
    references = ordered_unique(candidates)
    filenames = ordered_unique([re.split(r"[/\\]", ref)[-1] for ref in references])
    return references, filenames


def read_ledger(raw: bytes) -> tuple[list[str], list[LedgerRow]]:
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise QueueError("The ledger is not valid UTF-8; no output was published.") from exc
    # A large correction can legitimately exceed csv's conservative default.
    csv.field_size_limit(min(sys.maxsize, max(131_072, len(raw))))
    reader = csv.reader(io.StringIO(text, newline=""), delimiter="\t", strict=True)
    try:
        headers = next(reader)
    except StopIteration as exc:
        raise QueueError("The ledger has no header.") from exc
    except csv.Error as exc:
        raise QueueError("The ledger header is malformed TSV.") from exc
    if not headers or any(not header for header in headers):
        raise QueueError("The ledger contains an empty header name.")
    if len(set(headers)) != len(headers):
        raise QueueError("The ledger contains duplicate header names.")
    if not REQUIRED_COLUMNS.issubset(headers):
        raise QueueError("The ledger is missing one or more required original columns.")
    if set(headers).intersection(ADDED_COLUMNS):
        raise QueueError("An original header conflicts with a generated metadata column.")
    page_column = headers.index("printed_page")
    evidence_column = headers.index("evidence")
    rows: list[LedgerRow] = []
    try:
        for index, cells in enumerate(reader, 1):
            if len(cells) != len(headers):
                raise QueueError(f"Original row {index} has the wrong number of TSV cells.")
            key = printed_page_key(cells[page_column], index)
            references, filenames = extract_evidence_references(cells[evidence_column])
            rows.append(LedgerRow(
                index, tuple(cells), key, original_row_digest(headers, cells),
                references, filenames,
            ))
    except csv.Error as exc:
        raise QueueError("A ledger data record is malformed TSV.") from exc
    return headers, rows


def create_queue_bytes(headers: Sequence[str], rows: Sequence[LedgerRow]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_ALL)
    writer.writerow([*headers, *ADDED_COLUMNS])
    for queue_index, row in enumerate(rows, 1):
        writer.writerow([
            *row.values, str(queue_index), str(row.original_index), row.digest,
            compact_json(list(row.references)), compact_json(list(row.filenames)),
        ])
    return stream.getvalue().encode("utf-8")


def coverage_counts(headers: Sequence[str], rows: Sequence[LedgerRow]) -> dict[str, object]:
    page_column = headers.index("printed_page")
    page_counts = Counter(row.values[page_column] for row in rows)
    label_keys = {row.values[page_column]: row.page_key for row in rows}
    first_indices: dict[str, int] = {}
    for row in rows:
        first_indices.setdefault(row.values[page_column], row.original_index)
    labels = sorted(page_counts, key=lambda value: (*label_keys[value], first_indices[value]))
    result: dict[str, object] = {
        "input_rows": len(rows),
        "output_rows": len(rows),
        "distinct_row_digests": len({row.digest for row in rows}),
        "duplicate_content_row_instances": len(rows) - len({row.digest for row in rows}),
        "distinct_printed_page_labels": len(page_counts),
        "printed_page_rows": [
            {"printed_page": label, "label_class": "roman" if label_keys[label][0] == 0 else "arabic",
             "numeric_order": label_keys[label][1], "rows": page_counts[label]}
            for label in labels
        ],
    }
    for name in ("layer", "kind", "confidence", "run", "audit_run", "review_run", "pass"):
        if name in headers:
            position = headers.index(name)
            result["by_" + name] = dict(sorted(Counter(row.values[position] for row in rows).items()))
    return result


def make_manifest(
    input_name: str, raw: bytes, headers: Sequence[str], rows: Sequence[LedgerRow], queue: bytes,
) -> bytes:
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "input": {
            "filename": input_name, "bytes": len(raw), "sha256": sha256_bytes(raw),
            "encoding": "UTF-8", "utf8_bom_present": raw.startswith(b"\xef\xbb\xbf"),
            "columns": list(headers),
        },
        "queue": {
            "filename": QUEUE_NAME, "bytes": len(queue), "sha256": sha256_bytes(queue),
            "original_columns_preserved_in_order": True, "appended_columns": ADDED_COLUMNS,
            "format": "UTF-8 TSV; all cells quoted; record terminator LF; embedded cell newlines preserved",
        },
        "ordering": {
            "primary": "Canonical Roman labels numerically, then decimal labels numerically",
            "tie_breaker": "Original logical data-row index, 1-based after the header",
            "label_parsing": "Whitespace ignored only for sorting; Roman case ignored only for sorting; original cell unchanged",
            "unsupported_label_policy": "Refuse the whole generation; never omit or guess a row",
            "selection": "Every input data row; no run filtering and no deduplication",
            "run_assignment": "No run is inferred; any supplied run-related columns are preserved and counted",
        },
        "row_digest": {
            "algorithm": "SHA-256",
            "canonicalization": 'UTF-8 of json.dumps([domain, original_header_array, exact_cell_array], ensure_ascii=False, separators=(",", ":"), allow_nan=False)',
            "domain": ROW_DIGEST_DOMAIN,
            "indices_included": False,
            "meaning": "Exact field strings and header order; independent of TSV quote syntax and row position",
            "provenance_identity": "Input raw SHA-256 plus original_row_index; identical-content rows may share a row digest",
        },
        "coverage": coverage_counts(headers, rows),
        "evidence_extraction": {
            "supported_extensions": list(EVIDENCE_EXTENSIONS),
            "rows_with_filename_candidates": sum(bool(row.references) for row in rows),
            "rows_without_filename_candidates": sum(not row.references for row in rows),
            "unique_reference_candidates": len({value for row in rows for value in row.references}),
            "unique_filename_candidates": len({value for row in rows for value in row.filenames}),
            "policy": "Case-insensitive extensions; first-occurrence order; duplicate reference strings removed within a row; query/fragment removed only from extracted candidates",
            "limitations": "Heuristic filename-like spans; quoted/backtick/angle-bracket spans support spaces and parentheses; prose or unusual syntax can produce misses or false positives",
            "references_resolved_or_opened": False,
        },
        "limits": [
            "Coverage describes correction rows, not the completion or absence of differences on any page.",
            "No editorial verdict, confidence change, review mark, or second-reading completion is produced.",
            "The primary must still perform the actual final second reading.",
        ],
    }
    return (json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def fingerprint(path: Path) -> tuple[int, int, int, int, int]:
    stat = path.stat()
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def generate(ledger: Path, output_dir: Path) -> dict[str, int]:
    source = ledger.resolve(strict=True)
    destination = output_dir.resolve(strict=False)
    if not source.is_file():
        raise QueueError("The ledger must be a regular file.")
    if destination == source.parent or source.parent in destination.parents:
        raise QueueError("Choose a scratch output directory outside the ledger's parent tree.")
    if destination.exists():
        raise QueueError("The output directory already exists; use a fresh scratch directory.")
    if not destination.parent.is_dir():
        raise QueueError("The output directory's parent must already exist.")

    before = fingerprint(source)
    raw = source.read_bytes()
    if fingerprint(source) != before or len(raw) != before[2]:
        raise QueueError("The ledger changed while its snapshot was read; retry after freezing it.")
    headers, original_rows = read_ledger(raw)
    ordered_rows = sorted(original_rows, key=lambda row: (*row.page_key, row.original_index))
    queue = create_queue_bytes(headers, ordered_rows)
    manifest = make_manifest(source.name, raw, headers, ordered_rows, queue)
    if fingerprint(source) != before or sha256_bytes(source.read_bytes()) != sha256_bytes(raw):
        raise QueueError("The ledger changed during generation; no queue was published.")

    # Validation and serialization finish before any output directory is made.
    # Exclusive creation prevents overwriting another run's results.
    destination.mkdir(mode=0o700)
    written: list[Path] = []
    try:
        for name, data in ((QUEUE_NAME, queue), (MANIFEST_NAME, manifest)):
            path = destination / name
            with path.open("xb") as stream:
                written.append(path)
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
    except BaseException:
        for path in reversed(written):
            path.unlink(missing_ok=True)
        try:
            destination.rmdir()
        except OSError:
            pass
        raise
    return {"rows": len(ordered_rows), "queue_bytes": len(queue), "manifest_bytes": len(manifest)}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True, help="Frozen CORRECTIONS.tsv input, read-only.")
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="Fresh scratch directory outside the ledger parent tree; its parent must exist.")
    args = parser.parse_args(argv)
    try:
        result = generate(args.ledger, args.output_dir)
    except QueueError as error:
        print(f"Queue generation stopped: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"Queue generation stopped: filesystem operation failed (errno {error.errno}).", file=sys.stderr)
        return 2
    except UnicodeError:
        print("Queue generation stopped: metadata could not be encoded as UTF-8; no output was published.", file=sys.stderr)
        return 2
    print(f"Created {QUEUE_NAME} and {MANIFEST_NAME}: {result['rows']} rows; no review status recorded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
