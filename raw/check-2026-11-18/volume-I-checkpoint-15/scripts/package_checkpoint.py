"""Make a complete, size-limited checkpoint without uploading it.

Run from any directory. The default root is the deliverable tree containing
this script. Use --dry-run to inspect the plan without writing any files.
Invoke once at each 45-minute checkpoint time; this script is not a scheduler.
Only the caller can establish that a resulting archive was durably saved.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import zipfile


MAX_ARCHIVE_BYTES = 499_000_000  # Strictly below the requested 500 MB ceiling.
FIRST_CHECKPOINT_NUMBER = 10  # This continuation follows supplied checkpoint 09.
CHECKPOINT_INTERVAL_MINUTES = 45
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".bmp"}
ARCHIVE_SUFFIXES = {".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar"}
BUILD_SUFFIXES = {".aux", ".toc", ".out", ".fls", ".fdb_latexmk", ".bcf", ".blg"}
EXCLUDED_DIRS = {
    "__pycache__", ".git", ".pytest_cache", ".mypy_cache", "node_modules",
    "vendor", "tex-toolchain", "upload", "attachments", "inputs", "input", "scans", "originals",
    "tmp", "cache", "renders", "rendered",
}
REQUIRED_REPORTS = {
    "README.md", "CORRECTIONS.tsv", "CHECK_RECORD.md", "CHECK_EVENTS.tsv",
    "NOTES.md", "PDF_CHECK.md", "progress.log",
}
REQUIRED_SOURCES = {
    "ILLUSIE_I_CHECK": [
        "francais-corrige/08-volume-I-francais-corrige-par-gpt-5-6-sol.tex",
        "francais-corrige/CONSTRUIRE.md",
        "francais-corrige/front-matter.pdf",
        "francais-corrige/publisher-back-matter.pdf",
        "francais-corrige/assets/autumn-road-r1.png",
        "francais-diplomatique/02-volume-I-francais-diplomatique.tex",
        "francais-diplomatique/CONSTRUIRE.md",
        "francais-diplomatique/front-matter.pdf",
        "francais-diplomatique/publisher-back-matter.pdf",
        "francais-diplomatique/assets/autumn-road-r1.png",
        "english/02-volume-I-english.tex",
        "english/BUILD.md",
        "english/front-matter.pdf",
        "english/publisher-back-matter.pdf",
        "english/assets/autumn-road-r1.png",
    ],
    "ILLUSIE_II_CHECK": [
        "02-volume-II-fr-corrected.tex", "05-volume-II-fr-diplomatic.tex",
        "07-volume-II-english.tex", "BUILD.md", "assets/autumn-road-r1.png",
    ],
}
SCAN_NAME = re.compile(
    r"ILLUSIE_(?:I|II)_(?:LNM239|LNM283|author_errata|erratum_p305_springer)\.pdf$",
    re.IGNORECASE,
)


@dataclass
class Payload:
    member: str
    source: Path
    size: int
    digest: str
    fingerprint: tuple[int, int]


def checked_member(value: str) -> str:
    path = PurePosixPath(value)
    if (not value or path.is_absolute() or ".." in path.parts
            or "\\" in value or any(ord(c) < 32 for c in value)):
        raise ValueError("Archive member names must be safe relative names.")
    return path.as_posix()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fingerprint(path: Path) -> tuple[int, int]:
    info = path.stat()
    return info.st_size, info.st_mtime_ns


def evidence_references(root: Path) -> str:
    # A crop is eligible only when an audit report explicitly mentions it.
    # This is a packaging test, not a judgment about the report's reading.
    reports = sorted(root.glob("*.md")) + sorted(root.glob("*.tsv"))
    return "\n".join(p.read_text(encoding="utf-8") for p in reports
                     if p.name != "FILE_LIST.tsv")


def exclusion_reason(member: str, references: str) -> str | None:
    path = PurePosixPath(member)
    parts = path.parts
    suffix = path.suffix.lower()
    if path.name == "FILE_LIST.tsv":
        return "Prior generated packaging index; this archive generates its own index."
    if path.name in {".DS_Store", "Thumbs.db"}:
        return "Operating-system cache."
    if suffix in {".pyc", ".pyo"}:
        return "Python bytecode cache."
    if suffix in ARCHIVE_SUFFIXES:
        return "Input, earlier-version, or nested archive; archives are never nested."
    if SCAN_NAME.fullmatch(path.name):
        return "Supplied authority scan or errata PDF; retained separately as input."
    if suffix in BUILD_SUFFIXES or path.name.endswith(".synctex.gz"):
        return "Reproducible compiler intermediate."
    if suffix == ".log" and member != "progress.log":
        return "Raw compiler or runtime log; the audit record is a separate deliverable."
    if parts[0] == "evidence":
        if suffix in RASTER_SUFFIXES:
            if member in references or path.name in references:
                return None
            return "Image is not explicitly referenced in the current audit reports."
        return None
    if suffix in RASTER_SUFFIXES and parts[0] != "sources":
        return "Ordinary rendered image; retain discussed crops under evidence/."
    return None


def collect_tree(source: Path, prefix: str, references: str,
                 excluded: list[tuple[str, str]]) -> list[Payload]:
    result: list[Payload] = []

    def add_file(path: Path, member: str) -> None:
        member = checked_member(member)
        if path.is_symlink():
            raise ValueError(f"Symlink requires an explicit regular-file copy: {member}")
        reason = exclusion_reason(member, references)
        if reason:
            excluded.append((member, reason))
            return
        before = fingerprint(path)
        digest = sha256_file(path)
        if fingerprint(path) != before:
            raise ValueError(f"File changed during inspection: {member}")
        result.append(Payload(member, path, before[0], digest, before))

    if source.is_file():
        add_file(source, prefix or source.name)
        return result
    if not source.is_dir():
        raise ValueError("A requested support file or directory does not exist.")
    for directory, subdirs, files in os.walk(source, followlinks=False):
        subdirs.sort()
        files.sort()
        relative = Path(directory).relative_to(source)
        kept = []
        for name in subdirs:
            child = Path(directory) / name
            member = PurePosixPath(prefix, relative.as_posix(), name).as_posix()
            if name in EXCLUDED_DIRS:
                excluded.append((member + "/*", "Input, runtime, vendor, or cache directory."))
            elif child.is_symlink():
                raise ValueError(f"Symlink directory requires explicit copies: {member}")
            else:
                kept.append(name)
        subdirs[:] = kept
        for name in files:
            member = PurePosixPath(prefix, relative.as_posix(), name).as_posix()
            add_file(Path(directory) / name, member)
    return result


def zip_bound(item: Payload) -> int:
    # Conservative zlib compressBound plus ZIP headers and a further margin.
    n = item.size
    return n + (n >> 12) + (n >> 14) + (n >> 25) + 512 + 2 * len(item.member.encode("utf-8"))


def partition(items: list[Payload], max_bytes: int, index_reserve: int) -> list[list[Payload]]:
    budget = max_bytes - max(1_048_576, index_reserve)
    if budget <= 0:
        raise ValueError("The chosen part limit cannot hold the packaging index.")
    parts: list[list[Payload]] = [[]]
    used = 0
    for item in items:
        bound = zip_bound(item)
        if bound >= budget:
            raise ValueError(f"One member cannot fit safely in a ZIP part: {item.member}")
        if used + bound >= budget and parts[-1]:
            parts.append([])
            used = 0
        parts[-1].append(item)
        used += bound
    return parts


def make_index(parts: list[list[Payload]], names: list[str],
               excluded: list[tuple[str, str]], created: str, due: str) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(["archive_member", "status", "zip_part", "bytes", "sha256", "reason", "prior_checkpoint"])
    for name, items in zip(names, parts):
        for item in items:
            writer.writerow([item.member, "included", name, item.size, item.digest,
                             "Current complete deliverable or explicitly selected support file.", ""])
    writer.writerow(["FILE_LIST.tsv", "generated", names[0], "", "",
                     "Packaging index; no self-hash. Created " + created + "; 45-minute due time " + due + ".", ""])
    for member, reason in sorted(excluded):
        writer.writerow([member, "excluded", "", "", "", reason, ""])
    for category, reason in [
        ("[supplied attachments and extracted input trees]", "Outside checkpoint scope; original inputs remain separate."),
        ("[earlier checkpoints and earlier-version archives]", "Outside checkpoint scope; never copied into a checkpoint."),
        ("[runtime installations, vendor files, and ordinary rendered pages]", "Outside checkpoint scope; only report-referenced evidence crops are retained."),
        ("[unchanged-file omissions]", "None. All current deliverables and selected support files are included again; no prior-checkpoint references are needed."),
    ]:
        writer.writerow([category, "scope", "", "", "", reason, ""])
    return stream.getvalue().encode("utf-8")


def parse_start(root: Path) -> datetime:
    with (root / "progress.log").open(encoding="utf-8") as stream:
        line = stream.readline().rstrip("\r\n")
    return datetime.strptime(line, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)


def checkpoint_due(root: Path, number: int) -> datetime:
    if number < FIRST_CHECKPOINT_NUMBER:
        raise ValueError("This continuation starts at checkpoint 10; earlier checkpoints must remain intact.")
    intervals = number - FIRST_CHECKPOINT_NUMBER + 1
    return parse_start(root) + timedelta(minutes=CHECKPOINT_INTERVAL_MINUTES * intervals)


def publish_exclusively(staged: Path, destination: Path) -> None:
    # Never overwrite an earlier checkpoint, including a filename race.
    created_here = False
    try:
        with destination.open("xb") as target:
            created_here = True
            with staged.open("rb") as source:
                shutil.copyfileobj(source, target, 1024 * 1024)
                target.flush()
                os.fsync(target.fileno())
    except FileExistsError:
        raise ValueError("A checkpoint with the requested name already exists.") from None
    except BaseException:
        # Only the new, incomplete file created by this call may be removed.
        if created_here and destination.exists():
            destination.unlink()
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--number", type=int, required=True, help="Next checkpoint number, starting at 10 for this continuation.")
    parser.add_argument("--output-dir", type=Path, help="Defaults to a checkpoints folder beside the deliverable trees.")
    parser.add_argument("--support", action="append", default=[], metavar="MEMBER=FILE_OR_DIR",
                        help="Add our own new/modified support files under a safe relative member name.")
    parser.add_argument("--max-bytes", type=int, default=MAX_ARCHIVE_BYTES,
                        help="Upper ZIP-part bound, at most 499000000 bytes.")
    parser.add_argument("--dry-run", action="store_true", help="Read and report only; create no files or ZIPs.")
    args = parser.parse_args()
    root = args.root.resolve()
    if root.name not in {"ILLUSIE_I_CHECK", "ILLUSIE_II_CHECK"}:
        raise ValueError("The root must be an ILLUSIE_I_CHECK or ILLUSIE_II_CHECK deliverable tree.")
    if args.number < FIRST_CHECKPOINT_NUMBER or not 2_000_000 <= args.max_bytes <= MAX_ARCHIVE_BYTES:
        raise ValueError("Use checkpoint number 10 or greater and a part bound between 2000000 and 499000000 bytes.")
    due = checkpoint_due(root, args.number)
    now = datetime.now(timezone.utc)
    if not args.dry_run and now < due:
        raise ValueError("The 45-minute checkpoint time has not arrived; no archive was created.")
    missing = sorted(name for name in REQUIRED_REPORTS if not (root / name).is_file())
    missing.extend("sources/" + name for name in REQUIRED_SOURCES[root.name]
                   if not (root / "sources" / name).is_file())
    if missing or not (root / "sources").is_dir():
        raise ValueError("Required current deliverables are missing: " + ", ".join(missing or ["sources/"]))
    references = evidence_references(root)
    excluded: list[tuple[str, str]] = []
    items = collect_tree(root, "", references, excluded)
    for spec in args.support:
        if "=" not in spec:
            raise ValueError("Each --support value must be MEMBER=FILE_OR_DIR.")
        member, source = spec.split("=", 1)
        member = checked_member(member)
        source_path = Path(source).resolve()
        if any(part in EXCLUDED_DIRS for part in source_path.parts):
            raise ValueError("Support selection points into an excluded input/runtime/cache directory.")
        items.extend(collect_tree(source_path, member, references, excluded))
    items.sort(key=lambda item: item.member)
    members = [item.member for item in items]
    if len(members) != len(set(members)):
        raise ValueError("Two input files would have the same archive member name.")
    due_text = due.strftime("%Y-%m-%d %H:%M:%S UTC")
    created = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    index_reserve = 65_536 + sum(len(item.member.encode("utf-8")) + 512 for item in items)
    index_reserve += sum(len(member.encode("utf-8")) + len(reason.encode("utf-8")) + 256
                         for member, reason in excluded)
    parts = partition(items, args.max_bytes, index_reserve)
    stem = f"{root.name}_checkpoint_{args.number:02d}"
    names = ([stem + ".zip"] if len(parts) == 1
             else [f"{stem}_part{i}.zip" for i in range(1, len(parts) + 1)])
    index = make_index(parts, names, excluded, created, due_text)
    if len(index) > max(1_048_576, index_reserve):
        raise ValueError("Packaging index exceeds its conservative reserved space.")
    print(f"Checkpoint {args.number:02d}; 45-minute due time: {due_text}")
    print(f"Included files: {len(items)}; input bytes: {sum(item.size for item in items)}; ZIP parts: {len(parts)}")
    print(f"Excluded entries/categories: {len(excluded)} plus the index's scope categories.")
    print("No files are omitted merely because they are unchanged.")
    if args.dry_run:
        for name in names:
            print("Planned: " + name)
        for member, reason in sorted(excluded):
            print("Excluded: " + member + " — " + reason)
        print("Dry run only: no files or archives were created.")
        return 0
    destination = (args.output_dir or root.parent / "checkpoints").resolve()
    if destination.exists():
        pattern = re.compile(re.escape(root.name) + r"_checkpoint_(\d+)(?:_part\d+)?\.zip$")
        existing = [int(match.group(1)) for path in destination.iterdir()
                    if (match := pattern.fullmatch(path.name))]
        if existing and args.number <= max(existing):
            raise ValueError("The requested number is not greater than the existing local checkpoint numbers.")
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="checkpoint-stage-", dir=destination) as temporary:
        staging = Path(temporary)
        for part_number, (name, part) in enumerate(zip(names, parts)):
            staged = staging / name
            with zipfile.ZipFile(staged, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                if part_number == 0:
                    archive.writestr("FILE_LIST.tsv", index)
                for item in part:
                    if fingerprint(item.source) != item.fingerprint:
                        raise ValueError(f"File changed before archiving: {item.member}")
                    archive.write(item.source, item.member)
            if staged.stat().st_size >= args.max_bytes:
                raise ValueError("A staged ZIP exceeds the strict size bound; no checkpoint was published.")
            with zipfile.ZipFile(staged) as archive:
                for item in part:
                    with archive.open(item.member) as stream:
                        digest = hashlib.file_digest(stream, "sha256").hexdigest()
                    if digest != item.digest:
                        raise ValueError(f"Archive bytes differ from the inspected snapshot: {item.member}")
        if any(fingerprint(item.source) != item.fingerprint for item in items):
            raise ValueError("Deliverables changed during packaging; no checkpoint was published.")
        for name in names:
            target = destination / name
            publish_exclusively(staging / name, target)
            print(f"Created: {name}; bytes: {target.stat().st_size}; SHA-256: {sha256_file(target)}")
    print("Archive creation verified. Durable saving/upload is a separate caller action.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print("Checkpoint packaging stopped: " + str(error), file=sys.stderr)
        raise SystemExit(1)
