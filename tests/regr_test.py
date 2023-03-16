#!/usr/bin/env python3
"""Run mypy on the test cases for the stdlib and third-party stubs."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from enum import IntEnum
from itertools import product
from pathlib import Path
from typing_extensions import TypeAlias

from parse_metadata import get_recursive_requirements
from utils import (
    PackageInfo,
    VenvInfo,
    colored,
    get_all_testcase_directories,
    get_mypy_req,
    make_venv,
    print_error,
    print_success_msg,
    testcase_dir_from_package_name,
)

ReturnCode: TypeAlias = int

TEST_CASES = "test_cases"
VENV_DIR = ".venv"
TYPESHED = "typeshed"

SUPPORTED_PLATFORMS = ["linux", "darwin", "win32"]
SUPPORTED_VERSIONS = ["3.11", "3.10", "3.9", "3.8", "3.7"]


def package_with_test_cases(package_name: str) -> PackageInfo:
    """Helper function for argument-parsing"""

    if package_name == "stdlib":
        return PackageInfo("stdlib", Path(TEST_CASES))
    test_case_dir = testcase_dir_from_package_name(package_name)
    if test_case_dir.is_dir():
        if not os.listdir(test_case_dir):
            raise argparse.ArgumentTypeError(f"{package_name!r} has a 'test_cases' directory but it is empty!")
        return PackageInfo(package_name, test_case_dir)
    raise argparse.ArgumentTypeError(f"No test cases found for {package_name!r}!")


class Verbosity(IntEnum):
    QUIET = 0
    NORMAL = 1
    VERBOSE = 2


parser = argparse.ArgumentParser(description="Script to run mypy against various test cases for typeshed's stubs")
parser.add_argument(
    "packages_to_test",
    type=package_with_test_cases,
    nargs="*",
    action="extend",
    help="Test only these packages (defaults to all typeshed stubs that have test cases)",
)
parser.add_argument(
    "--all",
    action="store_true",
    help=(
        'Run tests on all available platforms and versions (defaults to "False"). '
        "Note that this cannot be specified if --platform and/or --python-version are specified."
    ),
)
parser.add_argument(
    "--verbosity",
    choices=[member.name for member in Verbosity],
    default=Verbosity.NORMAL.name,
    help="Control how much output to print to the terminal",
)
parser.add_argument(
    "--platform",
    dest="platforms_to_test",
    choices=SUPPORTED_PLATFORMS,
    nargs="*",
    action="extend",
    help=(
        "Run mypy for certain OS platforms (defaults to sys.platform). "
        "Note that this cannot be specified if --all is also specified."
    ),
)
parser.add_argument(
    "-p",
    "--python-version",
    dest="versions_to_test",
    choices=SUPPORTED_VERSIONS,
    nargs="*",
    action="extend",
    help=(
        "Run mypy for certain Python versions (defaults to sys.version_info[:2]). "
        "Note that this cannot be specified if --all is also specified."
    ),
)


def verbose_log(msg: str) -> None:
    print(colored("\n" + msg, "blue"))


def setup_testcase_dir(package: PackageInfo, tempdir: Path, new_test_case_dir: Path, verbosity: Verbosity) -> None:
    if verbosity is verbosity.VERBOSE:
        verbose_log(f"Setting up testcase dir in {tempdir}")
    # --warn-unused-ignores doesn't work for files inside typeshed.
    # SO, to work around this, we copy the test_cases directory into a TemporaryDirectory,
    # and run the test cases inside of that.
    shutil.copytree(package.test_case_directory, new_test_case_dir)
    if package.is_stdlib:
        return

    # HACK: we want to run these test cases in an isolated environment --
    # we want mypy to see all stub packages listed in the "requires" field of METADATA.toml
    # (and all stub packages required by those stub packages, etc. etc.),
    # but none of the other stubs in typeshed.
    #
    # The best way of doing that without stopping --warn-unused-ignore from working
    # seems to be to create a "new typeshed" directory in a tempdir
    # that has only the required stubs copied over.
    new_typeshed = tempdir / TYPESHED
    new_typeshed.mkdir()
    shutil.copytree(Path("stdlib"), new_typeshed / "stdlib")
    requirements = get_recursive_requirements(package.name)
    # mypy refuses to consider a directory a "valid typeshed directory"
    # unless there's a stubs/mypy-extensions path inside it,
    # so add that to the list of stubs to copy over to the new directory
    for requirement in {package.name, *requirements.typeshed_pkgs, "mypy-extensions"}:
        shutil.copytree(Path("stubs", requirement), new_typeshed / "stubs" / requirement)

    if requirements.external_pkgs:
        if verbosity is Verbosity.VERBOSE:
            verbose_log(f"Setting up venv in {tempdir / VENV_DIR}")
        pip_exe = make_venv(tempdir / VENV_DIR).pip_exe
        pip_command = [pip_exe, "install", get_mypy_req(), *requirements.external_pkgs]
        if verbosity is Verbosity.VERBOSE:
            verbose_log(f"{pip_command=}")
        try:
            subprocess.run(pip_command, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            raise


def run_testcases(
    package: PackageInfo, version: str, platform: str, *, tempdir: Path, verbosity: Verbosity
) -> subprocess.CompletedProcess[str]:
    env_vars = dict(os.environ)
    new_test_case_dir = tempdir / TEST_CASES
    testcasedir_already_setup = new_test_case_dir.exists() and new_test_case_dir.is_dir()

    if not testcasedir_already_setup:
        setup_testcase_dir(package, tempdir=tempdir, new_test_case_dir=new_test_case_dir, verbosity=verbosity)

    # "--enable-error-code ignore-without-code" is purposefully omitted.
    # See https://github.com/python/typeshed/pull/8083
    flags = [
        "--python-version",
        version,
        "--show-traceback",
        "--no-error-summary",
        "--platform",
        platform,
        "--strict",
        "--pretty",
    ]

    if package.is_stdlib:
        python_exe = sys.executable
        custom_typeshed = Path(__file__).parent.parent
        flags.append("--no-site-packages")
    else:
        custom_typeshed = tempdir / TYPESHED
        env_vars["MYPYPATH"] = os.pathsep.join(map(str, custom_typeshed.glob("stubs/*")))
        has_non_types_dependencies = (tempdir / VENV_DIR).exists()
        if has_non_types_dependencies:
            python_exe = VenvInfo.of_existing_venv(tempdir / VENV_DIR).python_exe
        else:
            python_exe = sys.executable
            flags.append("--no-site-packages")

    flags.extend(["--custom-typeshed-dir", str(custom_typeshed)])

    # If the test-case filename ends with -py39,
    # only run the test if --python-version was set to 3.9 or higher (for example)
    for path in new_test_case_dir.rglob("*.py"):
        if match := re.fullmatch(r".*-py3(\d{1,2})", path.stem):
            minor_version_required = int(match[1])
            assert f"3.{minor_version_required}" in SUPPORTED_VERSIONS
            python_minor_version = int(version.split(".")[1])
            if minor_version_required > python_minor_version:
                continue
        flags.append(str(path))

    mypy_command = [python_exe, "-m", "mypy"] + flags
    if verbosity is Verbosity.VERBOSE:
        verbose_log(f"{mypy_command=}")
        if "MYPYPATH" in env_vars:
            verbose_log(f"{env_vars['MYPYPATH']=}")
        else:
            verbose_log("MYPYPATH not set")
    return subprocess.run(mypy_command, capture_output=True, text=True, env=env_vars)


def test_testcase_directory(
    package: PackageInfo, version: str, platform: str, *, verbosity: Verbosity, tempdir: Path
) -> ReturnCode:
    msg = f"Running mypy --platform {platform} --python-version {version} on the "
    msg += "standard library test cases..." if package.is_stdlib else f"test cases for {package.name!r}..."
    if verbosity > Verbosity.QUIET:
        print(msg, end=" ", flush=True)

    result = run_testcases(package=package, version=version, platform=platform, tempdir=tempdir, verbosity=verbosity)

    if result.returncode:
        if verbosity is Verbosity.QUIET:
            # We'll already have printed this if --verbosity QUIET wasn't passed.
            # If --verbosity QUIET was passed, only print this if there were errors.
            # If there are errors, the output is inscrutable if this isn't printed.
            print(msg, end=" ")
        print_error("failure\n")
        replacements = (str(tempdir / TEST_CASES), str(package.test_case_directory))
        if result.stderr:
            print_error(result.stderr, fix_path=replacements)
        if result.stdout:
            print_error(result.stdout, fix_path=replacements)
    elif verbosity > Verbosity.QUIET:
        print_success_msg()
    return result.returncode


def main() -> ReturnCode:
    args = parser.parse_args()

    testcase_directories = args.packages_to_test or get_all_testcase_directories()
    verbosity = Verbosity[args.verbosity]
    if args.all:
        if args.platforms_to_test:
            parser.error("Cannot specify both --platform and --all")
        if args.versions_to_test:
            parser.error("Cannot specify both --python-version and --all")
        platforms_to_test, versions_to_test = SUPPORTED_PLATFORMS, SUPPORTED_VERSIONS
    else:
        platforms_to_test = args.platforms_to_test or [sys.platform]
        versions_to_test = args.versions_to_test or [f"3.{sys.version_info[1]}"]

    code = 0
    for testcase_dir in testcase_directories:
        with tempfile.TemporaryDirectory() as td:
            tempdir = Path(td)
            for platform, version in product(platforms_to_test, versions_to_test):
                this_code = test_testcase_directory(testcase_dir, version, platform, verbosity=verbosity, tempdir=tempdir)
                code = max(code, this_code)
    if code:
        print_error("\nTest completed with errors")
    else:
        print(colored("\nTest completed successfully!", "green"))

    return code


if __name__ == "__main__":
    try:
        code = main()
    except KeyboardInterrupt:
        print_error("Test aborted due to KeyboardInterrupt!")
        code = 1
    raise SystemExit(code)
