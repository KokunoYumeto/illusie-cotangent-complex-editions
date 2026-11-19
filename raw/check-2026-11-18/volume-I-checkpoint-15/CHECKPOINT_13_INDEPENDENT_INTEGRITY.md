# Independent checkpoint 13 integrity verification

**Verification capture:** 2026-11-19 04:02:04 UTC.

Local, read-only verification of the immutable archive, its manifest, and recorded metadata. No scan, substantive passage, mathematics, or Volume II content was reviewed. No active file or archive was changed, and no upload or new remote verification was performed.

## Archive identity and manifest

| Item | Verified value |
|---|---|
| Archive | `ILLUSIE_I_CHECK_checkpoint_13.zip` |
| Compressed bytes | **149,257,513** |
| SHA-256 | `fe1cade8f00773892b6675d8052260d008940465fb48512046a70b8f49c62333` |
| Included payloads | **1,652** |
| Total ZIP members | **1,653**, including the generated index |
| Sum of included payload bytes | **177,624,560** |
| Parts | **One**, below the strict 499,000,000-byte ceiling |
| Manifest creation time | **2026-11-19 03:59:53 UTC** |
| Scheduled due time in manifest | **2026-11-19 03:59:37 UTC** |

Every included payload was read completely from the ZIP and compared with its in-archive `FILE_LIST.tsv` entry. **All sizes, SHA-256 values, and part assignments matched.** Member reads completed their CRC checks. There were zero missing, unexpected, duplicate, unsafe, or symlink members and zero prior-checkpoint dependencies. The manifest's index entry correctly has no self-hash.

No nested archive, supplied scan/input tree, runtime/vendor/cache tree, or raw runtime log was present among the payloads. The explicit discovered-file exclusions are the old root `FILE_LIST.tsv` and unreferenced `evidence/I_p160_derivation.png`. The crop was not inspected; this report verifies only the recorded exclusion rule and filename.

## Recorded scope and current summaries

The archived README and top check-record status consistently state completion through **printed page 167 / scan page 185** and that **printed page 168 has not yet been begun**.

Every numbered page from 1 through 167 has a completion-log entry and a page-record heading. The last numbered completion is:

`page 167 done 2026-11-19 03:59:25 UTC`

There is no page-168 completion entry or heading and no correction row whose explicit printed-page locator names or numerically ranges across page 168. These are metadata checks, not a new certification of the primary reading.

The correction ledger contains **6,230 rows**. The displayed total and every layer/kind cell in the live table agree with the ledger. Layer totals are as-printed **1,998**, corrected **2,130**, English **2,092**, and build **10**. The question ledger has **18 rows**, agreeing with the question counts in both current top summaries. No stale completion endpoint or live-total mismatch was found in those current summaries; historical receipts and replay reports retain their earlier scopes.

## Mechanical privacy inspection

The scan covered **116 text members** and metadata from **six source-asset PDFs**. Boundary-aware local-path and email checks found no environment-specific absolute local path or email address. Seventy-eight broad Windows-style token matches were recognized as TeX command syntax; no mathematical meaning was assessed. Image pixels and PDF page text were not inspected, so this is not a visual privacy certification.

## Recorded save receipt

After the primary supplied the successful-save receipt, the active `CHECKPOINT_13_SAVE_RECEIPT.json`, its active `CHECKPOINTS.tsv` row, and the local archive identity attributes were compared. Their identifiers, bytes, hash, version, and recorded time agree:

- Library file ID: `libfile_fde3_f-0987a668970c81918b9e9d1d35d611f9_3de54532f60c8191850458563edee173`.
- File ID: `file_000000007c9c82128faa07fdeecec47e`.
- Version: **0**.
- Recorded success: **2026-11-19 04:00:43 UTC**.
- Receipt fields: helper exit **0**, per-file status **succeeded**, and successful local identity writeback.

The immutable archive contains prior receipt rows through checkpoint 12. Its own save receipt postdates packaging and was not repacked into checkpoint 13. Receipt comparison establishes local consistency with the primary's recorded result; no remote service was contacted by this verifier.

**Result:** all listed identity, manifest, size, exclusion, recorded-scope, live-total, privacy-pattern, and local receipt-consistency checks passed.

