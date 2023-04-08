#!/usr/bin/env python3
"""Test typeshed's third party stubs using stubtest"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NoReturn

from parse_metadata import get_recursive_requirements, read_metadata
from utils import colored, get_mypy_req, make_venv, print_error, print_success_msg


def run_stubtest(dist: Path, *, verbose: bool = False, specified_platforms_only: bool = False) -> bool:
    dist_name = dist.name
    metadata = read_metadata(dist_name)
    print(f"{dist_name}... ", end="")

    stubtest_settings = metadata.stubtest_settings
    if stubtest_settings.skipped:
        print(colored("skipping", "yellow"))
        return True

    if sys.platform not in stubtest_settings.platforms:
        if specified_platforms_only:
            print(colored("skipping (platform not specified in METADATA.toml)", "yellow"))
            return True
        print(colored(f"Note: {dist_name} is not currently tested on {sys.platform} in typeshed's CI.", "yellow"))

    with tempfile.TemporaryDirectory() as tmp:
        venv_dir = Path(tmp)
        try:
            pip_exe, python_exe = make_venv(venv_dir)
        except Exception:
            print_error("fail")
            raise
        dist_extras = ", ".join(stubtest_settings.extras)
        dist_req = f"{dist_name}[{dist_extras}]=={metadata.version}"

        # If tool.stubtest.stubtest_requirements exists, run "pip install" on it.
        if stubtest_settings.stubtest_requirements:
            pip_cmd = [pip_exe, "install"] + stubtest_settings.stubtest_requirements
            try:
                subprocess.run(pip_cmd, check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print_command_failure("Failed to install requirements", e)
                return False

        requirements = get_recursive_requirements(dist_name)

        # We need stubtest to be able to import the package, so install mypy into the venv
        # Hopefully mypy continues to not need too many dependencies
        # TODO: Maybe find a way to cache these in CI
        dists_to_install = [dist_req, get_mypy_req()]
        dists_to_install.extend(requirements.external_pkgs)  # Internal requirements are added to MYPYPATH
        pip_cmd = [pip_exe, "install"] + dists_to_install
        try:
            subprocess.run(pip_cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print_command_failure("Failed to install", e)
            return False

        ignore_missing_stub = ["--ignore-missing-stub"] if stubtest_settings.ignore_missing_stub else []
        packages_to_check = [d.name for d in dist.iterdir() if d.is_dir() and d.name.isidentifier()]
        modules_to_check = [d.stem for d in dist.iterdir() if d.is_file() and d.suffix == ".pyi"]
        stubtest_cmd = [
            python_exe,
            "-m",
            "mypy.stubtest",
            # Use --custom-typeshed-dir in case we make linked changes to stdlib or _typeshed
            "--custom-typeshed-dir",
            str(dist.parent.parent),
            *ignore_missing_stub,
            *packages_to_check,
            *modules_to_check,
        ]

        stubs_dir = dist.parent
        mypypath_items = [str(dist)] + [str(stubs_dir / pkg) for pkg in requirements.typeshed_pkgs]
        mypypath = os.pathsep.join(mypypath_items)
        # For packages that need a display, we need to pass at least $DISPLAY
        # to stubtest. $DISPLAY is set by xvfb-run in CI.
        #
        # It seems that some other environment variables are needed too,
        # because the CI fails if we pass only os.environ["DISPLAY"]. I didn't
        # "bisect" to see which variables are actually needed.
        stubtest_env = os.environ | {"MYPYPATH": mypypath, "MYPY_FORCE_COLOR": "1"}

        allowlist_path = dist / "@tests/stubtest_allowlist.txt"
        if allowlist_path.exists():
            stubtest_cmd.extend(["--allowlist", str(allowlist_path)])
        platform_allowlist = dist / f"@tests/stubtest_allowlist_{sys.platform}.txt"
        if platform_allowlist.exists():
            stubtest_cmd.extend(["--allowlist", str(platform_allowlist)])

        try:
            subprocess.run(stubtest_cmd, env=stubtest_env, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print_error("fail")
            print_commands(dist, pip_cmd, stubtest_cmd, mypypath)
            print_command_output(e)

            print("Ran with the following environment:", file=sys.stderr)
            ret = subprocess.run([pip_exe, "freeze", "--all"], capture_output=True)
            print_command_output(ret)

            if allowlist_path.exists():
                print(
                    f'To fix "unused allowlist" errors, remove the corresponding entries from {allowlist_path}', file=sys.stderr
                )
                print(file=sys.stderr)
            else:
                print(f"Re-running stubtest with --generate-allowlist.\nAdd the following to {allowlist_path}:", file=sys.stderr)
                ret = subprocess.run(stubtest_cmd + ["--generate-allowlist"], env=stubtest_env, capture_output=True)
                print_command_output(ret)

            return False
        else:
            print_success_msg()

    if verbose:
        print_commands(dist, pip_cmd, stubtest_cmd, mypypath)

    return True


def print_commands(dist: Path, pip_cmd: list[str], stubtest_cmd: list[str], mypypath: str) -> None:
    print(file=sys.stderr)
    print(" ".join(pip_cmd), file=sys.stderr)
    print(f"MYPYPATH={mypypath}", " ".join(stubtest_cmd), file=sys.stderr)
    print(file=sys.stderr)


def print_command_failure(message: str, e: subprocess.CalledProcessError) -> None:
    print_error("fail")
    print(file=sys.stderr)
    print(message, file=sys.stderr)
    print_command_output(e)


def print_command_output(e: subprocess.CalledProcessError | subprocess.CompletedProcess[bytes]) -> None:
    print(e.stdout.decode(), end="", file=sys.stderr)
    print(e.stderr.decode(), end="", file=sys.stderr)
    print(file=sys.stderr)


def main() -> NoReturn:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument(
        "--specified-platforms-only",
        action="store_true",
        help="skip the test if the current platform is not specified in METADATA.toml/tool.stubtest.platforms",
    )
    parser.add_argument("dists", metavar="DISTRIBUTION", type=str, nargs=argparse.ZERO_OR_MORE)
    args = parser.parse_args()

    typeshed_dir = Path(".").resolve()
    if len(args.dists) == 0:
        dists = sorted((typeshed_dir / "stubs").iterdir())
    else:
        dists = [typeshed_dir / "stubs" / d for d in args.dists]

    result = 0
    for i, dist in enumerate(dists):
        if i % args.num_shards != args.shard_index:
            continue
        if not run_stubtest(dist, verbose=args.verbose, specified_platforms_only=args.specified_platforms_only):
            result = 1
    sys.exit(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
