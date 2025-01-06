#!/usr/bin/env python3

# TODO: It should be possible to specify the Python version and platform
# and limit the output to the packages that are compatible with that version
# and platform.

from __future__ import annotations

import os
import sys

from packaging.requirements import Requirement

from ts_utils.metadata import read_dependencies

distributions = sys.argv[1:]
if not distributions:
    distributions = os.listdir("stubs")

requirements = set[Requirement]()
for distribution in distributions:
    requirements.update(read_dependencies(distribution).external_pkgs)

for requirement in sorted(requirements, key=str):
    print(requirement)
