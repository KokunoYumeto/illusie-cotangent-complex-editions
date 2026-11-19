# Attachment and restoration integrity

Verified: 2026-11-19 00:59:23 UTC

Infrastructure check only. No page reading, source-text verdict, or mathematical verification is implied.

All eight outer ZIP sizes and SHA-256 hashes agree with the supplied README.
Every included manifest/file-list member agrees in size and SHA-256. All indexes were parsed before extraction.
The archive indexes themselves have no self-hash. No unexpected unlisted members or prior-checkpoint dependencies were found.

| Archive | Listed payload files verified | Total archive files | Result |
|---|---:|---:|---|
| `ILLUSIE_II_CHECK_checkpoint_09.zip` | 18 | 19 | pass |
| `ILLUSIE_II_context.zip` | 25 | 26 | pass |
| `ILLUSIE_II_scans.zip` | 3 | 4 | pass |
| `ILLUSIE_II_sources.zip` | 5 | 6 | pass |
| `ILLUSIE_I_CHECK_checkpoint_09.zip` | 942 | 943 | pass |
| `ILLUSIE_I_context.zip` | 32 | 33 | pass |
| `ILLUSIE_I_scans.zip` | 2 | 3 | pass |
| `ILLUSIE_I_sources.zip` | 15 | 16 | pass |

## Restoration

- Checkpoint 09 was restored into the corresponding volume workspace.
- Supplied scans, original sources, and context remain in separate input trees.
- Supplied input ZIPs are linked beside, outside, the deliverable workspaces.
- Existing different content is never overwritten by the restoration script.
- The checkpoint `sources/MANIFEST.tsv` records the original release inputs; the checkpoint `FILE_LIST.tsv` is the hash authority for the checkpoint sources.
- Volume II was restored only; its text check has not begun.
