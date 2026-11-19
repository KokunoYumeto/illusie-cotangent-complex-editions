# Volume I build and diagnostic plan

Infrastructure preparation only: no edition build or PDF acceptance has been performed by this plan. The supplied build notes require **two serial LuaLaTeX passes in each layer's own source folder**. The restored private toolchain is described in `TOOLCHAIN_REPRODUCIBILITY.md`.

## Order and preserved evidence

Finish the required textual reading, correction re-reading, recurring-error searches, and terminology review before starting the edition build stage. Freeze the sources during each two-pass run. First build a baseline before making layout fixes; keep every pass's own raw log, stdout, PDF, and source snapshot together in private runtime storage. Use a new run name for each later attempt so the baseline remains available.

Raw runtime files stay outside the deliverable tree. The diagnostic extractor writes sanitized Markdown and TSV records into `build-diagnostics/`; these are eligible for checkpoints. It does not edit sources, correction ledgers, page status, or `PDF_CHECK.md`.

## Reproducible two-pass commands

Run the following from the Volume I deliverable root. Replace the two `<local>` placeholders with the private executable directory and a **new, nonexistent** runtime run directory, for example a directory named `baseline-01`. The environment-variable names are task-specific. The script does not change the system installation or shell startup files.

```bash
export ILLUSIE_TEX_BIN='<local>/bin/x86_64-linux'
export ILLUSIE_BUILD_RUN='<local>/baseline-01'
python3 - <<'PY'
from pathlib import Path
import csv, hashlib, os, re, shutil, subprocess

volume = Path.cwd().resolve()
texbin = Path(os.environ['ILLUSIE_TEX_BIN']).resolve()
runtime = Path(os.environ['ILLUSIE_BUILD_RUN']).resolve()
assert re.fullmatch(r'[A-Za-z0-9_-]+', runtime.name), 'Use a simple run-directory name'
runtime.mkdir(parents=True, exist_ok=False)
reports = volume / 'build-diagnostics' / runtime.name
reports.mkdir(parents=True, exist_ok=False)
environment = os.environ.copy()
environment['PATH'] = str(texbin) + os.pathsep + environment['PATH']
layers = [
    ('as-printed', 'francais-diplomatique/02-volume-I-francais-diplomatique.tex'),
    ('corrected', 'francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex'),
    ('English', 'english/02-volume-I-english.tex'),
]
with (reports / 'run-status.tsv').open('x', newline='') as status:
    writer = csv.writer(status, delimiter='\t', lineterminator='\n')
    writer.writerow(['layer', 'pass', 'exit_code', 'source', 'source_sha256', 'log_snapshot', 'pdf_snapshot'])
    for layer, relative in layers:
        source = volume / 'sources' / relative
        original_bytes = source.read_bytes()
        source_hash = hashlib.sha256(original_bytes).hexdigest()
        output = runtime / layer
        output.mkdir()
        snapshot = output / 'source-snapshot' / source.name
        snapshot.parent.mkdir()
        snapshot.write_bytes(original_bytes)
        for pass_number in (1, 2):
            assert source.read_bytes() == original_bytes, 'Source changed during the build pair'
            command = [str(texbin / 'lualatex'), '-no-shell-escape',
                       '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
                       '-output-directory=' + str(output), source.name]
            with (output / f'pass{pass_number}.stdout').open('x') as stdout:
                result = subprocess.run(command, cwd=source.parent, env=environment,
                                        stdout=stdout, stderr=subprocess.STDOUT)
            log = output / f'pass{pass_number}.log'
            shutil.copyfile(output / (source.stem + '.log'), log)
            pdf = output / f'pass{pass_number}.pdf'
            if result.returncode == 0:
                shutil.copyfile(output / (source.stem + '.pdf'), pdf)
            writer.writerow([layer, pass_number, result.returncode, relative,
                             source_hash, log.name, pdf.name if result.returncode == 0 else ''])
            status.flush()
            extract = ['python3', str(volume / 'scripts/extract_build_diagnostics.py'),
                       '--source', str(snapshot), '--log', str(log),
                       '--output-prefix', str(reports / layer / f'pass{pass_number}')]
            if result.returncode == 0:
                extract += ['--pdf', str(pdf)]
            subprocess.run(extract, check=True)
            if result.returncode:
                raise SystemExit(f'{layer} pass {pass_number} failed; inspect its raw log before another run')
        assert source.read_bytes() == original_bytes, 'Source changed during the build pair'
print('All three two-pass commands completed. Diagnostic and visual acceptance remain separate.')
PY
```

