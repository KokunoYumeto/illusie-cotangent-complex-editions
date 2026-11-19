# Checkpoint 15 mechanical prepack audit

Prepared **2026-11-19 05:29:00 UTC** for checkpoint 15 due **2026-11-19 05:29:37 UTC**.

**PASS for the requested frozen replay, metadata, count, and reference checks.** The refreshed snapshot was captured **2026-11-19 05:27:50 UTC**, within **05:27:50.318840–05:27:50.438640 UTC**. All 13 core source/ledger/report/history files have equal before-capture, after-capture, frozen, and post-audit hashes. The earlier 05:26:25 snapshot is preserved unchanged.

## Frozen boundary and counts

| Item | Result |
|---|---:|
| Completed printed pages | 1–188 |
| Active scan-page records | 1–206 |
| Last recorded completion | Page 188, 2026-11-19 05:25:29 UTC |
| Correction rows | **7,230** |
| Reading questions | 19 |
| Existing-correction records | 577 |
| Check events | 448 |
| Layer rows: as-printed / corrected / English / build | 2,224 / 2,526 / 2,470 / 10 |

All expected record schemas and numeric layer/kind totals agree. Canonical page coverage has no gaps, incorrect offsets, or timestamp disagreements. Completion records are unchanged from the first prepack snapshot: no new canonical completion was introduced by the nine-row follow-up. The inherited voided page 27 history remains preserved.

**Both refreshed top summaries now state 188/206.** No correction, existing-correction, or canonical completion record extends beyond page 188.

## Exact incremental replay

| Baseline | Appended rows | Result |
|---|---:|---|
| Frozen through185 | 168 | All three refreshed sources exact |
| Immutable checkpoint14 | 606 | All three refreshed sources exact |
| Initial prepack snapshot at 05:26:25 | 9 | All three refreshed sources exact |

Every appended old-byte value matches exactly once. All prior CORRECTIONS, EXISTING_CORRECTIONS, and CHECK_EVENTS field values remain unchanged against all three baselines. The 19-question file is byte-identical to each baseline.

The nine follow-up rows are **7222–7230**, all recorded as **typesetting**: page 186 has one per layer, and page 187 has two per layer. They are included in the 7,230 total. The updated through185 delta is:

| Page | As-printed | Corrected | English | Total |
|---:|---:|---:|---:|---:|
| 186 | 16 | 20 | 23 | 59 |
| 187 | 13 | 20 | 26 | 59 |
| 188 | 11 | 16 | 23 | 50 |
| **Total** | **40** | **56** | **72** | **168** |

This prepack check verifies incremental byte provenance. The earlier through185 report supplies the full original-source replay baseline; no new full-original replay or editorial assessment is claimed here.

## Evidence and frozen identities

All **1,783 explicit evidence/source-asset paths** resolve. All **1,809 operational image/PDF filename references** resolve to captured exact/relative/basename candidates or the existing separately supplied scan authority. No image or PDF content was opened.

| Frozen item | SHA-256 |
|---|---|
| Correction ledger | `df508481265a036d47ae6c2b7309493f100c073a6883381ca2a0b6214762f281` |
| English source | `4201511252755a1aa2eb31c8d8e5dcde109ea2083a4604555de9928d37775d14` |
| Corrected French source | `8aff908d47a348b822b544546bea0ab5b0b5e5715965fda77b8e1a13845ee5d9` |
| As-printed French source | `25286aa53e7195750e565abbab8e6754ed6cbb1f24d3b6706ab9b290deec4786` |

These source hashes equal all three incremental replay results. The checkpoint14 baseline retains its verified SHA-256 `206682f9df1d8ffb829866a3655cf60f26c984f2a59f123e86a2338b0ae9f4cc`.

## Scope

Only the coherent frozen core was checked. This report does not certify later live changes, infrastructure outside the captured core, a future ZIP, source meaning, mathematical correctness, translation, or any visual/second reading. No active files were edited and no historical editing script was executed. Volume II was untouched. No package or upload was created. The report is staged for primary review and installation.
