#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Generator, Iterable

import tomli


def install(distributions: Iterable[str] | None = None) -> None:
    dependencies = " ".join(get(distributions))
    print("install:", distributions, dependencies)
    subprocess.run(["pip", "install", dependencies], capture_output=True)


def get(distributions: Iterable[str] | None = None) -> Generator[str, None, None]:
    if not distributions:
        distributions = os.listdir("stubs")

    for distribution in distributions:
        with open(f"stubs/{distribution}/METADATA.toml", "rb") as file:
            for package in tomli.load(file).get("external_requires", []):
                yield package


if __name__ == "__main__":
    # print("main", sys.argv[1:])
    # install(sys.argv[1:])
    for dependency in get(sys.argv[1:]):
        print(dependency)
