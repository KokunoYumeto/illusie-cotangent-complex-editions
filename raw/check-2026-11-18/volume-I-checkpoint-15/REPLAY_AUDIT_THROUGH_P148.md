# Mechanical replay and completion audit through printed page 148

Frozen capture: **2026-11-19 02:58:27 UTC**. The three TeX sources, correction ledger, existing-correction ledger, check record, progress log, evidence index, and replay script were copied into a private snapshot. All nine file hashes agreed before capture, after capture, and in the copied files. An evidence/source-asset filename inventory was captured with them. The primary reader resumed page 149 after capture; later mutations are excluded from this report.

## Exact replay and schema

**All 5,804 correction rows replay exactly onto a fresh extraction of the supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The frozen existing replay script was used unchanged; each recorded replacement had to find exactly one occurrence of its old text.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,875 |
| corrected | 1,979 |
| English | 1,940 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,114 |
| typesetting | 2,875 |
| reading | 1,525 |
| translation | 133 |
| misprint of the original | 113 |
| terminology | 44 |

The ten-column schema matches the required header. No malformed row, empty required file/layer/old/new/evidence/kind/confidence field, or unknown correction kind was found.

## Explicit evidence references

All **1,325 explicit image/PDF paths** extracted from the two ledgers’ evidence fields, `CHECK_RECORD.md`, and `EVIDENCE_INDEX.md` resolve in the captured evidence/source-asset filename inventory. There are no missing explicit references.

This check establishes filename existence only. No scan, crop, facsimile, or mathematical text was inspected, and existence is not treated as a validation of the evidence’s editorial interpretation.

## Completion consistency

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page records | Exactly pages 1–148 |
| Active scan-page records | Exactly scan pages 1–166 |
| Printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last completion | Page 148, 2026-11-19 02:58:15 UTC |
| Completion records/events beyond page 148 | None |
| Numeric correction rows beyond page 148 | None |

No missing or duplicate canonical page record, active scan record, or missing numeric-page completion was found. The explicitly voided premature page-27 entry and its historical duplicate completion event remain preserved. The active scan count excludes that voided entry. No page-149 completion is inferred.

## Anchor and page-marker preservation

Literal identifiers were extracted from label, hyperlink-target, bookmark, and source-page-marker commands; macro-parameter placeholders containing `#` were excluded. Counts below apply to each of the three layers:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence remains identical to checkpoint 09 in all three layers.** No original identifier occurrence is missing. The inherited front-target additions, target-position changes, and cover duplicate remain baseline exceptions, not new changes. This lexical inventory does not expand TeX or validate compiled links.

## Preserved top-summary lag

The top summary remains at **5,604** changes, the checkpoint-11 state. The frozen ledger contains **5,804**, a difference of **200**:

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,816 | 1,875 | +59 |
| corrected | 1,905 | 1,979 | +74 |
| English | 1,873 | 1,940 | +67 |
| build | 10 | 10 | +0 |
| **Total** | **5,604** | **5,804** | **+200** |

The primary reader’s established procedure refreshes top totals/status before timed checkpoints. This audit reports the frozen difference and makes no refresh. The individual page records, current ledger, and completion timestamps agree on the completed-page boundary.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,051 | `59e89be67c7729040bd636ee5ae31a3b1df9c89930c99fcb70d743b76de33452` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,565,938 | `bdddd9f2cdf061d3e04a964588d1fdc13ee0303676d6507b54ad22bf4ec36a6f` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,176 | `761a6d5de018efad07d68ec0426f95ee46d84460b9c4d41b66d77cdf8122dde9` |

## Scope and handling

This is a mechanical exact-replay, schema, explicit-path, identifier-inventory, and completion-metadata audit. It is **not a visual reading**, textual or mathematical verdict, translation review, second reading of correction evidence, or build/PDF certification. Completion metadata remains the primary reader’s account of review performed.

No active source, correction row, verdict, report, question, progress/status record, checkpoint, or other active file was changed by this audit. No pages were marked complete. No Volume II material was read. This report was first written in staging for review and authorized installation by the primary reader. No ZIP was created or modified.
