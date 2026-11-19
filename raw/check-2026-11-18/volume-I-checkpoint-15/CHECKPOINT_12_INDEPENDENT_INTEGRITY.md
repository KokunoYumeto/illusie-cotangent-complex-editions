# Independent checkpoint 12 integrity verification

**Verification capture:** 2026-11-19 03:22:52 UTC.

This is a local verification of the immutable archive and its recorded receipt metadata. No book image, substantive passage, or mathematics was assessed. No active file or archive was altered, and no remote save was repeated or independently recertified.

## Archive identity

- Archive: `ILLUSIE_I_CHECK_checkpoint_12.zip`.
- Size: **131,079,088 bytes**, below the strict 499,000,000-byte part limit.
- SHA-256: `7708f54cf2d95121f5c0ece5c48c97fbc1d89625a25a4a54306ac6997ec50676`.
- Manifest creation time: **2026-11-19 03:14:42 UTC**.
- Scheduled due time recorded in the manifest: **2026-11-19 03:14:37 UTC**.
- Parts: **one**, with every included file assigned to that archive.

## File-list and exclusion checks

All **1,492 included payloads** were read completely from the ZIP and compared with `FILE_LIST.tsv`: every byte count, SHA-256, and part assignment matched. ZIP member reads also completed their CRC checks. Together with the generated index, the archive contains **1,493 members**.

There were **zero** missing, unexpected, duplicate, unsafe, or symlink members; **zero** file-list mismatches; and **zero** prior-checkpoint dependencies. No nested archive, supplied input/scans tree, runtime/vendor tree, bytecode cache, or raw runtime log was included. The generated index has the documented no-self-hash status.

The only explicit discovered-file exclusion in this frozen manifest is the prior root `FILE_LIST.tsv`, replaced inside the archive by the newly generated index. No unreferenced preview-crop exclusion remains in this frozen list. Scope-category rows retain the packager's general exclusions.

## Recorded reading scope

The archived `README.md`, top status of `CHECK_RECORD.md`, and `progress.log` agree on completed first-reading coverage through **printed page 154 / scan page 172**. Every numbered page from 1 through 154 has both a page-record heading and a completion-log entry. The last numbered completion is:

`page 154 done 2026-11-19 03:12:48 UTC`

The archived status explicitly says: **“Printed p. 155 is in progress; no completion is claimed.”**

- No page-155 completion-log entry or completion heading is present.
- The archive contains **5,929 correction rows**, with **zero** rows whose explicit printed-page locator names or numerically ranges across page 155.
- There are **zero** existing-correction verdict rows explicitly located on page 155.

These checks establish consistency of the recorded scope. They do not independently certify the primary review, translation, or mathematics.

## Receipt comparison

The archive's name, bytes, and SHA-256 agree with the active `CHECKPOINT_12_SAVE_RECEIPT.json` and the checkpoint-12 row in the active `CHECKPOINTS.tsv`. The receipt and TSV also agree on all seven receipt columns. Local Library identity/version attributes match:

- Library file ID: `libfile_fde3_f-e815a213df988191b1b1b2ba47071818_3de54532f60c8191850458563edee173`.
- File ID recorded in the receipt: `file_00000000418c81f6a27963880c63c2f3`.
- Version: **0**.
- Recorded save-success time: **2026-11-19 03:15:12 UTC**.

The inspected receipt records helper exit **0**, per-file status **succeeded**, successful local identity writeback, and the same 154 / 172 / 155 scope. Those are receipt statements; this inspection did not contact the remote service.

The archive contains the verified prior receipt rows for checkpoints 10 and 11, matching the active rows. Its own checkpoint-12 save receipt and row are absent from the immutable ZIP, as expected: they were recorded after archive creation. No repackaging is required.

**Result:** all integrity, receipt-consistency, size, exclusion, and recorded-scope checks described above passed.

