#!/usr/bin/env python3
import os
import sys

import tomli
from utils import METADATA_MAPPING

platform = sys.platform
distributions = sys.argv[1:]
if not distributions:
    distributions = os.listdir("stubs")

if platform in METADATA_MAPPING:
    for distribution in distributions:
        with open(f"stubs/{distribution}/METADATA.toml", "rb") as file:
            packages: list[str] = (
                tomli.load(file)
                .get("tool", {})
                .get("stubtest", {})
                # Loss of type due to infered dict[Unknown, Unknown]
                .get(METADATA_MAPPING[platform], [])  # pyright: ignore[reportUnknownMemberType]
            )
            for package in packages:
                print(package)
