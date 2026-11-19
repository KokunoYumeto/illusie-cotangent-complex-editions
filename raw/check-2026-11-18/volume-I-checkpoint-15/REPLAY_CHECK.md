# Mechanical source-replay check

**Snapshot:** 18 November 2026, 13:19:11 UTC, after the record for printed page 1. The captured ledger contained **476 correction data rows**, and the captured source tree contained **16 files**. Source and ledger fingerprints remained unchanged during capture. Subsequent page edits are outside this check's scope.

The canonical `scripts/replay_corrections.py` was run against a fresh extraction of the supplied Volume I source archive, using the captured ledger. Its first run stopped at correction data row **467**: the English page-boundary edit's `old` and `new` context still contained `\text{times}`, while the source and preceding replay state contained `\text{factors}`. This was stale context left after withdrawal of an unnecessary wording change; the intended page-boundary operation itself was unchanged.

In a private diagnostic ledger, only that context token was changed to `\text{factors}` in both fields. Canonical replay then completed with exit code **0**, applied all **476 rows**, and reproduced **all 16 captured source-tree files byte for byte**. SHA-256 comparison found no missing, extra, or different files. This includes the three edited TeX files and all thirteen remaining source-tree files, including unchanged required build assets and the supplied provenance manifest. The original TeX files contain no CR or CRLF line endings, so universal-newline conversion does not account for the agreement.

The same context-only repair has now been made in the live row 467 and mechanically confirmed there. It required no source-byte change. **No additional unrecorded source difference was found in the captured snapshot.**

This is a source-bookkeeping and byte-reproducibility check. It is **not** the required second visual reading against scan crops, an edition build, a layout inspection, a translation assessment, or a mathematical proof check. Those tasks retain their separate records and completion conditions.

## Subsequent snapshot after printed page 9

**Snapshot:** 18 November 2026, **14:05:16 UTC**, after the completion event for printed page 9 at 14:04:29 UTC. The captured ledger contained **828 correction data rows**, and the complete captured source tree contained **16 files**. Source and ledger fingerprints remained unchanged during capture. Later edits are outside this snapshot's scope.

The captured canonical `scripts/replay_corrections.py` replayed the captured ledger against a fresh extraction of the supplied Volume I sources and completed with exit code **0**. All **16 source-tree files were byte-identical** to the captured current sources, including unchanged necessary build assets. There were **no missing, extra, or differing files**, and no CR-normalization concern was detected. No additional ledger repair was required. **No unrecorded source mutation was found in this captured state.**

This result supplements the earlier 476-row check; it does not replace that check or its recorded context-only defect and repair. It is solely a mechanical replay and byte-comparison result. It is **not** a visual reading or second visual reading, scan assessment, translation or mathematical correctness assessment, layout inspection, or edition build.

## Recovery verification and subsequent snapshot

After workspace recovery, all **six supplied manifests** were rechecked mechanically. All **82 manifest-listed files** matched both their recorded byte counts and SHA-256 hashes, with no missing or mismatched entries. The per-tree counts were: Volume I context 32, scans 2, sources 15; Volume II context 25, scans 3, sources 5. This verification read file bytes for hashing only and did not inspect scan pages or assess context text.

**Recovery snapshot:** 18 November 2026, **14:10:57 UTC**. The captured ledger contained **862 correction data rows**, including the newly recorded printed-page-10 edits. This count is bookkeeping only and does not itself declare page 10 reviewed or complete; page completion has its separate record. Source, ledger, and canonical-script fingerprints remained unchanged during capture.

Canonical replay against a fresh copy of the recovered original source tree completed with exit code **0**. All **16 captured source-tree files**, including unchanged assets, were **byte-identical** to the replayed files, with **no missing, extra, or differing files**. The original source tree was also fingerprinted before and after copying and remained unchanged. **No unrecorded source mutation was found in this captured recovery state.** Later edits are outside this snapshot's scope.

The recovery verification supplements both earlier results. It is a manifest-integrity, exact-replay, and byte-comparison check only. It is **not** a visual reading or second visual reading, a scan or translation assessment, a mathematical proof check, a layout inspection, or an edition build.

## Snapshot before hourly checkpoint 02

**Snapshot:** 18 November 2026, **14:30:56 UTC**, after the recorded work through printed page 15. The captured ledger contained **997 correction data rows**, and the captured source tree contained **16 files**. At capture completion, every captured source-file SHA-256 matched the corresponding current file, and the captured ledger bytes exactly matched the current ledger. Later page edits are outside this snapshot's scope.

The canonical `scripts/replay_corrections.py` was copied and run against a fresh private copy of the supplied original Volume I source tree, using the captured ledger. The original tree contained **16 files**, and its fingerprints remained unchanged before and after copying; the copy matched those fingerprints. Replay completed at **14:31:22 UTC** with exit code **0**, empty stderr, and all **997 correction rows** applied. Direct byte comparison found all **16 replayed source-tree files identical** to the frozen current-source capture, including unchanged source assets and metadata. There were **no missing, extra, or differing files**. No ledger repair was required. **No unrecorded source mutation was found in this captured state.**

This check supplements all earlier proofs without replacing them. It is solely a mechanical source-replay and exact-byte-consistency check. It is **not** a visual reading or second visual reading, scan or translation assessment, mathematical proof check, layout inspection, or edition build. Page-review completion remains governed by the separate page records and progress events.

## Intermediate snapshot after printed page 25

A stable frozen capture completed on 18 November 2026 at **15:19:29 UTC**, with **1,391 correction rows** and **16 source files**. Canonical replay against a private copy of the original source tree finished at **15:20:01 UTC**, exit code **0**, empty stderr. All sixteen files matched the frozen current source tree byte for byte, with zero missing, extra or differing files. All thirteen non-TeX assets and metadata files also remained byte-identical to the supplied originals. The fifteen manifest-listed source files matched their recorded sizes and hashes at **15:20:41 UTC**.

This mechanical check did not separately identify and hash the protected credit/rights blocks within the edited TeX files, because no established byte-range locators were available in that check. It therefore does not independently certify those blocks. It did not read scans, assess mathematics or translation, inspect layout, perform a second visual reading, or build an edition.

## Snapshot before hourly checkpoint 03

A stable frozen capture completed on 18 November 2026 at **15:33:40 UTC**, after the valid completion of printed page 28. It contains **1,533 correction rows**, **16 source files**, and the canonical replay script. Source, ledger and script fingerprints were unchanged before and after copying. Canonical replay finished at **15:34:31 UTC**, exit code **0**, empty stderr; all sixteen replayed files matched exactly, with zero missing, extra or differing files. All thirteen non-TeX assets and metadata remain unchanged. All fifteen original manifest-listed files pass their size and SHA-256 checks.

The explicitly delimited `tex/common/p004.tex` source block containing `IllusiePfourPage` was compared byte for byte with the original in each of the three layers and is unchanged. The explicit `IllusiePthreeAuthor` macro also remains byte-identical in each layer. No separate dedicated edition-credits block was identified, so the result is limited to these established locators and the unchanged assets. It does not assert a broader unidentified-block comparison.

This is a mechanical replay and protected-block byte comparison. It does not constitute scan reading, translation assessment, mathematical verification, the required second visual reading, layout inspection, or an edition build. The premature p27 completion event remains explicitly voided in the audit history; the valid replacement completion governs scope.

## Frozen replay through printed page 33

