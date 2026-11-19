# Infrastructure changes for the 19 November continuation

This records packaging and restoration infrastructure only. No page reading, correction verdict, or mathematical check is implied.

## Checkpoint cadence

The current `scripts/package_checkpoint.py` now follows the continuation's required 45-minute cadence. Checkpoint numbering begins at 10; numbers below 10 are refused. The due time is the first UTC line of `progress.log` plus `45 × (number − 9)` minutes. With the continuation start `2026-11-19 00:59:37 UTC`, checkpoint 10 is due at `2026-11-19 01:44:37 UTC` and checkpoint 11 at `2026-11-19 02:29:37 UTC`.

A premature creation request now stops before reading the deliverable tree. The explicit dry-run mode remains available for planning and creates no archive. `scripts/PACKAGING.md` documents the new invocation and schedule. Earlier checkpoint archives, records, and script history were left intact.

The existing safeguards remain: exclusive creation without overwriting, monotonically increasing local checkpoint numbers, complete current deliverables, report-referenced evidence crops, no nested archives or supplied authority scans, conservative partitioning, a strict 499,000,000-byte ceiling for each ZIP, post-write SHA-256 checks, and rejection of files changed during packaging. The directory exclusions additionally name `input` and `inputs`.

## Restoration script

The final verified `infrastructure_restore.py` was copied from staging into `scripts/`. Its restoration destinations use the deliverable names `ILLUSIE_I_CHECK` and `ILLUSIE_II_CHECK`. It verifies all eight supplied ZIPs and their root indexes before extraction and refuses to overwrite different existing files.

## Validation

Python syntax passed. Direct schedule checks returned checkpoint 10 at 01:44:37 UTC, checkpoint 11 at 02:29:37 UTC, and checkpoint 12 at 03:14:37 UTC on 19 November 2026. Checkpoint 09 was rejected. A live attempt to invoke checkpoint 10 before its due time was refused by the early guard; no ZIP was created and no page/source/correction-ledger content was read for this validation. The copied restoration script is byte-for-byte identical to the staged final version.

Volume II's packaging infrastructure was left untouched pending its part of the task.

2026-11-19 05:26:37 UTC: Primary read and installed the read-only correction-review queue generator, its synthetic tests and documentation. Exact original fields and all rows are preserved, with stable original-row digests; no active queue was generated. It is reserved for the mandatory final second reading after all Volume I pages. Installed the fully read frozen through185 replay report and the separately scoped checkpoint15 ancillary metadata advisory.
