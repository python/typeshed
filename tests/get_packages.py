#!/usr/bin/env python3
import os
import sys

import tomli
from utils import metadata_mapping

platform = sys.platform
distributions = sys.argv[1:]
if not distributions:
    distributions = os.listdir("stubs")

if platform in metadata_mapping:
    for distribution in distributions:
        with open(f"stubs/{distribution}/METADATA.toml", "rb") as file:
            for package in tomli.load(file).get("tool", {}).get("stubtest", {}).get(metadata_mapping[platform], []):
                print(package)
