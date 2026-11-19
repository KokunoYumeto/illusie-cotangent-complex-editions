"""Record a page only after its human-directed visual audit is complete.

Reads the reviewer's explicit JSON findings from stdin. This script computes
source locators and ledger counts; it performs no visual or mathematical check.
"""
import collections
import csv
import json
import subprocess
import sys
from edit_support import ROOT, LAYERS

data = json.load(sys.stdin)
anchor = data.pop("source_anchor")
locators = []
for layer, relative in LAYERS.items():
    source = (ROOT / "sources" / relative).read_text(encoding="utf-8")
    start = source.index(anchor)
    end = source.index("\\end{illusie", start)
    first = source[:start].count("\n") + 1
    last = source[:end].count("\n") + 1
    locators.append(f"{layer}: sources/{relative}, lines {first}–{last}")
data["comparisons"] = "; ".join(locators) + ". " + data["comparisons"]
with (ROOT / "CORRECTIONS.tsv").open(encoding="utf-8", newline="") as handle:
    counts = collections.Counter(
        (row["layer"], row["kind"])
        for row in csv.DictReader(handle, delimiter="\t")
        if row["printed_page"] == data["printed_page"]
    )
data["changes"] = (
    "; ".join(f"{layer} {kind}: {number}" for (layer, kind), number in counts.items())
    or "No correction rows."
) + ". " + data.get("changes", "")
subprocess.run(
    [sys.executable, str(ROOT / "scripts" / "record_page.py")],
    input=json.dumps(data), text=True, check=True,
)
