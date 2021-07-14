"""Script to generate unannotated baseline stubs using stubgen.

Basic usage:
$ create_baseline_stubs.py <project>
"""

import argparse
import os
import re
import shutil
import sys
import subprocess


def pip_install(project: str) -> None:
    print(f'Installing distribution: pip install {project}')
    subprocess.run(['pip', 'install', project], check=True)


def run_stubgen(package: str) -> None:
    print(f'Running stubgen: stubgen -p {package}')
    subprocess.run(['python', '-m', 'mypy.stubgen', '-p', package], check=True)


def copy_stubs(src_base_dir: str, package: str, stub_dir: str) -> None:
    print(f'Copying stubs to {stub_dir}')
    src_dir = os.path.join(src_base_dir, package)
    if os.path.isdir(src_dir):
        shutil.copytree(src_dir, os.path.join(stub_dir, package))
    else:
        src_file = os.path.join('out', package + '.pyi')
        if not os.path.isfile(src_file):
            sys.exit('Error: Cannot find generated stubs')
        shutil.copy(src_file, stub_dir)


def run_black(stub_dir: str) -> None:
    print(f'Running black: black {stub_dir}')
    subprocess.run(['black', stub_dir])


def run_isort(stub_dir: str) -> None:
    print(f'Running isort: isort --recursive {stub_dir}')
    subprocess.run(['isort', '--recursive', stub_dir])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('project',
                        help='name of PyPI project for which to generate stubs under stubs/')
    parser.add_argument(
        '--package',
        help='generate stubs for this Python package (by default, infer from installed package)')
    args = parser.parse_args()
    project = args.project
    package = args.package

    if not re.match(r'[a-zA-Z0-9-_.]+$', project):
        sys.exit(f'Invalid character in project name: {project!r}')

    if not package:
        package = project  # TODO: infer from installed files

    if not os.path.isdir('stubs') or not os.path.isdir('stdlib'):
        sys.exit('Error: Current working directory must be the root of typeshed repository')

    stub_dir = os.path.join('stubs', project)
    if os.path.exists(stub_dir):
        sys.exit(f'Error: {stub_dir} already exists (delete it first)')

    pip_install(project)
    run_stubgen(package)
    copy_stubs('out', package, stub_dir)
    run_black(stub_dir)
    run_isort(stub_dir)

    # TODO: create METADATA.json
    # TODO: pyright exclusion

    print('Done.')


if __name__ == "__main__":
    main()
