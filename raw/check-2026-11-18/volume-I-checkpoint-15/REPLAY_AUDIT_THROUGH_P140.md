# Mechanical replay and completion audit through printed page 140

Frozen capture: **2026-11-19 02:39:23 UTC**. The three TeX sources, correction ledger, existing-correction ledger, check record, progress log, evidence index, and replay script were captured privately. All nine files had identical hashes before capture, after capture, and in the frozen copies. The evidence/source-asset filename inventory was captured with them. All checks below use that frozen state, excluding later page 141 work.

## Exact replay and schema

**All 5,645 correction rows replay exactly onto a fresh extraction of the supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The frozen existing replay script was used unchanged and required exactly one old-text occurrence for every row.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,826 |
| corrected | 1,919 |
| English | 1,890 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,060 |
| typesetting | 2,800 |
| reading | 1,501 |
| translation | 133 |
| misprint of the original | 111 |
| terminology | 40 |

The required ten-column header is present. There are no malformed rows, empty required file/layer/old/new/evidence/kind/confidence fields, or unknown correction kinds.

## Explicit evidence references

All **1,245 explicit image/PDF paths** extracted from the two ledgers’ evidence fields and from `CHECK_RECORD.md` and `EVIDENCE_INDEX.md` resolve in the captured evidence/source-asset filename inventory. No missing explicit reference was found.

This is a path-existence check. No scan, crop, facsimile, or other image content was inspected, and a file’s existence is not treated as evidence that an editorial decision is correct.

## Completion consistency

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page records | Exactly pages 1–140 |
| Active scan-page records | Exactly scan pages 1–158 |
| Printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last completion | Page 140, 2026-11-19 02:36:04 UTC |
| Completion records/events beyond page 140 | None |
| Numeric correction rows beyond page 140 | None |

No missing or duplicate canonical page record, active scan record, or missing numeric-page completion was found. The inherited premature page-27 entry remains explicitly voided, and its duplicate historical completion event is preserved. The active coverage counts exclude that voided entry. No page-141 completion is inferred from later workspace activity.

## Anchor and page-marker inventory

Literal identifiers were extracted from label, hyperlink-target, bookmark, and source-page-marker commands, excluding macro-parameter placeholders. The following counts apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. The inherited front-target additions and source-position changes remain unchanged. This lexical inventory does not expand TeX or validate compiled links.

## Preserved top-summary lag

The top-summary block remains at the checkpoint-11 state of **5,604** rows; the frozen ledger contains **5,645**, a difference of **41**:

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,816 | 1,826 | +10 |
| corrected | 1,905 | 1,919 | +14 |
| English | 1,873 | 1,890 | +17 |
| build | 10 | 10 | +0 |
| **Total** | **5,604** | **5,645** | **+41** |

The primary reader’s established procedure refreshes top totals/status before timed checkpoints. This report identifies the frozen difference without refreshing or changing the summary. The individual page records, ledger, and completion timestamps agree on the completed-page boundary.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,591 | `40a945432cdfeb7f960ef9ef942c7b28e9c881ca8796014eab0ff5ad31bfcaff` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,455 | `d515368f0b06da9310705d21fd602499d91288d390764806a3fced80d66ded37` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,743 | `892baa627848890bbee4fa7aa264da597975a5db251b74009c648258d218a9e8` |

## Scope and handling

This is a mechanical exact-replay, schema, explicit-path, anchor-inventory, and completion-metadata audit. It is **not a visual reading**, textual or mathematical verdict, translation review, second reading of correction evidence, or build/PDF certification. Completion metadata remains the primary reader’s account of review performed.

No active file was changed. In particular, sources, correction rows, verdicts, check records, questions, progress/status, prior reports, and checkpoints remain untouched by this audit. No Volume II material was read. This report was first written outside the active audit tree for the primary reader’s review before installation. No ZIP was created.
