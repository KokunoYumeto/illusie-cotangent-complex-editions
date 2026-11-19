# Checkpoint 14 independent mechanical integrity audit

Prepared: **2026-11-19 04:48:56 UTC**. Local immutable-archive examination began **2026-11-19 04:45:43 UTC**; the core archive check finished **2026-11-19 04:47:46 UTC**, and the separate privacy scan finished **2026-11-19 04:47:51 UTC**.

## Result and frozen scope

**PASS for the mechanical checks described below.** The examined checkpoint is complete and internally consistent at its frozen recorded boundary of **printed page 177 / scan page 195**. It contains **6,624 correction rows**, **19 reading-question records**, **561 existing-correction records**, and **416 check-event records**. Its last page-completion entry is **page 177, 2026-11-19 04:40:17 UTC**.

The archived README and CHECK_RECORD summary both identify **page 178 as in progress**. Ten page-178 crop files are present as partial-work evidence. The archive contains no page-178 correction row, existing-correction row, canonical completion section, or completion event in the progress log. The later live completion of page 178 is outside this immutable archive and outside this audit's completion scope.

No author text, mathematics, translation, source meaning, scan, crop, or PDF content was interpreted. Counts and completion entries describe the primary reader's records; they do not constitute a new reading certification.

## Archive identity and payload inventory

| Property | Independently verified value |
|---|---:|
| Archive | `ILLUSIE_I_CHECK_checkpoint_14.zip` |
| Compressed file size | **161,977,766 bytes** |
| Payload files | **1,804** |
| Generated index members | **1** (`FILE_LIST.tsv`) |
| Total ZIP members | **1,805**, with no directory entries |
| Uncompressed payload bytes | **192,966,085** |
| Index bytes | **385,544** |
| All-member uncompressed bytes | **193,351,629** |

Archive SHA-256:

`206682f9df1d8ffb829866a3655cf60f26c984f2a59f123e86a2338b0ae9f4cc`

The outer byte count and SHA-256 agree with the primary's supplied identity and remained unchanged when rechecked after the core audit. The ZIP is below the required 500 MB limit. ZIP decompression/CRC testing succeeded for every member.

| Payload area | Files |
|---|---:|
| Root deliverables | 40 |
| Evidence | 1,661 |
| Scripts | 87 |
| Sources and required source assets | 16 |
| **Total payload** | **1,804** |

All names are safe relative archive paths. There are no duplicate names, case-collision groups, symlinks, encrypted members, nested archives, supplied input directories, or bundled source/scan input ZIPs. Original scan inputs remain separate from the deliverable. Required source assets shipped with the edition remain in the `sources` tree.

## FILE_LIST and source provenance

The generated `FILE_LIST.tsv` has the expected seven-column schema and **1,811 data rows**: **1,804 included**, **1 generated**, **2 excluded**, and **4 scope rows**. Its SHA-256 is:

`b49487ef19b7c36455279fb657d8d6b9371a83ded15ef21b407e016b557289f6`

Every included row names exactly one payload member. Every payload is indexed. All **1,804 payload byte counts and SHA-256 values match**, and every included `zip_part` names this checkpoint. There are no malformed index rows or extra, missing, or duplicate payload entries. The generated index is intentionally not included in its own payload hash inventory.

The exclusion metadata identifies the prior FILE_LIST and Python cache files; scope rows identify input archives/trees, earlier checkpoints, runtime/vendor/rendered-page exclusions, and the absence of unchanged-file omissions. The packaged state is complete for this checkpoint rather than a delta archive.

The **15 rows** of `sources/MANIFEST.tsv` were separately checked against the supplied original source ZIP. Every original size and SHA-256 agrees. That manifest is original-source provenance: the three edited TeX files intentionally differ from its release hashes, while all other listed source assets agree byte-for-byte with the supplied originals. Current TeX identities are covered by the checkpoint FILE_LIST and replay checks below.

## Exact ordered correction replay

All **6,624 rows** replay successfully, in order, from the supplied original sources using the archived replay script. Every edit requires exactly one old-string occurrence. The resulting three source files are **byte-identical to the archived sources**.

The ten-column correction schema is correct. There are no malformed rows, empty required fields, or unknown correction kinds. The numeric layer/kind table agrees with the ledger in every cell and with the total of 6,624.

| Layer | Rows |
|---|---:|
| as-printed | 2,099 |
| corrected | 2,288 |
| English | 2,227 |
| build | 10 |
| **Total** | **6,624** |

