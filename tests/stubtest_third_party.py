#!/usr/bin/env python3
"""Test typeshed's third party stubs using stubtest"""

import subprocess
import sys
import tempfile
import toml
import venv
from pathlib import Path


EXCLUDE_LIST = ["Flask", "pyaudio", "backports", "pkg_resources", "six", "aiofiles"]


class StubtestFailed(Exception):
    pass


def run_stubtest(dist: Path) -> None:
    with open(dist / "METADATA.toml") as f:
        metadata = dict(toml.loads(f.read()))

    # Ignore stubs that don't support Python 2
    if not bool(metadata.get("python3", True)):
        return

    with tempfile.TemporaryDirectory() as tmp:
        venv_dir = Path(tmp)
        venv.create(venv_dir, with_pip=True, clear=True)

        pip_exe = str(venv_dir / "bin" / "pip")
        python_exe = str(venv_dir / "bin" / "python")

        # We need stubtest to be able to import the package, so install mypy into the venv
        # Hopefully mypy continues to not need too many dependencies
        # TODO: Pick package version based on metadata.get("version")
        # TODO: Maybe find a way to cache these in CI
        dists_to_install = [dist.name, "mypy==0.901"]
        dists_to_install.extend(metadata.get("requires", []))
        pip_cmd = [pip_exe, "install"] + dists_to_install
        print(" ".join(pip_cmd))
        subprocess.run(pip_cmd, check=True, capture_output=True)

        packages_to_check = [d.name for d in dist.iterdir() if d.is_dir() and d.name.isidentifier()]
        modules_to_check = [d.stem for d in dist.iterdir() if d.is_file() and d.suffix == ".pyi"]
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
            str(dist.parent.parent),
            *packages_to_check,
            *modules_to_check,
        ]
        allowlist_path = dist / "@tests/stubtest_allowlist.txt"
        if allowlist_path.exists():
            cmd.extend(["--allowlist", str(allowlist_path)])

        try:
            print(f"MYPYPATH={dist}", " ".join(cmd), file=sys.stderr)
            subprocess.run(cmd, env={"MYPYPATH": str(dist), "MYPY_FORCE_COLOR": "1"}, check=True)
        except subprocess.CalledProcessError:
            print(f"stubtest failed for {dist.name}", file=sys.stderr)
            if not allowlist_path.exists():
                print(
                    f"Consider using --generate-allowlist to add an allowlist at {allowlist_path}",
                    file=sys.stderr,
                )
            raise StubtestFailed from None
        else:
            print(f"stubtest succeeded for {dist.name}", file=sys.stderr)


def check_stubs(typeshed_dir: Path):
    # TODO: parallelise (maybe shard across multiple GA jobs)
    dists = sorted((typeshed_dir / "stubs").iterdir())
    for dist in dists:
        if dist.name in EXCLUDE_LIST:
            continue
        run_stubtest(dist)


if __name__ == "__main__":
    sys.exit(check_stubs(typeshed_dir=Path(".")))
