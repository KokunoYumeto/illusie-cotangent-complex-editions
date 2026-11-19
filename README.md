# Luc Illusie, *Complexe cotangent et déformations* I–II

[Version française](README.fr.md)

Editable LaTeX editions of Luc Illusie's *Complexe cotangent et déformations I* and *II* (Lecture Notes in
Mathematics 239 and 283, Springer-Verlag, 1971 and 1972), the work that founded the theory of the cotangent complex
and its use in deformation theory.

## Read and download

Each edition comes as a PDF, its complete LaTeX file, and a ZIP of its sources:

| | French, corrected | English | French, diplomatic |
|---|---|---|---|
| Volume I | [PDF][01] · [LaTeX][02] · [sources][03] | [PDF][04] · [LaTeX][05] · [sources][06] | [PDF][16] · [LaTeX][07] · [sources][08] |
| Volume II | [PDF][09] · [LaTeX][10] | [PDF][13] · [LaTeX][14] | [PDF][11] · [LaTeX][12] |

The three editions of Volume II share one [source ZIP][15]. The Volume I files are in the release
[check-2026-11-19](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/tag/check-2026-11-19), the Volume II files in [volume-II-2026-11-19](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/tag/volume-II-2026-11-19), and the `tex/` folder
of this repository holds the same LaTeX files.

- The **diplomatic** French keeps the printed text as it stands, slips included.
- The **corrected** French corrects evident slips of the printing.
- The **English** is a translation of the French.

Text, formulas and diagrams are LaTeX (the diagrams in TikZ), not page images.

## How it was made

The transcription, the corrections and the English translation were produced by AI with OpenAI Codex: mainly
GPT-5.6 Sol at Ultra effort, with parts done by GPT-6 Astra at Ultra effort, in August and September 2026.

## Quality

On 18–19 November 2026 GPT-6 Astra (ChatGPT Pro mode) checked Volume I against the scan of the printed volume
(Lecture Notes in Mathematics 239), page by page in the three layers: the diplomatic French against the print, the
corrected French and its corrections, and the English against the corrected French. **The front matter and printed
pages 1–188 are checked** (of 355); the author's errata for pp. 11, 60 and 87 are applied. It recorded 7,230 changes
(diplomatic 2,224, corrected 2,526, English 2,470, build 10), among them 130 misprints of the original, corrected in
the corrected French. The second reading of these changes, pages 189–355, the rest of the errata and the notes are
still to come; Volume II is not yet checked. The records are in
[raw/check-2026-11-18](raw/check-2026-11-18), the whole checkpoint is a release asset.

The checkpoint's LaTeX did not build. Claude (Claude Opus 5.5 at effort high) repaired it by script, typesetting only,
in 23 places (control words run together with the next letter, and a display macro used outside its scope), each
logged in [REPAIR_LOG.tsv](raw/check-2026-11-18/build-repair-2026-11-19/REPAIR_LOG.tsv); no reading was changed.
The three editions of Volume I build with LuaLaTeX, two passes, without error and with nothing running into the
margin (for one page of the English, the paragraph spacing of the build was given a little more shrink).
Claude compared two of the check's corrections with the scan (p. 149, "h = fp = qg"; p. 169, Exal_A(P, Ω_{P/A})):
both are as the record says. The diplomatic French of Volume I now also has a [PDF][16].

On 6 November 2026 Claude (Anthropic, Claude Opus 5.5 at effort max) compared three pages line by line with the printed volumes:
Volume I pages 13 and 35 and Volume II page 155 in the diplomatic French, and the English of Volume I page 13.

- The text, the formulas and the seven commutative diagrams on these pages match the print.
- The diplomatic French departs from the print in three small ways: a paragraph break added mid-sentence (I, p. 13);
  the punctuation after three displayed diagrams left out (I, p. 35); the printed misspelling "homormorphisme" given
  as "homomorphisme" (II, p. 155).
- The English of I, p. 13 is accurate and corrects a misprinted index in its last formula (Y′ → Y′ for Y → Y′).

Three pages are a small sample, and there will be other errors. Please report them as GitHub issues.

## About this edition

Luc Illusie's journal articles are freely available on Numdam, which publishes with the agreement of the journals,
writes to living authors, and withdraws the article of an author who refuses. We take this as an indication that
Luc Illusie may not object to this edition, but we may be wrong. We wrote to the author in October 2026 and have had
no reply.

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Our transcription, translation, corrections and typesetting were produced by AI. They have no human author and, in our understanding, are not protected by copyright; where any right of ours exists nonetheless, it is dedicated to the public domain under CC0 1.0. All of this work reproduces or translates the original work, so nothing here licenses or authorizes any reproduction, translation or other use of that work. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

[01]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/01-volume-I-francais-corrige.pdf
[02]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/02-volume-I-francais-corrige.tex
[03]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/03-volume-I-francais-corrige-sources.zip
[04]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/04-volume-I-english.pdf
[05]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/05-volume-I-english.tex
[06]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/06-volume-I-english-sources.zip
[07]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/07-volume-I-francais-diplomatique.tex
[08]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/08-volume-I-francais-diplomatique-sources.zip
[09]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/09-volume-II-francais-corrige.pdf
[10]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/10-volume-II-francais-corrige.tex
[11]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/11-volume-II-francais-diplomatique.pdf
[12]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/12-volume-II-francais-diplomatique.tex
[13]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/13-volume-II-english.pdf
[14]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/14-volume-II-english.tex
[15]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/volume-II-2026-11-19/15-volume-II-sources-completes.zip
[16]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/16-volume-I-francais-diplomatique.pdf
