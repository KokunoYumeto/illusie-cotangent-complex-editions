# Second pass ILLUSIE I and II, continued: Luc Illusie, *Complexe cotangent et déformations* I and II (Lecture Notes in Mathematics 239 and 283), every page against the print

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. This prompt continues an earlier run and
holds the whole task for both volumes: Part A, Volume I, then Part B, Volume II. Eight ZIP files and the two files of
a terminology standard are attached: for Volume I `ILLUSIE_I_scans.zip`, `ILLUSIE_I_sources.zip`,
`ILLUSIE_I_context.zip` and the earlier run's `ILLUSIE_I_CHECK_checkpoint_09.zip`; for Volume II the same four with
`ILLUSIE_II`. Each of the six input zips has `MANIFEST.tsv` at its root (path in the zip, source, bytes, SHA-256,
role); each checkpoint has `FILE_LIST.tsv`. Read them first.

## This run continues an earlier one

An earlier run (GPT-6 Astra, ChatGPT Pro mode, 18 November 2026, both volumes in one chat) stopped after its
checkpoint 09, saved at about 21:35 UTC. Each checkpoint 09 is that volume's complete state: its `FILE_LIST.tsv` lists
every file with its size and SHA-256, and no file is held only by an earlier checkpoint. We verified both against
their lists.

**Restore first.** Unzip each checkpoint into the workspace of its volume, with that volume's three input zips beside
it, and check every file against `FILE_LIST.tsv`. Then read its `README.md`, `CHECK_RECORD.md`, `progress.log`,
`CORRECTIONS.tsv`, `EXISTING_CORRECTIONS.tsv`, `READING_QUESTIONS.tsv`, `EVIDENCE_INDEX.md`, `REPLAY_CHECK.md`,
`TOOLCHAIN_REPRODUCIBILITY.md` and `scripts/`.

**The state at checkpoint 09:**
- Volume I: the first reading is done through scan page 125, that is the front matter and printed pages 1–107, in all
three layers. 4,809 changes are recorded (as-printed 1,570, corrected 1,635, English 1,594, build 10) and 426 verdicts
on corrections already present (`EXISTING_CORRECTIONS.tsv`). The author's errata for pp. 11, 60 and 87 are applied;
the next erratum on the errata page is for p. 219. `READING_QUESTIONS.tsv` has ten open questions (pp. 1, 15, 62, 67,
68–69, 83, 85–90, 91, 96–98 and 103–104). Not done: printed pages 108–355 and the back matter, the rest of the errata,
the second reading of every correction row, the recurring-error searches, the three builds and the PDF check, and the
notes. The PDFs are not built.
- Volume II: not begun. The checkpoint holds the supplied sources and empty ledgers.

**Your task is the whole task of Parts A and B, from that state.** The earlier run's work is the draft you build on.
Check each part of it as you use it: a recorded correction against the scan, a verdict on an existing correction
against the print and the mathematics, a reading question against the image. Where you find it wrong, correct it in
every layer it belongs to and record the correction in `CORRECTIONS.tsv`, with `corrects the earlier run:` at the
start of its evidence. Then finish everything pending: every remaining page of Volume I in all three layers, every
erratum, every reading question answered from the image, the second reading of every correction row of both runs, the
recurring-error searches, the builds and the PDF check, the notes and `CHECK_EVENTS.tsv`, and the final
`ILLUSIE_I_CHECK.zip`; then the whole of Part B and `ILLUSIE_II_CHECK.zip`.

Do Part A to its end, final ZIP included, before you start Part B. Each part keeps its own workspace, records,
checkpoints and final ZIP, as its text says; both parts' checkpoints continue the earlier run's numbering from 10.

**The terminology standard.** Two more files are attached: `STANDARDS_20261119.md` and `DECISIONS_20261119.tsv`, one
standard of terms, notation and register per language for all our editions, written on 19 November 2026 by Claude
Fable 5.2 at effort max. The terms of every translation follow this standard where it differs from the edition; in
this work that is the English of both volumes, read and corrected against it as you go and checked once more, term by
term, before each final ZIP. Each such change is recorded in `CORRECTIONS.tsv` with the kind `terminology` (a kind
besides those listed below). The decisions the standard marks with the confidence `low` are not applied: list them as
they are in `TERMINOLOGY_LOW_CONFIDENCE.md`, each with the places in the editions it would touch. Where the standard
and the glossary in the context zip differ, the standard holds.