Relative to the privately frozen through-176 audit, all **6,582 earlier row values remain unchanged**. The only appended source-edit rows are **42 rows for page 177**, numbered **6583–6624**: 9 as-printed, 17 corrected, and 16 English. Applying only these 42 rows to the through-176 source files independently reproduces all three archived sources exactly.

The 19-question file is byte-identical to through176, with the expected seven fields, no malformed records, and no duplicate IDs. Existing-correction and check-event record structures are also well formed. Earlier check-event row values are unchanged; the two appended event IDs occur exactly in the archived page-177 history script. No page-178 history editing script is included. This is a mechanical record association, without interpreting event outcomes.

| Source file | Bytes | SHA-256, also obtained by both replay paths |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,540,969 | `8b86e4f73fc6c6c47f96e1fcdfefae5302baacb15055c6e48ccb891f5a56f85c` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,568,864 | `a58f476f98e4d11ad669485a45a0478c5e21c1b7a1e93388125815d7fb1a00f1` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,586,601 | `5fafec06bbdc9d424584dd99a3ed873f94489d2d77df9a7fb2167d5de0eb88f6` |

## Evidence references and identifier preservation

All **1,663 explicit current image/PDF paths** checked in the correction ledgers, CHECK_RECORD, and EVIDENCE_INDEX exist in the archive. A broader scan of frozen root metadata found **1,705 distinct image/PDF filename references**, including **1,689 operational references**. All operational references resolve to an archived exact/relative/basename candidate or to the separately supplied original scan authority.

The one external scan-authority basename, `ILLUSIE_I_LNM239.pdf`, exists in the supplied input tree and is intentionally excluded from the deliverable ZIP. The three layer-specific front-matter files remain present under their existing source-layer directories.

Four nonresolving old literal spellings remain only as quotations in historical repair/audit reports: `Evidence/I_p004_postcat.png`, `exact-second.png`, `footnote.png`, and `note-call.png`. Their corrected evidence paths already exist, and no operational reference uses an unresolved former spelling. These preserved historical quotations are not new missing-evidence findings.

Each source retains all original literal identifier occurrences. After excluding macro-parameter placeholders, each layer contains **356 labels**, **3,943 hyperlink targets**, **1 bookmark ID**, **6 front-page markers**, and **355 body-page markers**. **All inspected identifier sequences are exactly identical to checkpoint 09.** The inherited extra front targets, earlier source-position changes, and cover duplicate remain baseline exceptions; no new identifier loss or reordering was found. This is lexical inventory checking, not compiled-link validation.

## Coverage, timestamps, and historical records

Canonical printed-page records are exactly **1–177**, and active scan-page records are exactly **1–195**, without gaps or duplicate active records. Printed-to-scan offsets all equal 18. Canonical completion timestamps agree with progress entries, and their page order and timestamps do not regress.

The historical premature page-27 entry remains explicitly voided. Its earlier completion event is preserved, so the progress log contains 178 historical numeric completion events for 177 distinct completed pages. Active coverage excludes the voided record. No history was rewritten.

Earlier replay reports and checkpoint receipts retain their original capture boundaries and counts. The archived report through176 remains a through176 report even though this checkpoint also contains completed page177.

## Mechanical privacy screen

A separate worker scanned **135 textual archive members** mechanically and checked all **1,805 member paths**. It found **no concrete email, file-URI, or environment-specific private-path issue**.

The screen classified 247 Windows-drive-like candidates as inherited TeX control syntax; every candidate's exact bytes occur in checkpoint09. It classified 170 UNC-like candidates as inherited TeX/script syntax, escaped TeX/newline strings, or a regular-expression substitution. The single generic interpreter shebang is valid launcher syntax, not a private environment path.

This is a pattern-based privacy screen of text bytes and member names. Image/PDF content and embedded binary metadata were not inspected. No private information is reproduced in this report.

## Separate post-freeze upload receipt

After the archive was frozen, the primary recorded a local `CHECKPOINT_14_SAVE_RECEIPT.json` at **2026-11-19 04:45:49 UTC**. The observed receipt records helper exit code **0**, status **succeeded**, metadata applied **true**, and version **0**. Its archive name, byte count, and SHA-256 agree with the independently checked local ZIP.

This receipt records the primary's observed successful upload. This audit did not perform an independent remote download or remote byte-hash comparison. The receipt and this new audit report are outside immutable checkpoint14; neither has been inserted into or used to alter that ZIP.

## Handling and limits

All audit extraction, replay, and working reports were confined to private staging. No active source, ledger, verdict, question, CHECK_RECORD, progress log, earlier report, or archive was edited. No ZIP was created, replaced, or uploaded by this audit. Volume II was untouched. This report was staged for the primary to inspect before any authorized installation.
