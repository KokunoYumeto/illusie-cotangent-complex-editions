# Staged correction queue validation

Validation recorded **2026-11-19 05:14:36 UTC**. This is infrastructure validation of synthetic fixtures only. No queue was generated from the active Illusie ledger, no source or image was opened, and no correction or page was marked reviewed.

## Result

The independent fixture suite returned **exit 0; 10 tests passed in 1.816 seconds**. Generator syntax parsing and CLI help also succeeded. The staged tested files have these SHA-256 values:

| File | SHA-256 |
|---|---|
| `correction_review_queue.py` | `05b9fe2353fc2259e1ceca966c020cab171597c79e16d917e80007cf9f27a5db` |
| `test_correction_review_queue.py` | `52faad14d1d4377a6e1c59c1697c70d6b13910c2cd55db425c51a75cc583043c` |

Tests cover Roman/decimal ordering; stable original-row ties; duplicate rows and both explicit fixture run labels; exact preservation of every original cell including tabs, LF/CRLF, quotes, Unicode, empty strings, surrounding whitespace, confidence strings, additional columns and a 200000-character field; a fixed independent row-digest vector, mutation and reorder behavior; repeatable queue bytes and manifest hashes; evidence extraction; schema/encoding/unsupported-label refusal; header-only input; no overwrite or output inside the input tree; changed-input refusal; and cleanup after a simulated publication failure.

Two synthetic evidence-extraction defects found during review were fixed and regression-tested: angle-wrapped Markdown targets with spaces, and filename-like text inside URL query suffixes.

To rerun only these synthetic checks:

```sh
python3 -B tmp/infrastructure/test_correction_review_queue.py
```

## Intentional limits

The CLI must be run against the frozen final ledger after the primary completes the first reading of all Volume I pages. It includes every original row without assigning a run where no run column exists. Unknown page-label forms stop generation. Evidence candidates are extracted mechanically and remain unresolved. Coverage counts describe correction records, not page-reading completion or editorial validity. The primary's actual final second reading remains required.

All staged paths are relative. The script stores only input/output filenames in its manifest and does not serialize local directory paths. No active source, ledger, report, checkpoint or save receipt was modified; no checkpoint was created or uploaded.
