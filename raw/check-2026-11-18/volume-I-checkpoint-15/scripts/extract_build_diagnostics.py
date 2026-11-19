"""Extract build diagnostics without certifying a PDF or changing edition files.

Use each pass's own log and PDF. Physical-page targets derived from named
destinations are conservative candidates; unresolved cases require manual work.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
import re


OVERFULL = re.compile(r"Overfull\s+\\([hv])box\s*\(\s*([0-9.]+)pt\s+too\s+(wide|high)\)")
SOURCE_LINES = re.compile(r"at\s+lines?\s+(\d+)(?:--(\d+))?")
BEGIN_PAGE = re.compile(r"\\begin\{(illusiebodypage|illusiefrontpage)\}\{([^}]+)\}")
FILE_LINE_ERROR = re.compile(r"^.+\.(?:tex|sty|cls|def|cfg):\d+:\s+")
WARNING = re.compile(r"(?:LaTeX(?: Font)?|Package .+?|Class .+?|LuaHBTeX|LuaTeX|pdfTeX)\s+[Ww]arning")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
WINDOWS_PATH = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/][^\s<>\x22\x27\x60]*")
UNIX_PATH = re.compile(r"(?<![A-Za-z0-9:/.])/(?:[^\s<>\x22\x27\x60]+)")


@dataclass
class Region:
    first: int
    last: int
    anchor: str
    next_anchor: str | None


def sanitize(value: str) -> str:
    value = EMAIL.sub("<redacted-email>", value)
    value = WINDOWS_PATH.sub("<local>", value)
    value = UNIX_PATH.sub("<local>", value)
    return value.replace("\t", " ").replace("\r", " ").replace("\n", " ")


def source_regions(source: Path) -> list[Region]:
    lines = source.read_text(encoding="utf-8").splitlines()
    starts = [(i, match) for i, line in enumerate(lines, 1)
              if (match := BEGIN_PAGE.search(line))]
    result = []
    for index, (first, match) in enumerate(starts):
        next_start, next_match = starts[index + 1] if index + 1 < len(starts) else (len(lines) + 1, None)
        ending = "\\end{" + match.group(1) + "}"
        last = next((i for i in range(first + 1, next_start) if ending in lines[i - 1]), next_start - 1)
        result.append(Region(first, last, match.group(2), next_match.group(2) if next_match else None))
    return result


def named_pages(pdf: Path | None) -> tuple[dict[str, int], int]:
    if pdf is None:
        return {}, 0
    from pypdf import PdfReader
    reader = PdfReader(pdf)
    pages = {}
    for name, destination in reader.named_destinations.items():
        page = reader.get_destination_page_number(destination)
        if isinstance(page, int) and 0 <= page < len(reader.pages):
            pages[str(name)] = page + 1
    return pages, len(reader.pages)


def write_tsv(path: Path, columns: list[str], rows: list[dict]) -> None:
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--output-prefix", type=Path, required=True)
    args = parser.parse_args()
    outputs = {key: Path(str(args.output_prefix) + suffix) for key, suffix in {
        "overflows": "-overflows.tsv", "diagnostics": "-diagnostics.tsv",
        "targets": "-over10-candidates.tsv", "summary": "-summary.md",
    }.items()}
    if any(path.exists() for path in outputs.values()):
        raise ValueError("A diagnostic output already exists; select a new prefix to preserve earlier runs.")

    regions = source_regions(args.source)
    duplicate_anchors = {anchor for anchor, count in Counter(r.anchor for r in regions).items() if count > 1}
    destination_pages, page_count = named_pages(args.pdf)
    log_lines = args.log.read_text(encoding="utf-8", errors="replace").splitlines()
    overflows, diagnostics, targets = [], [], []
    for index, line in enumerate(log_lines):
        match = OVERFULL.search(line)
        if match:
            # A long diagnostic header may wrap between digits. Join only the
            # header continuation, stopping before another diagnostic or a box trace.
            header = line
            for continuation in log_lines[index + 1:index + 4]:
                if not continuation or OVERFULL.search(continuation) or continuation.startswith(("!", "[]", "\\")):
                    break
                if SOURCE_LINES.search(header) and not re.search(r"--?\s*$", header):
                    break
                header += continuation
            location = SOURCE_LINES.search(header)
            first = int(location.group(1)) if location else None
            last = int(location.group(2) or location.group(1)) if location else None
            touched = [region for region in regions if first is not None and first <= region.last and last >= region.first]
            amount = Decimal(match.group(2))
            row = {
                "log_line": index + 1, "box": match.group(1) + "box",
                "excess_pt": str(amount), "direction": match.group(3),
                "source_first_line": first or "", "source_last_line": last or "",
                "source_anchors": ";".join(sanitize(region.anchor) for region in touched),
                "over_2pt": "yes" if amount > 2 else "no",
                "over_10pt": "yes" if amount > 10 else "no",
                "header": sanitize(header),
            }
            overflows.append(row)
            if amount <= 10:
                continue
            if not touched:
                targets.append({"log_line": index + 1, "excess_pt": str(amount), "source_anchor": "",
                                "candidate_pdf_page": "", "status": "unresolved",
                                "reason": "No source-page region maps to this diagnostic; locate it manually from the raw log."})
            for region in touched:
                start = destination_pages.get(region.anchor)
                stop = destination_pages.get(region.next_anchor) if region.next_anchor else page_count
                if region.anchor in duplicate_anchors or start is None or stop is None or not (1 <= start <= stop <= page_count):
                    targets.append({"log_line": index + 1, "excess_pt": str(amount), "source_anchor": sanitize(region.anchor),
                                    "candidate_pdf_page": "", "status": "unresolved",
                                    "reason": "The PDF or a unique required named destination is unavailable; locate pages manually."})
                else:
                    for page in range(start, stop + 1):
                        targets.append({"log_line": index + 1, "excess_pt": str(amount), "source_anchor": sanitize(region.anchor),
                                        "candidate_pdf_page": page, "status": "candidate",
                                        "reason": "Inclusive span between this source anchor and the next; confirm the affected pages visually."})

        severity = None
        if line.startswith("!") or FILE_LINE_ERROR.match(line) or "Fatal error occurred" in line or "Emergency stop" in line:
            severity = "error"
        elif "Missing character:" in line:
            severity = "missing-character"
        elif WARNING.search(line):
            severity = "warning"
        if severity:
            diagnostics.append({"log_line": index + 1, "severity": severity, "message": sanitize(line)})

    for path in outputs.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    write_tsv(outputs["overflows"], ["log_line", "box", "excess_pt", "direction", "source_first_line", "source_last_line", "source_anchors", "over_2pt", "over_10pt", "header"], overflows)
    write_tsv(outputs["diagnostics"], ["log_line", "severity", "message"], diagnostics)
    write_tsv(outputs["targets"], ["log_line", "excess_pt", "source_anchor", "candidate_pdf_page", "status", "reason"], targets)
    counts = Counter(row["severity"] for row in diagnostics)
    unresolved = sum(row["status"] == "unresolved" for row in targets)
    candidates = sorted({row["candidate_pdf_page"] for row in targets if row["status"] == "candidate"})
    summary = [
        "# Mechanical build-diagnostic extraction", "",
        f"Source: `{sanitize(args.source.name)}`. Log: `{sanitize(args.log.name)}`.",
        f"PDF: `{sanitize(args.pdf.name)}` ({page_count} physical pages)." if args.pdf else "No PDF supplied; physical-page mapping is unavailable.", "",
        f"- Overfull boxes: {len(overflows)}; over 2 pt: {sum(row['over_2pt'] == 'yes' for row in overflows)}; over 10 pt: {sum(row['over_10pt'] == 'yes' for row in overflows)}.",
        f"- Recognized error lines: {counts['error']}; warning lines: {counts['warning']}; missing-character lines: {counts['missing-character']}.",
        f"- Unresolved target rows: {unresolved}.",
        "- Candidate physical PDF pages: " + (", ".join(map(str, candidates)) if candidates else "none resolved") + ".", "",
        "These are diagnostic extraction results, not build or visual acceptance. Check the engine exit status and full raw log separately. The candidate spans include their boundary page and may contain unaffected pages. Delayed floats, macro-generated material, and warnings without source-line locations require manual resolution. Preserve each pass's PDF and log together; a later layout is not a substitute for the earlier PDF.", "",
        "No edition text, correction ledger, page status, or source file was changed by this script.", "",
    ]
    with outputs["summary"].open("x", encoding="utf-8") as stream:
        stream.write("\n".join(summary))
    print(f"Extracted {len(overflows)} overfull diagnostics; {unresolved} target rows remain unresolved.")
    print("No build, reading, or visual acceptance was inferred.")


if __name__ == "__main__":
    main()
