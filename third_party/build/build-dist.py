#!/usr/bin/env python3

# Build a stubs-only distribution for a third-party package.
#
# Usage: python3.7 build-dist.py <PACKAGE>
#
# The resulting wheel will be saved in third-party/build/dist.

import datetime
import os
import re
import shutil
import subprocess
import sys

try:
    from dataclasses import dataclass
    from pathlib import Path
    from typing import List
except ImportError:
    print("This script requires Python 3.7 or higher.", file=sys.stderr)
    sys.exit(1)

DIST_PREFIX = "types-"
MIN_PYTHON3_VERSION = (3, 4)
MAX_PYTHON3_VERSION = (3, 7)
EXCLUDED_PYTHON_VERSIONS = [(3, i) for i in range(MIN_PYTHON3_VERSION[1])]
TROVE_PREFIX = "Classifier: Programming Language :: Python :: "

pkg_version = "0." + datetime.datetime.now().strftime("%Y%m%d.%H%M")
py_version_re = re.compile(r"^(2and3|\d+(\.\d+)?)$")

base_dir = Path(__file__).parent
root_dir = base_dir.parent.parent
build_dir = base_dir / "build"
dist_dir = base_dir / "dist"


@dataclass
class PackageInfo:
    path: Path
    name: str
    py_version: str
    is_module: bool

    @property
    def stub_name(self) -> str:
        return f"{self.name}-stubs"


def py_version_to_wheel_tags(version: str) -> List[str]:
    if version == "2and3":
        return ["py2-none-any", "py3-none-any"]
    else:
        return [f"py{version}-none-any"]


def py_version_to_requires(version: str) -> str:
    if version == "2":
        return ">= 2.7, < 3"
    elif version == "2and3":
        formatted = [f"!= {ma}.{mi}.*" for ma, mi in EXCLUDED_PYTHON_VERSIONS]
        return ">= 2.7, " + ", ".join(formatted)
    elif version == "3":
        return f">= {MIN_PYTHON3_VERSION[0]}.{MIN_PYTHON3_VERSION[1]}"
    else:
        return ">= " + version


def py_version_to_trove(version: str) -> List[str]:
    py2_versions = ["2", "2.7"]
    if version == "2":
        versions = py2_versions + ["2 :: Only"]
    elif version == "2and3":
        versions = py2_versions + py3_versions()
    elif version == "3":
        versions = py3_versions() + ["3 :: Only"]
    else:
        versions = py3_versions(int(version[2:])) + ["3 :: Only"]
    return [TROVE_PREFIX + v for v in versions]


def py3_versions(min_v: int = MIN_PYTHON3_VERSION[1]) -> List[str]:
    assert min_v <= MAX_PYTHON3_VERSION[1]
    r = range(min_v, MAX_PYTHON3_VERSION[1] + 1)
    return ["3"] + [f"3.{i}" for i in r]


def parse_args() -> str:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} PACKAGE", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1]


def find_package(name: str) -> PackageInfo:
    for dir_ in base_dir.parent.iterdir():
        if not py_version_re.match(dir_.name):
            continue
        pkg_path = dir_ / name
        mod_path = dir_ / f"{name}.pyi"
        if pkg_path.is_dir():
            return PackageInfo(pkg_path, name, dir_.name, is_module=False)
        elif mod_path.is_file():
            return PackageInfo(mod_path, name, dir_.name, is_module=True)
    print(f"Stubs for package '{name}' not found", file=sys.stderr)
    sys.exit(1)


def build_distribution(package: PackageInfo) -> None:
    prepare_build_dir(package)
    pack_wheel(package)


def prepare_build_dir(package: PackageInfo) -> None:
    shutil.rmtree(build_dir, ignore_errors=True)
    copy_package(package)
    pkg = (DIST_PREFIX + package.name).replace("-", "_")
    dist_info_dir = build_dir / f"{pkg}-{pkg_version}.dist-info"
    os.mkdir(dist_info_dir)
    shutil.copy(root_dir / "LICENSE", dist_info_dir)
    create_wheel_file(package, base_dir / "WHEEL.tmpl",
                      dist_info_dir / "WHEEL")
    create_metadata(package, base_dir / "METADATA.tmpl",
                    dist_info_dir / "METADATA")


def copy_package(package: PackageInfo) -> None:
    dest_dir = build_dir / package.stub_name
    if package.is_module:
        os.makedirs(dest_dir)
        shutil.copyfile(package.path, dest_dir / "__init__.pyi")
    else:
        shutil.copytree(package.path, dest_dir)


def create_wheel_file(package: PackageInfo, src: Path, dest: Path) -> None:
    with open(dest, "w") as f:
        with open(src, "r") as src_f:
            for line in src_f:
                f.write(line)
        for tag in py_version_to_wheel_tags(package.py_version):
            f.write(f"Tag: {tag}\n")


def create_metadata(package: PackageInfo, src: Path, dest: Path) -> None:
    py_requires = py_version_to_requires(package.py_version)
    with open(dest, "w") as f:
        with open(src, "r") as src_f:
            for line in src_f:
                if line.startswith("$TROVE_PY$"):
                    for trove in py_version_to_trove(package.py_version):
                        f.write(f"Classifier: {trove}\n")
                else:
                    line = line.replace("$PACKAGE$", package.name)
                    line = line.replace("$VERSION$", pkg_version)
                    line = line.replace("$PY_REQUIRES$", py_requires)
                    f.write(line)


def pack_wheel(package: PackageInfo) -> None:
    os.makedirs(dist_dir, exist_ok=True)
    subprocess.run(["wheel", "pack", str(build_dir),
                    "--dest-dir", str(dist_dir)])


def main() -> None:
    package_name = parse_args()
    package = find_package(package_name)
    build_distribution(package)


if __name__ == "__main__":
    main()
