# Complexe cotangent et déformations I — standalone editions

This directory contains the completed local Volume I deliverables for Luc
Illusie's *Complexe cotangent et déformations I* (Springer Lecture Notes in
Mathematics 239):

- `french.pdf`: the standalone corrected-French edition;
- `english.pdf`: the standalone source-aligned English edition;
- `french-package.zip` and `english-package.zip`: independently buildable
  source packages for the corresponding edition;
- `manifest.csv`: byte and SHA-256 inventory for the outer deliverables;
- `validation.json`: deterministic build, structural, extraction, and visual
  QA receipt.

The bounded authority is the 380-page controlling scan identified by DOI
`10.1007/BFb0059052`, 14,349,904 bytes, SHA-256
`1855B49FE461B13B1CBAEE1341C8FC3E3E0CDDC034C54ABEC1165AF061B90A56`.
The authority scan and direct pixel evidence are identified but are not
redistributed in either package.

The corrected French and English attach to the same stable semantic units.
The diplomatic French remains an internal, auditable source-diplomatic layer and is not
presented as a third edition. Machine-readable Stacks-oriented records are a
pre-Stacks scaffold: blank or candidate fields do not assert an official
Stacks tag or an official equivalence.

From either unpacked package root, build the edition with LuaLaTeX using
`readers/fr.tex` or `readers/en.tex`. Three serial LuaLaTeX passes over the same master establish
the remembered-page overlays and stable cross-reference state. Required TeX
components include `fontspec`, TikZ, `tikz-cd`, `tabularx`, Latin Modern, and
TeX Gyre Heros.

These are local preservation artifacts. See `LICENSES.md` inside each package
for the deliberately conservative rights statement.