Capture completed 2026-11-18 15:50:51 UTC; replay and checks completed 15:51:35 UTC. The capture was stable before and after copying, and captured inputs were read-only. All 1,655 correction rows replayed with exit 0 and empty stderr. All 16 source files were byte-identical; missing/extra/differing: 0/0/0. All 13 non-TeX assets/metadata remained unchanged; all 15 original manifest entries matched byte counts and SHA-256 hashes. The complete explicit p004 rights source sections and IllusiePthreeAuthor macros remained byte-identical in all three layers; no unidentified credits block is claimed. Ledger SHA-256: 013722562c681da5450a52ca96882336db3725e9b959e07c222eaad8848d6803. Canonical replay script SHA-256: a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539. Private report SHA-256: 608532f3477137a8e8790564f1fb6c1584e5bead436766b2211919a11c38c63a. This read-only mechanical check excludes subsequent p34 edits and makes no visual or mathematical certification.

## Frozen replay through printed page 40

Capture completed at 2026-11-18 16:08:22 UTC; replay and checks completed at 2026-11-18 16:09:16 UTC. The frozen 1,799-row ledger and canonical script replayed with exit 0 and empty stderr. All 16 source files matched byte for byte, with no missing, extra or differing files. All 13 non-TeX assets/metadata remained unchanged, and all 15 original manifest members passed size and SHA-256 checks. In each of the three TeX layers, the complete BEGIN/END SOURCE block for tex/common/p004.tex and the IllusiePthreeAuthor macro remained byte-identical. No unidentified separate credits block is claimed. This mechanical replay certifies neither visual reading nor mathematical correctness. Later page edits are outside this frozen capture.

Ledger SHA-256: `a41d726fd34f70ac7a752e4a7d2a29b1f8b91e29ab7a6978ca14de170d2cba68`.

Replay script SHA-256: `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`.

Private integrity report SHA-256 (verified by the primary reviewer): `42c1af5ecbb9848bf4977cbdca359fcd5092f1bd78027b10b617d66ae131e7d4`.

## Frozen replay through printed page 45

Stable read-only capture: 2026-11-18 16:24:57 UTC. Replay and integrity checks completed 2026-11-18 16:25:15 UTC. All 1,971 ledger rows replayed successfully (exit 0, empty stderr), reproducing all 16 source files byte-for-byte, with no missing, extra or differing files. All 13 non-TeX files are unchanged and all 15 original manifest entries pass size/SHA-256 checks. In every layer the complete tex/common/p004.tex rights section and IllusiePthreeAuthor macro remain byte-identical. This claim covers these explicit protected blocks; it does not claim a separate unidentified edition-credit block.

Ledger SHA-256: `e9009c4f65c01129ac9555a75dd0ce1f96b0735aee97d042853952453a34937c`. Canonical replay-script SHA-256: `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`. Private integrity-report SHA-256: `5a96b3d53e83c31c19fdf3839de0bd17b3227e733eb098257539dd71794e832b`. Root inspected the full report and verified its hash. This is mechanical integrity verification only; p46 onward, second visual reading and edition-build validation are outside this snapshot.

## Frozen replay through printed page 47

Stable read-only capture: 2026-11-18 16:34:35 UTC. Replay completed: 2026-11-18 16:34:53 UTC. All 2,040 correction rows replayed with exit 0 and empty stderr. Original, captured and replayed trees each have 16 files; none missing, extra or differing. All 13 non-TeX assets and metadata files remain unchanged and all 15 original manifest members pass size/hash checks. The three explicit p004 rights blocks and the three author macros are byte-identical to their supplied originals. This is a mechanical consistency check, not a visual or mathematical certification.

Ledger SHA-256: `a77964ca2904d03b44db2aad53036fae4ee8091dc2ae7901428a1cde5fe8cae0`. Replay-script SHA-256: `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`. Private report SHA-256: `6d93c000e7d2ff4f1b6d74906de7893b3829fbd2181f7cf4b19e008d2ab64c66`. Later edits are outside this capture.

## Frozen replay through printed p51

The stable read-only capture at 2026-11-18 16:50:59 UTC contained 2,130 correction rows and all 16 source files, with no p52 edits. Canonical replay completed at 16:51:15 UTC with exit 0 and empty stderr. All 16 files matched byte for byte; missing, extra and differing files: zero. All 13 non-TeX assets remained unchanged, and all 15 supplied source-manifest entries passed size/hash checks. The complete p004 rights blocks and author macros in each of the three TeX files remained byte-identical to the supplied originals. These checks cover the explicitly identified blocks, not an unidentified separate credits block. Root read the complete private JSON report and verified its SHA-256 before adding this record.

Ledger SHA-256: `2ae4956a31a0de256046c468a676fbe9894e490c56dbdc66681b4fb7c032575f`. Canonical script SHA-256: `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`. Private report SHA-256: `4e7552fe334159f96cd2b4d402998935cf1c321a50e0979db8b2b572d047f1c4`. This is mechanical consistency evidence, not a second visual reading or an edition-build check.

## Frozen replay through printed page 55

Stable capture: 2026-11-18 17:09:27 UTC; replay completed 17:09:45 UTC; all checks completed 17:09:46 UTC. All 2,309 correction rows replayed with exit 0 and empty stderr. All 16 source members match exactly; missing/extra/differing counts are 0/0/0. All 13 non-TeX assets are unchanged and 15 supplied manifest members verify. The three explicitly identified complete p004 rights blocks and the three author macros remain byte-identical. No unlocated credits block is claimed checked. Root read the complete JSON and independently checked its SHA-256 before recording this receipt. Page 56 and later are outside this frozen comparison.

Ledger SHA-256: `b2fe355e889f97c1d90612a44d81ff8e3b2fe426e880627352b2f7beab7a2939`. Report SHA-256: `64a4a6a7ec0b14c90d04b348aa01806e59e6fe6529289a029c3ececea737e733`. This is a mechanical consistency check, not a substitute for visual or mathematical assessment.

## Frozen replay through printed page 62 (p062)

**Scope:** the frozen Volume I capture through printed page **62** / scan page **80**, captured at **2026-11-18 17:33:34 UTC**, with **2,560 correction rows** and **16 source files**. The recorded page-62 completion is **2026-11-18 17:32:32 UTC**. This section makes no assertion about the current live ledger or **checkpoint 05**.

**Result: PASS.** Capture fingerprints were stable. Canonical replay returned exit code **0**; direct comparison found **16/16 files byte-identical**, with **0 missing, 0 extra, and 0 differing files**. All **13 non-TeX files** matched supplied originals. All replay targets were confined to the private source copy. No original-TeX CR-normalization concern was found.

All **15 original Volume I source-manifest entries** matched their recorded byte counts and SHA-256 values and remained stable. All **six original manifest files** were copied exactly and remained stable; the Volume I source manifest also matched the captured copy and prior p055 copy. Manifest-listed scan/context contents were excluded from entry verification.

The **three explicitly delimited p004 rights sections** and **three IllusiePthreeAuthor definitions** were byte-identical across supplied, captured, and replayed copies, and matched the prior p055 hashes. The p004 rights-section hashes are:

| Layer | SHA-256 |
|---|---|
| as-printed | `4615e46b334818d23aa79ed959496a0b5aa59b89c156b67c5ab32c2f849ae27c` |
| corrected | `8017379f0f01bb3834c9fc3d0f6b95b2394d030edcf0edf0716bb21561c7c747` |
| English | `8017379f0f01bb3834c9fc3d0f6b95b2394d030edcf0edf0716bb21561c7c747` |

All three author definitions share SHA-256 `76bf773e9e4f4b5d3c49f744568967b9fca2fe8c448d5f4713aceb4afd95ca93`. No separate dedicated edition-credits block is claimed.

