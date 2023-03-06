#!/usr/bin/env python3
# Lack of pytype typing
# pyright: reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false, reportMissingTypeStubs=false
"""Test runner for typeshed.

Depends on pytype being installed.

If pytype is installed:
    1. For every pyi, do nothing if it is in pytype_exclude_list.txt.
    2. Otherwise, call 'pytype.io.parse_pyi'.
Option two will load the file and all the builtins, typeshed dependencies. This
will also discover incorrect usage of imported modules.
"""

from __future__ import annotations

import argparse
import os
import sys
import traceback
from collections.abc import Iterable, Sequence

import pkg_resources

from parse_metadata import read_dependencies

assert sys.platform != "win32"
# pytype is not py.typed https://github.com/google/pytype/issues/1325
from pytype import config as pytype_config, load_pytd  # type: ignore[import]  # noqa: E402
from pytype.imports import typeshed  # type: ignore[import]  # noqa: E402

TYPESHED_SUBDIRS = ["stdlib", "stubs"]
TYPESHED_HOME = "TYPESHED_HOME"
_LOADERS = {}


def main() -> None:
    args = create_parser().parse_args()
    typeshed_location = args.typeshed_location or os.getcwd()
    subdir_paths = [os.path.join(typeshed_location, d) for d in TYPESHED_SUBDIRS]
    check_subdirs_discoverable(subdir_paths)
    old_typeshed_home = os.environ.get(TYPESHED_HOME)
    os.environ[TYPESHED_HOME] = typeshed_location
    files_to_test = determine_files_to_test(paths=args.files or subdir_paths)
    run_all_tests(files_to_test=files_to_test, print_stderr=args.print_stderr, dry_run=args.dry_run)
    if old_typeshed_home is None:
        del os.environ[TYPESHED_HOME]
    else:
        os.environ[TYPESHED_HOME] = old_typeshed_home


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Pytype/typeshed tests.")
    parser.add_argument("-n", "--dry-run", action="store_true", default=False, help="Don't actually run tests")
    # Default to '' so that symlinking typeshed subdirs in cwd will work.
    parser.add_argument("--typeshed-location", type=str, default="", help="Path to typeshed installation.")
    # Set to true to print a stack trace every time an exception is thrown.
    parser.add_argument(
        "--print-stderr", action="store_true", default=False, help="Print stderr every time an error is encountered."
    )
    parser.add_argument(
        "files", metavar="FILE", type=str, nargs="*", help="Files or directories to check. (Default: Check all files.)"
    )
    return parser


def run_pytype(*, filename: str, python_version: str, missing_modules: Iterable[str]) -> str | None:
    """Runs pytype, returning the stderr if any."""
    if python_version not in _LOADERS:
        options = pytype_config.Options.create("", parse_pyi=True, python_version=python_version)
        # For simplicity, pretends missing modules are part of the stdlib.
        missing_modules = tuple(os.path.join("stdlib", m) for m in missing_modules)
        loader = load_pytd.create_loader(options, missing_modules)
        _LOADERS[python_version] = (options, loader)
    options, loader = _LOADERS[python_version]
    stderr: str | None
    try:
        with pytype_config.verbosity_from(options):
            ast = loader.load_file(_get_module_name(filename), filename)
            loader.finish_and_verify_ast(ast)
    except Exception:
        stderr = traceback.format_exc()
    else:
        stderr = None
    return stderr


def _get_relative(filename: str) -> str:
    top = 0
    for d in TYPESHED_SUBDIRS:
        try:
            top = filename.index(d + os.path.sep)
        except ValueError:
            continue
        else:
            break
    return filename[top:]


def _get_module_name(filename: str) -> str:
    """Converts a filename {subdir}/m.n/module/foo to module.foo."""
    parts = _get_relative(filename).split(os.path.sep)
    if parts[0] == "stdlib":
        module_parts = parts[1:]
    else:
        assert parts[0] == "stubs"
        module_parts = parts[2:]
    return ".".join(module_parts).replace(".pyi", "").replace(".__init__", "")


def check_subdirs_discoverable(subdir_paths: list[str]) -> None:
    for p in subdir_paths:
        if not os.path.isdir(p):
            raise SystemExit(f"Cannot find typeshed subdir at {p} (specify parent dir via --typeshed-location)")


def determine_files_to_test(*, paths: Sequence[str]) -> list[str]:
    """Determine all files to test, checking if it's in the exclude list and which Python versions to use.

    Returns a list of pairs of the file path and Python version as an int."""
    filenames = find_stubs_in_paths(paths)
    ts = typeshed.Typeshed()
    skipped = set(ts.read_blacklist())
    files = []
    for f in sorted(filenames):
        rel = _get_relative(f)
        if rel in skipped:
            continue
        files.append(f)
    return files


def find_stubs_in_paths(paths: Sequence[str]) -> list[str]:
    filenames: list[str] = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, fns in os.walk(path):
                filenames.extend(os.path.join(root, fn) for fn in fns if fn.endswith(".pyi"))
        else:
            filenames.append(path)
    return filenames


def get_missing_modules(files_to_test: Sequence[str]) -> Iterable[str]:
    """Gets module names provided by typeshed-external dependencies.

    Some typeshed stubs depend on dependencies outside of typeshed. Since pytype
    isn't able to read such dependencies, we instead declare them as "missing"
    modules, so that no errors are reported for them.
    """
    stub_distributions = set()
    for fi in files_to_test:
        parts = fi.split(os.sep)
        try:
            idx = parts.index("stubs")
        except ValueError:
            continue
        stub_distributions.add(parts[idx + 1])
    missing_modules = set()
    for distribution in stub_distributions:
        for pkg in read_dependencies(distribution).external_pkgs:
            egg_info = pkg_resources.get_distribution(pkg).egg_info
            assert isinstance(egg_info, str)
            # See https://stackoverflow.com/a/54853084
            top_level_file = os.path.join(egg_info, "top_level.txt")
            with open(top_level_file) as f:
                missing_modules.update(f.read().splitlines())
    return missing_modules


def run_all_tests(*, files_to_test: Sequence[str], print_stderr: bool, dry_run: bool) -> None:
    bad = []
    errors = 0
    total_tests = len(files_to_test)
    missing_modules = get_missing_modules(files_to_test)
    print("Testing files with pytype...")
    for i, f in enumerate(files_to_test):
        python_version = "{0.major}.{0.minor}".format(sys.version_info)
        if dry_run:
            stderr = None
        else:
            stderr = run_pytype(filename=f, python_version=python_version, missing_modules=missing_modules)
        if stderr:
            if print_stderr:
                print(f"\n{stderr}")
            errors += 1
            stacktrace_final_line = stderr.rstrip().rsplit("\n", 1)[-1]
            bad.append((_get_relative(f), python_version, stacktrace_final_line))

        runs = i + 1
        if runs % 25 == 0:
            print(f"  {runs:3d}/{total_tests:d} with {errors:3d} errors")

    print(f"Ran pytype with {total_tests:d} pyis, got {errors:d} errors.")
    for f, v, err in bad:
        print(f"\n{f} ({v}): {err}")
    if errors:
        raise SystemExit("\nRun again with --print-stderr to get the full stacktrace.")


if __name__ == "__main__":
    main()
