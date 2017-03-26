#!/usr/bin/env python3
"""Script to run mypy's test suite against this version of typeshed."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tempdir:
        dirpath = Path(tempdir)
        subprocess.run(['git', 'clone', '--depth', '1', 'git://github.com/python/mypy',
                        str(dirpath / 'mypy')], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-U', '-r',
                        str(dirpath / 'mypy/test-requirements.txt')], check=True)
        shutil.copytree('stdlib', str(dirpath / 'mypy/typeshed/stdlib'))
        shutil.copytree('third_party', str(dirpath / 'mypy/typeshed/third_party'))
        try:
            subprocess.run(['./runtests.py'], cwd=str(dirpath / 'mypy'))
        except subprocess.CalledProcessError:
            print('mypy tests failed', file=sys.stderr)
            sys.exit(1)
        else:
            print('mypy tests succeeded', file=sys.stderr)
            sys.exit(0)