**Verification times:** original-manifest check **17:37:11 UTC**; direct byte/protected-section comparisons **17:39:20 UTC**; completed receipt **17:41:51 UTC**, all on **18 November 2026**. The receipt digest was revalidated at **2026-11-18 17:49:04 UTC**.

**Captured ledger SHA-256:** `436fc1a781c1e3a545564599e9a4858bfbe575233f69830ecd84ef8fd670d58d`.

**Canonical replay script SHA-256:** `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`.

**Complete receipt:** `FROZEN_REPLAY_P062.json`, **58,871 bytes**, SHA-256 `f198743f3378b8d7dc8a00464d9cd6d774be78e24be80d41c2d905d9ea967b9b`.

All required replay and preservation assertions pass. The raw false flags identify the three TeX files as TeX and record their expected differences from supplied originals; they are not failed replay assertions. This is mechanical bookkeeping and byte-reproducibility evidence only. It does not certify a scan reading, second visual reading, translation, mathematics, layout, or edition build.

## Frozen replay through printed page 68 (p068)

This receipt applies only to the frozen Volume I capture through printed p68 / scan86. It does **not** certify the current live state or any checkpoint archive.

- Capture: **2026-11-18 18:08:54 UTC**, with matching live-before, copied and live-after source, ledger and replay-script hashes; completion-metadata hashes were also stable.
- Canonical replay: **2026-11-18 18:11:12–18:11:21 UTC**; exit 0, empty stderr. Direct source-byte and protected-block comparisons completed at **18:11:21 UTC**; all verification completed at **18:13:21 UTC**.
- **2,785 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the supplied originals.
- All **15 original Volume I source-manifest entries** matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p062 receipt; the captured I source manifest was byte-identical to its original. Manifest verification completed at **18:10:00 UTC**.
- All **36 required mechanical assertions passed**. Captured completion metadata accounted for active scan pages **1–86** in exact order, excluding only the explicitly void p27 / scan45 completion at **15:25:32 UTC**. The captured final completion was **p68 / scan86 at 2026-11-18 18:06:31 UTC**. Ledger page labels stopped at p68.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across supplied, captured and replayed sources and matched the p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed in this check.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` | `849836662bef260a96bc82232590d09ee6a3dfa480c1f7348ef39c630f7c6fc8` |
| Captured canonical `replay_corrections.py` | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P068.json` (104,186 bytes) | `1a6876a1da7e9160341e9e89c61609105771fd8837f754abb95ef7de92b87b3c` |
| `FROZEN_REPLAY_P068.md` (9,210 bytes) | `eae0ec4e417aa60c1107432c5647435727c253add27babfa4f7cd678aa864764` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes that recorded substitutions reproduce the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans or protected research-context bodies were read or assessed, and no active source, ledger or completion marker was changed by this replay check. No build, archive or upload was performed. These findings concern the frozen p068 capture only, not later live edits or any checkpoint archive.

## Frozen replay through printed page 74 (p074)

This receipt applies only to the frozen Volume I inputs through printed p74 / scan92, captured at **2026-11-18 18:28:23 UTC**. It does **not** certify the current live state or any checkpoint archive, including checkpoint06.

- Output sources, ledger, replay script, completion metadata and a separate copy of all supplied original sources matched their respective before/copied/after hashes and remained unchanged through verification.
- Canonical replay ran **2026-11-18 18:28:59–18:29:08 UTC**: exit 0, empty stderr. Direct source-byte and protected-block comparisons completed at **18:29:08 UTC**; manifest verification completed at **18:29:43 UTC**; all verification completed at **18:30:53 UTC**.
- **3,044 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p068 receipt. Frozen supplied, live original I and captured I source manifests were byte-identical.
- All **37 required mechanical assertions passed**. The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,041 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **93 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **92 active records/events** in exact scan order **1–92**. The last captured completion was **p74 / scan92 at 2026-11-18 18:27:40 UTC**. Ledger page labels stopped at p74.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (1,811,142 bytes) | `d5cfb0fc5fd896737f713398f21fb962b0c21bccc0fad326bb8761cfc10f6b5a` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P074.json` (127,183 bytes) | `a56afb046913cfc37622e4ea703ebc96f18936805bc437ce88bcacb4c583f952` |
| `FROZEN_REPLAY_P074.md` (8,661 bytes) | `78a03ccc33bcc22367a4770033bffcc69465a2bd9a9f567b8b25f4a442dd006e` |
| Captured/replayed English TeX (1,529,179 bytes) | `4d4d0ed712278e8c0c69b0d0b61df7459a6a648af1d395622b4b7cd6aba84170` |
| Captured/replayed corrected French TeX (1,557,193 bytes) | `a4a187e527fdaf8ea46406e277cc9ffde0dac2d5d91083f40e2188b193fd9bfd` |
| Captured/replayed as-printed French TeX (1,575,648 bytes) | `21215f5a15f46f2fbb1d1ef99f5280c94a25ed956afe6f80984b2eb0a3dc049b` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p074 copies only, not later live edits or any checkpoint archive.

## Frozen replay through printed page 77 (p077)

This receipt applies only to the frozen Volume I copies through printed p77 / scan95, captured at **2026-11-18 18:44:44–18:44:45 UTC**. It does **not** certify the current live state or any checkpoint archive.

- Output sources, ledger, canonical replay script, completion metadata and separately copied supplied original sources matched their respective before/copied/after hashes and remained unchanged through verification.
- Canonical replay ran **2026-11-18 18:45:31–18:45:41 UTC**: exit 0, empty stderr. Direct source-byte and protected-block comparisons completed at **18:45:41 UTC**; manifest verification completed at **18:45:36 UTC**; all verification completed at **18:47:48 UTC**.
- **3,243 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p074 receipt. Frozen supplied, live original I and captured I source manifests were byte-identical.
- All **41 required mechanical assertions passed**. The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,240 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **96 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **95 active records/events** in exact scan order **1–95**. The last captured completion was **p77 / scan95 at 2026-11-18 18:43:57 UTC**. Ledger page labels stopped at p77.

Page-77 replacement replayability: the first **3,044 ledger records** were exactly unchanged from the verified p074 ledger. The **199 appended records** comprised **35 p75**, **79 p76** and **85 p77**. All p77 records formed a contiguous tail: **28 as-printed**, **28 corrected** and **29 English**. Full canonical replay from frozen pristine originals completed without skips, manual repairs or replay restarts; its unique-old-text guard succeeded for every row, including the three large p77 replacements at data rows **3162, 3190 and 3218**, and all subsequent rows. Final source bytes matched exactly. This proves replayability of the completed ledger, including those replacements and resumed edits; it does not reconstruct the earlier partial-run execution history or assess the chi/token choice.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (1,971,486 bytes) | `ed0d76c16f552ce9551b361d107b3dc439846002d82c211cb79d1ef368badfff` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P077.json` (182,838 bytes) | `050de7a1a5c77dc6c46d55f9765cc379d6f6ec9ad5608f9e3b0c64407315bf9f` |
| `FROZEN_REPLAY_P077.md` (10,221 bytes) | `3f5ce3e02bfbc40f11937961b23c616187c6d4144986ff3255494bbca5f59f19` |
| Captured/replayed English TeX (1,529,478 bytes) | `deb87c6221b2b03e98860cd4fe237c02bca17dc606e1c69428601bfc563348be` |
| Captured/replayed corrected French TeX (1,557,498 bytes) | `bdc492437c0c54135393180673a601bd298458f53e9f8fcdf89a189e8400c8a3` |
| Captured/replayed as-printed French TeX (1,575,946 bytes) | `6f47505001da97388be578045f8d58cf5233aad0037901e30fa101ae0689254e` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p077 copies only, not later live edits or any checkpoint archive.

