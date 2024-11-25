import sys
from typing import Any

__all__ = ["tomllib"]

if sys.version_info >= (3, 11):
    import tomllib
else:
    # This is actually vendored
    import tomli as tomllib
