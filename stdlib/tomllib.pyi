from _typeshed import SupportsRead
from collections.abc import Callable
from typing import Any

__all__ = ("TOMLDecodeError", "load", "loads")

class TOMLDecodeError(ValueError): ...

def load(fp: SupportsRead[bytes], /, *, parse_float: Callable[[str], Any] = ...) -> dict[str, Any]: ...
def loads(s: str, /, *, parse_float: Callable[[str], Any] = ...) -> dict[str, Any]: ...
