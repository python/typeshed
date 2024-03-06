# pyright: reportWildcardImportFromLibrary=false
"""
This tests that star imports work when using "all += " syntax.
"""
from __future__ import annotations

import sys
from typing import *  # noqa: F403
from zipfile import *  # noqa: F403

if sys.version_info >= (3, 9):
    x: Annotated[int, 42]  # noqa: F405

p: Path  # noqa: F405
