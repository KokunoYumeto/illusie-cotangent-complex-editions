# Frozen mechanical replay and integrity audit through page 185

Prepared: **2026-11-19 05:20:11 UTC**. Capture boundary: **2026-11-19 05:17:46 UTC**, with reads checked from **05:17:46.682258 to 05:17:46.847174 UTC** on the first attempt. This report describes the private frozen state through printed page **185 / scan 203**; later page 186 changes are excluded.

## Result

**PASS: the complete ordered correction ledger reproduces every byte of the three frozen source files from the supplied originals.** All **7,062 rows** succeed. Independent incremental checks also reproduce those sources exactly from both requested baselines: **175 appended rows since through 182**, and **438 appended rows since checkpoint 14**.

All earlier field values in CORRECTIONS, EXISTING_CORRECTIONS, and CHECK_EVENTS remain unchanged against both baselines. The 19-question file is byte-identical to both. No unresolved operational evidence reference, missing original identifier, malformed record, or chronology error was found.

The capture contains **54 source, ledger, root-metadata, and script files**. Hashes agree before capture, after capture, in the frozen copies, and after the audit. The copied history scripts for pages 183–185 were retained as bytes; no historical editing script was executed. The captured evidence/source-asset filename inventory supports file-existence checks without opening image or PDF content.

## Exact replay and append-only deltas

The captured existing replay mechanism ran against private copies of the supplied original sources. Full replay and both incremental byte-replacement checks all equal the frozen sources. Each appended old-byte value occurs exactly once at its replay step.

| Baseline | Preserved correction rows | Appended correction rows | Row range |
|---|---:|---:|---|
| Frozen through 182 | 6,887 | 175 | 6888–7062 |
| Immutable checkpoint 14 | 6,624 | 438 | 6625–7062 |

| Printed page | As-printed | Corrected | English | Total appended rows |
|---:|---:|---:|---:|---:|
| 178 | 5 | 17 | 14 | 36 |
| 179 | 7 | 18 | 17 | 42 |
| 180 | 11 | 30 | 27 | 68 |
| 181 | 7 | 19 | 18 | 44 |
| 182 | 17 | 28 | 28 | 73 |
| 183 | 14 | 27 | 26 | 67 |
| 184 | 12 | 24 | 20 | 56 |
| 185 | 12 | 19 | 21 | 52 |

Pages 183–185 sum to 175 rows. The complete checkpoint 14 delta, pages 178–185, sums to 438. These are record counts, not new assessments of source meaning or correctness.

| Record set | Through 182 baseline | Frozen 185 | Appended since 182 | Appended since checkpoint 14 |
|---|---:|---:|---:|---:|
| CORRECTIONS | 6,887 | 7,062 | 175 | 438 |
| EXISTING_CORRECTIONS | 568 | 572 | 4 | 11 |
| CHECK_EVENTS | 428 | 437 | 9 | 21 |
| READING_QUESTIONS | 19 | 19 | 0; byte-identical | 0; byte-identical |

The correction ledger has the required ten-column schema, with no malformed rows, empty required fields, or unknown correction kinds. The question, existing-correction, and check-event schemas also agree with their expected structures. Question IDs are unique. Earlier verdict and event field values were compared mechanically, without interpreting them.

## Frozen counts and completion coverage

| Layer | Correction rows |
|---|---:|
| as-printed | 2,184 |
| corrected | 2,470 |
| English | 2,398 |
| build | 10 |
| **Total** | **7,062** |

The numeric layer/kind table matches every ledger cell and the 7,062 total. Canonical printed-page records are exactly **1–185**, in order; active scan records are exactly **1–203**. There are no gaps, duplicate active records, incorrect printed-to-scan offsets, or timestamp disagreements between canonical page records and progress entries.

The last frozen completion is **page 185, 2026-11-19 05:13:17 UTC**. Page-number and timestamp sequences do not regress, and no completion is later than capture. No numeric correction or existing-correction record extends beyond page 185. No canonical completion or progress-done entry for page 186 is present.

