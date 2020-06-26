import argparse
import os
import os.path
import shutil
import tempfile
from textwrap import dedent
from typing import List, Dict, Any

import toml

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
""")


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


def copy_stubs(distribution: str, dst: str) -> None:
    base_dir = os.path.join("stubs", distribution)
    for entry in os.listdir(base_dir):
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                continue
            stub_dir = os.path.join(dst, entry.split(".")[0] + "-stubs")
            os.mkdir(stub_dir)
            shutil.copy(os.path.join(base_dir, entry), os.path.join(stub_dir, "__init__.pyi"))
        else:
            stub_dir = os.path.join(dst, entry + "-stubs")
            shutil.copytree(os.path.join(base_dir, entry), stub_dir)
        shutil.copy(os.path.join(base_dir, "METADATA.toml"), stub_dir)


def generate_setup_file(distribution: str, increment: str) -> str:
    base_dir = os.path.join("stubs", distribution)
    metadata = read_matadata(os.path.join(base_dir, "METADATA.toml"))
    packages = []
    package_data = {}
    for entry in os.listdir(base_dir):
        if entry == "METADATA.toml":
            continue
        original_entry = entry
        if os.path.isfile(os.path.join(base_dir, entry)):
            if not entry.endswith(".pyi"):
                if not entry.endswith((".md", ".rst")):
                    raise ValueError("Only stub files are allowed")
                continue
            entry = entry.split('.')[0] + "-stubs"
            packages.append(entry)
            package_data[entry] = ["__init__.pyi"]
        else:
            entry += "-stubs"
            packages.append(entry)
            package_data[entry] = find_stub_files(
                os.path.join(base_dir, original_entry)
            )
        package_data[entry].append("METADATA.toml")
    return SETUP_TEMPLATE.format(
        distribution=distribution,
        version=f"{metadata['version']}.{increment}",
        requires=metadata.get("requires", []),
        packages=packages,
        package_data=package_data,
    )


def main(distribution: str, increment: str) -> None:
    os.chdir("out")
    tmpdir = tempfile.mkdtemp()
    print(tmpdir)
    with open(os.path.join(tmpdir, "setup.py"), "w") as f:
        f.write(generate_setup_file(distribution, increment))
    copy_stubs(distribution, tmpdir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("distribution", help="Third-party distribution to build")
    parser.add_argument("increment", help="Stub version increment")
    args = parser.parse_args()
    main(args.distribution, args.increment)