# Part A: Volume I

## What this is for

This is the second pass that brings our edition of Luc Illusie's *Complexe cotangent et déformations I* to the
standard of our SGA and EGA editions: the French as printed, the corrected French and the English, each checked
against the printed original, page by page. The record of the check is kept as well, so that we can see how well a
check of this kind works.

**The work and the edition.** Luc Illusie, *Complexe cotangent et déformations I*, Lecture Notes in Mathematics 239,
Springer, 1971. Our edition (github KokunoYumeto/illusie-cotangent-complex-editions, release `editions-2026-11-06`;
the repository's `tex/` folder holds the same three files) was AI-transcribed, corrected and AI-translated by OpenAI
Codex, mainly GPT-5.6 Sol at reasoning effort ultra, with parts by GPT-6 Astra at reasoning effort ultra, in August
and September 2026, from the scan of the printed volume.

**What earlier checks found.** On 6 November 2026 Claude Opus 5.5 at effort max compared three pages with the print,
two of them in this volume (pp. 13 and 35 of the diplomatic French, p. 13 of the English): the text, the formulas and
the diagrams matched, but the diplomatic French had a paragraph break added mid-sentence (p. 13) and had left out the
punctuation after three displayed diagrams (p. 35). Look for these kinds on every page. The edition's own records
(`edition_records/`, common to both volumes) list its source corrections, decisions and repairs.

## The attachments

- `ILLUSIE_I_scans.zip`: `ILLUSIE_I_LNM239.pdf`, the scan of the printed volume the edition records as its authority
  (380 pages: PDF page 1 the cover; pages 2–18 the front matter, printed I–XV and blanks; pages 19–360 printed pages
  1–342, printed page = PDF page − 18; pages 361–376 printed 343–358, of which 356–358 are blank; pages 377–380 the
  publisher's pages), and `ILLUSIE_I_author_errata.pdf`, the author's errata to this volume.
- `ILLUSIE_I_sources.zip`: the three editions of the release, each in its folder with what it needs to build:
  `francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex`, `english/02-volume-I-english.tex`,
  `francais-diplomatique/02-volume-I-francais-diplomatique.tex`; in each folder `front-matter.pdf` and
  `publisher-back-matter.pdf` (facsimile pages the edition includes), `assets/autumn-road-r1.png` (its cover image)
  and its build note.
- `ILLUSIE_I_context.zip`: start with its `README.md`. `edition_records/` holds the records the edition was made with:
  status files, logbooks, the correction, repair and decision ledgers and the page maps. They say what the makers
  corrected, normalised and doubted, and why; use them for item 2 below. The other folders serve the notes (item 5):
  `programme/` (our programme map and the reference page of Grothendieck's Montpellier archive), `glossary/` (the
  English standard of our SGA editions), `notes/` (research notes of our archive work that bear on this work),
  `stacks/` (our Stacks-style material drawn from this work).

**What the context is for.** The edition records tell you what earlier passes did; they are records of AI passes, not
authorities, and the scan decides every reading. The programme map, the notes and the Stacks material let your notes
connect this work to our programme: where it meets Grothendieck's archive, our open questions and our Stacks-style
statements. The check of the text does not depend on them: read them when you write the notes, after the pages are
done.

## The work, in order of importance

1. **The French as printed against the scans, every page.** The as-printed layer is
   `francais-diplomatique/02-volume-I-francais-diplomatique.tex`. Compare it with the scan line by line: words,
   punctuation, formulas, symbols, indices and exponents, the fonts of letters (italic, bold, roman, script, Gothic),
   emphasis, the numbering of sections and statements, cross-references, footnotes, which formulas are displayed and
   which run in the line, and the page markers. Every difference from the print is a correction of this layer: the
   as-printed layer says what the print says, its misprints included.
2. **The corrected French.** The corrected layer is
   `francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex`. The author's errata
   (`ILLUSIE_I_author_errata.pdf`) are corrections of the original too: each erratum that concerns this volume goes
   into the corrected layer and the English, with the errata PDF as its evidence and the kind `misprint of the
   original`. Every place where it differs from the as-printed layer is a correction of the original, and each one is
   justified: by the scan reading, and by the mathematical reason that makes the printed reading a misprint (a wrong
   index, a reversed arrow, a reference to the wrong number, a word that breaks the sentence). A correction that is
   not justified goes back to the printed reading. Misprints of the original that you find now are corrected in this
   layer and recorded. The corrected layer differs from the as-printed layer at these places and at no other.
3. **The English.** The English is `english/02-volume-I-english.tex`. Read it against the corrected French, paragraph
   by paragraph: every sentence says what the French says, with nothing left out and nothing added; the mathematics is
   correct and every formula is the corrected French formula; the terms are the same through the work and agree with
   the English of our SGA editions (`glossary/GLOSSARY_SGA_EN_UNIFIED.tsv`, one English rendering per French term) and
   with standard English usage in algebraic geometry. Correct errors of meaning, omissions, additions and inconsistent
   terms; leave style alone.
4. **The build.** Each builds with LuaLaTeX, two passes, in its own folder. The facsimile pages stay facsimiles where
   they hold the publisher's pages (cover, title, imprint, series list); a page of the author's text that the edition
   gives only as a facsimile is transcribed into all three layers. Every layer builds without errors, and no overfull
   box in any build log sticks out by more than 2pt. Fix overfull boxes in the preamble or by a reader-level pass
   (line-breaking parameters, `\emergencystretch`, a scaled or broken display set by a macro of the preamble), never
   by changing the text. Then render and look at every page of each PDF that had an overflow over 10pt before your
   fix, and a spread of pages over the whole book.
5. **Notes**, kept apart from the text; they never change a reading. Write in `NOTES.md`: the misprints and slips of
   the original, each with the corrected statement; the claims the author leaves without proof on these pages, each
   with what a proof needs; where later work corrects, extends or uses a result, with exact locators (cite only
   sources you can cite to the statement); where the work meets our programme, using the context; and your own ideas,
   labelled as yours, each with your confidence and your reason. One note per item, with its printed page and
   statement number.

## Rules

1. **The scan is the authority.** Render every page of the scan yourself at 400 dpi and look at it; enlarge every
   place you decide (crop and scale), and every index, exponent, accent and small sign. The text layer of a scan PDF
   and OCR may help you find your place and flag candidate differences; every reading you keep or change is decided by
   looking at the image.
2. **The as-printed layer is the print.** No modernization, no normalization of notation, no silent correction: the
   print's spelling, accents, punctuation, abbreviations, numbering and typography stay as printed.
3. **Edit the sources in place.** Keep each tree's structure, file names, macros, labels, anchors and page markers; a
   change of structure is made only where the print requires it (a missing or extra paragraph break, a heading, a
   display), and it is recorded like any other correction.
4. **Credits and rights notices stay exactly as they are** in every file, README and front matter: the rights
   statement of each README and front matter, and every name, model and source the edition credits.
5. **Work from the printed original only.** This check works from the printed volume and the author's errata only; no
   other edition or translation is consulted.
6. **Privacy.** The records replace local paths by `<local>`. Copy no local path and no e-mail address into any file
   you return.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`, and start
   `CHECK_RECORD.md` with a notation table: the recurring signs, alphabets and abbreviations of the print, each with
   how the layers write it in LaTeX. Keep it up to date.
2. **Page by page, in printed order** (the front matter, then printed pp. 1–355): render the page; read the as-printed
   layer against the image, line by line; then the corrected layer's text of that page; then the English of that page.
   Write each correction into the files at once and its row into `CORRECTIONS.tsv`, then the page's section of
   `CHECK_RECORD.md`, then append `page <printed page> done <current UTC time>` to `progress.log`. Only then go to the
   next page.
3. **One stream.** Do the pages yourself, in one stream, in order: do not split them among parallel workers or
   sub-agents. When the pages of an earlier transcription were split among workers, the same signs were read in
   different ways and the errors went unmarked.
4. **A second reading of every correction.** When the last page is done, go through `CORRECTIONS.tsv` row by row
   against the scan crop of each place: confirm, amend or withdraw each row, and say so in its `confidence` column.
   Then, for every kind of error you found on more than one page (a sign misread the same way, an index dropped, a
   term rendered two ways), search the whole work for it, page by page, and record what the search found.
5. **Build and PDF check** (item 4), recorded in `PDF_CHECK.md`: per layer, the build command, the errors and
   warnings, the overfull boxes before and after your fix with their sizes, and the pages you rendered and what you
   saw.
6. **The notes** (item 5): only now open `programme/`, `notes/` and the other folders of the context, and write
   `NOTES.md`. For each note, search the context for the same objects and words (grep works well on these files) and
   say where our materials already have the point and whether this work adds to it, restates it or differs from it.
   The notes in the context are leads from earlier runs, never results to cite as established.
7. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `ILLUSIE_I_CHECK_checkpoint_<NN>.zip` with `NN`
   counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a
   checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote,
   folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this
   conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding
   every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so
   far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files
   themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a
   summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation;
   earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is
   in no checkpoint is lost. This run's checkpoints continue the earlier run's numbering: the first is
   `ILLUSIE_I_CHECK_checkpoint_10.zip`. Keep every checkpoint ZIP, and the final ZIP, under 500 MB: the Library refuses a
   file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost. If one would be larger, save it as
   several ZIPs of under 500 MB each, `ILLUSIE_I_CHECK_checkpoint_<NN>_part<k>.zip`, the file list in the first part.
8. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
   intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
   back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had
   done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us
   only through checkpoint ZIPs and the final ZIP.

This task is long by design: the 380 pages of the scan, about 370 of them with text, each read in three layers against
the print, then the build and the notes. Work through all of it completely; do not stop at a sample or a plan, and do
not ask whether to continue. Ignore any clock. Read the last page as slowly as the first: the pages done fastest are
where errors cluster.

**Check events.** For every statement your work checks, uses or refutes (a claim in your notes, by its note; an entry
of our results state, by its id; a statement of the text, by its place), record its check events in
`CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check /
independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background
without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually
happened, neither more nor less: reading a statement while transcribing it is not a check of it. `CHECK_EVENTS.tsv`
goes into every checkpoint and into the final ZIP.

## What to return

One ZIP file, `ILLUSIE_I_CHECK.zip`, offered as the only download (under 500 MB; if it would be larger,
`ILLUSIE_I_CHECK_part<k>.zip`, the file list in the first part). It holds:

- `sources/`: the three corrected TeX trees, complete, in the layout of `ILLUSIE_I_sources.zip`, building as they
  stand;
- `CORRECTIONS.tsv`: one row per change, with the columns `file`, `layer` (as-printed, corrected, English, build),
  `printed_page`, `line` (line of the printed page), `statement` (the statement or section number, or empty), `old`,
  `new`, `evidence` (the scan page and what the image shows there), `kind` (one of: reading, misprint of the original,
  translation, typesetting, structure), `confidence` (high, medium, low, after the second reading);
- `CHECK_RECORD.md`: the notation table; then one section per printed page: the scan page, what was compared with what
  (each layer's file and lines against the image), by GPT-6 Astra (ChatGPT Pro mode), the number of corrections per
  layer and kind, the existing corrections of the corrected layer confirmed or reverted, and the time; at the top, the
  totals per layer and kind, the corrections that change the mathematics (one per line), and how many pages had no
  difference in each layer;
- `PDF_CHECK.md`, as in Method 5;
- `NOTES.md`, as in item 5;
- `pdf/`: the PDF of every layer, built from `sources/`;
- `README.md`: what each file is, the counts, how to build each layer, and the build status;
- `progress.log` and your scripts.

## When it is done

The task is finished only when every page of the print has its section in `CHECK_RECORD.md` for all three layers;
every existing correction of the corrected layer has its verdict; every change has its row with its evidence; every
layer builds and passes the PDF check; and `NOTES.md` is written. Keep working until then. Do not stop because what
remains is long, because a part of the work looks presentable, or because much has already been done.

Not acceptable:

- a sample of pages in place of all of them;
- a change without a row in `CORRECTIONS.tsv`, or a row without evidence from the scan;
- a change to the as-printed layer that the print does not show;
- a correction of a misprint made in the as-printed layer, or a difference between the two French layers that is not a
  recorded correction;
- a change of English style recorded as a correction of meaning;
- a credit or rights notice changed or removed;
- a local path or an e-mail address in any returned file.


# Part B: Volume II

## What this is for

This is the second pass that brings our edition of Luc Illusie's *Complexe cotangent et déformations II* to the
standard of our SGA and EGA editions: the French as printed, the corrected French and the English, each checked
against the printed original, page by page. The record of the check is kept as well, so that we can see how well a
check of this kind works.

**The work and the edition.** Luc Illusie, *Complexe cotangent et déformations II*, Lecture Notes in Mathematics 283,
Springer, 1972. Our edition (github KokunoYumeto/illusie-cotangent-complex-editions, release `pdf-check-2026-11-15`,
which rebuilt volume II with a typesetting-only fix of the commas after four full-width diagrams of chapter VIII; the
repository's `tex/` folder holds the same three files) was AI-transcribed, corrected and AI-translated by OpenAI
Codex, mainly GPT-5.6 Sol at reasoning effort ultra, with parts by GPT-6 Astra at reasoning effort ultra, in August
and September 2026, from the scan of the printed volume. Each of its three documents has 312 leaves: seven of front
matter, printed pages 1–304, and the Springer erratum leaf (printed p. 305).

**What earlier checks found.** On 6 November 2026 Claude Opus 5.5 at effort max compared three pages with the print,
one of them in this volume (p. 155 of the diplomatic French): the text, the formulas and the diagrams matched, but the
diplomatic French had silently corrected the printed misspelling "homormorphisme" to "homomorphisme". Look for this
kind on every page. The edition's own records (`edition_records/`, common to both volumes) list its source
corrections, decisions and repairs.

## The attachments

- `ILLUSIE_II_scans.zip`: `ILLUSIE_II_LNM283.pdf`, the scan of the printed volume the edition records as its authority
  (311 pages: PDF pages 1–6 the front matter, printed I–III and V–VII, the blank IV not scanned; pages 7–298 printed
  pages 1–292, printed page = PDF page − 6; page 299 blank; pages 300–311 printed 293–304, printed page = PDF page −
  7); `ILLUSIE_II_erratum_p305_springer.pdf`, the Springer erratum leaf (printed p. 305); and
  `ILLUSIE_II_author_errata.pdf`, the author's errata to this volume.
- `ILLUSIE_II_sources.zip`: the three assembled editions of the release, `02-volume-II-fr-corrected.tex`,
  `05-volume-II-fr-diplomatic.tex` and `07-volume-II-english.tex` (each holds its text and its macro definitions),
  `assets/autumn-road-r1.png` (the cover image) and `BUILD.md`.
- `ILLUSIE_II_context.zip`: start with its `README.md`. `edition_records/` holds the records the edition was made
  with: status files, logbooks, the correction, repair and decision ledgers and the page maps. They say what the
  makers corrected, normalised and doubted, and why; use them for item 2 below. The other folders serve the notes
  (item 5): `programme/` (our programme map and the reference page of Grothendieck's Montpellier archive), `glossary/`
  (the English standard of our SGA editions), `notes/` (research notes of our archive work that bear on this work),
  `stacks/` (our Stacks-style material drawn from this work).

**What the context is for.** The edition records tell you what earlier passes did; they are records of AI passes, not
authorities, and the scan decides every reading. The programme map, the notes and the Stacks material let your notes
connect this work to our programme: where it meets Grothendieck's archive, our open questions and our Stacks-style
statements. The check of the text does not depend on them: read them when you write the notes, after the pages are
done.

## The work, in order of importance

1. **The French as printed against the scans, every page.** The as-printed layer is `05-volume-II-fr-diplomatic.tex`.
   Compare it with the scan line by line: words, punctuation, formulas, symbols, indices and exponents, the fonts of
   letters (italic, bold, roman, script, Gothic), emphasis, the numbering of sections and statements,
   cross-references, footnotes, which formulas are displayed and which run in the line, and the page markers. Every
   difference from the print is a correction of this layer: the as-printed layer says what the print says, its
   misprints included.
2. **The corrected French.** The corrected layer is `02-volume-II-fr-corrected.tex`. The Springer erratum and the
   author's errata (`ILLUSIE_II_author_errata.pdf`) are corrections of the original too: each erratum that concerns
   this volume goes into the corrected layer and the English, with its errata PDF as evidence and the kind `misprint
   of the original`. Every place where it differs from the as-printed layer is a correction of the original, and each
   one is justified: by the scan reading, and by the mathematical reason that makes the printed reading a misprint (a
   wrong index, a reversed arrow, a reference to the wrong number, a word that breaks the sentence). A correction that
   is not justified goes back to the printed reading. Misprints of the original that you find now are corrected in
   this layer and recorded. The corrected layer differs from the as-printed layer at these places and at no other.
3. **The English.** The English is `07-volume-II-english.tex`. Read it against the corrected French, paragraph by
   paragraph: every sentence says what the French says, with nothing left out and nothing added; the mathematics is
   correct and every formula is the corrected French formula; the terms are the same through the work and agree with
   the English of our SGA editions (`glossary/GLOSSARY_SGA_EN_UNIFIED.tsv`, one English rendering per French term) and
   with standard English usage in algebraic geometry. Correct errors of meaning, omissions, additions and inconsistent
   terms; leave style alone.
4. **The build.** Each builds with LuaLaTeX, three passes (`BUILD.md`). Every layer builds without errors, and no
   overfull box in any build log sticks out by more than 2pt. Fix overfull boxes in the preamble or by a reader-level
   pass (line-breaking parameters, `\emergencystretch`, a scaled or broken display set by a macro of the preamble),
   never by changing the text. Then render and look at every page of each PDF that had an overflow over 10pt before
   your fix, and a spread of pages over the whole book.
5. **Notes**, kept apart from the text; they never change a reading. Write in `NOTES.md`: the misprints and slips of
   the original, each with the corrected statement; the claims the author leaves without proof on these pages, each
   with what a proof needs; where later work corrects, extends or uses a result, with exact locators (cite only
   sources you can cite to the statement); where the work meets our programme, using the context; and your own ideas,
   labelled as yours, each with your confidence and your reason. One note per item, with its printed page and
   statement number.

## Rules

1. **The scan is the authority.** Render every page of the scan yourself at 400 dpi and look at it; enlarge every
   place you decide (crop and scale), and every index, exponent, accent and small sign. The text layer of a scan PDF
   and OCR may help you find your place and flag candidate differences; every reading you keep or change is decided by
   looking at the image.
2. **The as-printed layer is the print.** No modernization, no normalization of notation, no silent correction: the
   print's spelling, accents, punctuation, abbreviations, numbering and typography stay as printed.
3. **Edit the sources in place.** Keep each tree's structure, file names, macros, labels, anchors and page markers; a
   change of structure is made only where the print requires it (a missing or extra paragraph break, a heading, a
   display), and it is recorded like any other correction.
4. **Credits and rights notices stay exactly as they are** in every file, README and front matter: the rights
   statement of each README and front matter, and every name, model and source the edition credits.
5. **Work from the printed original only.** This check works from the printed volume, its Springer erratum and the
   author's errata only; no other edition or translation is consulted.
6. **Privacy.** The records replace local paths by `<local>`. Copy no local path and no e-mail address into any file
   you return.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`, and start
   `CHECK_RECORD.md` with a notation table: the recurring signs, alphabets and abbreviations of the print, each with
   how the layers write it in LaTeX. Keep it up to date.
2. **Page by page, in printed order** (the front matter, printed pp. 1–304, then the erratum leaf): render the page;
   read the as-printed layer against the image, line by line; then the corrected layer's text of that page; then the
   English of that page. Write each correction into the files at once and its row into `CORRECTIONS.tsv`, then the
   page's section of `CHECK_RECORD.md`, then append `page <printed page> done <current UTC time>` to `progress.log`.
   Only then go to the next page.
3. **One stream.** Do the pages yourself, in one stream, in order: do not split them among parallel workers or
   sub-agents. When the pages of an earlier transcription were split among workers, the same signs were read in
   different ways and the errors went unmarked.
4. **A second reading of every correction.** When the last page is done, go through `CORRECTIONS.tsv` row by row
   against the scan crop of each place: confirm, amend or withdraw each row, and say so in its `confidence` column.
   Then, for every kind of error you found on more than one page (a sign misread the same way, an index dropped, a
   term rendered two ways), search the whole work for it, page by page, and record what the search found.
5. **Build and PDF check** (item 4), recorded in `PDF_CHECK.md`: per layer, the build command, the errors and
   warnings, the overfull boxes before and after your fix with their sizes, and the pages you rendered and what you
   saw.
6. **The notes** (item 5): only now open `programme/`, `notes/` and the other folders of the context, and write
   `NOTES.md`. For each note, search the context for the same objects and words (grep works well on these files) and
   say where our materials already have the point and whether this work adds to it, restates it or differs from it.
   The notes in the context are leads from earlier runs, never results to cite as established.
7. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `ILLUSIE_II_CHECK_checkpoint_<NN>.zip` with `NN`
   counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a
   checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote,
   folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this
   conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding
   every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so
   far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files
   themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a
   summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation;
   earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is
   in no checkpoint is lost. This run's checkpoints continue the earlier run's numbering: the first is
   `ILLUSIE_II_CHECK_checkpoint_10.zip`. Keep every checkpoint ZIP, and the final ZIP, under 500 MB: the Library refuses
   a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost. If one would be larger, save it
   as several ZIPs of under 500 MB each, `ILLUSIE_II_CHECK_checkpoint_<NN>_part<k>.zip`, the file list in the first part.
8. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
   intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
   back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had
   done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us
   only through checkpoint ZIPs and the final ZIP.

This task is long by design: the 311 pages of the scan and the erratum leaf, each read in three layers against the
print, then the build and the notes. Work through all of it completely; do not stop at a sample or a plan, and do not
ask whether to continue. Ignore any clock. Read the last page as slowly as the first: the pages done fastest are where
errors cluster.

**Check events.** For every statement your work checks, uses or refutes (a claim in your notes, by its note; an entry
of our results state, by its id; a statement of the text, by its place), record its check events in
`CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check /
independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background
without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually
happened, neither more nor less: reading a statement while transcribing it is not a check of it. `CHECK_EVENTS.tsv`
goes into every checkpoint and into the final ZIP.

## What to return

One ZIP file, `ILLUSIE_II_CHECK.zip`, offered as the only download (under 500 MB; if it would be larger,
`ILLUSIE_II_CHECK_part<k>.zip`, the file list in the first part). It holds:

- `sources/`: the three corrected TeX trees, complete, in the layout of `ILLUSIE_II_sources.zip`, building as they
  stand;
- `CORRECTIONS.tsv`: one row per change, with the columns `file`, `layer` (as-printed, corrected, English, build),
  `printed_page`, `line` (line of the printed page), `statement` (the statement or section number, or empty), `old`,
  `new`, `evidence` (the scan page and what the image shows there), `kind` (one of: reading, misprint of the original,
  translation, typesetting, structure), `confidence` (high, medium, low, after the second reading);
- `CHECK_RECORD.md`: the notation table; then one section per printed page: the scan page, what was compared with what
  (each layer's file and lines against the image), by GPT-6 Astra (ChatGPT Pro mode), the number of corrections per
  layer and kind, the existing corrections of the corrected layer confirmed or reverted, and the time; at the top, the
  totals per layer and kind, the corrections that change the mathematics (one per line), and how many pages had no
  difference in each layer;
- `PDF_CHECK.md`, as in Method 5;
- `NOTES.md`, as in item 5;
- `pdf/`: the PDF of every layer, built from `sources/`;
- `README.md`: what each file is, the counts, how to build each layer, and the build status;
- `progress.log` and your scripts.

## When it is done

The task is finished only when every page of the print has its section in `CHECK_RECORD.md` for all three layers;
every existing correction of the corrected layer has its verdict; every change has its row with its evidence; every
layer builds and passes the PDF check; and `NOTES.md` is written. Keep working until then. Do not stop because what
remains is long, because a part of the work looks presentable, or because much has already been done.

Not acceptable:

- a sample of pages in place of all of them;
- a change without a row in `CORRECTIONS.tsv`, or a row without evidence from the scan;
- a change to the as-printed layer that the print does not show;
- a correction of a misprint made in the as-printed layer, or a difference between the two French layers that is not a
  recorded correction;
- a change of English style recorded as a correction of meaning;
- a credit or rights notice changed or removed;
- a local path or an e-mail address in any returned file.
