import ast
import os
import os.path
import shutil

from dataclasses import dataclass
from typing import Optional, List, Set, Tuple

STDLIB_NAMESPACE = "stdlib"
THIRD_PARTY_NAMESPACE = "stubs"
DEFAULT_VERSION = "0.0.1"
DEFAULT_PY3_VERSION = "3.5"
PY2_NAMESPACE = "python2"
OUTPUT_DIR = "out"

MISSING_WHITELIST = {
    "thrift",
}

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


def get_top_imported_names(file: str) -> Set[str]:
    if not file.endswith(".pyi"):
        return set()
    with open(os.path.join(file), "rb") as f:
        content = f.read()
    parsed = ast.parse(content)
    top_imported = set()
    for node in ast.walk(parsed):
        if isinstance(node, ast.Import):
            for name in node.names:
                top_imported.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                continue
            assert node.module
            top_imported.add(node.module.split('.')[0])
    return top_imported


def populate_requirements(package: ThirdPartyPackage,
                          stdlib: List[str], py2_stdlib: List[str],
                          known_distributions: Set[str]) -> None:
    assert not package.requires, "Populate must be called once"
    if not package.is_dir:
        all_top_imports = get_top_imported_names(package.path)
    else:
        all_top_imports = set()
        for dir_path, dir_names, file_names in os.walk(package.path):
            for file_name in file_names:
                all_top_imports |= get_top_imported_names(os.path.join(dir_path, file_name))
    requirements = set()
    for name in all_top_imports:
        distribution = package_to_distribution.get(name, name)
        if package.py3_compatible and name not in stdlib:
            if distribution in known_distributions:
                requirements.add(distribution)
            else:
                # Likely a conditional import.
                assert distribution in py2_stdlib or distribution in MISSING_WHITELIST
        if package.py2_compatible and name not in py2_stdlib:
            if distribution in known_distributions:
                requirements.add(distribution)
            else:
                # Likely a conditional import.
                assert distribution in stdlib or distribution in MISSING_WHITELIST
    current_distribution = package_to_distribution.get(package.name, package.name)
    package.requires = sorted(requirements - {current_distribution})


def generate_versions(packages: List[StdLibPackage]) -> str:
    lines = []
    for package in packages:
        assert package.py_version is not None
        lines.append(f"{package.name}: {package.py_version}")
    return "\n".join(sorted(lines))


def copy_stdlib(packages: List[StdLibPackage], py2_packages: List[StdLibPackage]) -> None:
    stdlib_dir = os.path.join(OUTPUT_DIR, STDLIB_NAMESPACE)
    os.makedirs(stdlib_dir, exist_ok=True)
    with open(os.path.join(stdlib_dir, "VERSIONS"), "w") as f:
        f.write(generate_versions(packages))
        f.write("\n")

    for package in packages:
        if not package.is_dir:
            shutil.copy(package.path, stdlib_dir)
        else:
            shutil.copytree(package.path, os.path.join(stdlib_dir, package.name))

    if py2_packages:
        py2_stdlib_dir = os.path.join(stdlib_dir, PY2_NAMESPACE)
        os.makedirs(py2_stdlib_dir, exist_ok=True)
        for package in py2_packages:
            if not package.is_dir:
                shutil.copy(package.path, py2_stdlib_dir)
            else:
                shutil.copytree(package.path, os.path.join(py2_stdlib_dir, package.name))


def generate_metadata(package: ThirdPartyPackage, py2_packages: List[str]) -> str:
    lines = [f"version = {DEFAULT_VERSION}"]
    if package.py2_compatible or package.name in py2_packages:
        lines.append("python2 = true")
    if not package.py3_compatible:
        lines.append("python3 = false")
    if package.requires:
        lines.append(f"requires = [{', '.join(package.requires)}]")
    return "\n".join(lines)


def copy_third_party(packages: List[ThirdPartyPackage],
                     py2_packages: List[ThirdPartyPackage]) -> None:
    third_party_dir = os.path.join(OUTPUT_DIR, THIRD_PARTY_NAMESPACE)
    os.makedirs(third_party_dir, exist_ok=True)
    for package in packages:
        distribution = package_to_distribution.get(package.name, package.name)
        distribution_dir = os.path.join(third_party_dir, distribution)
        os.makedirs(distribution_dir, exist_ok=True)
        metadate_file = os.path.join(distribution_dir, "METADATA.toml")
        if not os.path.isfile(metadate_file):
            with open(metadate_file, "w") as f:
                f.write(generate_metadata(package, [package.name for package in py2_packages]))
                f.write("\n")
        if not package.is_dir:
            shutil.copy(package.path, distribution_dir)
        else:
            shutil.copytree(package.path, os.path.join(distribution_dir, package.name))

    for package in py2_packages:
        distribution = package_to_distribution.get(package.name, package.name)
        distribution_dir = os.path.join(third_party_dir, distribution, PY2_NAMESPACE)
        os.makedirs(distribution_dir, exist_ok=True)
        if not package.is_dir:
            shutil.copy(package.path, distribution_dir)
        else:
            shutil.copytree(package.path, os.path.join(distribution_dir, package.name))


def main() -> None:
    stdlib, py2_stdlib = collect_stdlib_packages()
    third_party, py2_third_party = collect_third_party_packages()

    stdlib_names = [package.name for package in stdlib]
    py2_stdlib_names = [package.name for package in py2_stdlib]
    py2_stdlib_names += [package.name for package in stdlib if package.py_version == "2.7"]

    known_distributions = {package_to_distribution.get(package.name, package.name)
                           for package in third_party + py2_third_party}

    for package in third_party + py2_third_party:
        populate_requirements(package, stdlib_names, py2_stdlib_names, known_distributions)

    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    copy_stdlib(stdlib, py2_stdlib)
    copy_third_party(third_party, py2_third_party)


if __name__ == "__main__":
    main()
