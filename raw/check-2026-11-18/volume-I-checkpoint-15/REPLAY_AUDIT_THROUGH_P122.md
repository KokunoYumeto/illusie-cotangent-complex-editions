# Mechanical replay audit through printed page 122

Frozen capture: **2026-11-19 01:43:05 UTC**. The primary reader identified this state as complete through printed page 122, with its last completion at 01:42:12 UTC. This report applies to that private frozen snapshot; primary reading and later live edits may have continued afterward. Page-reading coverage is supplied by the primary reader, not independently certified here.

## Exact replay and schema

**Replay passed for 5,263 correction rows.** The unchanged existing replay script applied the frozen ledger to a fresh extraction of `ILLUSIE_I_sources.zip`, requiring exactly one old-text occurrence for each row. All three resulting source files are byte-for-byte identical to the frozen source files.

| Layer | Rows |
|---|---:|
| as-printed | 1,718 |
| corrected | 1,788 |
| English | 1,747 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 943 |
| typesetting | 2,631 |
| reading | 1,449 |
| translation | 130 |
| misprint of the original | 100 |
| terminology | 10 |

The ten-column header matches the required schema. Malformed rows: 0. Rows with empty required file, layer, old, new, evidence, kind, or confidence fields: 0.

## Evidence filename resolution

The frozen ledger contains **116 distinct image/PDF filename references**: **113 explicit evidence paths**, 2 uniquely resolved evidence basenames, and 1 supplied input PDF references. Unresolved literal references: **0**. Reference-to-row mapping uses exact extracted filename tokens, so a short filename cannot spuriously match inside an already complete path.

File existence was checked against the captured filename inventory. Image content was not inspected. No evidence-reference repair was made by this audit.

## Source-anchor and page-marker inventory

Literal identifiers were extracted from `label`, `hypertarget`, `pdfbookmark`, `illusiefrontpage`, and `illusiebodypage`; macro-parameter placeholders containing `#` were excluded. This is a lexical inventory without TeX expansion or compilation. Counts below apply to each source layer.

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

All five identifier sequences in all three layers are identical to checkpoint 09. Every original identifier occurrence is retained. The original-to-frozen hyperlink-target differences remain the inherited three front targets `illusie:I:front:p007`, `illusie:I:front:p008`, and `illusie:I:front:p009`, plus inherited source-position changes. The original cover target duplicate remains unchanged. No new identifier inventory or sequence difference from checkpoint 09 was found.

## Frozen source hashes

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,539,253 | `57a7563a0641061a453a7f6bc3ca37f60aad58c3e1174e61048b501754add2a2` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,567,247 | `ce1de98330bea23769c68e9c353c0d2b0ba74bbabb30a584f7aa0ba42437d6c2` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,585,647 | `1fb5538a94fc54b80be8bcfb80e5269698f6e77aa3696e1679f9901487cc44d2` |

## Consistency and limitations

The four captured files had identical SHA-256 hashes before capture, after capture, and in their frozen copies. Replay and anchor checks used those copies, not subsequent live state.

This audit establishes mechanical edit accountability, ledger structure, filename existence, and literal identifier preservation. It is **not a second visual reading**, textual adjudication, mathematical proof check, translation review, PDF/build check, or assurance that every necessary correction has been found. Existing files are not thereby certified as evidence for the associated readings.

No live source, correction ledger, prior audit report, progress log, or page-status record was changed. This new scoped report is the only active-tree addition. No ZIP was created. Checkpoint 10 remains due at 2026-11-19 01:44:37 UTC.
