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
import importlib.metadata
import inspect
import os
import sys
import textwrap
import traceback
from collections import defaultdict
from collections.abc import Iterable, Sequence
from pathlib import Path

from packaging.requirements import Requirement

from parse_metadata import read_dependencies, read_metadata
from utils import PYTHON_VERSION, chdir, colored

if sys.platform == "win32":
    print("pytype does not support Windows.", file=sys.stderr)
    sys.exit(1)
if sys.version_info >= (3, 11):
    print("pytype does not support Python 3.11+ yet.", file=sys.stderr)
    sys.exit(1)

# pytype is not py.typed https://github.com/google/pytype/issues/1325
from pytype import config as pytype_config, load_pytd  # type: ignore[import]
from pytype.imports import typeshed  # type: ignore[import]

TYPESHED_SUBDIRS = ["stdlib", "stubs"]
TYPESHED_HOME = "TYPESHED_HOME"
_LOADERS = {}


def main() -> None:
    args = create_parser().parse_args()
    typeshed_location = args.typeshed_location or os.getcwd()
    old_typeshed_home = os.environ.get(TYPESHED_HOME)
    os.environ[TYPESHED_HOME] = typeshed_location
    print(f"Testing files with pytype on Python {PYTHON_VERSION}...")
    with chdir(typeshed_location):
        check_subdirs_discoverable(TYPESHED_SUBDIRS)
        files_to_test = determine_files_to_test(paths=args.files or TYPESHED_SUBDIRS)
        if not files_to_test:
            print(colored("Nothing to do; exit 1.", "red"))
            sys.exit(1)
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


def classify_files(paths: Sequence[str]) -> tuple[list[str], defaultdict[str, list[str]]]:
    """Classify files into stdlib and stubs by distribution."""
    stdlib: list[str] = []
    stubs: defaultdict[str, list[str]] = defaultdict(list)
    stubs_path = Path("stubs")
    stubs_absolute_path = stubs_path.resolve()
    for path_s in paths:
        path = Path(path_s).resolve()
        if path.samefile(stubs_absolute_path):
            # All stubs, classify by distribution for version checking later.
            for subdir in stubs_path.iterdir():
                stubs[subdir.name].append(str(subdir))
        elif path.is_relative_to(stubs_absolute_path):
            # A single stub directory or file.
            distribution = path.relative_to(stubs_absolute_path).parts[0]
            stubs[distribution].append(path_s)
        else:
            stdlib.append(path_s)
    return stdlib, stubs


def determine_files_to_test(*, paths: Sequence[str]) -> list[str]:
    """Determine all files to test, checking if it's in the exclude list and which Python versions to use.

    Returns a list of pairs of the file path and Python version as an int."""
    stdlib, stubs = classify_files(paths)
    paths_to_test = list(stdlib)
    for pkg, pkg_paths in stubs.items():
        requires_python = read_metadata(pkg).requires_python
        if not requires_python.contains(PYTHON_VERSION):
            msg = f"skipping {pkg!r} (requires Python {requires_python}; test is being run using Python {PYTHON_VERSION})"
            print(colored(msg, "yellow"))
            continue
        paths_to_test.extend(pkg_paths)
    filenames = find_stubs_in_paths(paths_to_test)
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


def _get_pkgs_associated_with_requirement(req_name: str) -> list[str]:
    dist = importlib.metadata.distribution(req_name)
    toplevel_txt_contents = dist.read_text("top_level.txt")
    if toplevel_txt_contents is None:
        if dist.files is None:
            raise RuntimeError("Can't read find the packages associated with requirement {req_name!r}")
        maybe_modules = [f.parts[0] if len(f.parts) > 1 else inspect.getmodulename(f) for f in dist.files]
        packages = [name for name in maybe_modules if name is not None and "." not in name]
    else:
        packages = toplevel_txt_contents.split()
    # https://peps.python.org/pep-0561/#stub-only-packages
    return sorted({package.removesuffix("-stubs") for package in packages})


def get_missing_modules(files_to_test: Sequence[str]) -> Iterable[str]:
    """Get names of modules that should be treated as missing.

    Some typeshed stubs depend on dependencies outside of typeshed. Since pytype
    isn't able to read such dependencies, we instead declare them as "missing"
    modules, so that no errors are reported for them.

    Similarly, pytype cannot parse files on its exclude list, so we also treat
    those as missing.
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
        for external_req in read_dependencies(distribution).external_pkgs:
            req_name = Requirement(external_req).name
            associated_packages = _get_pkgs_associated_with_requirement(req_name)
            missing_modules.update(associated_packages)

    test_dir = os.path.dirname(__file__)
    exclude_list = os.path.join(test_dir, "pytype_exclude_list.txt")
    with open(exclude_list) as f:
        excluded_files = f.readlines()
        for fi in excluded_files:
            if not fi.startswith("stubs/"):
                # Skips comments, empty lines, and stdlib files, which are in
                # the exclude list because pytype has its own version.
                continue
            unused_stubs_prefix, unused_pkg, mod_path = fi.split("/", 2)  # pyright: ignore [reportUnusedVariable]
            missing_modules.add(os.path.splitext(mod_path)[0])
    return missing_modules


def run_all_tests(*, files_to_test: Sequence[str], print_stderr: bool, dry_run: bool) -> None:
    bad = []
    errors = 0
    total_tests = len(files_to_test)
    missing_modules = get_missing_modules(files_to_test)
    for runs, f in enumerate(files_to_test, start=1):
        if dry_run:
            stderr = None
        else:
            stderr = run_pytype(filename=f, python_version=PYTHON_VERSION, missing_modules=missing_modules)
        if stderr:
            errors += 1
            test_file = f"{_get_relative(f)}:"
            if print_stderr:
                print(colored(test_file, "red"))
                print(f"{textwrap.indent(stderr, '  ')}")
            stacktrace_final_line = stderr.rstrip().rsplit("\n", 1)[-1]
            bad.append((test_file, stacktrace_final_line))

        if runs % 25 == 0:
            color = "red" if errors else "green"
            print(colored(f"  {runs:4d}/{total_tests:d} with {errors:4d} errors", color))

    for test, err in bad:
        print(colored(test, "red"), err)

    file_plural = "file" if total_tests == 1 else "files"
    error_plural = "error" if errors == 1 else "errors"
    msg = f"\nRan pytype with {total_tests:d} pyi {file_plural}, got {errors:d} {error_plural}."
    if errors:
        color = "red"
        code = 1
        if not print_stderr:
            msg += "\nRun again with --print-stderr to get the full stacktrace."
    else:
        color = "green"
        code = 0
    print(colored(msg, color))
    sys.exit(code)


if __name__ == "__main__":
    main()
