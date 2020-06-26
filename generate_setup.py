import argparse
import os
import os.path
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
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
            elif not file.endswith((".md", ".rst")):
                raise ValueError("Only stub files are allowed")
    return result


def read_matadata(file: str) -> Dict[str, Any]:
    with open(file) as f:
        return toml.loads(f.read())


def main(distribution: str) -> None:
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "distribution", help="Third-party distribution to build"
    )
    args = parser.parse_args()
    main(args.distribution)
