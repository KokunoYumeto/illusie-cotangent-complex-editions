"""Replay this run's exact source edits onto a fresh copy of the supplied tree.

Usage: python scripts/replay_corrections.py CORRECTIONS.tsv fresh_audit_directory
The directory must contain sources/ in the archive's original layout.
This replays edits; it does not audit, compile, or certify the text.
"""
import csv
import sys
from pathlib import Path

ledger, destination = map(Path, sys.argv[1:3])
with ledger.open(encoding="utf-8", newline="") as f:
    for n,row in enumerate(csv.DictReader(f, delimiter="\t"),1):
        target = destination / row["file"]
        text = target.read_text(encoding="utf-8")
        if text.count(row["old"]) != 1:
            raise ValueError(f"Correction {n}: expected one exact old-text occurrence")
        target.write_text(text.replace(row["old"],row["new"],1),encoding="utf-8")
print("Exact source edits replayed; no audit or build certification implied.")
