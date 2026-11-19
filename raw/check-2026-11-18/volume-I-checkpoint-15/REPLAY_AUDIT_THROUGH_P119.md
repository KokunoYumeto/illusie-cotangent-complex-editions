# Mechanical replay audit through printed page 119

Frozen snapshot: **2026-11-19 01:34:39 UTC**. The primary reader identified the milestone as completed through printed page 119 at 01:34:06 UTC and continued page 120 onward after capture. This report applies only to the frozen snapshot and does not certify the later live state or independently determine page-reading coverage.

## Replay and ledger structure

**All 5,185 recorded replacements replay exactly onto a fresh extraction of the supplied original Volume I sources. All three resulting TeX files are byte-for-byte identical to the frozen working sources.**

| Layer | Ledger rows |
|---|---:|
| as-printed | 1,693 |
| corrected | 1,762 |
| English | 1,720 |
| build | 10 |

| Kind | Ledger rows |
|---|---:|
| structure | 922 |
| typesetting | 2,584 |
| reading | 1,442 |
| translation | 130 |
| misprint of the original | 100 |
| terminology | 7 |

The ledger has exactly the required ten columns. No malformed row or empty required field was found among file, layer, old, new, evidence, kind, and confidence. Each old-text replacement was required to match exactly once by the unchanged existing replay script. The replay operated only on a private tree extracted from `ILLUSIE_I_sources.zip`.

## Evidence filename resolution

The frozen ledger contains **104 distinct image/PDF filename references**: **99 explicit evidence paths**, two uniquely resolved evidence basenames, one supplied scan PDF, and two shortened names unresolved as literal paths. All 99 explicit evidence paths exist. Both shortened names have unique same-page filename candidates in the captured evidence-file inventory:

| Literal reference | Ledger rows | Same-page filename candidate |
|---|---|---|
| `footnote.png` | 5111, 5121, 5131 | `evidence/I_p117_footnote.png` |
| `note-call.png` | 5111, 5121, 5131 | `evidence/I_p117_note-call.png` |

The affected rows are printed page 117, respectively as-printed, corrected, and English. These are literal-reference flags, not findings that the image files are missing. No filename was repaired by this audit, and no image content was inspected. Reference-to-row mapping uses exact extracted filename tokens, avoiding accidental matches inside already complete paths.

## Anchor and page-marker inventory

Literal identifiers were extracted mechanically from `label`, `hypertarget`, `pdfbookmark`, and the `illusiefrontpage` / `illusiebodypage` environments. Macro-parameter placeholders containing `#` were excluded. This is a syntactic inventory, without TeX expansion or compilation. The following counts apply to **each of the three source layers**:

| Identifier class | Original source occurrences | Frozen occurrences | Preservation result |
|---|---:|---:|---|
| Labels | 356 | 356 | Identical identifier sequence |
| Hyperlink targets | 3,940 | 3,943 | Every original occurrence retained; three additions |
| PDF bookmark IDs | 1 | 1 | Identical identifier sequence |
| Front-page markers | 6 | 6 | Identical identifier sequence |
| Body-page markers | 355 | 355 | Identical identifier sequence |

No original identifier occurrence is missing. The added literal hyperlink targets are `illusie:I:front:p007`, `illusie:I:front:p008`, and `illusie:I:front:p009`. The original duplicate target `illusie:I:cover` still occurs twice; there are no new duplicate literal target IDs.

The raw hyperlink-target sequence differs from the original source sequence: ten retained note-target identifiers changed position, in addition to the three additions. All five identifier sequences—including those target positions—are **identical to supplied checkpoint 09** in each layer. Thus these inventory differences predate the present continuation; this audit makes no editorial judgment about them.

The ten position-changed identifiers are:

- `illusie:I:ch1:s2:1:2:n1`
- `illusie:I:ch1:s2:2:6:n1`
- `illusie:I:ch1:s2:2:6:n2`
- `illusie:I:ch1:s2:2:7:n1`
- `illusie:I:ch1:s2:2:8:n1`
- `illusie:I:ch1:s2:3:1:n2`
- `illusie:I:ch1:s2:3:6:n1`
- `illusie:I:ch1:s2:3:13:n1`
- `illusie:I:ch1:s2:3:13:n2`
- `illusie:I:ch1:s3:1:4:n1`

## Frozen source identity

| Source | Bytes | SHA-256 |
|---|---:|---|
| `sources/english/02-volume-I-english.tex` | 1,539,448 | `9fc96754ce83658ea253c821fbf195097c49498836b78ecadac239a388ed16b4` |
| `sources/francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex` | 1,567,444 | `7360b35024b9dc000c8c4add4a2bb4b6f4ca8cfa10d2039072188a394157ae09` |
| `sources/francais-diplomatique/02-volume-I-francais-diplomatique.tex` | 1,585,833 | `dd7ddf388f22cca8dafa0afd1a743cec7327da75c634b6b5abb5b450dc790754` |

## Snapshot consistency and scope

The correction ledger and three sources had identical SHA-256 values before capture, after capture, and in their private frozen copies. Subsequent primary-reader edits do not alter this audit snapshot. The evidence filename inventory was captured with the snapshot, and the full replay and inventory results remain in private audit support material.

This is an exact edit-replay, schema, filename-resolution, and identifier-inventory audit. It is **not a second visual reading**, an interpretation of a scan, a translation or mathematical judgment, a build check, or a claim that every needed correction has been found. File existence alone does not establish evidence for a reading.

No live source, correction row, prior report, progress log, or page-status record was changed. The only addition to the active deliverable tree is this scoped report. No ZIP was created. Checkpoint 10 remains due at 2026-11-19 01:44:37 UTC.
