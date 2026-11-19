#!/usr/bin/env python3
"""Verify the supplied Illusie archives before safely restoring their trees.

Usage: python infrastructure_restore.py --root <local>
No printed reading or textual correction is assessed by this script.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_tsv(data: bytes) -> list[dict[str, str]]:
    text = data.decode('utf-8-sig')
    return list(csv.DictReader(io.StringIO('\n'.join(
        line for line in text.splitlines() if not line.startswith('#')
    )), delimiter='\t'))


def safe_member(name: str) -> None:
    p = PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts or '\\' in name:
        raise ValueError(f'Unsafe archive member: {name!r}')


def verify_archive(archive: Path, expected: tuple[int, str]) -> dict:
    data = archive.read_bytes()
    if len(data) != expected[0] or digest(data) != expected[1]:
        raise ValueError(f'Outer archive hash/size mismatch: {archive.name}')
    with ZipFile(archive) as z:
        infos = z.infolist()
        names = [i.filename for i in infos if not i.is_dir()]
        if len(names) != len(set(names)):
            raise ValueError(f'Duplicate members: {archive.name}')
        for info in infos:
            safe_member(info.filename)
            if ((info.external_attr >> 16) & 0o170000) == 0o120000:
                raise ValueError(f'Archive contains symlink: {archive.name}')
        index = 'FILE_LIST.tsv' if 'CHECK_checkpoint' in archive.name else 'MANIFEST.tsv'
        rows = parse_tsv(z.read(index))
        checked = []
        for row in rows:
            if index == 'FILE_LIST.tsv' and row['status'] != 'included':
                continue
            member = row['archive_member'] if index == 'FILE_LIST.tsv' else row['path_in_zip']
            safe_member(member)
            payload = z.read(member)
            if len(payload) != int(row['bytes']) or digest(payload) != row['sha256'].lower():
                raise ValueError(f'Member hash/size mismatch: {archive.name}: {member}')
            if row.get('prior_checkpoint'):
                raise ValueError(f'Unexpected prior-checkpoint dependency: {archive.name}: {member}')
            checked.append(member)
        unexpected = set(names) - set(checked) - {index}
        if unexpected:
            raise ValueError(f'Unlisted files: {archive.name}: {sorted(unexpected)!r}')
        return dict(archive=archive.name, bytes=len(data), sha256=digest(data),
                    index=index, index_rows=len(rows), verified_members=len(checked),
                    total_files=len(names), uncompressed_bytes=sum(i.file_size for i in infos),
                    verified_member_names=checked)


def extract_archive(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(archive) as z:
        for info in z.infolist():
            safe_member(info.filename)
            target = destination.joinpath(*PurePosixPath(info.filename).parts)
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            data = z.read(info)
            if target.exists():
                if not target.is_file() or target.read_bytes() != data:
                    raise ValueError(f'Refusing to overwrite changed member: {archive.name}: {info.filename}')
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    upload = root / 'upload'
    readme = next(upload.glob('README*.md')).read_text()
    expected = {
        name: (int(size.replace(',', '')), sha)
        for name, size, sha in re.findall(r'\| `([^`]+)` \| ([\d,]+) \| ([0-9a-f]{64}) \|', readme)
    }
    archives = sorted(upload.glob('*.zip'))
    if len(archives) != 8:
        raise ValueError(f'Expected eight archives; found {len(archives)}')
    # Complete verification precedes all extraction.
    report = [verify_archive(f, expected[f.name]) for f in archives]
    for f in archives:
        volume = 'II' if f.name.startswith('ILLUSIE_II_') else 'I'
        suffix = f.name.removeprefix(f'ILLUSIE_{volume}_')
        destination = (root/'work'/f'ILLUSIE_{volume}_CHECK' if suffix.startswith('CHECK_checkpoint')
                       else root/'inputs'/f'ILLUSIE_{volume}'/suffix.removesuffix('.zip'))
        extract_archive(f, destination)
        if not suffix.startswith('CHECK_checkpoint'):
            link = root/'work'/f'ILLUSIE_{volume}_{suffix}'
            if not link.exists():
                link.symlink_to(Path('..')/'upload'/f.name)
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    staging = root/'staging'
    staging.mkdir(exist_ok=True)
    (staging/'ARCHIVE_INTEGRITY.json').write_text(json.dumps(
        dict(verified_at=now, archives=report), indent=2)+'\n')
    lines = ['# Attachment and restoration integrity', '', f'Verified: {now}', '',
             'Infrastructure check only. No page reading, source-text verdict, or mathematical verification is implied.', '',
             'All eight outer ZIP sizes and SHA-256 hashes agree with the supplied README.',
             'Every included manifest/file-list member agrees in size and SHA-256. All indexes were parsed before extraction.',
             'The archive indexes themselves have no self-hash. No unexpected unlisted members or prior-checkpoint dependencies were found.', '',
             '| Archive | Listed payload files verified | Total archive files | Result |',
             '|---|---:|---:|---|']
    for result in report:
        lines.append(f"| `{result['archive']}` | {result['verified_members']} | {result['total_files']} | pass |")
    lines += ['', '## Restoration', '',
              '- Checkpoint 09 was restored into the corresponding volume workspace.',
              '- Supplied scans, original sources, and context remain in separate input trees.',
              '- Supplied input ZIPs are linked beside, outside, the deliverable workspaces.',
              '- Existing different content is never overwritten by the restoration script.',
              '- The checkpoint `sources/MANIFEST.tsv` records the original release inputs; the checkpoint `FILE_LIST.tsv` is the hash authority for the checkpoint sources.',
              '- Volume II was restored only; its text check has not begun.', '']
    (staging/'ARCHIVE_INTEGRITY.md').write_text('\n'.join(lines))
    print(json.dumps(dict(verified_at=now, archives=[{k:v for k,v in r.items() if k != 'verified_member_names'} for r in report]), indent=2))


if __name__ == '__main__':
    main()
