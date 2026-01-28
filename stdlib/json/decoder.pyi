from collections.abc import Callable
from typing import Any
from _typeshed import Incomplete

__all__ = ["JSONDecoder", "JSONDecodeError"]

class JSONDecodeError(ValueError):
    msg: str
    doc: str
    pos: int
    lineno: int
    colno: int
    def __init__(self, msg: str, doc: str, pos: int) -> None: ...

def JSONObject(
    s_and_end: tuple[str, int],
    strict: bool,
    scan_once: Callable[[Incomplete], Incomplete],
    object_hook: Callable[[Incomplete], Incomplete] | None,
    object_pairs_hook: Callable[[Incomplete], Incomplete] | None,
    memo: dict[Incomplete, Incomplete] | None = None,
    _w: Callable[[str, int], Incomplete] = ...,
    _ws: str = ...
) -> tuple[Incomplete, int]: ...

def JSONArray(
    s_and_end: tuple[str, int],
    scan_once: Callable[[Incomplete], Incomplete],
    _w: Callable[[str, int], Incomplete] = ...,
    _ws: str = ...
) -> tuple[list[Incomplete], int]: ...

class JSONDecoder:
    object_hook: Callable[[dict[str, Any]], Any]
    parse_float: Callable[[str], Any]
    parse_int: Callable[[str], Any]
    parse_constant: Callable[[str], Any]
    strict: bool
    object_pairs_hook: Callable[[list[tuple[str, Any]]], Any]
    parse_object: Callable[[Incomplete], Incomplete]
    parse_array: Callable[[Incomplete], Incomplete]
    parse_string: Callable[[Incomplete], Incomplete]
    memo: dict[Incomplete, Incomplete]
    def __init__(
        self,
        *,
        object_hook: Callable[[dict[str, Any]], Any] | None = None,
        parse_float: Callable[[str], Any] | None = None,
        parse_int: Callable[[str], Any] | None = None,
        parse_constant: Callable[[str], Any] | None = None,
        strict: bool = True,
        object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None = None,
    ) -> None: ...
    def decode(self, s: str, _w: Callable[..., Any] = ...) -> Any: ...  # _w is undocumented
    def raw_decode(self, s: str, idx: int = 0) -> tuple[Any, int]: ...
