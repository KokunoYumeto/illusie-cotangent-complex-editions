# Checkpoint 14 mechanical prepack advisory

Metadata captured 2026-11-19 04:43:04 UTC; advisory prepared 2026-11-19 04:43:39 UTC. Counts are capture-time observations from an actively changing tree.

## Timing and scope

- Due exactly **2026-11-19 04:44:37 UTC**. This inspection created no archive and performed no upload.
- Progress metadata records printed pages **1–177** complete, with no gaps; latest completion is p177 at **04:40:17 UTC**. Printed **p178 remains in progress**, with zero p178 completion, correction, or existing-correction verdict rows at capture.
- README and the top CHECK_RECORD coverage paragraph now agree on completion through printed p177 / scan195 and p178 in progress. The root replay audit through p176 is present. These are metadata checks, not a certification of page reading or mathematical content.
- The completion log contains a historical duplicate completion marker; details below. Distinct completed positive pages remain 177.

## Capture-time counts

| Metadata | Count |
|---|---:|
| Correction rows | 6624 |
| As-printed layer | 2099 |
| Corrected layer | 2288 |
| English layer | 2227 |
| Build layer | 10 |
| Existing-correction verdicts | 561 |
| Reading questions | 19 |
| Check events | 416 |

Kinds: structure 1295; typesetting 3314; reading 1684; translation 154; misprint of the original 125; terminology 52.

## Packaging and privacy

The read-only command `python3 -B work/ILLUSIE_I_CHECK/scripts/package_checkpoint.py --number 14 --dry-run` exited 0: **1793 payload files**, **191244141 input bytes**, **one planned ZIP part**. The script enforces a strict part size below 499000000 bytes, rejects early packaging, includes unchanged files, checks each payload hash on readback, and rejects concurrent changes. Free space at capture: 31943823360 bytes.

Only two explicit exclusions were reported: the prior generated `FILE_LIST.tsv`, which is regenerated inside the ZIP, and `scripts/__pycache__/*`. No unreferenced evidence image exclusion appeared in this plan. No checkpoint14 ZIP existed at capture.

A boundary-aware mechanical scan of **54 active ancillary metadata/script files** found **zero concrete private local-path or email matches**. Source text and image/PDF contents were not reviewed. Existing save receipt JSON files for checkpoints12 and13 are present. This preflight does not establish a new remote save.

## Freeze-time checklist

At or after the exact due time, capture the final endpoint and counts again, run `scripts/update_totals.py` if needed, and reconcile README, top CHECK_RECORD coverage, the live totals block, and the question count with that frozen state. Preserve p178 as in progress unless the primary has finished and recorded it. Freeze all active writes during actual packaging; retain the generated FILE_LIST and verify the resulting ZIP identity. Record the actual successful save receipt only after the upload has succeeded; carry it into the next checkpoint without rewriting the immutable archive.

Historical duplicate completion metadata: {"27": ["2026-11-18 15:25:32 UTC", "2026-11-18 15:26:17 UTC"]}

No active source, ledger, report, or checkpoint was modified by this check.
