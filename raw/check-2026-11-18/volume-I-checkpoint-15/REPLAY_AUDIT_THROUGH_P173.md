# Frozen mechanical integrity audit through recorded printed page 173

Capture boundary: **2026-11-19 04:26:12 UTC**. A private snapshot captured **39** source, ledger, root-metadata, and replay-script files. Their SHA-256 values agree before capture, after capture, and in the copied files. An evidence/source-asset filename inventory was captured alongside them. The snapshot has **6,465 correction rows** and **19 reading-question records**, with no numeric correction row or recorded completion beyond page 173. Later page-174 activity is excluded.

This report checks mechanical edit accountability and metadata consistency. It does not certify a first or second reading, interpret author text or images, adjudicate translation, or prove mathematics.

## Full replay and live numeric totals

**All 6,465 correction rows replay exactly onto a fresh extraction of the immutable supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The captured existing replay script was used unchanged, requiring one exact old-text occurrence for every row.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 2,060 |
| corrected | 2,225 |
| English | 2,170 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,256 |
| typesetting | 3,247 |
| reading | 1,631 |
| translation | 154 |
| misprint of the original | 125 |
| terminology | 52 |

The ten-column correction schema is correct. No malformed row, empty required field, or unknown correction kind was found. The live numeric table agrees with every layer/kind count and with the total of **6,465**. No numeric totals were refreshed by this audit.

## All appended rows since the through-169 snapshot

The prior **6,319 ledger-row values are unchanged**. Exactly **146 rows** have been appended:

| Printed page | As-printed | Corrected | English | Appended rows |
|---:|---:|---:|---:|---:|
| 170 | 7 | 8 | 9 | 24 |
| 171 | 10 | 27 | 15 | 52 |
| 172 | 6 | 8 | 9 | 23 |
| 173 | 11 | 19 | 17 | 47 |
| **Total** | **34** | **62** | **50** | **146** |

A separate incremental replay applied only these 146 rows to private copies of the frozen through-169 sources. **The resulting files exactly reproduce all three through-173 source files.** This accounts for every source-byte change since that earlier audit without altering any earlier ledger-row value.

## Independent checkpoint-13 baseline comparison

The checkpoint-13 baseline ledger has **6,230 rows**, whose values likewise remain unchanged in the current ledger. Its **235 appended rows** cover pages 168–173. Applying only those 235 rows to the checkpoint-13 source files also reproduces the current frozen sources byte for byte in all three layers.

The immutable baseline was identified and checked as follows:

- Archive: `ILLUSIE_I_CHECK_checkpoint_13.zip`.
- Bytes: **149,257,513**.
- SHA-256: `fe1cade8f00773892b6675d8052260d008940465fb48512046a70b8f49c62333`.
- Selected baseline members verified against the archive file list: the correction ledger and all three TeX files.

This baseline check verifies those selected members and identifies the complete ZIP by hash. It is not represented as a new remote-save verification or a complete re-audit of every other checkpoint-13 member.

## Evidence-reference audit, including questions and historical metadata

All **1,610 current explicit image/PDF paths** extracted by the normal ledger/check-record/evidence-index audit resolve in the captured filename inventory.

A wider scan covered all frozen root Markdown/TSV metadata, including the reading-question evidence column. It found **1,647 distinct filename references**. All **1,636 references appearing in operational metadata** have existing path, supplied-authority, or relative/basename candidates. The **71 distinct references in reading-question evidence** also resolve.

The wider scan encountered four former literal spellings only in preserved historical audit/repair reports:

| Historical literal | Existing corrected target(s) |
|---|---|
| `Evidence/I_p004_postcat.png` | `evidence/I_p004_postcat.png` |
| `exact-second.png` | `evidence/I_p110_exact-second.png` |
| `footnote.png` | `evidence/I_p111_footnote.png`, `evidence/I_p117_footnote.png` |
| `note-call.png` | `evidence/I_p117_note-call.png` |

These are intentionally recorded former spellings from already documented metadata repairs. They do not occur as unresolved operational evidence references in this snapshot. Historical reports are kept unchanged; the audit does not turn their quoted former literals into new missing-file findings. The previously documented three-layer `front-matter.pdf` shorthand remains contextual metadata, and all explicit source-asset paths exist.

No image or book text was interpreted. File existence and filename resolution do not establish that an image supports an editorial claim.

## Reading-question record structure

`READING_QUESTIONS.tsv` contains **19 records** with the expected seven fields: id, printed page, statement, question, retained reading, status, and evidence. There are no malformed records or duplicate IDs. The audit checks count, structure, identifier uniqueness, and evidence-file existence only. It does not evaluate, resolve, close, or change any question or status.

## Progress, ordering, and timestamps

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page record order | Exactly 1–173, in order |
| Active scan-page records | Exactly 1–191 |
| Numeric printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 173, 2026-11-19 04:25:02 UTC |
| Numeric completion events | 174 historical events for 173 distinct pages |
| Timestamp or page-number regressions | None |
| Completion timestamps after capture | None |
| Completion/correction metadata beyond page 173 | None |

The premature page-27 record remains explicitly voided and its historical duplicate completion event remains preserved. The active scan count excludes that voided heading. Completion events remain the primary reader’s account of work performed; this audit supplies no separate reading certification.

## Exact label and anchor preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared against the supplied originals and checkpoint 09; macro-parameter placeholders containing `#` were excluded. Counts below apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. The inherited front-target additions, target-position changes, and cover duplicate remain baseline exceptions; the newly appended rows introduce no identifier-sequence change. This lexical inventory does not expand TeX or test compiled PDF links.

## Capture and replay hashes

Each value below is identical before capture, after capture, and in the frozen copy. For the three source files it also equals the full original-source replay and both incremental baseline-replay results.

| File | Identical SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `81e0d845e98420372cae0d1dfbb103fe61247392b8f9325128fc6309985226e7` |
| `READING_QUESTIONS.tsv` | `608d98df6b8384c2df8d783dbb085581579a583ee01ee0aae7120587c1964b76` |
| `sources/english/02-volume-I-english.tex` | `c61f212a1d2ce9296cf3fef7380be8ba599f9b82e528db526ec02d68eb987e41` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `efc6fa78b9b426b06a12b6eec742b516a756ea4cd7aac48cf1c65b6103c8fab8` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `7e1329284980e68562efe058fb6aa7a958e699987072bf4b57bb80e37b1deab4` |

## Scope and handling

This is an infrastructure-only replay, schema, explicit/metadata-reference, identifier, count, chronology, and hash audit. It makes no author-text, translation, mathematical, image, first-reading, second-reading, or PDF/build certification. Historical reports retain their original boundaries and counts.

No active source, ledger, verdict, report, question, progress/status record, log, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first staged for primary-reader inspection and authorized installation. No packaging, checkpoint creation, or upload was performed.
