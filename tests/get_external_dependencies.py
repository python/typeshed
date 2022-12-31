#!/usr/bin/env python3
from __future__ import annotations

import os
import sys

from utils import read_dependencies

distributions = sys.argv[1:]

if not distributions:
    distributions = os.listdir("stubs")

for distribution in distributions:
    for package in read_dependencies(distribution).external_pkgs:
        print(package)