The unchanged, explicitly voided page 27 history accounts for 186 historical numeric completion events for 185 unique completed pages. Active scan coverage excludes that voided heading.

**Endpoint metadata distinction:** the top README and CHECK_RECORD prose still states checkpoint 14's completed boundary of 177/195. Current canonical sections and progress reach 185/203, and the numeric table is current at 7,062. This report preserves and identifies that summary lag without changing it or treating it as a loss of recorded completions. Earlier reports retain their original counts and boundaries.

## Evidence-reference resolution

All **1,754 explicit current image/PDF paths** checked in CORRECTIONS, EXISTING_CORRECTIONS, CHECK_RECORD, and EVIDENCE_INDEX exist in the captured filename inventory.

The broader operational metadata check, also including question evidence and README, finds **1,780 distinct image/PDF filename references**. All resolve to existing exact paths, relative/basename candidates, or the separately supplied original scan authority. The basename `ILLUSIE_I_LNM239.pdf` refers to that existing external input; source-layer front-matter assets remain present under their established paths.

These are existence checks. No scan, crop, source illustration, or PDF content was opened or assessed, and no claim about the interpretation of evidence is made.

## Label and anchor preservation

All original literal label, hyperlink-target, bookmark, and source-page-marker occurrences are retained. **Every inspected identifier sequence in all three sources is exactly identical to checkpoint 09.** Counts per layer remain 356 labels, 3,943 hyperlink targets, 1 bookmark ID, 6 front-page markers, and 355 body-page markers. Macro-parameter placeholders are excluded from the inventory. Previously documented baseline exceptions are unchanged.

This is lexical identifier preservation, not TeX expansion, PDF build validation, or a compiled-link check.

## Frozen byte identities

Each hash below agrees before and after capture, in the private frozen copy, and after the audit. Source-file hashes also agree with the full original-source replay and both incremental replay results.

| File | SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `dc3f8d3aae71292d32c26d65a70314373d704be71e539cfb4fcab646ab0253e3` |
| `EXISTING_CORRECTIONS.tsv` | `52a475aacb7d5fce65f821ea42326cc25b6db01ada84d31a3b9c139739f8be0e` |
| `CHECK_EVENTS.tsv` | `ca9564eac39029fb34cc830bf4a45a5bcb3d2d170fc2457fbc5133b214263289` |
| `READING_QUESTIONS.tsv` | `608d98df6b8384c2df8d783dbb085581579a583ee01ee0aae7120587c1964b76` |
| `sources/english/02-volume-I-english.tex` | `1f62ba2030b6fabb1de67f05a9d8cb4e2d874d20d37acb6f86b7783d20715e69` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `b7f509c30c9ae552178825404873539307109f95531ab513ba72c6e4a31f18b1` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `8be865dba0c904d4bc96ea4a7a48f31d84fde5337c2e0fb01d33166aab7f253a` |

The immutable checkpoint 14 baseline was independently identified as **161,977,766 bytes**, SHA-256:

`206682f9df1d8ffb829866a3655cf60f26c984f2a59f123e86a2338b0ae9f4cc`

That identity agrees with its earlier verified archive. The through 182 baseline is the private snapshot captured **2026-11-19 05:00:54 UTC**. Neither baseline or earlier report was changed.

## Scope and handling

This is a mechanical replay, schema, provenance, reference-existence, identifier, count, and chronology audit. It does not interpret author prose, mathematical content, translation, notes, scans, or images. Completion metadata remains the primary reader's recorded account; this audit supplies no first-reading or second-reading certification.

No active source, ledger, verdict, question, CHECK_RECORD, progress log, report, or archive was edited. No page was marked or reclassified. Volume II was untouched. No checkpoint, ZIP, or upload was created. Checkpoint 15 remains scheduled for **2026-11-19 05:29:37 UTC**; this audit does not package it. The report is staged for primary review before any installation.

Any separately prepared ancillary privacy/capacity advisory has its own later timestamp and scope and does not extend this frozen replay boundary.
