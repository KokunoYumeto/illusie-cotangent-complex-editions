# Mechanical replay audit through printed page 110

Frozen state: **19 November 2026, 01:10:21 UTC**. The primary reader identified this state as complete through printed page 110. This infrastructure audit does not independently determine page-reading coverage.

## Result

**All 4,926 recorded changes replay exactly onto the supplied original Volume I sources. The three resulting TeX files are byte-for-byte identical to the frozen working sources.**

| Layer | Ledger rows |
|---|---:|
| as-printed | 1,607 |
| corrected | 1,675 |
| English | 1,634 |
| build | 10 |

| Kind | Ledger rows |
|---|---:|
| structure | 847 |
| typesetting | 2,447 |
| reading | 1,404 |
| translation | 127 |
| misprint of the original | 100 |
| terminology | 1 |

## Method and checks

- Captured the correction ledger and all three TeX files into a private frozen workspace. SHA-256 values were identical before capture, after capture, and in the captured copies.
- Extracted the supplied `ILLUSIE_I_sources.zip` into a separate private replay tree.
- Ran the existing `scripts/replay_corrections.py` unchanged against the frozen ledger. Each row required exactly one occurrence of its `old` text before replacement.
- Compared the replayed file bytes with the frozen source bytes after all rows completed.
- The ledger has exactly the expected ten columns. There are no malformed rows or empty required fields among file, layer, old, new, evidence, kind, and confidence.
- All 71 distinct explicit `evidence/` image references in the frozen ledger point to existing files.
- The broader filename check found 76 distinct image/PDF references, including 2 evidence basenames and 1 supplied scan/errata PDF references; unresolved references: 2.

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,148 | `df458d13823a57d1faf16ed6cac03c531bf3aa1eb848112a09b1b137442ec0ce` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,122 | `cfabd5a20d4998451117dff45e28349829ff0c22478e83fee50c0d1aebdb1a2e` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,516 | `0c299f80abe4466c190f5892274d21a5e8d31e3134ea147d0366f2769c69fb7c` |

## Reference exceptions requiring reader review

The broader filename parser found two literal strings that do not resolve as written. These do not affect exact edit replay. The names below are mechanical matches only; no image-content interpretation was made.

| Literal reference | Ledger row(s) | Mechanical filename candidate(s) |
|---|---|---|
| `Evidence/I_p004_postcat.png` | 570 (p. 4, corrected), 583 (p. 4, English) | `evidence/I_p004_postcat.png` |
| `exact-second.png` | 4897 (p. 110, as-printed), 4908 (p. 110, corrected), 4919 (p. 110, English) | `evidence/I_p110_exact-second.png` |

## Metadata-reference repairs after the frozen audit

Applied: **2026-11-19 01:12:32 UTC**. The primary reader authorized the following literal evidence-reference repairs in the active ledger after the frozen replay audit. The frozen snapshot and replay results above remain unchanged.

| Correction row(s) | Original literal | Repaired literal |
|---|---|---|
| 570, 583 | `Evidence/I_p004_postcat.png` | `evidence/I_p004_postcat.png` |
| 4897, 4908, 4919 | `exact-second.png` | `evidence/I_p110_exact-second.png` |

These are **metadata-reference repairs only**. Exactly the five listed `evidence` cells changed. Every other cell, including `old`, `new`, `confidence`, source filename, page, and layer, was verified unchanged. Each repaired relative path resolves to an existing evidence image. The replacement of the shortened filename was bounded so that an already complete path could not be altered.

No TeX source or page text was changed. No new correction row was added, no correction was visually reconsidered, and no confidence or mathematical verdict was changed. The additional report was installed as `REPLAY_AUDIT_THROUGH_P110.md`; the older `REPLAY_CHECK.md` was preserved.

## Scope

This is a mechanical replay and file-reference audit. It establishes that the recorded exact replacements account for the frozen source bytes. It is **not a second visual reading**, a scan-based adjudication, an assessment of translation or mathematics, a compilation check, or a certification that every needed correction has been recorded. Evidence existence does not establish that an image supports its associated reading.

The frozen audit itself changed no active source, correction ledger, check record, or replay report. The subsequent authorized metadata-reference repairs and installation of this additional report are documented above. No ZIP was created.
