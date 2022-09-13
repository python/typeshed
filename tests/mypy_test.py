#!/usr/bin/env python3
"""Run mypy on typeshed's stdlib and third-party stubs."""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass
from io import StringIO
from itertools import product
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from _typeshed import StrPath

from typing_extensions import Annotated, TypeAlias

import tomli
from utils import colored, print_error, print_success_msg, read_dependencies

SUPPORTED_VERSIONS = [(3, 11), (3, 10), (3, 9), (3, 8), (3, 7)]
SUPPORTED_PLATFORMS = ("linux", "win32", "darwin")
TYPESHED_DIRECTORIES = frozenset({"stdlib", "stubs"})

ReturnCode: TypeAlias = int
MajorVersion: TypeAlias = int
MinorVersion: TypeAlias = int
MinVersion: TypeAlias = tuple[MajorVersion, MinorVersion]
MaxVersion: TypeAlias = tuple[MajorVersion, MinorVersion]
Platform: TypeAlias = Annotated[str, "Must be one of the entries in SUPPORTED_PLATFORMS"]
Directory: TypeAlias = Annotated[str, "Must be one of the entries in TYPESHED_DIRECTORIES"]


def python_version(arg: str) -> tuple[MajorVersion, MinorVersion]:
    version = tuple(map(int, arg.split(".")))  # This will naturally raise TypeError if it's not in the form "{major}.{minor}"
    if version not in SUPPORTED_VERSIONS:
        raise ValueError
    # mypy infers the return type as tuple[int, ...]
    return version  # type: ignore[return-value]


class CommandLineArgs(argparse.Namespace):
    verbose: int
    exclude: list[str] | None
    python_version: list[tuple[MajorVersion, MinorVersion]] | None
    dir: list[Directory] | None
    platform: list[Platform] | None
    filter: list[str]


parser = argparse.ArgumentParser(
    description="Typecheck typeshed's stubs with mypy. Patterns are unanchored regexps on the full path."
)
parser.add_argument("-v", "--verbose", action="count", default=0, help="More output")
parser.add_argument("-x", "--exclude", type=str, nargs="*", help="Exclude pattern")
parser.add_argument(
    "-p", "--python-version", type=python_version, nargs="*", action="extend", help="These versions only (major[.minor])"
)
parser.add_argument(
    "-d",
    "--dir",
    choices=TYPESHED_DIRECTORIES,
    nargs="*",
    action="extend",
    help="Test only these top-level typeshed directories (defaults to all typeshed directories)",
)
parser.add_argument(
    "--platform",
    choices=SUPPORTED_PLATFORMS,
    nargs="*",
    action="extend",
    help="Run mypy for certain OS platforms (defaults to sys.platform only)",
)
parser.add_argument("filter", type=str, nargs="*", help="Include pattern (default all)")


@dataclass
class TestConfig:
    """Configuration settings for a single run of the `test_typeshed` function."""

    verbose: int
    exclude: list[str] | None
    major: MajorVersion
    minor: MinorVersion
    directories: frozenset[Directory]
    platform: Platform
    filter: list[str]


def log(args: TestConfig, *varargs: object) -> None:
    if args.verbose >= 2:
        print(*varargs)


def match(path: Path, args: TestConfig) -> bool:
    fn = str(path)
    if not args.filter and not args.exclude:
        log(args, fn, "accept by default")
        return True
    if args.exclude:
        for f in args.exclude:
            if re.search(f, fn):
                log(args, fn, "excluded by pattern", f)
                return False
    if args.filter:
        for f in args.filter:
            if re.search(f, fn):
                log(args, fn, "accepted by pattern", f)
                return True
    if args.filter:
        log(args, fn, "rejected (no pattern matches)")
        return False
    log(args, fn, "accepted (no exclude pattern matches)")
    return True


_VERSION_LINE_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_.]*): ([23]\.\d{1,2})-([23]\.\d{1,2})?$")


def parse_versions(fname: StrPath) -> dict[str, tuple[MinVersion, MaxVersion]]:
    result = {}
    with open(fname) as f:
        for line in f:
            # Allow having some comments or empty lines.
            line = line.split("#")[0].strip()
            if line == "":
                continue
            m = _VERSION_LINE_RE.match(line)
            assert m, f"invalid VERSIONS line: {line}"
            mod: str = m.group(1)
            min_version = parse_version(m.group(2))
            max_version = parse_version(m.group(3)) if m.group(3) else (99, 99)
            result[mod] = min_version, max_version
    return result


