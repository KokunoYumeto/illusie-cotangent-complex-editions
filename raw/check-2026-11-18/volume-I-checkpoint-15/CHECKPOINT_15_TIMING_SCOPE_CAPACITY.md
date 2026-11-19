# Checkpoint 15 timing, scope and capacity advisory

Prepared **2026-11-19 04:56:09 UTC**. Inventory and count capture: **2026-11-19 04:54:30 UTC**. Independent ancillary privacy capture ended **2026-11-19 04:55:20 UTC**. These observations describe an actively changing work tree; refresh them at the due-time freeze. Historical checkpoint captures remain historical.

## Exact timing

Checkpoint15 is due **2026-11-19 05:29:37 UTC**. The current `scripts/package_checkpoint.py` derives this from the first line of `progress.log`, **2026-11-19 00:59:37 UTC**, plus `45 × (15 − 9)` minutes. Its non-dry-run path rejects creation before the due time. The script does not schedule or upload. Checkpoint16 is consequently due **06:14:37 UTC** on the same day; retain the fixed schedule rather than resetting it to upload completion time.

## Current scope and metadata

Progress records all printed pages **1–180**, with no gaps. The last completion is **p180 at 04:51:14 UTC**; its CHECK_RECORD heading maps to scan page **198**. **p181 is in progress** per the primary's instruction and has no completion, correction, or existing-correction verdict record at capture.

| Capture-time metadata | Count |
|---|---:|
| Corrections | 6770 |
| As-printed / corrected / English / build | 2122 / 2353 / 2285 / 10 |
| Existing-correction verdicts | 564 |
| Reading questions | 19 |
| Check events | 423 |

Kind counts: reading 1726; misprint of the original 125; translation 157; typesetting 3376; structure 1333; terminology 53.

**Top-summary refresh required:** README and the separate CHECK_RECORD coverage paragraph still record the checkpoint14 scope, through **p177 / scan195**, with **p178 in progress**. CHECK_RECORD's live total and layer table already agree with **6770** rows. README's nineteen-question count agrees at capture. `scripts/update_totals.py` updates only the marked live-total section; it does not refresh coverage, in-progress status, question count, verdict/event counts, or pending work.

## Capacity and exclusions

The current packaging functions completed a read-only plan: **1833 payload files**, **195741690 input bytes**, **one part**. The conservative bound including the reserved index is **197917492 bytes**, leaving **301082508 bytes** below the script's strict **499000000-byte** part limit. This bound is an estimate for planning, not an actual ZIP size. Free disk space at capture was **31721533440 bytes**. No checkpoint15 ZIP existed.

Explicit exclusions are the old root `FILE_LIST.tsv`, `scripts/__pycache__/*`, and **12 unreferenced p181 evidence crops**. The crop suffixes are `canonical`, `complex-sequence`, `conclusion`, `diagram`, `differentials-intro`, `differentials-sequence`, `double-star`, `factorization`, `flatness`, `hypotheses`, `morphism-intro`, and `star`, all under `evidence/I_p181_*.png`. This is a report-reference eligibility result; no images were opened. If the primary wants partial-work evidence preserved at freeze, the corresponding report must explicitly identify those relative paths or filenames.

All eligible current deliverables, including unchanged source layers and required assets, remain selected. The script excludes input scans, old/nested archives, runtime/vendor/cache trees, raw compiler logs and intermediates, and ordinary renders. It generates a fresh FILE_LIST inside the ZIP; the active root FILE_LIST and supplied source provenance manifest should not be rewritten to impersonate new provenance. Unsafe member paths and symlinks are rejected, payload hashes are checked on readback, and concurrent active-file changes abort packaging.

## Privacy and prior receipt continuity

The independent byte-pattern scan checked **132 ancillary metadata/script files (13349803 bytes)**, with stable before/after hashes, and found **zero concrete private local-path or email findings**. It checked **1833 eligible payload filenames** with no unsafe names, symlinks, or case collisions. Edition source content and all `sources/` content were excluded from this privacy scan; source prose, mathematics, scans, images, and PDF contents were not inspected. The classified TeX/regex syntax matches were not treated as actual paths.

Checkpoint14's existing local receipt and CHECKPOINTS row agree on its recorded save at **04:45:49 UTC**, size **161977766 bytes**, SHA-256 **206682f9df1d8ffb829866a3655cf60f26c984f2a59f123e86a2338b0ae9f4cc**, and file identities/version. Its receipt and independent integrity report are selected for checkpoint15. This only compares existing local metadata; it does not re-certify remote persistence or rerun the old audit.

## Next checkpoint obligations

1. At freeze, recapture the actual completed endpoint and the page then in progress. Refresh README, CHECK_RECORD's separate coverage/pending-work paragraph, live totals, question count and other displayed counters from that state. Do not promote partial work to completion. Preserve earlier timed captures.
2. Check a fresh plan using `python3 -B work/ILLUSIE_I_CHECK/scripts/package_checkpoint.py --number 15 --dry-run`. The totals mutator, if needed and authorized for the freeze, is `python3 -B work/ILLUSIE_I_CHECK/scripts/update_totals.py`.
3. **At or after 05:29:37 UTC**, pause active writes and run `python3 -B work/ILLUSIE_I_CHECK/scripts/package_checkpoint.py --number 15`. Do not overwrite or renumber any earlier archive. The expected single-part name is `ILLUSIE_I_CHECK_checkpoint_15.zip`; honor any split plan if the final payload has grown.
4. Verify the published archive size/hash and its generated FILE_LIST against that immutable snapshot. Preserve every required part and save every part through the established upload helper. Archive creation alone is not a successful save.
5. After actual successful saving, record the returned file identities, version, exact ZIP bytes/hash, helper outcome, and actual `save_success_recorded_utc` in the new receipt, checkpoint register and progress log. Do not invent an earlier timestamp. A post-save receipt belongs to the active tree and next checkpoint; do not repack the immutable checkpoint merely to insert its own receipt.

Supporting capture files in this directory: `checkpoint15_metadata_20261119.json` and `checkpoint15_ancillary_privacy.json`. This advisory was written outside the active deliverable tree. No active source, ledger, report or archive was changed; no packaging or upload was performed.

## Actual checkpoint timing

The scheduled boundary was 2026-11-19 05:29:37 UTC. The first clock check after context restoration was 05:30:33 UTC, so packaging began after the scheduled boundary. The package records its actual creation time; no timestamp is backdated. The completed boundary remains printed 188 / scan 206, with 7,230 correction rows. Printed 189 has only its three source regions read; complete scan viewing, details, decisions, edits, and completion remain pending. The refreshed mechanical prepack report was personally read and installed before packaging.
