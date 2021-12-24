import sys
from collections.abc import Awaitable

if sys.version_info >= (3, 7):
    from typing import TypeVar

    _T = TypeVar("_T")
    if sys.version_info >= (3, 8):
        def run(main: Awaitable[_T], *, debug: bool | None = ...) -> _T: ...
    else:
        def run(main: Awaitable[_T], *, debug: bool = ...) -> _T: ...
