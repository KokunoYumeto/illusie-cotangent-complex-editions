# Evidence-reference metadata repairs

These entries document literal reference repairs only. They do not record a new visual reading, source correction, confidence assessment, or mathematical judgment.

## Printed page 117 — 2026-11-19 01:37:40 UTC

The primary reader authorized replacing two shortened evidence filenames in correction rows **5111, 5121, and 5131**. Their page/layer metadata was checked mechanically: printed page 117, respectively as-printed, corrected, and English.

| Original literal | Repaired literal |
|---|---|
| `footnote.png` | `evidence/I_p117_footnote.png` |
| `note-call.png` | `evidence/I_p117_note-call.png` |

Each target is the unique existing exact-page crop matching that filename suffix. The replacements were bounded to the bare literals so that an already complete path could not be changed. The terminal punctuation after the filenames was preserved.

Exactly **three evidence cells** changed, with two literal replacements per cell. The raw TSV records were patched without reserializing the ledger. All other rows remained byte-identical, and all other fields—including `old`, `new`, `confidence`, source filename, page, and layer—were verified unchanged. The ledger contained **5,185 rows** at this repair.

Ledger SHA-256 before: `2e425b91c57187984f389a1a92db9948007c15cf54596d844c46aa583bfcceff`. Ledger SHA-256 after: `b8b86408d57feed27f1a8541c432871d58a06e9498b09e70f2b353dd3fb28d88`.

No source text, image content, or printed reading was reviewed. No TeX source, `CHECK_RECORD.md`, progress log, prior report, or frozen replay snapshot was changed. `REPLAY_AUDIT_THROUGH_P119.md` continues to describe its original frozen state, including the pre-repair shortened references. No ZIP was created.
