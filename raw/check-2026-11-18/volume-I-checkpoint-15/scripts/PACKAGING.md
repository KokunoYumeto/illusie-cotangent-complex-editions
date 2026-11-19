# Checkpoint packaging for the continuation

`package_checkpoint.py` creates a complete checkpoint snapshot. It does not schedule work, upload files, assert that a save succeeded, change the audit records, or mark pages complete.

## Inspect without creating an archive

Run this command from the deliverable root:

```text
python3 -B scripts/package_checkpoint.py --number 10 --dry-run
```

The default root is the deliverable tree containing the script, so the script also works when invoked from another directory. A dry run reads and hashes the selected files, reports inclusions/exclusions and the planned filenames, and creates no files or archives.

## Create at each 45-minute checkpoint time

```text
python3 -B scripts/package_checkpoint.py --number 10
```

Increment the number for each later checkpoint, starting at **10** after the supplied checkpoint 09. The script derives checkpoint `NN`'s earliest creation time from the first UTC line of this continuation's `progress.log` plus `45 × (NN − 9)` minutes. The continuation starts at **2026-11-19 00:59:37 UTC**; checkpoint 10 is due at **2026-11-19 01:44:37 UTC**, checkpoint 11 at **2026-11-19 02:29:37 UTC**, and so on. Numbers below 10 are refused. This guard does not replace the caller's responsibility to make one checkpoint at each 45-minute interval. Do not create additional checkpoints after individual pages, sections, chapters, readers, or other milestones. The script is not a scheduler, and it does not modify earlier checkpoint records or archives.

By default, archives are created in a `checkpoints` directory beside the deliverable trees. `--output-dir` selects another destination. Names follow `ILLUSIE_I_CHECK_checkpoint_NN.zip` or `ILLUSIE_II_CHECK_checkpoint_NN.zip`, according to the root. If several parts are needed, their names end with `_part1.zip`, `_part2.zip`, and so on; the first part contains the complete file list.

Existing checkpoint files are never overwritten. The requested number must exceed any checkpoint numbers already present in the selected destination. When earlier checkpoints exist only in durable storage, the caller must supply the next correct number from that storage record.

After archive creation, the caller must save every part to durable storage and inspect the save receipt. The script's successful creation message is not evidence of a successful durable save.

## Contents and exclusions

Every invocation includes all current deliverables again, including unchanged TeX files and the necessary unchanged cover images and facsimile PDFs in `sources/`. It verifies that all three source layers and their original required build assets are present. It includes the current reports, `CHECK_EVENTS.tsv`, `progress.log`, scripts, and other eligible files in the deliverable tree. It does not substitute the latest pages or a summary for the complete current deliverables.

Our own support files kept outside the deliverable tree can be included explicitly:

```text
python3 -B scripts/package_checkpoint.py --number 10 --support support/analysis.tsv=analysis.tsv
```

The left side is the safe relative name to use inside the ZIP. The right side identifies the current local file or directory. Use this option only for our own new or modified support material, not original attachments or runtime/vendor data. Prefer placing reusable scripts and audit support material in the deliverable tree so they are included automatically in later checkpoints.

The script excludes nested archives; authority scans and errata PDFs; input, runtime, vendor, and cache directories; bytecode; raw compiler/runtime logs; compiler intermediates; and ordinary rendered images. A raster image under `evidence/` is included only when its relative path or filename is explicitly mentioned by a current Markdown or TSV audit report. Source-tree raster assets remain included regardless of report mentions. A report reference determines packaging eligibility only; it does not certify the image interpretation.

`FILE_LIST.tsv` records each included member, its part, size, and SHA-256, along with discovered exclusions and scope categories. It records no absolute environment paths. No file is omitted merely because it is unchanged, so there are no unchanged-file omissions requiring earlier-checkpoint references. Each checkpoint is therefore self-contained apart from the separately supplied inputs; no previous checkpoint is required to restore its deliverables.

The input `sources/MANIFEST.tsv`, when present, remains the supplied provenance record. It is not rewritten to make new source hashes appear original. The newly generated `FILE_LIST.tsv` contains the hashes of the current checkpoint bytes.

## Integrity and size checks

The default part limit is 499,000,000 bytes, strictly below 500 MB. A conservative uncompressed-size bound determines the part plan. The script verifies each staged ZIP's actual size and re-reads every archived file to compare its SHA-256 with the inspected source bytes. It also checks that the deliverables did not change during packaging. If any check fails, it stops before publishing those staged archives.

Every archive member uses a safe relative name. Symlinks are refused rather than followed into unrelated material. A single member too large for the conservative per-part budget is reported as a blocker; the script does not silently truncate or fragment a source file. None of the currently supplied source assets approaches that limit.

The temporary TeX installation is reproducible runtime material. Its sanitized setup is recorded separately in `TOOLCHAIN_REPRODUCIBILITY.md`; raw installation files, caches, and logs remain outside checkpoint scope.