_VERSION_RE = re.compile(r"^([23])\.(\d+)$")


def parse_version(v_str: str) -> tuple[int, int]:
    m = _VERSION_RE.match(v_str)
    assert m, f"invalid version: {v_str}"
    return int(m.group(1)), int(m.group(2))


def add_files(files: list[Path], seen: set[str], module: Path, args: TestConfig) -> None:
    """Add all files in package or module represented by 'name' located in 'root'."""
    if module.is_file() and module.suffix == ".pyi":
        files.append(module)
        seen.add(module.stem)
    else:
        to_add = sorted(module.rglob("*.pyi"))
        files.extend(to_add)
        seen.update(path.stem for path in to_add)


class MypyDistConf(NamedTuple):
    module_name: str
    values: dict


# The configuration section in the metadata file looks like the following, with multiple module sections possible
# [mypy-tests]
# [mypy-tests.yaml]
# module_name = "yaml"
# [mypy-tests.yaml.values]
# disallow_incomplete_defs = true
# disallow_untyped_defs = true


def add_configuration(configurations: list[MypyDistConf], distribution: str) -> None:
    with Path("stubs", distribution, "METADATA.toml").open("rb") as f:
        data = tomli.load(f)

    mypy_tests_conf = data.get("mypy-tests")
    if not mypy_tests_conf:
        return

    assert isinstance(mypy_tests_conf, dict), "mypy-tests should be a section"
    for section_name, mypy_section in mypy_tests_conf.items():
        assert isinstance(mypy_section, dict), f"{section_name} should be a section"
        module_name = mypy_section.get("module_name")

        assert module_name is not None, f"{section_name} should have a module_name key"
        assert isinstance(module_name, str), f"{section_name} should be a key-value pair"

        values = mypy_section.get("values")
        assert values is not None, f"{section_name} should have a values section"
        assert isinstance(values, dict), "values should be a section"

        configurations.append(MypyDistConf(module_name, values.copy()))


def run_mypy(args: TestConfig, configurations: list[MypyDistConf], files: list[Path]) -> ReturnCode:
    try:
        from mypy.api import run as mypy_run
    except ImportError:
        print_error("Cannot import mypy. Did you install it?")
        sys.exit(1)

    with tempfile.NamedTemporaryFile("w+") as temp:
        temp.write("[mypy]\n")
        for dist_conf in configurations:
            temp.write(f"[mypy-{dist_conf.module_name}]\n")
            for k, v in dist_conf.values.items():
                temp.write(f"{k} = {v}\n")
        temp.flush()

        flags = get_mypy_flags(args, temp.name)
        mypy_args = [*flags, *map(str, files)]
        if args.verbose:
            print("running mypy", " ".join(mypy_args))
        stdout_redirect, stderr_redirect = StringIO(), StringIO()
        with redirect_stdout(stdout_redirect), redirect_stderr(stderr_redirect):
            returned_stdout, returned_stderr, exit_code = mypy_run(mypy_args)

        if exit_code:
            print_error("failure\n")
            captured_stdout = stdout_redirect.getvalue()
            captured_stderr = stderr_redirect.getvalue()
            if returned_stderr:
                print_error(returned_stderr)
            if captured_stderr:
                print_error(captured_stderr)
            if returned_stdout:
                print_error(returned_stdout)
            if captured_stdout:
                print_error(captured_stdout, end="")
        else:
            print_success_msg()
        return exit_code


def get_mypy_flags(args: TestConfig, temp_name: str) -> list[str]:
    return [
        "--python-version",
        f"{args.major}.{args.minor}",
        "--show-traceback",
        "--warn-incomplete-stub",
        "--show-error-codes",
        "--no-error-summary",
        "--platform",
        args.platform,
        "--no-site-packages",
        "--custom-typeshed-dir",
        str(Path(__file__).parent.parent),
        "--no-implicit-optional",
        "--disallow-untyped-decorators",
        "--disallow-any-generics",
        "--strict-equality",
        "--enable-error-code",
        "ignore-without-code",
        "--config-file",
        temp_name,
    ]