The `-output-directory` option keeps compiler products together outside the source trees; the working directory remains the layer folder so the supplied relative asset references resolve normally. Every pass's PDF is preserved before the next pass can overwrite it. A failed pass is recorded and stops the sequence; an old PDF is not relabelled as that failed pass's output.

## Diagnostic outputs and page targets

`extract_build_diagnostics.py` produces four files per pass:

| Suffix | Contents |
|---|---|
| `-overflows.tsv` | Every recognized overfull horizontal or vertical box, size in pt, source lines, source anchors, and strict `>2 pt` / `>10 pt` flags |
| `-diagnostics.tsv` | Recognized error, warning, and missing-character lines, with private paths and email addresses removed |
| `-over10-candidates.tsv` | Physical PDF-page candidates for each `>10 pt` overflow, or an explicit unresolved row |
| `-summary.md` | Mechanical counts and remaining mapping limitations |

The source-page environments use continuous reflow. **Do not infer a built-PDF page from the printed-page number or a fixed offset.** The extractor finds the source-page anchors touched by the diagnostic's source-line range, then reads the corresponding PDF named destinations. Its candidate span includes the next anchor's page because two source-page regions may share one physical page.

These spans are navigation aids. They may include unaffected pages. Delayed floats, macro-generated material, missing anchors, and diagnostics without source-line ranges require manual resolution from the raw log and PDF. Resolve every unresolved `>10 pt` row; none counts as a reviewed page merely because extraction ran.

To extract one pass separately:

```text
python3 scripts/extract_build_diagnostics.py --source <local>/source-snapshot.tex --log <local>/pass2.log --pdf <local>/pass2.pdf --output-prefix build-diagnostics/baseline-01/as-printed/pass2
```

The output prefix must be unused; the extractor refuses to overwrite an earlier diagnostic set. Source line numbers must come from the matching source snapshot. After a preamble or macro fix changes line numbers, do not apply the old log to the edited source. Reidentify the affected final-PDF spans by the preserved source-anchor IDs, rather than reusing old physical page numbers.

## Layout fixes, visual review, and final acceptance

For every layer, preserve the initial `>10 pt` targets before fixing layout. Apply permitted line-breaking, scaling, or display-layout fixes through the preamble or reader macros, recording the actual changes as required. Leave the text unchanged. Build another two-pass run under a new name and retain both the before and after diagnostic sizes.

The final pair must return exit code zero, have no unresolved errors or missing characters, and contain no overfull box exceeding **2 pt**. Inspect all warnings and the complete raw logs; the extractor recognizes common diagnostic forms and is not an exhaustive TeX verifier. Resolve unstable references and rerun warnings before treating a pair as final.

Render and inspect every page identified by an initial `>10 pt` overflow and the corresponding pages in the final layout, plus a spread of pages across the whole book. For a chosen **physical** PDF page:

```text
pdftoppm -f PAGE -l PAGE -r 160 -singlefile -png <local>/pass2.pdf <local>/review-page
```

Use higher resolution for ambiguous glyphs or close layout decisions. Record the commands, actual errors and warnings, overflow sizes before and after, inspected physical pages and source anchors, and observations in `PDF_CHECK.md`. Only after that acceptance step should the three final second-pass PDFs be copied to `pdf/` under their source basenames. The build stage cannot be marked complete from this plan or from mechanical extraction alone.

## Infrastructure validation performed

The extractor was exercised only with a content-free synthetic source, log, and two-page PDF. That fixture checked strict threshold handling at 2 and 10 pt, a wrapped source-line range, PDF named-destination mapping, an explicit unresolved vertical-box warning, ordinary errors and warnings, missing-character detection, and removal of private paths and email addresses. No edition was compiled or visually inspected for this infrastructure preparation.
