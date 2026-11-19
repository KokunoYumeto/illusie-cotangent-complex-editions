# Frozen mechanical replay and provenance audit through page 182

Prepared: **2026-11-19 05:03:11 UTC**. Snapshot captured **2026-11-19 05:00:54 UTC**, within **05:00:54.380789–05:00:54.547462 UTC** on the first capture attempt. This report describes that private frozen state only; later page-183 work is excluded.

## Result and capture boundary

**PASS: all 6,887 correction rows replay exactly from the supplied original sources into the three frozen TeX files.** Two additional incremental comparisons independently reproduce the same source bytes: **263 appended rows since checkpoint 14**, and **305 appended rows since the through 176 snapshot**. Earlier correction-row field values remain unchanged in both comparisons.

The capture includes **52 source, ledger, root-metadata, replay-script, and history-script files**. Their hashes agree before capture, after capture, in the frozen copies, and again after this audit. The final page 181 and page 182 history scripts are included in the frozen capture. Evidence/source-asset filenames were inventoried for reference-existence checks; image and PDF contents were not inspected.

The frozen records end at **printed page 182 / scan page 200**, with page 182 completed **2026-11-19 05:00:25 UTC**. There are **6,887 correction rows**, **19 reading-question records**, **568 existing-correction records**, and **428 check-event records**. There are no numeric correction or existing-correction rows beyond page 182, and no later canonical page-completion or progress-done entry.

## Source replay and incremental provenance

The captured existing replay mechanism was run only against private copies of the supplied original sources. The full ordered ledger succeeds and produces exact equality for every byte of all three current source files. The correction ledger has the required ten columns, with no malformed rows, empty required fields, or unknown correction kinds.

| Baseline | Earlier correction rows unchanged | Appended rows | Incremental result |
|---|---:|---:|---|
| Immutable checkpoint 14 | 6,624 | 263, rows 6625–6887 | All three frozen sources exact |
| Frozen through 176 snapshot | 6,582 | 305, rows 6583–6887 | All three frozen sources exact |

Every appended edit has exactly one old-byte occurrence at its replay step. The incremental comparison accounts for the following complete source deltas:

| Printed page | As-printed | Corrected | English | Total rows |
|---:|---:|---:|---:|---:|
| 177 | 9 | 17 | 16 | 42 |
| 178 | 5 | 17 | 14 | 36 |
| 179 | 7 | 18 | 17 | 42 |
| 180 | 11 | 30 | 27 | 68 |
| 181 | 7 | 19 | 18 | 44 |
| 182 | 17 | 28 | 28 | 73 |

Page 177 belongs only to the comparison from through 176; it was already included in checkpoint 14. Pages 178–182 total 263 rows. The source hashes obtained by the full original-source replay and by both incremental replay paths are identical to the frozen hashes below.

The question file is byte-identical to both checkpoint 14 and through 176, with 19 records, seven expected fields, no malformed records, and no duplicate IDs. Existing-correction and check-event schemas are well formed. Since checkpoint 14, the existing-correction ledger has 7 appended rows and the check-event ledger has 12; every earlier field value in both ledgers is unchanged. No verdict or event outcome was interpreted.

## Specific page 181 and page 182 execution concern

The primary supplied this execution history: page 181 completed successfully once; page 182 first stopped at a parse-time SyntaxError before mutations, then completed successfully once after the syntax fix. This history is identified as supplied context, not as an execution log independently observed by this audit.

The frozen final-state checks show:

| Check | Page 181 | Page 182 |
|---|---:|---:|
| Correction rows | 44 | 73 |
| Ledger row range | 6771–6814 | 6815–6887 |
| Duplicate identical `(file, old, new)` tuples | 0 | 0 |
| Rows with identical old and new values | 0 | 0 |
| Canonical completion records | 1 | 1 |
| Progress completion events | 1 | 1 |
| Recorded completion UTC | 2026-11-19 04:56:24 | 2026-11-19 05:00:25 |
| Final captured history script passes `ast.parse` | Yes | Yes |

Neither historical editing script was executed by this audit. The originally failed page 182 script version and its invocation timing were not independently reconstructed. The exact full and incremental replays establish that **no unledgered source-byte difference remains in this frozen state**. They do not independently certify invocation counts or whether the recorded editorial changes were correct or sufficient.

## Current totals and completion metadata

