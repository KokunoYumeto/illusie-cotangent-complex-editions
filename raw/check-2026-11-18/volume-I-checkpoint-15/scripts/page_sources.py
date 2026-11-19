"""Show the three edition source regions for manual sequential review.

Extraction and diffs are navigation aids, never reading or proof certificates.
"""
import argparse
import difflib
import re
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("sources", type=Path)
p.add_argument("page", type=int)
p.add_argument("--front", action="store_true", help="page is a physical front-matter page")
args = p.parse_args()
paths = {
    "as-printed": args.sources / "francais-diplomatique/02-volume-I-francais-diplomatique.tex",
    "corrected": args.sources / "francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex",
    "English": args.sources / "english/02-volume-I-english.tex",
}
env = "illusiefrontpage" if args.front else "illusiebodypage"
regions = {}
for layer, path in paths.items():
    lines = path.read_text().splitlines()
    matches = [i for i,s in enumerate(lines) if re.search(r"\\begin\{"+env+r"\}\{[^}]*:p"+f"{args.page:03}"+r"\}",s)]
    if len(matches) != 1:
        raise ValueError(f"{layer}: expected one page region; found {len(matches)}")
    start = matches[0]
    end = next(i for i in range(start+1,len(lines)) if "\\end{"+env+"}" in lines[i])
    body = lines[start:end+1]
    regions[layer] = body
    print(f"\n## {layer}: {path.relative_to(args.sources)} lines {start+1}-{end+1}\n")
    for n,s in enumerate(body,start+1): print(f"{n}: {s}")
print("\n## Exact French-source diff (navigation only)\n")
print("\n".join(difflib.unified_diff(regions['as-printed'],regions['corrected'],fromfile='as-printed',tofile='corrected',lineterm='')))
