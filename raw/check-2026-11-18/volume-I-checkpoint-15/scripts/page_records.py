"""Select explicit page records without assessing their content.

Example:
  python -B scripts/page_records.py context/edition_records \
    --work LNM239 --printed-page 9 --physical-page 27

Accept the edition_records directory (whose working_folder child holds the files)
or the direct ledger directory. Only the five named JSONL files below are opened.
Match top-level work/work_id
(or works/work_ids) and printed_page/printed_pages or physical_page/physical_pages.
A singular key may also contain an actual JSON list. At least one populated page
axis must match; every populated locator field must agree with the query. Missing
axes are allowed, contradictory axes are excluded, and prose/ranges are never
searched. Integers and their exact decimal strings agree; booleans/floats do not.
Roman labels stay case-sensitive and distinct from Arabic numbers.

Output is JSONL with record-set name, physical JSONL line, and the full matching
record except bulky evidence/path/hash lists. Omitted fields are listed explicitly.
Use --full-fields to retain those lists, or --pretty for indented JSON objects.
This is a read-only navigation aid, not a review or completeness certification.
"""

import argparse
import json
import sys
from pathlib import Path


RECORD_SETS = (
    'SOURCE_CORRECTIONS',
    'NORMALIZATION_DECISIONS',
    'TRANSCRIPTION_DECISIONS',
    'TRANSLATION_DECISIONS',
    'REVERSALS_AND_GLOBAL_REPAIRS',
)
WORK_KEYS = ('work', 'work_id', 'works', 'work_ids')
PRINTED_KEYS = ('printed_page', 'printed_pages')
PHYSICAL_KEYS = ('physical_page', 'physical_pages')
BOOKKEEPING_LIST_KEYS = frozenset('''
evidence evidence_refs evidence_files evidence_paths raw_evidence obsolete_evidence
prior_evidence previous_evidence historical_evidence evidence_history source_evidence
old_evidence obsolete_evidence_paths paths file_paths source_paths original_paths
old_paths previous_paths path_history obsolete_paths input_paths output_paths
asset_paths reference_paths hashes checksums sha256s source_hashes file_hashes
sha256_hashes hash_history original_hashes old_hashes previous_hashes
'''.split())


def populated(value):
    return value is not None and value != '' and value != []


def exact(value, target):
    return type(value) in (str, int) and str(value) == str(target)


def field_matches(value, target):
    if isinstance(value, list):
        return any(exact(item, target) for item in value)
    return exact(value, target)


def axis(row, keys, target):
    values = [row[key] for key in keys if key in row and populated(row[key])]
    return bool(values), all(field_matches(value, target) for value in values)


def matches(row, work, printed_page, physical_page):
    has_work, work_ok = axis(row, WORK_KEYS, work)
    has_printed, printed_ok = axis(row, PRINTED_KEYS, printed_page)
    has_physical, physical_ok = axis(row, PHYSICAL_KEYS, physical_page)
    return (has_work and work_ok and (has_printed or has_physical)
            and printed_ok and physical_ok)


def compact_record(row):
    omitted = []

    def walk(value, trail=()):
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                key_lower = key.lower()
                bookkeeping = key_lower in BOOKKEEPING_LIST_KEYS
                bulky = isinstance(item, list) and (len(item) > 8 or
                        len(json.dumps(item, ensure_ascii=False)) > 1024)
                if bookkeeping and bulky:
                    omitted.append({'field': '.'.join((*trail, key)),
                                    'items': len(item)})
                else:
                    result[key] = walk(item, (*trail, key))
            return result
        if isinstance(value, list):
            return [walk(item, (*trail, str(index)))
                    for index, item in enumerate(value)]
        return value

    return walk(row), omitted


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON object key')
        result[key] = value
    return result


def reject_json_constant(value):
    raise ValueError('nonstandard JSON constant: ' + value)


def ledger_directory(directory):
    candidates = (directory, directory / 'working_folder')
    complete = [candidate for candidate in candidates
                if all((candidate / (name + '.jsonl')).is_file() for name in RECORD_SETS)]
    if len(complete) != 1:
        raise ValueError('Expected exactly one complete five-file record set in the supplied '
                         'directory or its working_folder child; supply the direct ledger '
                         'directory if both exist.')
    return complete[0]


def select_records(directory, work, printed_page, physical_page, full_fields=False):
    directory = ledger_directory(directory)
    selected = []
    for name in RECORD_SETS:
        filename = name + '.jsonl'
        try:
            stream = (directory / filename).open(encoding='utf-8-sig')
        except OSError as exc:
            raise ValueError(f'{filename}: cannot read required file ({type(exc).__name__})') from None
        with stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line, object_pairs_hook=no_duplicate_keys,
                                     parse_constant=reject_json_constant)
                except (ValueError, TypeError):
                    raise ValueError(f'{filename}:{line_number}: invalid or ambiguous JSON') from None
                if not isinstance(row, dict):
                    raise ValueError(f'{filename}:{line_number}: expected one JSON object')
                if not matches(row, work, printed_page, physical_page):
                    continue
                record, omitted = (row, []) if full_fields else compact_record(row)
                item = {'record_set': name, 'jsonl_line': line_number,
                        'record': record}
                if omitted:
                    item['omitted_lists'] = omitted
                selected.append(item)
    return selected


def positive_integer(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('physical page must be a positive integer') from None
    if number < 1 or str(number) != value:
        raise argparse.ArgumentTypeError('physical page must be a positive decimal integer')
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('edition_records', type=Path)
    parser.add_argument('--work', required=True, choices=('LNM239', 'LNM283'))
    parser.add_argument('--printed-page', required=True)
    parser.add_argument('--physical-page', required=True, type=positive_integer)
    parser.add_argument('--full-fields', action='store_true')
    parser.add_argument('--pretty', action='store_true')
    args = parser.parse_args(argv)
    try:
        selected = select_records(args.edition_records, args.work, args.printed_page,
                                  args.physical_page, args.full_fields)
        encoded = [json.dumps(item, ensure_ascii=False, allow_nan=False,
                              indent=2 if args.pretty else None)
                   for item in selected]
    except (ValueError, UnicodeError) as exc:
        print('page_records: ' + str(exc), file=sys.stderr)
        return 2
    for item in encoded:
        print(item)
    print(f'{len(selected)} matching records from {len(RECORD_SETS)} record sets.',
          file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
