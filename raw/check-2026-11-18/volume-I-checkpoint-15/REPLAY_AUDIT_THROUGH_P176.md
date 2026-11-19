# Frozen mechanical integrity and page-176 resumption audit

Capture boundary: **2026-11-19 04:38:41 UTC**, through recorded printed page **176**. Forty-three source, ledger, root-metadata, and script files were copied into a private snapshot. All hashes agree before capture, after capture, and in the frozen copies. Both `continue_p176.py` and `continue_p176_resume.py` were captured as historical files, along with the evidence/source-asset filename inventory. No numeric correction row or recorded completion beyond page 176 exists in this state; later page-177 work is excluded.

## Result and the interrupted-script risk

**The final frozen sources are fully accounted for by the ordered correction ledger.** All **6,582 rows** replay exactly from the supplied original sources, and all three resulting TeX files match the frozen source bytes. Independently, the **117 appended rows since the through-173 snapshot** reproduce those same source files when replayed onto the through-173 sources.

The primary reader reported that the initial page-176 script applied spacing and initial as-printed changes before stopping at an escaped-apostrophe exact-target mismatch, then the resume script applied the remaining work. This audit did not re-execute either editing script or interpret its editorial intentions. It examined the final ledger/source state and the following concrete safeguards:

- All **6,465 earlier ledger-row values remain unchanged** from the through-173 snapshot.
- Page 176 has **44 appended rows**, numbered **6539–6582**.
- No page-176 row has identical old/new strings.
- No identical `(file, old, new)` edit tuple is repeated among those 44 rows.
- Every row succeeds in the exact ordered replay, with one old-text occurrence required.
- Page 176 has exactly **one canonical record** and **one completion event**, at **2026-11-19 04:37:42 UTC**.

These results establish that no unrecorded source-byte difference from the interrupted/resumed work remains in the snapshot. They do not establish that every intended editorial change was correct or sufficient, and they do not certify completion of a visual or mathematical review.

## Full ledger totals and schema

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 2,090 |
| corrected | 2,271 |
| English | 2,211 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,286 |
| typesetting | 3,289 |
| reading | 1,676 |
| translation | 154 |
| misprint of the original | 125 |
| terminology | 52 |

The required ten-column schema is present. No malformed row, empty required field, or unknown correction kind was found. The numeric table agrees with every layer/kind count and with the total of **6,582**. The replay uses the captured existing replay script, unchanged, against private source copies.

## Complete source delta from the through-173 snapshot

| Printed page | As-printed | Corrected | English | Appended rows |
|---:|---:|---:|---:|---:|
| 174 | 11 | 13 | 11 | 35 |
| 175 | 6 | 17 | 15 | 38 |
| 176 | 13 | 16 | 15 | 44 |
| **Total** | **30** | **46** | **41** | **117** |

Applying only these appended rows to the frozen through-173 source files exactly reproduces all three through-176 sources. Together with the unchanged earlier ledger values, this independently accounts for all source-byte changes after that prior audit.

## Evidence-reference existence

All **1,642 current explicit image/PDF paths** from the normal correction/existing-correction/check-record/evidence-index audit resolve in the captured filename inventory.

The wider frozen root-metadata scan found **1,690 distinct filename references**. All **1,668 references occurring in operational metadata**, including reading-question evidence, have existing path, supplied-authority, or relative/basename candidates.

Four former literal spellings remain quoted only in preserved historical repair/audit reports:

| Historical literal | Existing corrected target(s) |
|---|---|
| `Evidence/I_p004_postcat.png` | `evidence/I_p004_postcat.png` |
| `exact-second.png` | `evidence/I_p110_exact-second.png` |
| `footnote.png` | `evidence/I_p111_footnote.png`, `evidence/I_p117_footnote.png` |
| `note-call.png` | `evidence/I_p117_note-call.png` |

These are historical quotations of repaired metadata, not unresolved operational evidence references. Historical reports remain unchanged. No scan, crop, facsimile, book text, or mathematical meaning was inspected; file presence does not validate evidentiary interpretation.

## Reading-question records

`READING_QUESTIONS.tsv` contains **19 records**, with the expected seven fields, no malformed rows, and no duplicate IDs. Its bytes are **identical to the through-173 snapshot**. No question or status was interpreted, resolved, or changed by this audit.

## Progress and chronology

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page record order | Exactly 1–176, in order |
| Active scan-page records | Exactly 1–194 |
| Numeric printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 176, 2026-11-19 04:37:42 UTC |
| Numeric completion events | 177 historical events for 176 distinct pages |
| Timestamp or page-number regressions | None |
| Completion timestamps after capture | None |
| Completion/correction metadata beyond page 176 | None |

The historical premature page-27 record remains explicitly voided, with its duplicate completion event preserved. Active scan counts exclude that voided heading. Completion metadata remains the primary reader’s account of work performed, not a new certification from this audit.

## Identifier preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared with the supplied originals and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. Counts apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. The inherited front-target additions, source-position changes, and cover duplicate remain baseline exceptions. This lexical inventory does not expand TeX or test compiled links.

## Capture and replay identity

Each hash below is identical before capture, after capture, and in the frozen copy. Source hashes also equal both the complete original-source replay and the incremental through-173 replay results.

| File | Identical SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `bffc39f28361d9b346712fc05dea722b8b897c9d748232ab2fc30adace13b860` |
| `READING_QUESTIONS.tsv` | `608d98df6b8384c2df8d783dbb085581579a583ee01ee0aae7120587c1964b76` |
| `sources/english/02-volume-I-english.tex` | `45e43f59805225ae4cb380a016029f0faf71a19dbe6874c6e529bf17db33819d` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `9146c937497e0cfa676f3f182af5ae41c12e98340c3321a392d37e93424853e9` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `bbe4a850a62c3a32641f08c800e2fcccc044f378156cd594039035b4e11a91d1` |
| `scripts/history/continue_p176.py` | `65224f0ebdc9a6406793efebaff53c2e40969be5b9bb2751f8839b6a6746f627` |
| `scripts/history/continue_p176_resume.py` | `deff04a11d1b3b34083e600e0138d3216e83e53805f5aeca54c0f474ffb6f4e1` |

## Scope and handling

This is an infrastructure-only replay, schema, reference-existence, identifier, count, chronology, and hash-coherence audit. It supplies no author-text, translation, mathematical, image, first-reading, second-reading, or PDF/build certification.

No active source, ledger, verdict, report, question, log, progress/status record, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first staged for primary-reader inspection and authorized installation. No packaging, checkpoint creation, or upload was performed.
