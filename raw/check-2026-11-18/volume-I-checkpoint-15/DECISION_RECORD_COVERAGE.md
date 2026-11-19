# Supplied decision-record coverage at printed page 133

Metadata inspection, 19 November 2026. This report concerns the supplied record schemas and lookup coverage only. It does not assess a reading, repair prose, mathematical claim, or the correctness of an existing edition change.

## Finding

The zero returned by `scripts/page_records.py` for `LNM239`, printed page **133**, physical scan page **151**, is genuine within the supplied exact-page decision ledgers. The four per-page JSONL ledgers in `ILLUSIE_I_context.zip`, under `edition_records/working_folder/`, all end at printed page **132**, physical page **150**. Their final entries share timestamp `2026-08-14T15:20:17.341Z`.

| File | Final physical JSONL line | Final record ID |
|---|---:|---|
| `SOURCE_CORRECTIONS.jsonl` | 129 | `ILL-SC-20260804-0129` |
| `NORMALIZATION_DECISIONS.jsonl` | 161 | `ILL-NORM-20260804-0160` |
| `TRANSCRIPTION_DECISIONS.jsonl` | 156 | `ILL-TX-20260804-0156` |
| `TRANSLATION_DECISIONS.jsonl` | 158 | `ILL-TR-20260804-0158` |

Each supplies one exact record for every printed page from 125 through 132, explaining the preceding count of four matches per page. No page-133/151 record was hidden by a numeric/string mismatch, conflicting locator, alternate work identifier, or nested explicit page locator. The recorded page-range fields do not extend to printed page 133. No helper change was required or made.

## Other supplied metadata

- `DIAGRAM_AND_FORMULA_REVIEW.csv` reaches printed page 132 / PDF page 150.
- `NOTATION_INDEX.csv` and `TERM_INDEX.csv` reach printed page 66 / PDF page 84.
- The 13 common record files are byte-identical in the two supplied context archives. The other context copy therefore supplies no later version of these records. This was a byte comparison; no Volume II edition text was inspected.

Two mapping records cover the queried location, but are navigation metadata rather than reading or correction decisions:

| File | CSV line, including header | Record ID | Coverage |
|---|---:|---|---|
| `PAGE_AND_UNIT_MAP.csv` | 9 | `ILL-PMAP-I-008` | Printed 114–150 / physical 132–168 |
| `SOURCE_PAGE_MAP.csv` | 4 | `illusie:I:pdf:p019-p360` | Printed 1–342 / physical 19–360 |

## Global-repair caveat

None of the 347 rows in `REVERSALS_AND_GLOBAL_REPAIRS.jsonl` has the top-level work/page locator fields required by `page_records.py`. The helper deliberately matches explicit locators and does not infer page applicability from prose. Its exact-page query therefore cannot establish that no global repair applies. No explicit page-133/151 metadata locator was found in that file; its repair prose was not assessed.

The precise conclusion is: **no matching explicit page decision in the supplied ledgers; their per-page coverage ends at printed page 132**. This does not establish that printed page 133 has no existing correction. Determining and adjudicating differences between the edition layers remains part of the primary review against the scans.

No source, ledger, or page-review record was changed by this metadata inspection.
