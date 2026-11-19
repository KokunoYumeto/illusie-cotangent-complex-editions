# Mechanical replay audit through printed page 112

Frozen snapshot: **2026-11-19 01:19:23 UTC**. The primary reader identified this state as complete through printed page 112, with page 113 active. This infrastructure audit does not independently certify page-reading coverage.

## Result

**All 4,996 recorded changes replay exactly onto a fresh extraction of the supplied original Volume I sources. The three resulting TeX files are byte-for-byte identical to the frozen working sources.**

| Layer | Ledger rows |
|---|---:|
| as-printed | 1,634 |
| corrected | 1,697 |
| English | 1,655 |
| build | 10 |

| Kind | Ledger rows |
|---|---:|
| structure | 859 |
| typesetting | 2,486 |
| reading | 1,423 |
| translation | 127 |
| misprint of the original | 100 |
| terminology | 1 |

## Mechanical method and structural validation

- Captured `CORRECTIONS.tsv` and the three TeX files into a private frozen workspace; their hashes agreed before capture, after capture, and in the captured copies.
- Extracted `ILLUSIE_I_sources.zip` into a separate private replay tree and ran the existing `replay_corrections.py` unchanged against the frozen ledger.
- Every replacement found exactly one occurrence of its `old` text; all resulting file bytes matched the frozen working sources.
- The ten-column ledger header is correct. There are no malformed rows and no empty required fields among file, layer, old, new, evidence, kind, and confidence.
- The evidence scan found 87 distinct image/PDF filename references: 83 exact evidence paths, two uniquely resolved evidence basenames, one supplied scan PDF, and one shortened filename that does not resolve literally as written.
- All 83 explicit evidence paths exist. No missing image was established: the unresolved shortened filename has the same-page filename candidate documented below.

## Reference exception for reader review

| Literal reference | Ledger row(s) | Same-page mechanical filename candidate |
|---|---|---|
| `footnote.png` | 4930 (p. 111, as-printed), 4943 (p. 111, corrected), 4956 (p. 111, English) | `evidence/I_p111_footnote.png` |

The filename candidate is a mechanical match only. Its image content was not inspected. The audit initially left the ledger unchanged; the later authorized metadata repair is recorded below.

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,538,434 | `6ad1dcb412f36efbde5412ac6ccf8bf3607a2c42a3a5fd9aa56754d01f8e5ca6` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,566,416 | `f166846f51e800484c84a1721db08937530c7925e628e902a3b62798f2437f12` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,584,804 | `fd568ff3ac07aa34569c9b764c9e0f858e3f6c1069a7c53497257edd1ecad69d` |

## Authorized metadata-reference repair after the audit

Applied: **2026-11-19 01:20:41 UTC**. The primary reader authorized replacing the bare literal `footnote.png` with `evidence/I_p111_footnote.png` in the `evidence` cells of correction rows **4930, 4943, and 4956** (printed page 111, respectively as-printed, corrected, and English). The target is the unique existing exact-page crop matching that filename suffix.

This was a **metadata-reference repair only**. The raw ledger was patched within those three evidence fields without reserializing other fields. Every other field value, including `old`, `new`, `confidence`, page, and layer, was verified unchanged. Earlier p. 110 metadata-reference repairs were retained. No source or page text was changed; no visual reading, confidence judgment, or mathematical verdict was revised. The frozen snapshot and exact replay result above remain unchanged.

## Scope and preservation

This is an exact edit-replay, record-structure, and filename-resolution audit. It is **not a second visual reading**, a scan-based adjudication, a mathematical or translation check, a build check, or certification that all necessary corrections have been found. File existence does not establish evidentiary support for a reading.

No scan or page content was inspected. The audit itself added only this report. The subsequent authorized repair changed the three evidence fields documented above; all source text, confidence cells, progress logs, and earlier audit reports remained unchanged. No ZIP was created. Checkpoint 10 remains due at 2026-11-19 01:44:37 UTC.
