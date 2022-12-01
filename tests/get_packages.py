#!/usr/bin/env python3
import os
import sys

import tomli
from utils import METADATA_MAPPING


def main() -> None:
    platform = sys.platform
    distributions = sys.argv[1:]
    if not distributions:
        distributions = os.listdir("stubs")

    if platform in METADATA_MAPPING:
        for distribution in distributions:
            with open(f"stubs/{distribution}/METADATA.toml", "rb") as file:
                for package in tomli.load(file).get("tool", {}).get("stubtest", {}).get(METADATA_MAPPING[platform], []):
                    print(package)


if __name__ == "__main__":
    main()
