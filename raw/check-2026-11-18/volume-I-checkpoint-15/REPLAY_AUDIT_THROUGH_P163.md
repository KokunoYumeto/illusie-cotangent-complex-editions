# Frozen mechanical integrity audit through recorded printed page 163

Capture boundary: **2026-11-19 03:45:34 UTC**. Ten source, ledger, report, checkpoint-metadata, and replay-script files were frozen into a private copy. Their hashes agree before capture, after capture, and in the copied files. The evidence/source-asset filename inventory was captured alongside them. The snapshot records completion through printed page 163 / scan page 181; page 164 had no correction rows or completion event in this state and is excluded from completion claims.

This report checks recorded metadata and byte accountability only. It does not review future pages, scans, mathematical statements, or translation content, and does not certify a first or second reading.

## Exact correction replay and schema

**All 6,133 correction rows replay exactly onto a fresh extraction of the immutable supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The captured replay script was used unchanged, with one exact old-text occurrence required for each replacement.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,970 |
| corrected | 2,097 |
| English | 2,056 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,190 |
| typesetting | 3,073 |
| reading | 1,560 |
| translation | 138 |
| misprint of the original | 121 |
| terminology | 51 |

The ten-column schema is correct. No malformed record, empty required field, or unknown correction kind was found.

## Targeted earlier-page repair captured during page 162

The snapshot contains the three requested page-68 repair rows:

| Ledger row | Printed page | Layer | Recorded kind | Required evidence prefix |
|---:|---:|---|---|---|
| 6105 | 68 | as-printed | typesetting | `corrects the earlier run:` |
| 6106 | 68 | corrected | typesetting | `corrects the earlier run:` |
| 6107 | 68 | English | typesetting | `corrects the earlier run:` |

All three evidence cells begin with that exact prefix. They are bracketed in ledger order by row 6104 and row 6108, both associated with printed page 162, consistent with the primary reader’s identification of the repair as made during the page-162 pass. No separate repair timestamp is invented: the correction ledger itself has no timestamp column.

The three rows are included in the successful exact replay above; their recorded old/new strings account mechanically for the frozen source bytes. This audit does not interpret those strings, assess the repair’s mathematical or typographical correctness, inspect its images, change confidence, or close a reading question.

## Explicit evidence references

All **1,479 explicit image/PDF paths** extracted from the evidence fields of both ledgers and from `CHECK_RECORD.md` and `EVIDENCE_INDEX.md` resolve in the captured evidence/source-asset filename inventory. No missing explicit path was found.

Filename existence is not certification of evidentiary support. Prepared images, where present, do not establish completion of a page. No image was opened or interpreted.

## Page-done order and timestamps

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page records | Exactly 1–163, in order |
| Active scan-page records | Exactly 1–181 |
| Numeric page/scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 163, 2026-11-19 03:44:48 UTC |
| Numeric completion events | 164 historical events for 163 distinct pages |
| Timestamp or page-number regressions | None |
| Completion events after capture | None |
| Completion/correction metadata beyond page 163 | None |

The explicitly voided premature page-27 entry and its duplicate historical completion event are retained as history. Active scan counts exclude the voided heading. The backward page number on the three page-68 correction rows is an explicitly identified earlier-page repair; it is not a new page-completion event and does not alter the sequential completion chronology.

## Anchor and label preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared against the immutable original sources and checkpoint 09, excluding macro-parameter placeholders. Counts below apply to each source layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. The inherited front-target additions, source-position changes, and cover duplicate remain baseline exceptions. This lexical inventory does not expand TeX or certify compiled links.

## Before/after capture hashes

The following SHA-256 values explicitly identify both sides of the capture. The frozen copies have these same values. The replayed source files also have these same values; the correction ledger is the replay input.

| File | Before capture SHA-256 | After capture SHA-256 |
|---|---|---|
| `CORRECTIONS.tsv` | `910960da677adbdff3d9e409b307550286757f48921f4c04017d8a66c0b83205` | `910960da677adbdff3d9e409b307550286757f48921f4c04017d8a66c0b83205` |
| `sources/english/02-volume-I-english.tex` | `c46a0ca7b8e1e349655514d85e246336e391684f0fd77854ffc8c0b1de63ee38` | `c46a0ca7b8e1e349655514d85e246336e391684f0fd77854ffc8c0b1de63ee38` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `66ad268b50e98ab2e5416907481f3047362c0cc01a40db8193ed2c9618a09d12` | `66ad268b50e98ab2e5416907481f3047362c0cc01a40db8193ed2c9618a09d12` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `27192882f18c352c5751f2f71758820b73d57daa6b40be80f588a9731b9e006d` | `27192882f18c352c5751f2f71758820b73d57daa6b40be80f588a9731b9e006d` |

All ten captured files passed this before/after/frozen equality check. Source byte lengths are:

| Source | Bytes |
|---|---:|
| `sources/english/02-volume-I-english.tex` | 1,539,220 |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,567,018 |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,585,167 |

## Preserved top-summary lag

The top numeric summary remains at **5,929**, the checkpoint-12 state, while the frozen ledger contains **6,133** (**+204**):

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,910 | 1,970 | +60 |
| corrected | 2,024 | 2,097 | +73 |
| English | 1,985 | 2,056 | +71 |
| build | 10 | 10 | +0 |
| **Total** | **5,929** | **6,133** | **+204** |

The primary reader refreshes top totals/status before timed checkpoints. This audit records the capture-state difference without refreshing the summary. Historical reports keep their original counts and scopes.

## Scope and handling

This is a mechanical exact-replay, schema, explicit-filename, identifier, chronology, count, and hash-coherence audit. It makes no textual, mathematical, translation, image, first-reading, second-reading, or PDF/build certification.

No active source, ledger, verdict, report, question, progress/status record, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first written in temporary workspace for primary-reader inspection and authorized installation.
