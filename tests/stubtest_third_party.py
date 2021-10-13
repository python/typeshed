#!/usr/bin/env python3
"""Test typeshed's third party stubs using stubtest"""

import argparse
import functools
import subprocess
import sys
import tempfile
import venv
from glob import glob
from pathlib import Path

typeshed_path = Path(__file__).parent.parent
sys.path.append(str(typeshed_path / "src"))

from typeshed_utils import (  # noqa E402
    distribution_modules,
    distribution_path,
    read_metadata,
    supported_python_versions,
    third_party_distributions,
)

EXCLUDE_LIST = [
    "Flask",  # fails when stubtest tries to stringify some object
    "pyaudio",  # install failure locally
    "backports",  # errors on python version
    "six",  # ???
    "aiofiles",  # easily fixable, some platform specific difference between local and ci
    "pycurl",  # install failure, missing libcurl
]


class StubtestFailed(Exception):
    pass


@functools.lru_cache()
def get_mypy_req():
    with open("requirements-tests-py3.txt") as f:
        return next(line.strip() for line in f if "mypy" in line)


def run_stubtest(dist: str) -> None:
    dist_path = distribution_path(typeshed_path, dist)
    metadata = read_metadata(typeshed_path, dist)

    # Ignore stubs that don't support Python 3
    if 3 not in supported_python_versions(typeshed_path, dist):
        return

    with tempfile.TemporaryDirectory() as tmp:
        venv_dir = Path(tmp)
        venv.create(venv_dir, with_pip=True, clear=True)

        pip_exe = str(venv_dir / "bin" / "pip")
        python_exe = str(venv_dir / "bin" / "python")

        dist_req = f"{dist}=={metadata.version}"

        # If @tests/requirements-stubtest.txt exists, run "pip install" on it.
        req_path = dist_path / "@tests" / "requirements-stubtest.txt"
        if req_path.exists():
            try:
                pip_cmd = [pip_exe, "install", "-r", str(req_path)]
                subprocess.run(pip_cmd, check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to install requirements for {dist}", file=sys.stderr)
                print(e.stdout.decode(), file=sys.stderr)
                print(e.stderr.decode(), file=sys.stderr)
                raise

        # We need stubtest to be able to import the package, so install mypy into the venv
        # Hopefully mypy continues to not need too many dependencies
        # TODO: Maybe find a way to cache these in CI
        dists_to_install = [dist_req, get_mypy_req()]
        dists_to_install.extend(metadata.requires)
        pip_cmd = [pip_exe, "install"] + dists_to_install
        print(" ".join(pip_cmd), file=sys.stderr)
        try:
            subprocess.run(pip_cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {dist}", file=sys.stderr)
            print(e.stdout.decode(), file=sys.stderr)
            print(e.stderr.decode(), file=sys.stderr)
            raise

        to_check = [m[0] for m in distribution_modules(typeshed_path, dist)]
        cmd = [
            python_exe,
            "-m",
            "mypy.stubtest",
            # Use --ignore-missing-stub, because if someone makes a correct addition, they'll need to
            # also make a allowlist change and if someone makes an incorrect addition, they'll run into
            # false negatives.
            "--ignore-missing-stub",
            # Use --custom-typeshed-dir in case we make linked changes to stdlib or _typeshed
            "--custom-typeshed-dir",
            str(typeshed_path),
            *to_check,
        ]
        allowlist_path = dist_path / "@tests" / "stubtest_allowlist.txt"
        if allowlist_path.exists():
            cmd.extend(["--allowlist", str(allowlist_path)])

        try:
            print(f"MYPYPATH={dist_path}", " ".join(cmd), file=sys.stderr)
            subprocess.run(cmd, env={"MYPYPATH": str(dist_path), "MYPY_FORCE_COLOR": "1"}, check=True)
        except subprocess.CalledProcessError:
            print(f"stubtest failed for {dist}", file=sys.stderr)
            print("\n\n", file=sys.stderr)
            if not allowlist_path.exists():
                print("Re-running stubtest with --generate-allowlist.\n" f"Add the following to {allowlist_path}:")
                subprocess.run(cmd + ["--generate-allowlist"], env={"MYPYPATH": str(dist_path)})
                print("\n\n")
            raise StubtestFailed from None
        else:
            print(f"stubtest succeeded for {dist}", file=sys.stderr)
        print("\n\n", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-shards", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("dists", metavar="DISTRIBUTION", type=str, nargs=argparse.ZERO_OR_MORE)
    args = parser.parse_args()

    if len(args.dists) == 0:
        dists = third_party_distributions(typeshed_path)
    else:
        dists = args.dists

    for i, dist in enumerate(dists):
        if i % args.num_shards != args.shard_index:
            continue
        if dist in EXCLUDE_LIST:
            continue
        run_stubtest(dist)


if __name__ == "__main__":
    main()
