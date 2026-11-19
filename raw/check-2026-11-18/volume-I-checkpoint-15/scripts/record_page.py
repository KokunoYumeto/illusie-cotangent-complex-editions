"""Append a reviewer-supplied page record; never infer a review from a render."""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parent.parent
data = json.load(sys.stdin)
required = {"printed_page", "scan_page", "comparisons", "findings", "changes", "existing_corrections"}
if not required <= data.keys():
    raise ValueError("Missing reviewer-supplied record fields")
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
entry = f"### {data['printed_page']} (scan PDF page {data['scan_page']})\n\n"
entry += f"Reviewer: GPT-6 Astra Pro. Completed: {now}.\n\n"
entry += "Authority rendered at 400 dpi. " + data["comparisons"] + "\n\n"
entry += "Findings: " + data["findings"] + "\n\n"
entry += "Changes: " + data["changes"] + "\n\n"
entry += "Existing corrections: " + data["existing_corrections"] + "\n\n"
if data.get("limitations"):
    entry += "Limits: " + data["limitations"] + "\n\n"
with (root/"CHECK_RECORD.md").open("a", encoding="utf-8") as f: f.write(entry)
with (root/"progress.log").open("a", encoding="utf-8") as f:
    f.write(f"page {data['printed_page']} done {now}\n")
print(f"Recorded {data['printed_page']} at {now}.")
