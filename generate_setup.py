import argparse
import os
import os.path
import shutil
import tempfile
from textwrap import dedent
from typing import List, Dict, Any, Tuple

import toml

META = "METADATA.toml"

THIRD_PARTY_NAMESPACE = "stubs"
PY2_NAMESPACE = "python2"
SUFFIX = "-stubs"
PY2_SUFFIX = "-python2-stubs"
OUTPUT_DIR = "out"

SETUP_TEMPLATE = dedent("""
from setuptools import setup

name = "types-{distribution}"
description = "Typing stubs for {distribution}"

setup(name=name,
      version="{version}",
      description=description,
      long_description=description,
      url="https://github.com/python/typeshed",
      install_requires={requires},
      packages={packages},
      package_data={package_data},
      classifiers=[
          "Typing :: Typed",
      ]
)
""").lstrip()


def find_stub_files(top: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.endswith(".pyi"):
                result.append(os.path.relpath(os.path.join(root, file), top))
            elif not file.endswith((".md", ".rst")):
                raise ValueError("Only stub files are allowed")
    return result


def read_matadata(file: str) -> Dict[str, Any]:
    with open(file) as f:
        return toml.loads(f.read())


def copy_stubs(distribution: str, dst: str, suffix: str) -> None:
    base_dir = os.path.join(THIRD_PARTY_NAMESPACE, distribution)
    for entry in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                continue
            stub_dir = os.path.join(dst, entry.split(".")[0] + suffix)
            os.mkdir(stub_dir)
            shutil.copy(os.path.join(base_dir, entry), os.path.join(stub_dir, "__init__.pyi"))
        else:
            if entry == PY2_NAMESPACE:
                continue
            else:
                stub_dir = os.path.join(dst, entry + suffix)
                shutil.copytree(os.path.join(base_dir, entry), stub_dir)

        if os.path.isfile(os.path.join(base_dir, META)):
            shutil.copy(os.path.join(base_dir, META), stub_dir)
        else:
            upper_dir = os.path.dirname(base_dir)
            assert os.path.isfile(os.path.join(upper_dir, META))
            shutil.copy(os.path.join(upper_dir, META), stub_dir)


def collect_setup_entries(distribution: str,
                          suffix: str) -> Tuple[List[str], Dict[str, List[str]]]:
    packages = []
    package_data = {}
    base_dir = os.path.join(THIRD_PARTY_NAMESPACE, distribution)
    for entry in os.listdir(base_dir):
        if entry == META:
            continue
        original_entry = entry
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                if not entry.endswith((".md", ".rst")):
                    raise ValueError("Only stub files are allowed")
                continue
            entry = entry.split('.')[0] + suffix
            packages.append(entry)
            package_data[entry] = ["__init__.pyi"]
        else:
            if entry == PY2_NAMESPACE:
                continue
            entry += suffix
            packages.append(entry)
            package_data[entry] = find_stub_files(
                os.path.join(base_dir, original_entry)
            )
        package_data[entry].append(META)
    return packages, package_data


def generate_setup_file(distribution: str, increment: str) -> str:
    base_dir = os.path.join(THIRD_PARTY_NAMESPACE, distribution)
    metadata = read_matadata(os.path.join(base_dir, META))
    packages, package_data = collect_setup_entries(distribution, SUFFIX)
    if PY2_NAMESPACE in os.listdir(os.path.join(THIRD_PARTY_NAMESPACE, distribution)):
        py2_packages, py2_package_data = collect_setup_entries(
            os.path.join(distribution, PY2_NAMESPACE), PY2_SUFFIX
        )
        packages += py2_packages
        package_data.update(py2_package_data)
    return SETUP_TEMPLATE.format(
        distribution=distribution,
        version=f"{metadata['version']}.{increment}",
        requires=metadata.get("requires", []),
        packages=packages,
        package_data=package_data,
    )


def main(distribution: str, increment: str) -> None:
    os.chdir(OUTPUT_DIR)
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, "setup.py"), "w") as f:
        f.write(generate_setup_file(distribution, increment))
    copy_stubs(distribution, tmpdir, SUFFIX)
    if PY2_NAMESPACE in os.listdir(os.path.join(THIRD_PARTY_NAMESPACE, distribution)):
        copy_stubs(os.path.join(distribution, PY2_NAMESPACE), tmpdir, PY2_SUFFIX)
    print(tmpdir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("increment", help="Stub version increment")
    args = parser.parse_args()
    main(args.distribution, args.increment)
