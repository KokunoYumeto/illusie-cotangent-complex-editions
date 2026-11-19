"""Repair the LuaLaTeX build of Illusie I at checkpoint 15 (ILLUSIE_I_CHECK, 19 Nov 2026), typesetting only, in the
publication copy build/ (a fresh copy of checkpoint 15's sources). French-school field agent (Claude Opus 5.5 at
effort high), 19 Nov 2026. Every change goes to REPAIR_LOG.tsv. Run: python -I -B fix_ill.py [--dry]"""
import csv, pathlib, re, shutil, sys

H = pathlib.Path(__file__).parent
CP = H.parent / "returns/ILLUSIE_I_CHECK_checkpoint_15_20261119T0530Z_unzipped"
B = H / "build"
DRY = "--dry" in sys.argv
if not DRY:
    if B.exists():
        shutil.rmtree(B)
    shutil.copytree(CP / "sources", B)
FILES = ["francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex",
         "francais-diplomatique/02-volume-I-francais-diplomatique.tex", "english/02-volume-I-english.tex"]
BS = chr(92)
CMDS = "longmapsto|mapsto|longrightarrow|rightarrow|simeq|otimes|oplus|cong|times|to|xrightarrow"
MERGED = re.compile(re.escape(BS) + "(" + CMDS + ")([A-Z])")
DEF_ANCHOR = BS + "newlength{" + BS + "ReflowMathWidth}\n"
DEF = (BS + "newcommand{" + BS + "IllusiePthirtynineDisplay}[2]{" + BS + "ReflowDisplay{}{" + BS + "hbox to" + BS
       + "linewidth{" + BS + "text{#1}" + BS + "hfill$" + BS + "displaystyle #2$" + BS + "hfill" + BS + "phantom{" + BS
       + "text{#1}}}}}\n")
rows = []
for rel in FILES:
    f = (CP / "sources" if DRY else B) / rel
    t = f.read_text(encoding="utf-8")
    for m in MERGED.finditer(t):
        rows.append([rel, t.count("\n", 0, m.start()) + 1, "Undefined control sequence", m.group(0),
                     BS + m.group(1) + " " + m.group(2), "control word run together with the next letter; a space added"])
    t = MERGED.sub(lambda m: BS + m.group(1) + " " + m.group(2), t)
    USE = BS + "IllusiePthirtynineDisplay{(2.3.8.1)}{"
    if t.count(USE) == 1:
        d0 = t.index("newcommand{" + BS + "IllusiePthirtynineDisplay}") - 1
        d1 = t.index(BS + "par" + BS + "vspace{2.4bp}}", d0) + len(BS + "par" + BS + "vspace{2.4bp}}")
        NL = chr(10)
        prov = t[d0:d1].replace(BS + "newcommand", BS + "providecommand", 1) + NL
        pos = t.index(USE)
        line_start = t.rfind(NL, 0, pos) + 1
        rows.append([rel, t.count(NL, 0, pos) + 1, "Undefined control sequence (IllusiePthirtynineDisplay) and the errors after it",
                     "", prov.strip().replace(NL, " "), "the display macro is defined inside an earlier page group and is out of "
                     "scope at (2.3.8.1); the same definition given again before this use (providecommand)"])
        t = t[:line_start] + prov + t[line_start:]
    # the revised rights notice of 15 Nov 2026, printed after the end of the volume (the PDFs printed none)
    sys.path.insert(0, str(H.parent))
    from apply_notice import FR_TR, EN_TR
    END = BS + "end{document}"
    assert t.count(END) == 1, rel
    note = EN_TR if rel.startswith("english") else FR_TR
    block = (BS + "clearpage" + NL + BS + "noindent" + BS + "begin{minipage}{" + BS + "linewidth}" + BS + "small " + note
             + BS + "end{minipage}" + BS + "par" + NL)
    rows.append([rel, t[:t.index(END)].count(NL) + 1, "", "", "rights notice of 15 Nov 2026",
                 "the revised rights notice printed on a last page (notice only)"])
    t = t.replace(END, block + END)
    # English only: one page (PDF p. 252, chapter V) was 2.97pt too full with all its glue shrunk; more shrink in the
    # paragraph skip of the reflow settings lets the page builder fit it (layout only)
    PS = "{2bp plus .3bp minus .2bp}"
    if rel.startswith("english"):
        assert t.count(PS) == 1, rel
        rows.append([rel, t[:t.index(PS)].count(NL) + 1, "Overfull vbox 2.97pt while output is active (PDF p. 252)",
                     PS, "{2bp plus .3bp minus 1bp}", "paragraph skip of ReflowSettings given 1bp of shrink instead of "
                     ".2bp (layout only)"])
        t = t.replace(PS, "{2bp plus .3bp minus 1bp}")
    if not DRY:
        f.write_text(t, encoding="utf-8", newline="")
for r in rows:
    print(r[0].split("/")[0], r[1], r[3][:40], "->", r[4][:60])
if not DRY:
    with open(H / "REPAIR_LOG.tsv", "w", encoding="utf-8", newline="") as out:
        w = csv.writer(out, delimiter="\t", lineterminator="\n")
        w.writerow(["file", "line", "build error (LuaLaTeX)", "before", "after", "repair"])
        w.writerows(rows)
print(len(rows), "places")
