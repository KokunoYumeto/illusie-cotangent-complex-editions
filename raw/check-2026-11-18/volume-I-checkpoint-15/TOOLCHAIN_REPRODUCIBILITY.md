# TeX toolchain preparation

This note records preparation of the compilation environment. It is not a record of an edition build or a page comparison; those records belong in `PDF_CHECK.md` and `CHECK_RECORD.md`.

## Prepared environment

A separate, writable TeX Live 2025 installation was prepared with the official TeX Live installer and `tlmgr`. The existing system installation was incomplete and was left unchanged. The working engine identifies itself as **LuaHBTeX 1.22.0 (TeX Live 2025)**, with **LaTeX2e 2025-11-01** and **L3 programming layer 2026-01-19**.

The installation used the archived 2025 repository:

<https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2025/tlnet-final>

The installer was obtained from that repository's `install-tl-unx.tar.gz`. Its installation profile selected `scheme-infraonly`, the `x86_64-linux` binaries, and portable installation. All TeX configuration and cache directories were placed within the chosen writable installation. Automatic global path adjustment, automatic repository replacement, documentation downloads, source downloads, and initial format creation were disabled. No system permissions or edition sources were changed.

## Reproduction

Use the official installer with the profile choices above and a writable installation directory chosen for the new environment. Keep its package manager pointed at the archived 2025 repository. Make that installation's executables available for the following commands; these commands must not select an unrelated system TeX installation.

```text
tlmgr install latex-bin luahbtex luaotfload fontspec amsmath amsfonts geometry graphics xcolor ulem pgf hyperref tikz-cd tools pdfpages adjustbox fancyhdr needspace lm lm-math tex-gyre dejavu etoolbox epstopdf-pkg pdflscape
fmtutil-sys --byfmt lualatex
```

`tlmgr` installs the declared package dependencies and generates the filename databases, configuration, and font maps. The final three companion packages in the installation list were necessary in the actual probe; installing only the edition's explicitly named packages did not supply all of them.

The requested font families are Latin Modern Roman, Sans, Mono, and Math; TeX Gyre Heros, Heros Cn, Cursor, and Termes; and DejaVu Math TeX Gyre. In this environment, the first eight families resolved from the private installation, while DejaVu Math TeX Gyre resolved from the already installed system font. A new environment must make that exact DejaVu Math font available as well. Font substitution is not part of this setup.

## Readiness check actually performed

A single-line scratch document loaded the following sixteen packages and four TikZ libraries, selected all nine font families, and exercised the Unicode glyphs `∑`, `⨁`, `⋂`, and `∫`:

```text
adjustbox amsmath amssymb fancyhdr fontspec geometry graphicx hyperref
longtable needspace pdfpages tabularx tikz tikz-cd ulem xcolor

arrows arrows.meta calc shapes.geometric
```

The command was:

```text
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error probe.tex
```

The successful run returned exit code 0 and produced one PDF page. The log contained no LaTeX errors, missing-character messages, or overfull boxes. Font inspection of the PDF confirmed embedding of all nine requested families. Its first successful pass reported the expected disabled-shell-escape warning from `epstopdf` and the initial outline-rerun warning from `rerunfilecheck`.

This check establishes package and font readiness. Edition-specific compilation, overflow checks, and visual examination remain separate tasks, recorded as they are performed.

## Edition build commands

Run each command in the corresponding source folder. Volume I requires two serial passes per edition; Volume II requires three. Retain all supplied build assets, including the facsimile PDFs and cover images.

```text
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 08-volume-I-francais-corrige-par-gpt-5-6-sol.tex
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 02-volume-I-francais-diplomatique.tex
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 02-volume-I-english.tex

lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 02-volume-II-fr-corrected.tex
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 05-volume-II-fr-diplomatic.tex
lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error 07-volume-II-english.tex
```

The temporary installation, downloaded vendor files, raw installation logs, font caches, and probe products are runtime material and are not included in checkpoints. This note preserves the setup without copying private environment paths.

## Runtime status after workspace recovery

The temporary private TeX installation and scratch probe products were lost during workspace recovery on **18 November 2026**. The successful engine, package, and font checks recorded above remain historical results; they do **not** establish current runtime readiness after that loss. This recovery step did not recreate or revalidate the installation and did not perform an edition build. Before further compilation, the documented toolchain must be restored or recreated and its content-free readiness probe repeated. The original setup and probe findings above have been preserved unchanged.

## Restored runtime verified on 18 November 2026

**Restoration and verification completed: 2026-11-18 14:41:53 UTC.** A new private, portable TeX Live 2025 installation was created from the same archived repository and the same recorded package inventory. The installer and package installation returned exit code **0**, as did explicit generation of the private `lualatex` format with `fmtutil-sys --byfmt lualatex`. System TeX directories, permissions, and edition sources were not changed.

