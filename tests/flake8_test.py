#!/usr/bin/env python3
import pathlib
import subprocess
import sys

PY2_ONLY_KEYWORDS = [
    'StandardError',
    'apply',
    'basestring',
    'buffer',
    'cmp',
    'coerce',
    'execfile',
    'file',
    'intern',
    'long',
    'raw_input',
    'reduce',
    'reload',
    'unichr',
    'unicode',
    'xrange',
]

root = pathlib.Path(__file__).parent.parent
paths = list(sorted(str(p) for p in root.glob('**/*.pyi')))
window = 0
size = 100
returncode = 0

print('Running flake8 on {} .pyi files...'.format(len(paths)))

while True:
    chunk = paths[window:window + size]
    if not chunk:
        break

    proc = subprocess.run(
        ['flake8', '--builtins=' + ','.join(PY2_ONLY_KEYWORDS)] + chunk,
    )
    if proc.returncode:
        print('flake8 run failed!')
        sys.exit(1)

    window += size

print('flake8 run clean.')
