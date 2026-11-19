# Mechanical replay and metadata audit through printed page 135

Frozen capture: **2026-11-19 02:18:27 UTC**. Eight files—the three TeX sources, `CORRECTIONS.tsv`, `CHECK_RECORD.md`, `progress.log`, `EXISTING_CORRECTIONS.tsv`, and `EVIDENCE_INDEX.md`—had identical hashes before capture, after capture, and in their private frozen copies. The evidence filename inventory was captured with them. The primary reader resumed mutations after this capture while proceeding to page 136.

## Exact replay and correction schema

**All 5,531 recorded replacements replay exactly onto the supplied original sources, and all three replayed TeX files are byte-for-byte identical to the frozen working sources.** The existing replay script was run unchanged against a private fresh extraction, requiring one exact old-text occurrence for each row.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,795 |
| corrected | 1,881 |
| English | 1,845 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,030 |
| typesetting | 2,745 |
| reading | 1,487 |
| translation | 130 |
| misprint of the original | 107 |
| terminology | 32 |

The ten-column correction schema is correct. No malformed row or empty required file, layer, old, new, evidence, kind, or confidence field was found.

## Evidence-reference metadata

References were extracted mechanically from the evidence columns of both ledgers and from `EVIDENCE_INDEX.md` and `CHECK_RECORD.md`. Across those four frozen files there are **1,218 distinct image/PDF filename references**. **Every reference has an existing file candidate; no missing file was found.** Explicit paths resolve directly. One bare source-asset basename remains ambiguous by filename alone, as described below.

Explicit evidence paths were checked against the captured filename inventory. Bare evidence basenames were resolved by filename only. The three explicitly named source-tree `front-matter.pdf` files exist and remain byte-for-byte identical to their supplied source-ZIP counterparts. The bare `front-matter.pdf` reference in frozen `CHECK_RECORD.md` lines 111, 123, and 135 has those three source-tree candidates, with **3 distinct SHA-256 values**. This audit records that basename ambiguity without choosing a layer or interpreting the differing file bytes. Each explicit source-tree path resolves and matches its own supplied original; the ambiguity does not establish that any asset is missing.


| Facsimile source asset | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/front-matter.pdf` | 3,490,226 | `84676a5f9af77cc427d0a17b056eebe0d8ead4cbd44a5f469cbb519d309733fe` |
| `sources/francais-corrige/front-matter.pdf` | 3,493,488 | `f66fa36c2d2dae409a378a6bfd1c47db109f892070f84ff764ed3b1214ebb048` |
| `sources/francais-diplomatique/front-matter.pdf` | 124,439 | `834d1f73ba61831dad8614a34392e6e50a83fa0d7d7dc5377deca1eb9dec19d1` |

No evidence image or facsimile content was inspected. File existence and byte identity do not certify that a referenced image supports an editorial reading.

## Coverage and timestamps

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page sections | Exactly one each for pages 1–135 |
| Active scan-page headings | Exactly one each for scan pages 1–153 |
| Numeric page/scan offsets | All satisfy scan page = printed page + 18 |
| Progress completion events | 136 historical events, 135 distinct numeric pages |
| Record/progress completion timestamps | All canonical numeric-page timestamps agree |
| Last completion | Page 135, 2026-11-19 02:17:57 UTC |
| Highest numeric correction page | 135 |

The preserved premature page 27 entry remains explicitly marked `PREMATURE ENTRY VOID`; the two historical page 27 completion events are retained. Excluding the voided heading leaves no scan-page gap or duplicate. No coverage or history was rewritten.

## Local source-difference provenance IDs

The frozen `EXISTING_CORRECTIONS.tsv` has 513 rows and the expected six-field record structure. No malformed record was found. The three new local IDs are unique and agree exactly with their recorded pages:

| Existing-correction row | Printed page | Local ID |
|---:|---:|---|
| 511 | 133 | `SUPPLIED-SOURCE-DIFF:I:p133` |
| 512 | 134 | `SUPPLIED-SOURCE-DIFF:I:p134` |
| 513 | 135 | `SUPPLIED-SOURCE-DIFF:I:p135` |

These `SUPPLIED-SOURCE-DIFF` IDs are local source-comparison provenance labels. As specified by the primary reader, they are deliberately distinct from supplied page-record identifiers: supplied page records are absent after printed page 132. Their absence from those supplied records is therefore not treated as a missing-reference failure. This audit checked only ID uniqueness, format, and page association; it did not inspect or adjudicate the diplomatic, corrected, or verdict content.

## Top-total summary at capture

The top totals are intentionally refreshed before timed checkpoints. In this frozen snapshot the top summary remains at 5,263 changes while the current ledger has 5,531, a difference of 268:

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,718 | 1,795 | +77 |
| corrected | 1,788 | 1,881 | +93 |
| English | 1,747 | 1,845 | +98 |
| build | 10 | 10 | +0 |
| **Total** | **5,263** | **5,531** | **+268** |

This preserved summary lag follows the primary reader’s stated checkpoint-refresh cadence; the audit uses the frozen ledger counts above. No total, status, page section, or completion event was refreshed by this audit.

## Source anchors and page markers

Each layer retains every original literal anchor occurrence: 356 labels, 355 body-page markers, six front-page markers, one PDF bookmark ID, and all 3,940 original literal hyperlink-target occurrences. The frozen hyperlink-target count is 3,943 because of the three inherited front-matter targets.

**Every inspected anchor/page-marker sequence remains identical to checkpoint 09.** The inherited front-target additions, source-position changes, and duplicate cover target are unchanged. No original ID occurrence is missing. The comparison extracts literal identifiers and excludes macro-parameter placeholders; it does not expand TeX or validate compiled PDF links.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,807 | `1be2391033544ec7b4db32099ff09d54e75e42bf962a57e2d916160c1242f380` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,715 | `ad168c6d6c977c5b34cdaeeadb275c96d0ad7daf567548640d759418b3d58900` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,585,068 | `85b1f8f404074454baeda9a6636a9ebc0b5d9e7d88b1af6440bad6a2148fb444` |

## Scope and preservation

This is a mechanical replay, schema, filename-resolution, provenance-ID, anchor-inventory, coverage, and timestamp audit of a frozen snapshot. It is **not a second visual reading**, a textual or mathematical verdict, a translation adjudication, a build check, or a claim that every necessary correction has been discovered. Recorded completion remains the primary reader’s review claim.

No live source, correction row, existing-correction verdict, `CHECK_RECORD.md`, reading question, progress log, total/status block, prior report, or frozen audit was changed. This new scoped report is the only active-tree addition. No ZIP was created.
