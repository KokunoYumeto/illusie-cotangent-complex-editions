# Frozen mechanical replay and chronology audit through recorded page 157

Capture: **2026-11-19 03:28:57 UTC**. Ten source, ledger, report, checkpoint-metadata, and replay-script files were copied into a private snapshot. Their hashes agreed before capture, after capture, and in the copied files. An evidence/source-asset filename inventory was captured with them. The snapshot contains no numeric correction rows beyond page 157; subsequent page-158 work is excluded.

The primary record marks printed page 157 (scan page 175) complete. This audit checks mechanical consistency of that recorded state; it does not certify the first or second reading.

## Exact correction replay

**All 5,995 correction rows replay exactly onto a fresh extraction of the supplied original Volume I sources. All three replayed source files are byte-for-byte identical to the frozen working sources.** The frozen existing replay script was run unchanged; each replacement required exactly one old-text occurrence.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,928 |
| corrected | 2,048 |
| English | 2,009 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,168 |
| typesetting | 2,980 |
| reading | 1,542 |
| translation | 135 |
| misprint of the original | 119 |
| terminology | 51 |

The required ten-column schema is present. No malformed row, empty required file/layer/old/new/evidence/kind/confidence field, or unknown correction kind was found.

## Explicit evidence-reference existence

All **1,424 explicit image/PDF paths** extracted from the evidence fields of both ledgers, `CHECK_RECORD.md`, and `EVIDENCE_INDEX.md` resolve in the captured evidence/source-asset filename inventory. No missing explicit reference was found.

Only filename existence was checked. No scan, page image, book text, or mathematical claim was inspected or decided. File presence is not a validation of the associated evidence interpretation.

## Recorded coverage and chronology

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page record order | Exactly 1–157, in order |
| Active scan-page records | Exactly 1–175 |
| Printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 157, 2026-11-19 03:24:48 UTC |
| Numeric completion events | 158 events for 157 distinct pages |
| Page-number or timestamp regression | None |
| Completion timestamps after capture | None |
| Completion/correction metadata beyond page 157 | None |

The extra historical completion event is the preserved premature page-27 entry, explicitly voided in the check record. The canonical record and active scan sequences exclude that voided heading. The captured checkpoint table has 11 receipt rows; their recorded timestamps parse correctly and none postdates capture. These checks concern recorded chronology and do not independently validate remote save operations.

## Anchor and page-marker preservation

Literal labels, hyperlink targets, PDF bookmark IDs, and source-page markers were compared with the original sources and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. Counts below apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. Inherited front-target additions, source-position changes, and the cover duplicate remain baseline exceptions. This lexical check does not expand TeX or validate compiled PDF links.

## Preserved top-summary lag

The top numeric summary remains at **5,929**, the checkpoint-12 state. The frozen ledger contains **5,995**, a difference of **66**:

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,910 | 1,928 | +18 |
| corrected | 2,024 | 2,048 | +24 |
| English | 1,985 | 2,009 | +24 |
| build | 10 | 10 | +0 |
| **Total** | **5,929** | **5,995** | **+66** |

The primary reader’s established procedure refreshes top totals/status before timed checkpoints. This report preserves and identifies the frozen difference; it changes no totals or statuses. Historical reports retain their own recorded counts.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,381 | `7a71a4d2ad27a1bfd1a0ae6023cbadc34031bf6366c68878ef938700fb151d74` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,249 | `7c141013e910ec8b72c1cd1472da1783da6c0c78997e973d4c26f44cee8761f2` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,418 | `559ef7f131a76bf89ec2f652033c61d6de922d6de891a015a6903fc00ab76b31` |

## Scope and handling

This is a mechanical replay, schema, explicit-filename, identifier, count, and chronology audit. It makes **no certification of first or second reading**, textual correctness, translation fidelity, mathematical validity, or built-PDF quality. It does not inspect scans or prove the author’s statements.

No active source, ledger, verdict, report, question, progress/status record, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first written in temporary workspace for the primary reader to inspect and authorize installation. No ZIP was created or modified.
