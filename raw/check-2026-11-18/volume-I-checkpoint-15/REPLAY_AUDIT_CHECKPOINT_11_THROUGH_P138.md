# Frozen checkpoint 11 integrity audit through printed page 138

## Frozen object and archive integrity

This report audits only **`ILLUSIE_I_CHECK_checkpoint_11.zip`**. It does not describe the later active workspace. The ZIP was observed complete before extraction, and its size/modification fingerprint remained stable during capture.

- Archive size: **109,190,224 bytes**.
- Archive SHA-256: `6ada25023d615fe6fed2537ade08b17d9437c26e63da804520f87f296a5ef62e`.
- Verification/capture: **2026-11-19 02:32:11 UTC**.
- Payload members verified against `FILE_LIST.tsv`: **1,306**.
- Total archive members, including the index: **1,307**.
- Size/hash mismatches, missing members, unexpected unlisted members, and earlier-checkpoint dependencies: **none**.

Packaging metadata recorded by the ZIP:

> Packaging index; no self-hash. Created 2026-11-19 02:31:10 UTC; 45-minute due time 2026-11-19 02:29:37 UTC.

Every listed payload was read from the ZIP and verified against its recorded byte count and SHA-256. The index is the generated packaging record and has no self-hash; the archive hash above identifies the complete ZIP.

## Exact replay and correction schema

**All 5,604 correction rows replay successfully onto a fresh private extraction of the supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the sources stored in checkpoint 11.** The replay script used was the unchanged script stored in that checkpoint; every old-text replacement had to match exactly once.

| Layer | Checkpoint ledger rows |
|---|---:|
| as-printed | 1,816 |
| corrected | 1,905 |
| English | 1,873 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,048 |
| typesetting | 2,785 |
| reading | 1,494 |
| translation | 131 |
| misprint of the original | 109 |
| terminology | 37 |

The ten-column header matches the required schema. No malformed record or empty required file, layer, old, new, evidence, kind, or confidence field was found. The recorded top totals match the checkpoint ledger in every layer/kind cell and in the total of **5,604**.

## Explicit evidence references

All **1,223 distinct explicit image/PDF paths** extracted from the evidence columns of `CORRECTIONS.tsv` and `EXISTING_CORRECTIONS.tsv`, plus `CHECK_RECORD.md` and `EVIDENCE_INDEX.md`, identify members present in the checkpoint ZIP. There are **no missing explicit references**. This includes evidence crops and explicitly named source-tree facsimile assets.

The check is limited to filename/path existence and archived-byte integrity. No image or facsimile content was inspected, and file presence is not treated as proof that a reading is supported.

## Completed-page boundary and timestamps

| Metadata check | Checkpoint result |
|---|---|
| Canonical completed printed-page sections | Exactly pages 1–138 |
| Active scan-page headings | Exactly scan pages 1–156 |
| Numeric printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last completion | Page 138, 2026-11-19 02:27:30 UTC |
| Completion record or event for page 139 | None |
| Correction rows with numeric page above 138 | None |

**Page 139 was in progress and is excluded from completion claims.** Its full source scaffolding or any preparatory material in a checkpoint does not imply a completed reading. This report does not extend its coverage claim based on subsequent workspace activity.

The inherited page-27 premature entry remains explicitly voided; the duplicate historical completion event is preserved. Excluding the voided heading gives the active scan coverage above with no gaps or duplicates. No history was rewritten.

## Anchor and page-marker preservation

Literal IDs from `label`, `hypertarget`, `pdfbookmark`, `illusiefrontpage`, and `illusiebodypage` were compared with the supplied original sources and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. Each source layer retains:

- 356 labels;
- 355 body-page markers;
- six front-page markers;
- one PDF bookmark ID;
- every one of the 3,940 original literal hyperlink-target occurrences, plus the three inherited front targets, giving 3,943 occurrences.

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** The inherited target additions, target-position changes, and duplicate cover target remain unchanged. No original identifier occurrence is missing. This is a lexical inventory, not TeX expansion or compiled-link validation.

## Checkpoint source identity

| Source member | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,759 | `43eba55c0a644e8dbcd2bc68e3ae0af1e752cc4d8c166a29e4e56c22ba7b5362` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,619 | `7c8a1fa769e10b78bf51098978a8b14951b3eecb189b4faf3ea055116d7154c2` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,911 | `1aea21a978f34fc9990aacc02a9d1ffba87fdd298f4e4bb7b1ad792cd150f288` |

## Scope and handling

This is a mechanical ZIP, ledger replay, schema, explicit-path, anchor-inventory, coverage, and timestamp audit. It is **not a visual reading**, textual or mathematical adjudication, translation review, second reading of corrections, or PDF/build certification. Completion metadata remains the primary reader’s record of the reading performed.

No active workspace file, source, correction row, verdict, page-status record, progress log, earlier report, or checkpoint ZIP was changed. This report was first written outside the active tree for review before any installation. It is a later audit of checkpoint 11 and is not represented as a member of that unchanged archive. No new ZIP was created.
