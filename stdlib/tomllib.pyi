from _typeshed import SupportsRead
from collections.abc import Callable
import sys
from typing import Any

__all__ = ("loads", "load", "TOMLDecodeError")

if sys.version_info >= (3, 14):
    class TOMLDecodeError(ValueError):
        msg: str
        doc: str
        pos: int
        lineno: int
        colno: int
        def __init__(self, msg: str, doc: str, pos: int) -> None: ...
else:
    class TOMLDecodeError(ValueError): ...

def load(fp: SupportsRead[bytes], /, *, parse_float: Callable[[str], Any] = ...) -> dict[str, Any]: ...
def loads(s: str, /, *, parse_float: Callable[[str], Any] = ...) -> dict[str, Any]: ...