def add_third_party_files(
    distribution: str, files: list[Path], args: TestConfig, configurations: list[MypyDistConf], seen_dists: set[str]
) -> None:
    if distribution in seen_dists:
        return
    seen_dists.add(distribution)

    dependencies = read_dependencies(distribution)
    for dependency in dependencies:
        add_third_party_files(dependency, files, args, configurations, seen_dists)

    root = Path("stubs", distribution)
    for name in os.listdir(root):
        if name.startswith("."):
            continue
        add_files(files, set(), (root / name), args)
        add_configuration(configurations, distribution)


class TestResults(NamedTuple):
    exit_code: int
    files_checked: int


def test_third_party_distribution(distribution: str, args: TestConfig) -> TestResults:
    """Test the stubs of a third-party distribution.

    Return a tuple, where the first element indicates mypy's return code
    and the second element is the number of checked files.
    """

    files: list[Path] = []
    configurations: list[MypyDistConf] = []
    seen_dists: set[str] = set()
    add_third_party_files(distribution, files, args, configurations, seen_dists)

    if not files and args.filter:
        return TestResults(0, 0)

    print(f"testing {distribution} ({len(files)} files)... ", end="")

    if not files:
        print_error("no files found")
        sys.exit(1)

    code = run_mypy(args, configurations, files)
    return TestResults(code, len(files))


def is_probably_stubs_folder(distribution: str, distribution_path: Path) -> bool:
    """Validate that `dist_path` is a folder containing stubs"""
    return distribution != ".mypy_cache" and distribution_path.is_dir()


def test_stdlib(code: int, args: TestConfig) -> TestResults:
    seen = {"builtins", "typing"}  # Always ignore these.
    files: list[Path] = []
    stdlib = Path("stdlib")
    supported_versions = parse_versions(stdlib / "VERSIONS")
    for name in os.listdir(stdlib):
        if name == "VERSIONS" or name.startswith("."):
            continue
        module = Path(name).stem
        if supported_versions[module][0] <= (args.major, args.minor) <= supported_versions[module][1]:
            add_files(files, seen, (stdlib / name), args)

    if files:
        print(f"Testing stdlib ({len(files)} files)...")
        print("Running mypy " + " ".join(get_mypy_flags(args, "/tmp/...")))
        this_code = run_mypy(args, [], files)
        code = max(code, this_code)

    return TestResults(code, len(files))


def test_third_party_stubs(code: int, args: TestConfig) -> TestResults:
    print("Testing third-party packages...")
    print("Running mypy " + " ".join(get_mypy_flags(args, "/tmp/...")))
    files_checked = 0

    for distribution in sorted(os.listdir("stubs")):
        distribution_path = Path("stubs", distribution)

        if not is_probably_stubs_folder(distribution, distribution_path):
            continue

        this_code, checked = test_third_party_distribution(distribution, args)
        code = max(code, this_code)
        files_checked += checked

    return TestResults(code, files_checked)


def test_typeshed(code: int, args: TestConfig) -> TestResults:
    print(f"*** Testing Python {args.major}.{args.minor} on {args.platform}")
    files_checked_this_version = 0
    if "stdlib" in args.directories:
        code, stdlib_files_checked = test_stdlib(code, args)
        files_checked_this_version += stdlib_files_checked
        print()

    if "stubs" in args.directories:
        code, third_party_files_checked = test_third_party_stubs(code, args)
        files_checked_this_version += third_party_files_checked
        print()

    return TestResults(code, files_checked_this_version)


def main() -> None:
    args = parser.parse_args(namespace=CommandLineArgs())
    versions = args.python_version or SUPPORTED_VERSIONS
    platforms = args.platform or [sys.platform]
    tested_directories = frozenset(args.dir) if args.dir else TYPESHED_DIRECTORIES
    code = 0
    total_files_checked = 0
    for (major, minor), platform in product(versions, platforms):
        config = TestConfig(
            verbose=args.verbose,
            exclude=args.exclude,
            major=major,
            minor=minor,
            directories=tested_directories,
            platform=platform,
            filter=args.filter,
        )
        code, files_checked_this_version = test_typeshed(code, args=config)
        total_files_checked += files_checked_this_version
    if code:
        print_error(f"--- exit status {code}, {total_files_checked} files checked ---")
        sys.exit(code)
    if not total_files_checked:
        print_error("--- nothing to do; exit 1 ---")
        sys.exit(1)
    print(colored(f"--- success, {total_files_checked} files checked ---", "green"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("\n\n!!!\nTest aborted due to KeyboardInterrupt\n!!!")
        sys.exit(1)
