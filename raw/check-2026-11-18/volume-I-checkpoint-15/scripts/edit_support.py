"""Exact-match edition edits with an evidence row for each accepted change."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAYERS = {
    "as-printed": "francais-diplomatique/02-volume-I-francais-diplomatique.tex",
    "corrected": "francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex",
    "English": "english/02-volume-I-english.tex",
}

def edit(layer, old, new, page, line, statement, evidence, kind, ledger_layer=None):
    path = ROOT / "sources" / LAYERS[layer]
    contents = path.read_text(encoding="utf-8")
    if contents.count(old) != 1:
        raise ValueError(f"{layer}: exact edit target count is {contents.count(old)}")
    path.write_text(contents.replace(old, new, 1), encoding="utf-8")
    row = [str(path.relative_to(ROOT)), ledger_layer or layer, page, line, statement,
           old, new, evidence, kind, "high (first reading; second reading pending)"]
    with (ROOT / "CORRECTIONS.tsv").open("a", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerow(row)

def verdict(page, statement, diplomatic, corrected, verdict_text, evidence):
    with (ROOT / "EXISTING_CORRECTIONS.tsv").open("a", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerow(
            [page,statement,diplomatic,corrected,verdict_text,evidence])

def edit_page(layer, anchor, old, new, page, line, statement, evidence, kind):
    """Restrict a reviewed edit to one page, retaining unique replay context."""
    contents = (ROOT / "sources" / LAYERS[layer]).read_text(encoding="utf-8")
    begin = contents.index(anchor)
    end = contents.index("\\end{illusie", begin)
    region = contents[begin:end]
    if region.count(old) != 1:
        raise ValueError(f"{layer}, {page}: page target count {region.count(old)}")
    pos = begin + region.index(old)
    lo, hi = pos, pos + len(old)
    while contents.count(contents[lo:hi]) != 1:
        lo = max(0, contents.rfind("\n", 0, max(0, lo-1)) + 1)
        next_line = contents.find("\n", hi+1)
        hi = len(contents) if next_line < 0 else next_line
    before = contents[lo:hi]
    after = contents[lo:pos] + new + contents[pos+len(old):hi]
    edit(layer, before, after, page, line, statement, evidence, kind)
