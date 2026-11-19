# Frozen mechanical integrity audit through recorded printed page 167

Capture boundary: **2026-11-19 04:00:09 UTC**. Ten source, ledger, report, checkpoint-metadata, and replay-script files were copied into a private snapshot. All hashes agree before capture, after capture, and in the frozen copies. An evidence/source-asset filename inventory was captured alongside them. The snapshot has no numeric correction rows or recorded completion after page 167; later page-168 work is excluded.

The primary record marks page 167 complete at 03:59:25 UTC. This audit checks only byte accountability and metadata consistency; it does not certify a first or second reading.

## Exact replay and correction schema

**All 6,230 correction rows replay exactly onto a fresh extraction of the immutable supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The existing captured replay script was used unchanged, requiring exactly one old-text occurrence for every replacement.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,998 |
| corrected | 2,130 |
| English | 2,092 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,202 |
| typesetting | 3,136 |
| reading | 1,573 |
| translation | 144 |
| misprint of the original | 123 |
| terminology | 52 |

The required ten-column header is present. No malformed row, empty required field, or unknown correction kind was found. The refreshed top numeric totals agree with every layer/kind cell and with the total of **6,230**. Historical reports retain their earlier counts.

## Captured repairs of earlier-run pages 77 and 79

The following new rows, all after the previous through-163 audit boundary, were captured:

| Ledger row | Printed page | Layer | Recorded kind | Evidence prefix |
|---:|---:|---|---|---|
| 6158 | 77 | as-printed | typesetting | `corrects the earlier run:` |
| 6159 | 77 | corrected | typesetting | `corrects the earlier run:` |
| 6160 | 77 | English | typesetting | `corrects the earlier run:` |
| 6183 | 79 | as-printed | typesetting | `corrects the earlier run:` |
| 6184 | 79 | corrected | typesetting | `corrects the earlier run:` |
| 6185 | 79 | English | typesetting | `corrects the earlier run:` |
| 6186 | 79 | English | translation | `corrects the earlier run:` |

All seven evidence cells begin with that exact prefix. The page-77 rows follow row 6157, associated with page 164, and precede row 6161, associated with page 165. The page-79 rows follow row 6182, associated with page 165, and precede row 6187, associated with page 166. This ledger placement is consistent with the primary reader’s stated provenance: the page-77 repair arose from page 164 and the page-79 repair from page 165.

These rows are included in the successful replay. Their old/new byte strings are mechanically accounted for, but their content, correctness, translation, images, and confidence are not adjudicated here. No per-row time is invented; the ledger has no timestamp column.

## Explicit evidence-reference existence

All **1,531 explicit image/PDF paths** extracted from the evidence fields of the correction and existing-correction ledgers, plus `CHECK_RECORD.md` and `EVIDENCE_INDEX.md`, resolve in the captured evidence/source-asset filename inventory. No missing explicit path was found.

This is an existence check only. No scan, page image, author text, translation, or mathematical meaning was read or interpreted. A prepared file does not establish completed page review.

## Progress order and timestamps

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page record order | Exactly 1–167, in order |
| Active scan-page records | Exactly 1–185 |
| Numeric printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 167, 2026-11-19 03:59:25 UTC |
| Numeric completion events | 168 historical events for 167 distinct pages |
| Timestamp or page-number regressions | None |
| Completion timestamps after capture | None |
| Completion/correction metadata beyond page 167 | None |

The preserved premature page-27 record remains explicitly voided, with its duplicate historical completion event retained. The active scan count excludes that voided heading. Earlier-page correction rows are not new page-completion events and do not change the recorded sequential progress.

## Anchor and label preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared with the supplied originals and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. Counts below apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. Inherited front-target additions, target-position changes, and the cover duplicate remain baseline exceptions. This lexical inventory does not expand TeX or validate compiled PDF links.

## Capture and source hashes

The before-capture, after-capture, and frozen SHA-256 values are identical for every captured file. The values below identify the correction ledger and three sources; replayed source hashes also equal these values.

| File | Identical before/after/frozen SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `680ea73967cf38f0869a226628b8969bfe2ed0209b5d99c6644ad78400f9a76c` |
| `sources/english/02-volume-I-english.tex` | `11e3baac3cbbc100e2dcabff7328d64d381c3837beb91f657156d50f1e97524e` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `d87dfbaefa170f70c3185d2c0b16b1ea36cd4a0ad7c71f566d0d3f0cc4fa9de8` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `a9e5d760ef50017dc7c5a517d8804a182c8bb74157fc45924a1986686b19f61b` |

## Scope and handling

This is an infrastructure-only exact-replay, schema, explicit-reference, identifier, count, and progress-metadata audit. It makes **no author-text, translation, mathematical, image, first-reading, second-reading, or PDF/build certification**.

No active source, ledger, verdict, report, question, progress/status record, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first written under staging for primary-reader inspection and authorized installation.
