import os.path

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


def collect_stdlib_packages() -> Tuple[List[StdLibPackage], List[StdLibPackage]]:
    return [], []


def collect_third_party_packages() -> Tuple[List[ThirdPartyPackage], List[ThirdPartyPackage]]:
    return [], []


def populate_requirements(package: ThirdPartyPackage, stdlib: List[str], py2_stdlib: List[str]) -> None:
    pass


def copy_stdlib(packages: List[StdLibPackage], py2_packages: List[StdLibPackage]) -> None:
    pass


def copy_third_party(packages: List[ThirdPartyPackage], py2_packages: List[ThirdPartyPackage]) -> None:
    pass


def main() -> None:
    stdlib, py2_stdlib = collect_stdlib_packages()
    third_party, py2_third_party = collect_third_party_packages()

    stdlib_names = [package.name for package in stdlib]
    py2_stdlib_names = [package.name for package in py2_stdlib]
    py2_stdlib_names += [package.name for package in stdlib if package.py_version == "2.7"]

    for package in third_party + py2_third_party:
        populate_requirements(package, stdlib_names, py2_stdlib_names)

    copy_stdlib(stdlib, py2_stdlib)
    copy_third_party(third_party, py2_third_party)


if __name__ == "__main__":
    main()