## Frozen replay through printed page 80 (p080)

This receipt applies only to the frozen Volume I copies through printed p80 / scan98, captured at **2026-11-18 18:55:35 UTC**. It does **not** certify the current live state or any checkpoint archive.

- Output sources, ledger, canonical replay script, completion metadata and separately copied supplied originals matched their respective before/copied/after hashes and remained unchanged through verification.
- Canonical replay ran **2026-11-18 18:56:02–18:56:12 UTC**: exit 0, empty stderr, with no skipped rows, manual repairs or restarts. Direct source-byte and protected-block comparisons completed at **18:56:12 UTC**; manifest verification completed at **18:56:11 UTC**; all verification completed at **18:59:21 UTC**.
- **3,431 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p077 receipt. Frozen supplied, live original I and captured I source manifests were byte-identical.
- All **45 required mechanical assertions passed**. The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,428 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **99 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **98 active records/events** in exact scan order **1–98**. The last captured completion was **p80 / scan98 at 2026-11-18 18:54:44 UTC**. Ledger page labels stopped at p80.

Exact p077 ledger-prefix comparison: all fields of the first **3,243 records** were identical to the hash-verified frozen p077 ledger; there were **zero changed prefix records**. The **188 appended records** comprised **28 p78**, **49 p79** and **111 p80**. All p80 records formed a contiguous tail: **37 as-printed**, **36 corrected** and **38 English**.

Mechanical p80 string-count scope: exact markers uniquely located the p80 source region in each supplied, captured and replayed TeX file. All **24 selected case-sensitive literal substring counts** matched between captured and replayed regions, and every count change against supplied regions equalled the corresponding sum of p80 ledger new-minus-old string counts. Independently in each of the three layers, `[->]` had **19 supplied / 17 captured / 17 replayed** occurrences, while `[-]` had **0 / 2 / 2**. The literal strings `\longrightarrow`, `\xrightarrow` and `\xleftarrow` remained at **4, 1 and 1** occurrences respectively. These are string counts without whitespace normalization, macro expansion, rendering or glyph interpretation. Counts can overlap and must not be added as a count of mathematical arrows; no arrow shape, orientation or meaning is certified.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (2,089,521 bytes) | `7be739652d35c28b6e986ec3b59e0411d2fa2384187657ae9e5fab42dea27fc3` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P080.json` (155,704 bytes) | `d86eaface661bdc6efcef504fe22695d01bcdefe1b5e795f8c65c838d1892305` |
| `FROZEN_REPLAY_P080.md` (10,941 bytes) | `1d84091278e8b7fe884e22aa682600f62362e3b3f2126795a2d882b3a685b39e` |
| Captured/replayed English TeX (1,529,952 bytes) | `ed2018ab80b398a99aa198e864c99c0a28c309c16db9353dd3fa51ed16f85756` |
| Captured/replayed corrected French TeX (1,557,966 bytes) | `f68f09f9a5eb3dc7c814046f829810e1cde0e5e92fc93a45929c086fa4925e3f` |
| Captured/replayed as-printed French TeX (1,576,419 bytes) | `9fa4f8e946820f33d8db6667e3333705baff3c1d199d3efeb883bfa2977d1d32` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments, reconstruct earlier partial-run history or validate token choices. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p080 copies only, not later live edits or any checkpoint archive.

## Frozen replay through printed page 84 (p084)

This receipt applies only to the frozen Volume I copies through printed p84 / scan102, captured at **2026-11-18 19:17:45 UTC**. It does **not** certify the current live state or any checkpoint archive. **Replay PASS:** all **42 core** and **11 scoped ancillary** assertions passed; **two extensionless evidence-like occurrences remain unclassified**.

- Output sources, ledger, canonical replay script, five metadata/progress files and separately copied supplied originals matched their respective before/copied/after hashes and remained unchanged through verification. The **658-entry evidence filename/stat inventory** was also stable during capture.
- Canonical replay ran **2026-11-18 19:18:58–19:19:09 UTC**: exit 0, empty stderr, with no skipped rows, manual repairs or restarts. Direct source-byte and protected-block comparisons completed at **19:19:09 UTC**; manifest verification completed at **19:18:29 UTC**; ancillary evidence/path QA completed at **19:23:29 UTC**; all verification and receipt assembly completed at **19:26:06 UTC**.
- **3,610 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p080 receipt. Frozen supplied, live original I and captured I source manifests were byte-identical.
- The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,607 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **103 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **102 active records/events** in exact scan order **1–102**. The last captured completion was **p84 / scan102 at 2026-11-18 19:16:42 UTC**. Ledger page labels stopped at p84.

Exact p080 ledger-prefix comparison: all fields of the first **3,431 records** were identical to the hash-verified frozen p080 ledger; there were **zero changed prefix records**. The **179 appended records** comprised **64 p81**, **33 p82**, **47 p83** and **35 p84**, in nondecreasing page order. Their as-printed / corrected / English row counts were respectively **22 / 21 / 21**, **11 / 11 / 11**, **16 / 15 / 16** and **11 / 12 / 12**. Full-ledger layer totals were **1,186 as-printed**, **1,217 corrected**, **1,197 English** and **10 build**; kind totals were **861 reading**, **72 misprint of the original**, **96 translation**, **1,881 typesetting** and **700 structure**.

Ancillary evidence-reference scope: **855 explicit file-reference occurrences** and **4 wildcard-pattern occurrences** resolved against the frozen inventory, covering **658 unique files**. Unsafe / missing / empty / symlink targets among recognized explicit references and wildcard matches were **0 / 0 / 0 / 0**; unreferenced inventory entries were **0**. The wildcard patterns `evidence/I_p005_*.png`, `evidence/I_p006_*.png`, `evidence/I_p007_*.png` and `evidence/I_p008_*.png` matched **7, 5, 6 and 7** files respectively. **The token `evidence/replay` occurs twice in captured `CHECK_RECORD.md` and remains unclassified.** These extensionless occurrences were not asserted to be broken links or to resolve, and their surrounding prose was not inspected. **No claim is made that every path-like token resolves or that any evidence content is sufficient or correct.** Evidence images were not opened, decoded or rendered for this check; reference resolution used only frozen names/stat metadata.

Ancillary local-path scope: there were **zero new strong local-path candidates** in comparable frozen source text, replay script and metadata, the unchanged ledger prefix, or the **179 appended ledger records**. Current-only `EVIDENCE_INDEX.md` and `READING_QUESTIONS.tsv` also had zero candidates; because they lack p080 counterparts, their contents are not characterized as newly introduced. Textual scanning covered **seven source text files**, the replay script, **five metadata files** and every ledger field; **nine source image/PDF assets** were excluded from this textual scan. Network URLs were masked and generic mathematical slashes were not classified as host paths. Signature-based checking is not an exhaustive guarantee about every possible path encoding.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (2,213,259 bytes) | `bffdc9ff66ee26b67328693381885a0ff67bfd8ea46ad0a07de8f328cce412c0` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P084.json` (577,575 bytes) | `f5fb673eedb7456e11682a1af8373eeb4925b4bc6f8fc8bcb174e6b77f01a2dd` |
| `FROZEN_REPLAY_P084.md` (14,665 bytes) | `846a50f54e46c197d6abd3c9442621c4d9674be346cb4a382d688d5fab52dfc8` |
| Captured/replayed English TeX (1,530,672 bytes) | `1e3d27d810d61a60f373cdd49002a30516338ef00017b32aaaa1502d8fc5700d` |
| Captured/replayed corrected French TeX (1,558,686 bytes) | `bd27fddc819c6651cdf58ecde14cf032b244da861cf365534a16a95ba5913bf9` |
| Captured/replayed as-printed French TeX (1,577,111 bytes) | `422948d280ab9c51cf503ef1a9e0964ea40e98784f92b762ba45aa89afca4ff4` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments, reconstruct earlier partial-run history or validate token choices. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p084 copies only, not later live edits or any checkpoint archive. The two unclassified extensionless evidence-like occurrences remain outside any claim that all path-like tokens resolve.

