# Correction queue for the final second reading

`correction_review_queue.py` prepares a mechanical, unreviewed queue from a frozen `CORRECTIONS.tsv`. Run it **after the primary has completed the first reading of all Volume I pages**. It reads the ledger only; it does not open source files, evidence files, scans, or images. It writes into a caller-selected fresh scratch directory, never the active deliverable tree.

The queue does not perform, certify, or replace the primary's mandatory final second reading. It adds no verdict, confidence adjustment, or review/completion mark.

## Command

From this deliverable directory, after the first reading is complete and the ledger is frozen (create the sibling scratch parent directory first):

```sh
python3 -B scripts/correction_review_queue.py \
  --ledger CORRECTIONS.tsv \
  --output-dir ../scratch/volume_I_final_second_reading_queue
```

The output directory must not exist, its parent must exist, and it must be outside the ledger's parent tree. A later generation requires another fresh directory. The script uses Python 3.10 or newer and only the standard library. It has no scheduler, checkpoint, upload, source-editing, or ledger-writing action.

## What is preserved and how rows are ordered

Every logical data row is included, without filtering by run, confidence, kind, layer, or any other value. Identical rows remain separate. The current supplied ledger has no explicit run column; the generator does not infer which run produced a row. Retaining every row includes both runs already recorded in the ledger.

Every original column stays in its original order, with every field string preserved exactly, including `old`, `new`, `evidence`, `kind`, and `confidence`. Embedded tabs, LF/CRLF, quotes, Unicode, empty strings, and surrounding whitespace remain field values. UTF-8 input with or without an initial BOM is accepted. The output is UTF-8 TSV with every cell quoted and LF record separators; TSV quoting and outer record separators may differ from the input. No spreadsheet escaping or Unicode normalization is applied to original values.

Ordering is:

1. Canonical Roman page labels in numerical order, for the front matter.
2. Decimal page labels in numerical order.
3. Original logical data-row index for ties.

Whitespace and Roman case are ignored only when deriving the sort key. The original `printed_page` cell is unchanged. Unsupported page labels cause the whole generation to fail before publication; the generator does not silently omit a row or guess how to place a range or a global label. If later ledger records introduce such labels, review and extend the explicit ordering policy before generating the final queue.

## Output files and appended columns

`correction_review_queue.tsv` contains all original columns followed by:

| Column | Meaning |
|---|---|
| `queue_index` | One-based position after sorting. |
| `original_row_index` | One-based logical data-record position after the original header, not a physical line number. Quoted multiline cells do not change this index. |
| `original_row_sha256` | Stable digest of the original header and exact original field strings, defined below. |
| `evidence_file_refs_json` | Ordered unique filename-like reference candidates extracted from the original evidence cell. |
| `evidence_filenames_json` | Ordered unique basenames of those candidates. |

`correction_review_manifest.json` records the input raw-byte size and SHA-256, output TSV size and SHA-256, original schema, ordering/digest definitions, exact-label row counts, layer/kind/confidence counts, any supplied run-column counts, duplicate-content counts, and evidence-extraction coverage. Paths in the manifest are filenames only. It records no editorial verdict or review status. A header-only input produces a zero-row queue and corresponding metadata; that is not a completion statement.

Coverage counts describe records in the correction ledger. A page without a correction row cannot be classified as read, unread, correct, or reviewed from this queue.

## Row digest definition

For each original row, compute UTF-8 bytes from:

```python
json.dumps(
    ["illusie-correction-row-v1", original_header_array, exact_original_cell_array],
    ensure_ascii=False,
    separators=(",", ":"),
    allow_nan=False,
)
```

`original_row_sha256` is the lowercase hexadecimal SHA-256 of those bytes. The digest includes the original schema order and every original field, including any additional columns. It excludes both row indices and every generated field. Reordering records therefore preserves their content digests; identical-content rows share a digest but retain distinct original indices. The input file SHA-256 together with `original_row_index` identifies provenance within a particular ledger snapshot. The digest authenticates decoded field values, not the input TSV's particular quote syntax or outer newline convention.

## Evidence reference extraction

The extractor recognizes common image, PDF, text, TeX, JSON/JSONL, table, log, and ZIP suffixes, case-insensitively. The manifest lists the exact supported suffixes. Plain references, Markdown link targets, and quoted/backtick/angle-bracket references are supported; these wrappers allow spaces and parentheses in a reference. Extracted query/fragment suffixes are omitted. Repeated reference strings within one evidence cell are reduced to their first occurrence; this never deduplicates ledger rows or modifies the original evidence cell.

These are mechanical filename candidates. Unusual syntax can produce misses, and quoted prose ending in a recognized suffix can produce a false positive. The original evidence string is always available beside the extracted fields. No reference is resolved, opened, checked for existence, or judged sufficient; those tasks belong to the primary's actual reading.

## Input and output safeguards

Duplicate/empty headers, missing required fields, malformed TSV, inconsistent cell counts, metadata-column name collisions, invalid UTF-8, and unsupported page labels fail explicitly. A completely blank physical record is rejected as a zero-cell data record; quoted empty cells remain valid values. A changed ledger snapshot is rejected before publication. Output directories and files are created exclusively and never overwritten; the manifest is written last. No output is published during input validation. Generation should occur with the final ledger frozen.

The script and fixture checks are staged for primary review. No queue has been generated from the active Illusie ledger by this infrastructure task, and no page or correction has been marked reviewed.

Primary installation note: generator, synthetic test source, README and validation report were read in full before installation. No active review queue has been generated. The validation report retains the original staging command and tested file hashes; installed code bytes are unchanged.
