import os
import os.path
import shutil

from dataclasses import dataclass
from typing import Optional, List, Tuple

STDLIB_NAMESPACE = "stdlib"
THIRD_PARTY_NAMESPACE = "stubs"
DEFAULT_VERSION = "0.0.1"
DEFAULT_PY3_VERSION = "3.5"
PY2_NAMESPACE = "python2"
OUTPUT_DIR = "out"

# Manually collected special cases.
package_to_distribution = {
    "_pytest": "pytest",
    "yaml": "PyYAML",
    "typing_extensions": "typing-extensions",
    "mypy_extensions": "mypy-extensions"
}


class PackageBase:
    path: str
    is_dir: bool

    @property
    def name(self) -> str:
        _, tail = os.path.split(self.path)
        if self.is_dir:
            assert not tail.endswith(".pyi")
            return tail
        assert tail.endswith(".pyi")
        name, _ = os.path.splitext(tail)
        return name


@dataclass
class StdLibPackage(PackageBase):
    path: str
    py_version: Optional[str]
    is_dir: bool


@dataclass
class ThirdPartyPackage(PackageBase):
    path: str
    py2_compatible: bool
    py3_compatible: bool
    is_dir: bool
    requires: List[str]  # distributions it depends on


def add_stdlib_packages_from(subdir: str, packages: List[StdLibPackage],
                             py_version: Optional[str]) -> None:
    for name in os.listdir(subdir):
        path = os.path.join(subdir, name)
        packages.append(StdLibPackage(path, py_version, is_dir=os.path.isdir(path)))


def collect_stdlib_packages() -> Tuple[List[StdLibPackage], List[StdLibPackage]]:
    stdlib = []
    py2_stdlib = []
    add_stdlib_packages_from("stdlib/2", py2_stdlib, None)
    add_stdlib_packages_from("stdlib/2and3", stdlib, "2.7")
    add_stdlib_packages_from("stdlib/3", stdlib, DEFAULT_PY3_VERSION)
    for version in ("3.6", "3.7", "3.8", "3.9"):
        subdir = os.path.join("stdlib", version)
        if os.path.isdir(subdir):
            add_stdlib_packages_from(subdir, stdlib, version)
    return stdlib, py2_stdlib


def add_third_party_packages_from(subdir: str, packages: List[ThirdPartyPackage],
                                  py2_compatible: bool, py3_compatible: bool) -> None:
    for name in os.listdir(subdir):
        path = os.path.join(subdir, name)
        packages.append(ThirdPartyPackage(path, py2_compatible, py3_compatible,
                                          requires=[], is_dir=os.path.isdir(path)))


def collect_third_party_packages() -> Tuple[List[ThirdPartyPackage], List[ThirdPartyPackage]]:
    third_party = []
    py2_third_party = []
    add_third_party_packages_from("third_party/3", third_party,
                                  py2_compatible=False, py3_compatible=True)
    add_third_party_packages_from("third_party/2and3", third_party,
                                  py2_compatible=True, py3_compatible=True)
    # Special case for third party packages like six.
    subdir = "third_party/2"
    py3_packages = os.listdir("third_party/3")
    for name in os.listdir(subdir):
        path = os.path.join(subdir, name)
        package = ThirdPartyPackage(path, py2_compatible=True, py3_compatible=False,
                                    requires=[], is_dir=os.path.isdir(path))
        if name in py3_packages:
            py2_third_party.append(package)
        else:
            third_party.append(package)
    return third_party, py2_third_party


def populate_requirements(package: ThirdPartyPackage,
                          stdlib: List[str], py2_stdlib: List[str]) -> None:
    pass


def generate_versions(packages: List[StdLibPackage]) -> str:
    lines = []
    for package in packages:
        assert package.py_version is not None
        lines.append(f"{package.name}: {package.py_version}")
    return "\n".join(lines)


def copy_stdlib(packages: List[StdLibPackage], py2_packages: List[StdLibPackage]) -> None:
    stdlib_dir = os.path.join(OUTPUT_DIR, STDLIB_NAMESPACE)
    os.makedirs(stdlib_dir, exist_ok=True)
    with open(os.path.join(stdlib_dir, "VERSIONS")) as f:
        f.write(generate_versions(packages))
        f.write("\n")

    for package in packages:
        if package.is_dir:
            shutil.copy(package.path, stdlib_dir)
        else:
            shutil.copytree(package.path, stdlib_dir)

    if py2_packages:
        py2_stdlib_dir = os.path.join(stdlib_dir, PY2_NAMESPACE)
        os.makedirs(py2_stdlib_dir, exist_ok=True)
        for package in py2_packages:
            if package.is_dir:
                shutil.copy(package.path, py2_stdlib_dir)
            else:
                shutil.copytree(package.path, py2_stdlib_dir)


def copy_third_party(packages: List[ThirdPartyPackage],
                     py2_packages: List[ThirdPartyPackage]) -> None:
    pass


def main() -> None:
    stdlib, py2_stdlib = collect_stdlib_packages()
    third_party, py2_third_party = collect_third_party_packages()

    stdlib_names = [package.name for package in stdlib]
    py2_stdlib_names = [package.name for package in py2_stdlib]
    py2_stdlib_names += [package.name for package in stdlib if package.py_version == "2.7"]

    for package in third_party + py2_third_party:
        populate_requirements(package, stdlib_names, py2_stdlib_names)

    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    copy_stdlib(stdlib, py2_stdlib)
    copy_third_party(third_party, py2_third_party)


if __name__ == "__main__":
    main()