## Frozen replay through printed page 87 (p087)

This receipt applies only to the frozen Volume I copies through printed p87 / scan105, captured at **2026-11-18 19:31:15–19:31:16 UTC**. It does **not** certify the current live state or any checkpoint archive, including checkpoint07. **All 41 required mechanical assertions passed.**

- Output sources, ledger, canonical replay script, five metadata/progress files and separately copied supplied originals matched their respective before/copied/after hashes and remained unchanged through verification.
- Canonical replay ran **2026-11-18 19:31:53–19:32:05 UTC**: exit 0, empty stderr, with no skipped rows, manual repairs or restarts. Direct source-byte and protected-block comparisons completed at **19:32:05 UTC**; manifest verification completed at **19:32:00 UTC**; all verification and receipt assembly completed at **19:33:37 UTC**.
- **3,766 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p084 manifest baseline. Frozen supplied, live original I and captured I source manifests were byte-identical.
- The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,763 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **106 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **105 active records/events** in exact scan order **1–105**. The last captured completion was **p87 / scan105 at 2026-11-18 19:30:36 UTC**. Ledger page labels stopped at p87.

Exact p084 ledger-prefix comparison: all fields of the first **3,610 records** were identical to the hash-verified frozen p084 ledger; there were **zero changed prefix records**. The **156 appended records** comprised **42 p85**, **59 p86** and **55 p87**, in nondecreasing page order. Their as-printed / corrected / English row counts were respectively **13 / 17 / 12**, **17 / 25 / 17** and **18 / 19 / 18**. Full-ledger layer totals were **1,234 as-printed**, **1,278 corrected**, **1,244 English** and **10 build**; kind totals were **910 reading**, **74 misprint of the original**, **96 translation**, **1,976 typesetting** and **710 structure**.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Ancillary scope: the **p084 evidence-reference and local-path check was not repeated or extended to p087**. Its two unclassified extensionless `evidence/replay` occurrences remain outside this check. This receipt neither resolves them nor certifies current evidence references or local-path safety. The verified p084 manifest proof was used only as the manifest baseline, separately from its ancillary qualification.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (2,326,211 bytes) | `72be4012c0d58bff1c948eec519d19a5828b78e35685060a6b83cd36298c1ba3` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P087.json` (135,464 bytes) | `d32935dcfa020892e670acf99fb6a28639378f16be76ec8592f2035ecdba185f` |
| `FROZEN_REPLAY_P087.md` (9,854 bytes) | `b3bff86c7570c56bb42ab55e95d1bd5d4a8bdd61e3475b4099e03a9c0347497f` |
| Captured/replayed English TeX (1,530,967 bytes) | `99b06cd61ce802ab90f71076625648768c40b5dade1919be03e69eaf05f41390` |
| Captured/replayed corrected French TeX (1,558,978 bytes) | `73b9f0dbba7f5501896cfa8ee914e4aac2464591c27471331090c6cec5796687` |
| Captured/replayed as-printed French TeX (1,577,414 bytes) | `99fb0b050a9ee521ec59cf86d943742b9639c58b793ca94b361900033a068213` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments, reconstruct earlier partial-run history or validate token choices. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p087 copies only, not later live edits or any checkpoint archive, including checkpoint07. The earlier ancillary qualifications remain unextended and unresolved by this check.

## Frozen replay through printed page 90 (p090)

This receipt applies only to the frozen Volume I copies through printed p90 / scan108, captured at **2026-11-18 19:48:30 UTC**. It does **not** certify the current live state or any checkpoint archive. **Replay PASS:** all **43 core** and **11 scoped ancillary** assertions passed; **two extensionless evidence-like occurrences remain unclassified**.

- Output sources, ledger, canonical replay script, five metadata/progress files and separately copied supplied originals matched their respective before/copied/after hashes and remained unchanged through verification. The **723-entry evidence filename/stat inventory** was also stable during capture.
- Canonical replay ran **2026-11-18 19:49:30–19:49:41 UTC**: exit 0, empty stderr, in one uninterrupted pass from pristine frozen originals, without skipped rows, manual repairs or restarts. Direct source-byte and protected-block comparisons completed at **19:49:41 UTC**; manifest verification completed at **19:49:16 UTC**; ancillary evidence/path QA completed at **19:50:11 UTC**; all verification and receipt assembly completed at **19:53:00 UTC**.
- **3,910 correction rows** reproduced **all 16 captured source files byte-for-byte**; missing / extra / differing files: **0 / 0 / 0**. All **13 non-TeX files** remained byte-identical to the separately frozen supplied originals.
- All **15 original Volume I source-manifest entries**, checked from the frozen supplied copy, matched declared sizes and SHA-256 values. All **6 original manifest files** remained stable and matched the verified p087 baseline. Frozen supplied, live original I and captured I source manifests were byte-identical.
- The ledger had the exact ten-column schema, no malformed row widths and no unknown kind values. Confidence metadata comprised **3,907 high** and **3 medium referencing I-Q004**, all explicitly first-reading / second-reading-pending; no confidence judgment is made here.
- Captured completion metadata contained **109 raw records/events**, less only the explicitly void p27 / scan45 completion at **15:25:32 UTC**, leaving **108 active records/events** in exact scan order **1–108**. The last captured completion was **p90 / scan108 at 2026-11-18 19:47:41 UTC**. Ledger page labels stopped at p90.

Exact p087 ledger-prefix comparison: all fields of the first **3,766 records** were identical to the hash-verified frozen p087 ledger; there were **zero changed prefix records**. The **144 appended records** comprised **39 p88**, **66 p89** and **39 p90**, in nondecreasing page order. Their as-printed / corrected / English row counts were respectively **12 / 16 / 11**, **21 / 22 / 23** and **13 / 13 / 13**. Full-ledger layer totals were **1,280 as-printed**, **1,329 corrected**, **1,291 English** and **10 build**; kind totals were **976 reading**, **76 misprint of the original**, **97 translation**, **2,036 typesetting** and **725 structure**.

Page-90 final-state scope: all **39 p90 records** formed the contiguous final block, data rows **3872–3910**, with **13 per layer**. Every one passed the canonical unique-old-text guard during the complete 3,910-row replay, and final source bytes matched exactly. This proves replayability of the completed recorded state. The earlier failed edit attempt and guarded resumption were not inspected or reconstructed; no claim is made about that execution history or the correctness of its token choices.

Ancillary evidence-reference scope: **924 explicit file-reference occurrences** and **4 wildcard-pattern occurrences** resolved against the frozen inventory, covering **723 unique files**. Unsafe / missing / empty / symlink targets among recognized explicit references and wildcard matches were **0 / 0 / 0 / 0**; unreferenced inventory entries were **0**. The wildcard patterns `evidence/I_p005_*.png`, `evidence/I_p006_*.png`, `evidence/I_p007_*.png` and `evidence/I_p008_*.png` matched **7, 5, 6 and 7** files respectively. **The token `evidence/replay` occurs twice in captured `CHECK_RECORD.md` and remains unclassified.** These extensionless occurrences were not asserted to be broken links or to resolve, and their surrounding prose was not inspected. **No claim is made that every path-like token resolves or that evidence content is sufficient or correct.** Evidence images were not opened, decoded or rendered for this check; reference resolution used only frozen names/stat metadata.

Ancillary local-path scope: the earlier narrow parser/signature method was reused with **frozen p087 inputs as the baseline**. There were **zero new strong local-path candidates** in comparable frozen source text, replay script and metadata, the unchanged ledger prefix, or any field of the **144 appended ledger records**. All **five metadata files** had p087 counterparts. Textual scanning covered **seven source text files**, the replay script, all five metadata files and every ledger field; **nine source image/PDF assets** were excluded from this textual scan. Network URLs were masked and generic mathematical slashes were not classified as host paths. Signature-based checking is not an exhaustive guarantee about every possible path encoding.

Protected-byte scope: the **three explicitly delimited `tex/common/p004.tex` rights sections**, including both delimiter lines, and the **three unique `IllusiePthreeAuthor` definition lines**, excluding their line endings, were byte-identical across frozen supplied, captured and replayed sources and matched the verified p062 protected hashes. No separately identified edition-credits block or semantic assessment is claimed. The six-manifest check covered the manifest files themselves; listed scan/context bodies and Volume II source contents were not rehashed.

Verified SHA-256 values:

| Item | SHA-256 |
|---|---|
| Frozen `CORRECTIONS.tsv` (2,426,448 bytes) | `02bb6b16bb43f60f743e5cc5230de818c3ed863c5c5b1f2ef2bf18d5ac85ab2f` |
| Captured canonical `replay_corrections.py` (901 bytes) | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| `FROZEN_REPLAY_P090.json` (613,749 bytes) | `ebd33538d1e0956d00424142b3e4b731b6f6088e0a95c6add5e3260ab85c1113` |
| `FROZEN_REPLAY_P090.md` (13,731 bytes) | `20b3e4019865c9d8e86f477f425894fbe91cea8fd3bfea08202567d1dd9a0392` |
| Captured/replayed English TeX (1,531,202 bytes) | `93601d7960ec52cbfe15b820793051c03addb6200b6b512b8e89098337c5cb07` |
| Captured/replayed corrected French TeX (1,559,209 bytes) | `09f00667cba56824334883791cd463be1752dbe7c64075b7df873b83a34cfb16` |
| Captured/replayed as-printed French TeX (1,577,636 bytes) | `a0cc8ff63a3afe2ee0ccb4b441e7a49858e12c47edc5107cdf372a8d438fba37` |

Limits: page scope derives from captured ledger labels and completion markers, not interpretation of source prose, mathematics or edit locations. Successful replay establishes reproduction of the captured bytes; it does not establish editorial or mathematical correctness, evidence sufficiency or confidence judgments, reconstruct earlier partial-run history or validate token choices. This was not a first or second visual reading, proof check, PDF layout review or edition build. No scans, source-page prose or mathematics were assessed, and no protected research-context bodies were read. No live source, ledger or completion marker was changed by this replay check; no build, archive, packaging or upload was performed. These findings concern the frozen p090 copies only, not later live edits or any checkpoint archive. The two unclassified extensionless evidence-like occurrences remain outside any claim that all path-like tokens resolve.


## Frozen p95 mechanical replay — appended 2026-11-18 20:26:26 UTC

**PASS: all 57 scoped mechanical assertions passed (43 core; 14 ancillary).** The primary reviewer read the entire bounded receipt and independently verified its Markdown, JSON and frozen-ledger hashes before authorizing this append.

The frozen scope ends at **printed p95 / scan113**, with the last recorded completion at **2026-11-18 20:13:51 UTC**. Capture ran **20:14:32–20:14:33 UTC**; canonical replay ran **20:15:46–20:16:01 UTC**; final verification completed **20:19:35 UTC**, all on 2026-11-18. This receipt concerns that frozen state only.

### Capture qualification and replay

The live output was copied once. No live-output before/copy/after hash triplet was taken. Exact ledger/source reproduction and unchanged frozen verification inputs were established separately. The supplied-original source copy does have matching before/copied/after inventories.

All **4,164 correction rows** replayed once, in order, from pristine frozen original sources, without skipped rows, manual repairs or restarts. Replay exited 0 with empty stderr. All **16 captured/replayed source files** are directly byte-identical; missing, extra and differing files are all zero. All **13 non-TeX assets** remain byte-identical to supplied originals. The ledger has the exact ten-column schema, valid row widths and only the five allowed kinds.

Completion metadata contains 114 raw records/events, minus the one explicit void p27 completion, yielding **113 active records/events** and the exact ordered scan sequence **1–113**. Each active record matches its done event and timestamp. These checks validate recorded metadata, not the underlying reading claims.

### Prefix, appended rows and manifests

Every field of the first **3,910 ledger records** is unchanged from the hash-verified p90 snapshot. The **254 appended rows** belong only to pages91–95 in nondecreasing page order:

| Printed page | As-printed | Corrected | English | Total |
|---|---:|---:|---:|---:|
| 91 | 24 | 26 | 24 | 74 |
| 92 | 16 | 15 | 22 | 53 |
| 93 | 20 | 17 | 17 | 54 |
| 94 | 14 | 11 | 11 | 36 |
| 95 | 13 | 12 | 12 | 37 |

The 37 final p95 rows are data rows **4128–4164**. The replay verifies the final recorded state; earlier editing attempts were not reconstructed. Confidence fields comprise 4,161 high entries and three medium I-Q004 entries, all marked second-reading-pending; no confidence judgment is implied.

All **six original MANIFEST.tsv files** match the verified p90 baseline and remain stable. All **15 declared Volume I source entries** match their declared byte sizes and SHA-256 values. The frozen original, live original and captured I source manifests are byte-identical. This does not rehash the scan/context payloads or Volume II source payloads.

### Protected bytes and evidence paths

The three explicit `tex/common/p004.tex` rights sections, including their delimiter lines, and the unique complete `IllusiePthreeAuthor` definition line in each TeX file, excluding its line ending, are byte-identical across supplied, captured and replayed states. Their hashes match the verified p62 baseline. No separate edition-credits block or semantic assessment is asserted checked.

The evidence inventory contains **777 files**. All listed files were rehashed without image decoding and retained their recorded size, SHA-256 and non-symlink regular-file status at **20:17:58 UTC**. Later additional live evidence files are outside that inventory.

The independent lexical check, completed at **20:18:26 UTC**, resolves **982 explicit file-reference occurrences** and **four wildcard occurrences** to all 777 inventory files. Unsafe, missing, empty, symlink and unreferenced recognized targets are all zero. The four wildcard patterns for pages5–8 match 7, 5, 6 and 7 files. Two extensionless `evidence/replay` occurrences remain unclassified; surrounding prose was not inspected, and they are not asserted to be missing files.

All 30 inputs to the independent lexical check remained byte-stable. Strong host-path comparisons against p90 found zero new candidates in the seven source text files, canonical replay script, five metadata files, unchanged ledger prefix or any field of the 254 appended rows. Network URLs were masked. The reference parser reproduced the exact p90 occurrence set; the prior undisclosed host-path regex implementation is not claimed byte-identical. These signatures are not exhaustive for every host path or encoding.

### Exact frozen hashes

| Item | Bytes | SHA-256 |
|---|---:|---|
| Frozen `CORRECTIONS.tsv` | 2650613 | `89ab08d49b9c72a64da705ae0099158a4ebce314ebe54372447a124e4534fded` |
| `FROZEN_REPLAY_P095.md` | 13120 | `c51db68a8f77daee4ae1266a4cb96250d358a99f9870fffa46775eb4b0fefbfa` |
| `FROZEN_REPLAY_P095.json` | 705488 | `fa2eb02b9f40bf9b290499aaa96d527cfbb80a3a6fca185684dbc3927b52bb2d` |
| Canonical `replay_corrections.py` | 901 | `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539` |
| English TeX source | 1532954 | `380549be7d6de057c145a862dc1468adf6e1b77e10e101c79e71c21a4c3482e9` |
| Corrected French TeX source | 1560945 | `f342d20045a9da86a59f4c592fa82bbe6abe296d629417baa1ad2af57a787b9e` |
| Diplomatic French TeX source | 1579383 | `8fe9e4b52bd763868783e103560e24bac1eb490245daa1299d53d4924093e70d` |

### Limits of this append

No scans or image contents were inspected, no mathematics or source-page prose was assessed, and no protected research-context bodies were read. This was not a first or second visual reading, proof check, PDF-layout review, edition build, packaging or upload. No correctness, evidence-sufficiency or completion claim beyond the stated mechanical checks is made. The receipt does not certify later live edits or any checkpoint archive. This append changes only `REPLAY_CHECK.md`; source files, correction rows and completion markers are untouched by this operation.


## Frozen p98 mechanical replay — scoped receipt

Recorded: **2026-11-18 20:43:29 UTC**. Root read the complete 14,064-byte bounded receipt and independently verified its Markdown, JSON and frozen-ledger hashes before authorizing this append.

**PASS: 63 scoped mechanical assertions (46 core + 17 ancillary).** Frozen Volume I scope: through printed p98 / scan116, last recorded completion **2026-11-18 20:32:59 UTC**; capture **2026-11-18 20:33:53 UTC**; verification completed **2026-11-18 20:37:08 UTC**.

### Capture and replay

Explicit before/copied/after byte inventories match for all **16 source files, 13 top-level metadata files and 12 scripts**. The separately frozen original source tree also has matching before/copied/after inventories. All **813 evidence entries** have matching filename, size, SHA-256 and symlink inventories before and after capture; every listed entry was rehashed unchanged at **2026-11-18 20:35:16 UTC**. Frozen verification inputs remained byte-stable. This establishes an observed stable copy interval, not an atomic filesystem snapshot; evidence files added later are outside the inventory.

The canonical replay ran **2026-11-18 20:34:44–20:34:59 UTC**, applying all **4,332 ledger rows once, in order, from pristine frozen originals**, without skips, repairs or restarts. Exit status 0; stderr empty. All **16 captured/replayed source files are directly byte-identical**, with missing/extra/differing counts **0/0/0**. All **13 non-TeX assets** are unchanged from supplied originals. The ledger has the exact ten-column schema, no malformed widths and only the five allowed kinds. Lexical confidence counts are 4,329 high and three medium I-Q004; all are first-reading/second-reading-pending. These counts are not confidence judgments.

Recorded completion metadata contains 117 raw records/events minus the explicit void p27 completion at 15:25:32 UTC, yielding **116 active completions in exact scan order 1–116**. Active record/event labels, timestamps and order match; the final active entry is p98 / scan116 at 20:32:59 UTC. These checks do not independently establish visual completion.

### Prefix, protected bytes and manifests

Every field of the first **4,164 ledger records** matches the verified p95 ledger. The **168 appended rows** are confined to pages96–98 in nondecreasing order:

| Printed page | As-printed | Corrected | English | Total |
|---|---:|---:|---:|---:|
| 96 | 23 | 21 | 21 | 65 |
| 97 | 16 | 16 | 15 | 47 |
| 98 | 17 | 20 | 19 | 56 |

The final 56 p98 records occupy data rows4277–4332 and all participated in the complete canonical replay. No prior failed-edit or resumption history was reconstructed.

Protected-byte comparison covers only the explicit `tex/common/p004.tex` rights block **including both delimiter lines**, and the unique complete `IllusiePthreeAuthor` definition line **excluding its line ending**, in each of the three TeX files. All three rights blocks and all three author lines are identical across supplied, captured and replayed states; their hashes match the verified p62 baseline. No separate edition-credits block is asserted checked.

All **six original manifest files** are stable and match the verified p95 baseline. All **15 declared original I source entries** match their sizes and SHA-256 values. Frozen-original, live-original and captured I source manifests are byte-identical. Scan/context payloads and II source payloads were not rehashed.

### Evidence and lexical path scope

The ancillary check resolves **1,026 explicit file-reference occurrences and four wildcard occurrences** to all **813 unique inventoried evidence files**. Unsafe, missing, empty, symlink and unreferenced recognized targets: **0**. Two extensionless `evidence/replay` occurrences remain unclassified and are not asserted missing. All 30 inputs to the independent lexical checker remained byte-stable. Its parser reproduces the p95 occurrence set. Comparable source/script/metadata text and every ledger field show no new strong-host-path candidates under its stated signatures and URL masking. This is a bounded lexical check, not an exhaustive assertion about every path encoding. Images were byte-hashed only, never viewed or decoded.

### Frozen artifact hashes

- Bounded Markdown: `tmp/frozen-replay-p098-9j1cxw22/FROZEN_REPLAY_P098.md`; **14,064 bytes**; SHA-256 `afa785ecb2cdaf9cb8ebb0496275917bcbeaf05bcca16038d7aa59a8822799e1`.
- Aggregate JSON: `tmp/frozen-replay-p098-9j1cxw22/FROZEN_REPLAY_P098.json`; **733,666 bytes**; SHA-256 `4694d45d16e6427bb2314aa2de326bd45fb3695a951b4e5cf6b875170a7129cc`.
- Frozen `captured/CORRECTIONS.tsv`: **2,799,726 bytes**; SHA-256 `c603baa82cbe1b41af9d433785f28e47300210d375b44f4997337f3193bc5cb1`.
- Canonical replay script: SHA-256 `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`.

| Captured/replayed source | Bytes | SHA-256 |
|---|---:|---|
| `english/02-volume-I-english.tex` | 1534666 | `c6723f0663ac8049fc7af66dffd4514faa769288992cc1aad3083774daba1805` |
| `francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1562670 | `cbdf2fb98b4bc821936e7e4b3793c7a3b3f790a4a206498129c7c0a9fa2c3925` |
| `francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1581084 | `fda05495c327fb77394cf4637a5e9a8654c8beb499522580f4005f9e240d4ba9` |

This receipt concerns only the frozen p98 state. It does not certify later live edits or checkpoint archives. No scans, image contents, source prose, mathematics, research-context bodies, evidence sufficiency or editorial judgments were assessed. No visual first/second reading, proof check, PDF layout review, edition build, packaging or upload was performed by this mechanical verification. This authorized receipt append changes only `REPLAY_CHECK.md`.


## Frozen p99 narrow source/ledger replay — scoped receipt

Recorded: **2026-11-18 20:49:51 UTC**. Root read the complete 8,684-byte narrow receipt and independently verified its Markdown, JSON and frozen-ledger byte sizes and SHA-256 values before authorizing this append.

**PASS: 51 scoped assertions (27 core + 21 independent prefix/completion checks + three final stability checks).** Scope: frozen Volume I through **printed p99 / scan117**, final recorded completion **2026-11-18 20:40:02 UTC**; capture **2026-11-18 20:43:29 UTC**; final verification **2026-11-18 20:47:13 UTC**.

Explicit **before/copied/after byte inventories match** for all 16 captured live source files; the ledger, three completion metadata files and canonical replay script; and all 16 separately copied pristine originals. The pristine seed also matches the verified p98 seed. All **38 private frozen inputs** remained byte-stable through final assembly, as did the p98 baseline ledger. All 16 replayed outputs retained their hashes and direct byte equality. This establishes an observed stable copy interval, not an atomic filesystem snapshot.

The unchanged canonical replay ran **2026-11-18 20:44:53–20:45:08 UTC**, applying all **4,385 rows once, in order, from pristine frozen originals**, without skips, repairs or restarts. Exit status 0; stderr empty. All **16 captured/replayed source files are directly byte-identical**, with missing/extra/differing **0/0/0**. All **13 non-TeX files** are also byte-identical to the supplied originals. Both ledgers have the exact ten-column schema and valid record widths; replay targets are confined to the three expected relative TeX paths.

Every field of the first **4,332 records** is unchanged from p98. The complete p98 ledger is also an exact raw-byte prefix, including its header and line endings. The **53 additions**, data rows **4333–4385**, are exclusively p99: **15 as-printed, 21 corrected and 17 English**. Added kind counts are seven structure, nine typesetting, 34 reading and three translation.

The unique final p99 done marker in `progress.log` and final active p99/scan117 record in `CHECK_RECORD.md` agree on **20:40:02 UTC**. `CHECK_EVENTS.tsv` contains 220 statement-check records, latest timestamp **20:39:44 UTC**, and does not independently record the page-completion time. No parseable event timestamp is later than completion. These are mechanical metadata checks, not independent evidence of visual reading.

### Frozen artifact hashes

- `tmp/frozen-replay-p099-nvqbpau7/FROZEN_REPLAY_P099_NARROW.md`: **8,684 bytes**; SHA-256 `6a2b6e486f85f305d8a3dd442c95be998c763076319356dbea59e6a40697d969`.
- `tmp/frozen-replay-p099-nvqbpau7/FROZEN_REPLAY_P099_NARROW.json`: **64,847 bytes**; SHA-256 `228b978fb7c3b9632c451df6696dd98ff10da0d66a1aca814b40b265a2f0a7b7`.
- Frozen `captured/CORRECTIONS.tsv`: **2,840,342 bytes**; SHA-256 `63417c547a9e3da986de2bc47948aee286c1bb9c407764fb841fd87bf8a9a55b`.
- Canonical replay script: **901 bytes**; SHA-256 `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`.

This verifies reproducibility of the **captured final p99 state** after the reported partial edit and resumption. **The transient partial-edit/resumption sequence was not reconstructed.** Later live edits and checkpoint archives are outside scope. Evidence resolution/hashing, the six-manifest check, dedicated rights/author extraction, strong-host-path scanning and confidence-distribution checks were **not repeated for p99**. No images, scans, source prose, mathematics, protected research-context bodies or editorial correctness were assessed. No visual reading, edition build, PDF review, packaging or upload was performed by this narrow verification. This authorized append changes only `REPLAY_CHECK.md`.


## Frozen p102 narrow source/ledger replay — scoped receipt

Recorded: **2026-11-18 21:04:27 UTC**. Root read the complete 10,871-byte bounded receipt and independently verified its Markdown, JSON and frozen-ledger byte sizes and SHA-256 values before authorizing this append.

**PASS: 61 scoped assertions (28 core + 30 independent prefix/completion/scope checks + three final stability checks).** Scope: frozen Volume I through **printed p102 / scan120**, final recorded completion **2026-11-18 20:56:08 UTC**; capture **2026-11-18 20:56:46 UTC**; final verification **2026-11-18 21:00:46 UTC**.

Explicit **before/copied/after byte inventories match** for all 16 captured live source files; the ledger, four scope/completion metadata files and canonical replay script; and all 16 separately copied pristine originals. The pristine seed also matches the verified p99 seed. All **39 private frozen inputs** remained byte-stable through final assembly, as did the p99 baseline ledger. All 16 replayed outputs retained their comparison hashes and direct byte equality. This establishes an observed stable copy interval, not an atomic filesystem snapshot.

The unchanged canonical replay ran **2026-11-18 20:57:34–20:57:48 UTC**, applying all **4,538 rows once, in order, from pristine frozen originals**, without skips, patches, repairs or restarts. Exit status 0; stderr empty. All **16 captured/replayed source files are directly byte-identical**, with missing/extra/differing **0/0/0**. All **13 non-TeX files** are also byte-identical to the supplied originals. Both ledgers have the exact ten-column schema, all current widths are valid, only allowed kinds occur, and replay targets are confined to the three expected relative TeX paths.

Every field of the first **4,385 records** is unchanged from p99. The complete p99 ledger is also an exact raw-byte prefix, including its header and line endings. The **153 additions**, data rows **4386–4538**, form contiguous, ordered blocks:

| Printed page | Data-row range | As-printed | Corrected | English | Total |
|---|---|---:|---:|---:|---:|
| 100 | 4386–4441 | 17 | 19 | 20 | 56 |
| 101 | 4442–4491 | 13 | 18 | 19 | 50 |
| 102 | 4492–4538 | 16 | 18 | 13 | 47 |
| **Total** | **4386–4538** | **46** | **55** | **52** | **153** |

The unique final p102 done marker in `progress.log` and final active p102/scan120 record in `CHECK_RECORD.md` agree on **20:56:08 UTC**. `CHECK_EVENTS.tsv` contains 231 statement-check records, latest timestamp **20:55:42 UTC**, and does not independently record the page-completion time. No parseable event timestamp is later than completion.

The current-summary lexical search was restricted to **CHECK_RECORD lines 1–92**, excluding historical page records, and **README lines 1–10**. Requested numeric markers agree: `CHECK_RECORD.md` line 9 gives notation scope through **printed p. 102**; line 76 gives **scans 1–120 / printed pp. 1–102**, with remaining scans **121–380**; `README.md` line 8 gives **scan120 / printed pages 1–102**. No requested marker was stale or ambiguous, and no metadata was repaired. Only these numeric fields were validated; surrounding narrative, notation correctness and visual-completion claims were not assessed.

### Frozen artifact hashes

- `tmp/frozen-replay-p102-6lqo4s2_/FROZEN_REPLAY_P102_NARROW.md`: **10,871 bytes**; SHA-256 `a3925675e994abcf5a3c430a14ba49bacc16c435995734de7b83c38ff297428d`.
- `tmp/frozen-replay-p102-6lqo4s2_/FROZEN_REPLAY_P102_NARROW.json`: **76,545 bytes**; SHA-256 `5f0548f5d1a281536d12ced4849906233e4b3fac14eddede2889187cc664f5ad`.
- Frozen `captured/CORRECTIONS.tsv`: **2,953,104 bytes**; SHA-256 `7451b4ffbb87e72c3a59e4af52df5047f637a876ffb6ac37aa7b44e0b8df1f96`.
- Canonical replay script: **901 bytes**; SHA-256 `a918ca20865b47522d2719f1ec4c6eeccdc063071c1fbc810e8f26e3f474e539`.

This verifies reproducibility of the **captured final p102 state**. Earlier transient editing histories were not reconstructed; later live edits and checkpoint archives are outside scope. Evidence resolution/hashing, the six-manifest check, dedicated rights/author extraction, strong-host-path scanning and confidence-distribution checks were **not repeated for p102**. No images, scans, source prose, mathematics or protected research-context bodies were assessed. No visual reading, edition build, PDF review, packaging or upload was performed by this narrow verification. This authorized append changes only `REPLAY_CHECK.md`; no new replay was run for the append.
