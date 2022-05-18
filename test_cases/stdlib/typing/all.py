"""
This tests that star imports work when using "all += " syntax.
"""

import sys
from typing import *

if sys.version_info >= (3, 9):
    x: Annotated[int, 42]