The restored versions match the earlier successful setup: **LuaHBTeX 1.22.0 (TeX Live 2025)**, **LaTeX2e 2025-11-01**, and **L3 programming layer 2026-01-19**.

A new, content-free `readiness.tex` specimen loaded all **16 required packages**, all **four TikZ libraries**, and all **nine exact font families** listed above. Two serial LuaLaTeX passes returned exit code **0** and produced one PDF page. The final log contained **no LaTeX errors, missing-character messages, or overfull boxes**. PDF metadata and labelled glyph specimens confirmed that all nine requested families were embedded, including the condensed Heros face. The rendered specimen was inspected for the presence and visibility of its font, Greek-glyph, and arrow samples; no edition or scan page was inspected.

The same specimen checked the local upright-Latin math macro. The tested bare Latin characters used **CMMI10**, changed locally to **LMRoman10-Regular**, and returned to **CMMI10** after the group. In the tested expressions, explicit `\mathit`, `\mathbf`, `\mathcal`, `\mathbb`, and `\sin` retained their original font selections. The three content-free TikZ samples used `->`, `left hook->`, and `right hook->`, with `>=latex` and paths directed left to right. This is a glyph and font-availability check, not a choice of notation for any source page.

Two actual warnings are recorded. The package manager reported a valid repository signature whose signing key had expired; its verification settings were not changed. The final probe log contained the expected `epstopdf` warning that shell escape was disabled. Neither warning prevented the recorded successful commands.

Current content-free toolchain readiness is therefore restored as of the time above. The earlier preparation, loss, and probe records remain preserved. This result does **not** certify an edition build, layout, translation, mathematical correctness, or a visual reading against scans. The installation, caches, raw logs, and probe products remain private runtime material and are excluded from checkpoints.

## Restored runtime verified on 19 November 2026

**Restoration and verification completed: 2026-11-19 01:08:17 UTC.** A fresh private, portable TeX Live 2025 installation was created from the archived repository specified above. The official installer download was accessible over HTTPS. Its archive had 5,866,884 bytes and SHA-256 `311df9f1477fd90c520159d1feddc2d6270f010d8349d1f6bdb9461a93b48a5c`. The infrastructure installer returned exit code **0**; installation of the documented package inventory and its dependencies (89 package entries) returned exit code **0**; explicit generation of the private `lualatex` format returned exit code **0**. No elevated privileges were requested. The installer profile kept global path adjustment and automatic repository replacement disabled, omitted documentation and source downloads, and used portable configuration and cache directories within the private installation. The selected configuration, variable, and local trees were checked with the private `kpsewhich` executable.

The restored versions match the historical successful setup: **LuaHBTeX 1.22.0 (TeX Live 2025)**, **LaTeX2e 2025-11-01**, and **L3 programming layer 2026-01-19**. The initial system installation was not used for the probe: it exposed LuaHBTeX 1.18.0, did not resolve `ulem.sty` or `lualatex.fmt`, and substituted Nimbus faces for the required TeX Gyre fonts. The restored private installation supplied the required components without altering the system installation.

A new, content-free one-page specimen loaded all **16 required packages** and all **four TikZ/PGF libraries**, selected the **nine exact font families**, and exercised the Unicode glyphs `α`, `β`, `∑`, `⨁`, `⋂`, and `∫` in Latin Modern Math and DejaVu Math TeX Gyre. It also exercised ordinary mathematical alphabets, three hook/arrow forms, the `Latex` arrow tip, a geometric node, a coordinate calculation, and a small `tikz-cd` square. It contained no edition text or scan material.

Two serial runs of `lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error readiness.tex` both returned exit code **0**. The final PDF had **one page** and **66,429 bytes**. Its final log contained **no LaTeX errors, missing-character messages, or overfull boxes**. `pdffonts` confirmed embedding of the exact nine requested regular font families, including **TeXGyreHerosCondensed-Regular**; none of the previously observed Nimbus substitutions appeared. A 144 dpi rendering of the specimen was inspected: the nine labelled samples, Greek and operator glyphs, mathematical alphabet samples, hook and arrow samples, and diagram were visible without clipping or overlap.

Two actual warnings are retained. The package manager reported a valid repository signature with an expired signing key; verification settings were left unchanged. The final probe log reported the expected `epstopdf` warning because shell escape was disabled. Neither prevented successful completion.

This step verifies current package, font, engine, and basic rendering readiness only. It did not build any edition, inspect any printed page, adjudicate a reading, or certify the correctness or layout of an edition. The historical records above are preserved. The private installation, downloaded vendor files, raw logs, caches, and probe products remain runtime material outside checkpoints.
