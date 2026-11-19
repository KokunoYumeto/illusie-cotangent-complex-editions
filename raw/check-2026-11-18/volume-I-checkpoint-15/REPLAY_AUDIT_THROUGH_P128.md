# Mechanical replay and coverage audit through printed page 128

Frozen capture: **2026-11-19 02:02:00 UTC**. Six files—the three TeX sources, `CORRECTIONS.tsv`, `CHECK_RECORD.md`, and `progress.log`—had matching hashes before capture, after capture, and in their private frozen copies. The primary reader continued page 129 after capture. This report applies only to the frozen state.

## Exact replay and ledger structure

**All 5,402 recorded replacements replay exactly, and all three resulting TeX sources are byte-for-byte identical to the frozen working sources.** The unchanged existing replay script used a separate fresh extraction of `ILLUSIE_I_sources.zip` and required exactly one old-text occurrence for every row.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,759 |
| corrected | 1,837 |
| English | 1,796 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 982 |
| typesetting | 2,698 |
| reading | 1,468 |
| translation | 130 |
| misprint of the original | 105 |
| terminology | 19 |

The ten-column schema matches the required header. No malformed row or empty required file, layer, old, new, evidence, kind, or confidence field was found.

## Evidence references

The frozen ledger contains 139 distinct image/PDF filename references: 136 explicit evidence paths, 2 uniquely resolved evidence basenames, and 1 supplied input PDF references. **No unresolved filename reference was found.** Reference matching used complete extracted filename tokens and the captured evidence-file inventory.

No image content was inspected. File existence does not certify that an image supports its associated reading.

## Coverage metadata

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page sections | Exactly one each for pages 1–128 |
| Active scan-page headings | Exactly one each for scan pages 1–146 |
| Printed-to-scan mapping | Every numeric page maps to scan page = printed page + 18 |
| Numeric completion events | 129 historical events for 128 distinct pages |
| Canonical record versus progress timestamps | Every numeric page agrees |
| Last completion | Page 128, 2026-11-19 01:59:22 UTC |
| Highest numeric page in the correction ledger | 128 |

The raw scan-heading count is 147 because it includes the preserved heading `### 27 (scan PDF page 45) — PREMATURE ENTRY VOID`, followed by the canonical page 27 record. The progress log likewise retains page 27 completion events at 15:25:32 UTC and 15:26:17 UTC on 18 November 2026. These historical entries are identical to checkpoint 09. Excluding the explicitly voided heading gives 146 active scan records with no gaps or duplicates. No history was altered.

## Top-total summary lag at the frozen capture

The frozen top live-totals block still shows the earlier **5,263-row** state, while the frozen ledger contains **5,402 rows**. The exact differences are:

| Layer | Top summary | Frozen ledger | Difference |
|---|---:|---:|---:|
| as-printed | 1,718 | 1,759 | +41 |
| corrected | 1,788 | 1,837 | +49 |
| English | 1,747 | 1,796 | +49 |
| build | 10 | 10 | +0 |
| **Total** | **5,263** | **5,402** | **+139** |

After this mechanical difference was reported, the primary reader confirmed that the top totals/status are intentionally refreshed before timed checkpoints; individual page sections and the ledger are current. The reader will refresh the top totals before checkpoint 11. The audit preserves the frozen mismatch transparently and does not treat the older summary as the current ledger count. No summary or status was changed by this audit.

## Source anchors and page markers

Literal IDs from `label`, `hypertarget`, `pdfbookmark`, `illusiefrontpage`, and `illusiebodypage` were compared against both the original release sources and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. Each layer retains all 356 labels, 355 body-page markers, six front-page markers, one PDF bookmark ID, and all 3,940 original literal hyperlink-target occurrences. The frozen target count is 3,943 because of three inherited front-page targets.

**Every inspected anchor/page-marker sequence is identical to checkpoint 09.** The inherited front-target additions, target-position changes, and duplicate cover target remain as recorded in the earlier inventory audit. No original identifier occurrence is missing, and this continuation has introduced no difference in those sequences. This lexical comparison does not perform TeX expansion or validate compiled PDF links.

## Frozen source hashes

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,539,018 | `2fee24b9dd5d7b8685d6428d2a4511241a0c8a1a232b41a1b2879defedc7a22e` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,942 | `0fa19506359bbc8873d57db22ae3be325f50f0c86dd0e714203708257c333f9d` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,585,323 | `965de744b8c6c5dfca858cd52a75e653379c107cdad511f33bccc8f26cc0fc37` |

## Scope and preservation

This audit checks exact edit replay, schema, filename existence, literal identifier preservation, and consistency of recorded coverage metadata. It does **not** read or decide page text or mathematics, constitute a second visual reading, assess translations, compile the edition, or certify that every necessary correction has been found. Recorded completion events remain the primary reader’s claims of completed review.

No live source, correction row, existing-correction verdict, `CHECK_RECORD.md`, reading question, progress log, page-status record, or previous audit report was changed. This scoped report is the only active-tree addition. No ZIP was created.
