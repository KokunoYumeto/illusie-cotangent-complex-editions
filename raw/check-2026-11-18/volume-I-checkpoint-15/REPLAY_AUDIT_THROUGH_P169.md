# Frozen mechanical integrity audit through recorded printed page 169

Capture boundary: **2026-11-19 04:10:33 UTC**. Eleven source, ledger, report, README, checkpoint-metadata, and replay-script files were copied into a private snapshot, with identical hashes before capture, after capture, and in the copied files. The evidence/source-asset filename inventory was captured with them. No numeric correction row or recorded completion beyond page 169 exists in this snapshot; subsequent work is excluded.

This audit checks byte accountability and metadata consistency only. It does not review author text, mathematical statements, translation, or images, and does not certify a first or second reading.

## Full exact replay and correction schema

**All 6,319 correction rows replay exactly onto a fresh extraction of the immutable supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The captured existing replay script was used unchanged, requiring one exact old-text occurrence for each replacement.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 2,026 |
| corrected | 2,163 |
| English | 2,120 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,226 |
| typesetting | 3,189 |
| reading | 1,582 |
| translation | 145 |
| misprint of the original | 125 |
| terminology | 52 |

The ten-column schema matches the required header. No malformed row, empty required field, or unknown correction kind was found. The refreshed numeric top table agrees with every layer/kind cell and with the total of **6,319**.

## Complete accounting for the page-168/169 source changes

The first **6,230 ledger-row values are unchanged** from the frozen through-167 snapshot of 2026-11-19 04:00:09 UTC. Exactly **89 rows** were appended, and all are associated with pages 168 and 169:

| Printed page | As-printed | Corrected | English | Appended rows |
|---:|---:|---:|---:|---:|
| 168 | 17 | 16 | 17 | 50 |
| 169 | 11 | 17 | 11 | 39 |
| **Total** | **28** | **33** | **28** | **89** |

As a separate incremental check, the unchanged replay script applied only these 89 rows to private copies of the frozen through-167 sources. **The resulting files match the through-169 frozen sources byte for byte in all three layers.** Thus every source-byte change since that earlier snapshot is accounted for by these appended rows. No appended row has identical old/new strings.

This is mechanical source-change accounting, without adjudicating the correctness, meaning, translation, or evidence of any replacement.

## Explicit evidence-reference existence

All **1,557 explicit image/PDF paths** extracted from the evidence fields of both ledgers and from `CHECK_RECORD.md` and `EVIDENCE_INDEX.md` resolve in the captured evidence/source-asset filename inventory. There are no missing explicit references.

No scan, crop, facsimile, or other image was inspected. Filename existence does not establish that a file supports the associated editorial decision.

## Recorded progress and chronology

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page records | Exactly 1–169, in order |
| Active scan-page records | Exactly 1–187 |
| Printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress timestamps | All agree |
| Last recorded completion | Page 169, 2026-11-19 04:10:10 UTC |
| Numeric completion events | 170 historical events for 169 distinct pages |
| Timestamp or page-number regressions | None |
| Completion timestamps after capture | None |
| Completion/correction metadata beyond page 169 | None |

The explicitly voided premature page-27 record and its duplicate historical completion event remain preserved. The active scan count excludes that voided heading.

## Deliberately historical checkpoint endpoint prose

As specified by the primary reader, the README and top endpoint prose continue to describe **checkpoint 13’s through-page-167 state** until scheduled checkpoint 14. That prose is deliberately historical snapshot wording. It is not a claim that the subsequent page-168/169 work was lost or incomplete.

The current detailed page records and progress log consistently record completion through page 169, and the numeric table has already been refreshed to 6,319. The prose snapshot, current numeric counts, and detailed completion records therefore have different stated update scopes. This audit leaves them unchanged and does not treat the historical endpoint wording as a completion gap.

## Exact identifier preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared with the supplied originals and checkpoint 09, excluding macro-parameter placeholders containing `#`. Counts below apply to each source layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** Consequently it also remains identical to the already-verified through-167 inventory. No original identifier occurrence is missing, and the new page-168/169 edits introduced no identifier-sequence change. Inherited front-target additions, target-position changes, and the cover duplicate remain baseline exceptions. This lexical inventory does not expand TeX or validate compiled links.

## Capture and replay hashes

Each value below is identical before capture, after capture, and in the frozen copy. For the three sources it also equals both the full replay result and the incremental replay result.

| File | Identical SHA-256 |
|---|---|
| `CORRECTIONS.tsv` | `10ce7e83b8b9f4738c99eb93f5ebc22d2a60091fc19a014465e58f08bfd5ae51` |
| `sources/english/02-volume-I-english.tex` | `ddf4279c2752c67377bce6250542edbb1a4f8b33e4b87bcd7f649956e733c906` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | `9db1a199e122ae0a5f24658e07502f5d86e49c7e4b1f4e363b704ef7b4ced51d` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | `cf23e3f0c3ec3592a6d15375d2c15a1c08cb0f4216e1d509732c5ba8f7b9c782` |

## Scope and handling

This is an infrastructure-only replay, schema, explicit-reference, identifier, count, chronology, and source-hash audit. It makes no author-text, mathematical, translation, image, first-reading, second-reading, or PDF/build certification.

No active source, ledger, verdict, report, README, question, progress/status record, historical audit, or checkpoint ZIP was changed. No page was marked or reclassified. No Volume II material was read. This report was first written under staging for primary-reader inspection and authorized installation. No checkpoint was created or uploaded.
