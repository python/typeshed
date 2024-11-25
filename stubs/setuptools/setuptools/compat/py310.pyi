from typing import Any
import sys

__all__ = ["tomllib"]

if sys.version_info >= (3, 11):
    import tomllib
else:
    # This is actually vendored, but CI is flaky when using the following line:
    # import tomli as tomllib
    tomllib: Any
