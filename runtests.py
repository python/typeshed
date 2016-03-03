#!/usr/bin/env python3
"""Test runner for typeshed.

Depends on mypy being installed.

Approach:

1. Parse sys.argv
2. Compute appropriate arguments for mypy
3. Stuff those arguments into sys.argv
4. Run mypy.main('')
5. Repeat steps 2-4 for other mypy runs (e.g. --py2)
"""

import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description="Test runner for typeshed. Patterns are unanchored regexps on the full path.")
parser.add_argument('-v', '--verbose', action='count', default=0, help="More output")
parser.add_argument('-n', '--dry-run', action='store_true', help="Don't actually run mypy")
parser.add_argument('-x', '--exclude', type=str, nargs='*', help="Exclude pattern")
parser.add_argument('filter', type=str, nargs='*', help="Include pattern (default all)")


def log(args, *varargs):
    if args.verbose >= 2:
        print(*varargs)

def match(args, fn):
    if not args.filter and not args.exclude:
        log(args, fn, 'accept by default')
        return True
    if args.exclude:
        for f in args.exclude:
            if re.search(f, fn):
                log(args, fn, 'excluded by pattern', f)
                return False
    if args.filter:
        for f in args.filter:
            if re.search(f, fn):
                log(args, fn, 'accepted by pattern', f)
                return True
    if args.filter:
        log(args, fn, 'rejected (no pattern matches)')
        return False
    log(args, fn, 'accepted (no exclude pattern matches)')
    return True


def main():
    args = parser.parse_args()

    try:
        from mypy.main import main as mypy_main
    except ImportError:
        print("Cannot import mypy. Did you install it?")
        sys.exit(1)

    files2 = []
    files3 = []
    for dir, subdirs, files in os.walk('.'):
        for file in files:
            if file == '__builtin__.pyi':
                continue  # Special case (alias for builtins.py).
            if file == 'typing.pyi':
                continue  # Hack for https://github.com/python/mypy/issues/1254
            if file.endswith('.pyi') or file.endswith('.py'):
                full = os.path.join(dir, file)
                if match(args, full):
                    if '/2' in dir:
                        files2.append(full)
                    if '/3' in dir or '/2and3' in dir:
                        files3.append(full)
    if not (files2 or files3):
        print('--- nothing to do ---')
    code = 0
    for flags, files in [([], files3), (['--py2'], files2)]:
        if files:
            sys.argv = ['mypy'] + flags + files
            if args.verbose:
                print('running', ' '.join(sys.argv))
            else:
                print('running mypy', ' '.join(flags), '# with', len(files), 'files')
            try:
                if not args.dry_run:
                    mypy_main('')
            except SystemExit as err:
                code = max(code, err.code)
    if code:
        print('--- exit status', code, '---')
        sys.exit(code)


if __name__ == '__main__':
    main()