| Layer | Correction rows |
|---|---:|
| as-printed | 2,146 |
| corrected | 2,400 |
| English | 2,331 |
| build | 10 |
| **Total** | **6,887** |

The numeric layer/kind table matches every ledger cell and the 6,887 total. Canonical printed-page records are exactly 1–182 in order, and active scan-page records are exactly 1–200. All printed-to-scan offsets equal 18; canonical completion timestamps match progress entries. There are no timestamp regressions, page-number regressions, or completion timestamps after capture.

The inherited voided page 27 history remains unchanged: 183 historical numeric completion events describe 182 distinct completed pages. Active coverage excludes the voided heading.

**Scoped metadata observation:** the README and CHECK_RECORD top endpoint prose still carry checkpoint 14's through 177/scan 195 boundary. Current page sections and progress reach 182/200, and the numeric table is current at 6,887. This report records that summary lag without treating it as a loss of recorded completions or refreshing any active text. Earlier reports retain their original boundaries and counts.

## Evidence-reference existence and identifiers

All **1,712 explicit current image/PDF paths** from the correction/existing-correction ledgers, CHECK_RECORD, and EVIDENCE_INDEX exist in the captured filename inventory. The broader operational metadata check, also including question evidence and README, finds **1,738 distinct filename references**, all resolving to an existing exact path, relative/basename candidate, or separately supplied scan authority. The original scan basename `ILLUSIE_I_LNM239.pdf` remains an external input authority. No evidence content was opened or evaluated.

Literal source labels, hyperlink targets, bookmark IDs, and front/body page markers retain all original occurrences. **Every inspected identifier sequence in every layer is identical to checkpoint 09.** The counts per layer remain 356 labels, 3,943 hyperlink targets, 1 bookmark ID, 6 front-page markers, and 355 body-page markers. Prior baseline exceptions are unchanged; this is lexical preservation checking, without TeX expansion or compiled-link testing.

## Frozen file identities

Each hash below agrees before and after capture, in the frozen copy, and after this audit. For the three source files it also agrees with the full and both incremental replays.

| File | SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `3df1084af97e5027c09abafde4d6e522dd3fec1ce61d0b0dde981dec9bc2fa4c` |
| `READING_QUESTIONS.tsv` | `608d98df6b8384c2df8d783dbb085581579a583ee01ee0aae7120587c1964b76` |
| `sources/english/02-volume-I-english.tex` | `a8eb040f4aa878b1ff4f8ee8be86bc89d63c05c7aafd93e2b59d2fc3e23946cb` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `d781e1b9ecf15a68640c11fb8f77f86d3a8d3128cf1beabe98f9292a823408b9` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `553f2864031708ee57876026e81ea96730968dd2655bad380973124fbbe05cee` |
| `scripts/history/continue_p181.py` | `3bc518ac0ebe10742e7e07a371364b1cc89b52921eb167292a9624cc441eed17` |
| `scripts/history/continue_p182.py` | `de90adb06c997df550a7619ccd13813cc8a281dcb4a5a7cd00da7cacb75b4d10` |

Relevant immutable-baseline identities recorded for this audit:

| Baseline | Bytes | SHA-256 |
|---|---:|---|
| Supplied original source ZIP | 18,388,315 | `fe16c420cac00e0cd2991fd535c415c355469851b11ccd4bf7a4d3550bf33914` |
| Supplied checkpoint 09 | 74,705,847 | `3cb915f39087b3554c1d0e89c62be27b953c12d431e5280bc9726ebe1cbb4128` |
| Checkpoint 14 | 161,977,766 | `206682f9df1d8ffb829866a3655cf60f26c984f2a59f123e86a2338b0ae9f4cc` |

Checkpoint 14's identity agrees with its earlier independently verified immutable archive. Baselines were used only for the replay/provenance and identifier comparisons relevant to this snapshot; prior audits were not revised.

## Scope and handling

This is a mechanical audit of replay, record structure, reference existence, identifiers, counts, chronology, and byte provenance. It provides no author-text, translation, mathematical, visual-reading, first-reading, second-reading, build, or PDF certification.

No active source, correction row, verdict, question, report, CHECK_RECORD, progress log, or checkpoint was edited. No page was marked or reclassified. No image, scan, notes meaning, or Volume II material was reviewed. No packaging or upload was performed. The report is staged for primary review; installation has not been performed by this audit.
