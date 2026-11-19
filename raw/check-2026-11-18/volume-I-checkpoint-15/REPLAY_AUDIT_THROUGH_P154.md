# Mechanical replay, evidence, and privacy audit through printed page 154

Frozen capture: **2026-11-19 03:14:21 UTC**. A private snapshot captured **98** source, ledger, report, metadata, and script text files, with matching hashes before capture, after capture, and in the copied files. An evidence/source-asset filename inventory was captured with them. All claims below refer to this state, before later primary-reader status/progress updates or checkpoint-12 receipt additions.

This report was prepared independently while scheduled packaging proceeded. It is an audit of the frozen working snapshot, not a claim to have re-audited checkpoint 12 or its subsequent durable save.

## Exact replay and schema

**All 5,929 correction rows replay exactly onto a fresh extraction of the supplied original Volume I sources. All three replayed TeX files are byte-for-byte identical to the frozen working sources.** The captured existing replay script was used unchanged and required exactly one old-text occurrence for each recorded replacement.

| Layer | Frozen ledger rows |
|---|---:|
| as-printed | 1,910 |
| corrected | 2,024 |
| English | 1,985 |
| build | 10 |

| Kind | Rows |
|---|---:|
| structure | 1,150 |
| typesetting | 2,943 |
| reading | 1,537 |
| translation | 135 |
| misprint of the original | 115 |
| terminology | 49 |

The ten-column header matches the required correction schema. No malformed row, empty required field, or unknown correction kind was found. The numeric top-total block agrees with the frozen ledger in every layer/kind cell and in the total of **5,929**. This does not retroactively incorporate any narrative-status update made after capture.

## Explicit evidence references

All **1,389 explicit image/PDF paths** extracted from the evidence columns of the correction and existing-correction ledgers, plus `CHECK_RECORD.md` and `EVIDENCE_INDEX.md`, resolve in the captured evidence/source-asset filename inventory. No missing explicit reference was found.

Only path existence was assessed. No scan, crop, facsimile, book text, or mathematical meaning was inspected or adjudicated.

## Completion consistency

| Metadata check | Frozen result |
|---|---|
| Canonical printed-page records | Exactly pages 1–154 |
| Active scan-page records | Exactly scan pages 1–172 |
| Printed-to-scan offsets | All equal printed page + 18 |
| Canonical record/progress completion timestamps | All agree |
| Last completion | Page 154, 2026-11-19 03:12:48 UTC |
| Completion metadata beyond page 154 | None |
| Numeric correction rows beyond page 154 | None |

Page 155 is excluded from completion claims. The inherited explicitly voided premature page-27 record and its historical duplicate completion event remain preserved; active scan counts exclude that voided heading. No page was marked or reclassified by this audit.

## Anchor and page-marker preservation

Literal labels, hyperlink targets, bookmark IDs, and source-page markers were compared with the original release sources and checkpoint 09. Macro-parameter placeholders containing `#` were excluded. The following counts apply to each layer:

| Identifier class | Original occurrences | Frozen occurrences | Missing original occurrences |
|---|---:|---:|---:|
| labels | 356 | 356 | 0 |
| hypertargets | 3,940 | 3,943 | 0 |
| pdfbookmark_ids | 1 | 1 | 0 |
| front_page_markers | 6 | 6 | 0 |
| body_page_markers | 355 | 355 | 0 |

**Every inspected identifier sequence is identical to checkpoint 09 in all three layers.** No original occurrence is missing. Inherited front-target additions, target-position changes, and the cover duplicate remain baseline exceptions. This is a lexical inventory, without TeX expansion or compiled-link testing.

## Text privacy comparison with checkpoint 09

The captured text files were screened mechanically for email-address patterns, file URIs, common Unix absolute-path prefixes, and Windows drive-path patterns. The same screening was applied to checkpoint 09 text for comparison.

| Screening result | Finding |
|---|---|
| Email-address pattern matches | None |
| File-URI pattern matches | None |
| New Windows-style token values versus checkpoint 09 | None |
| Broad Windows-pattern matches | 188 occurrences; inherited TeX syntax matches |
| New Unix-path-shaped token | One generic interpreter-launch shebang in `scripts/infrastructure_restore.py`, line 1 |

The shebang is generic interpreter syntax, **not an environment-specific local or private workspace path**. The primary reader confirmed this distinction and instructed that it remain unchanged. No new environment-specific path or email identifier was identified by this screening. The broad Windows-pattern matches are inherited lexical false positives from TeX syntax; no mathematical interpretation was performed.

This is a pattern-based text screen. It does not inspect image pixels, binary metadata, or every possible encoding of private information. No source, script, or report was modified or redacted by this audit.

## Retrospective checkpoint-receipt metadata

The captured `CHECKPOINTS.tsv` contains the checkpoint-10 and checkpoint-11 receipt rows with record timestamp **2026-11-19 03:13:18 UTC**. The captured progress log explicitly labels both entries as retrospective at that time. The rows are structurally complete, and their recorded archive sizes and SHA-256 values agree with the corresponding existing local checkpoint ZIPs.

These checks preserve the distinction between recording earlier save receipts and performing a new save. This audit did not repeat or independently validate the remote durable-save operations. Later checkpoint-12 receipt metadata is outside the frozen snapshot and is not imported into this report.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,355 | `8f6d3f24b270a14ab2349231b97a1d69395fb822d237460d4e5be8045cdd0e3c` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,249 | `a3b4d5877f6c04a89b1a97e3c2da3dae1c3bad8f56f2abe2c87072832791802a` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,447 | `7c5365dc1b1e2cd7d2e06bb0738ab404a6a609087b20cecdaae634035f1c7260` |

## Scope and handling

This is a mechanical exact-replay, schema, explicit-path, identifier, completion/timestamp, receipt-metadata, and text-privacy audit. It is **not a visual reading**, textual or mathematical verdict, translation review, second reading of correction evidence, or PDF/build certification. Recorded completion remains the primary reader’s account of work performed.

No active source, ledger, verdict, report, question, progress/status record, checkpoint ZIP, or other active file was changed. Historical reports retain their own counts and capture states. No page was marked complete. No Volume II material was read. This report was first written in staging for the primary reader’s review and authorized installation.
