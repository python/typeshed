import sys
from _typeshed import Incomplete
from collections.abc import Callable
from re import Match
from typing import Any

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
    scan_once: Callable[[str, int], tuple[Any, int]],
    object_hook: Callable[[dict[str, Any]], Any] | None,
    object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None,
    memo: dict[str, str] | None = None,
    _w: Callable[[str, int], Match[str] | None] = ...,
    _ws: str = ...,
) -> tuple[Any, int]: ...

if sys.version_info >= (3, 15):
    def JSONArray(
        s_and_end: tuple[str, int],
        scan_once: Callable[[str, int], tuple[Any, int]],
        array_hook: Callable[[list[Any]], Any] | None,
        _w: Callable[[str, int], Match[str] | None] = ...,
        _ws: str = ...,
    ) -> tuple[Any, int]: ...

else:
    def JSONArray(
        s_and_end: tuple[str, int],
        scan_once: Callable[[str, int], tuple[Any, int]],
        _w: Callable[[str, int], Match[str] | None] = ...,
        _ws: str = ...,
    ) -> tuple[list[Any], int]: ...

class JSONDecoder:
    if sys.version_info >= (3, 15):
        array_hook: Callable[[list[Any]], Any] | None
    object_hook: Callable[[dict[str, Any]], Any]
    parse_float: Callable[[str], Any]
    parse_int: Callable[[str], Any]
    parse_constant: Callable[[str], Any]
    strict: bool
    object_pairs_hook: Callable[[list[tuple[str, Any]]], Any]
    parse_object: Callable[..., Incomplete]
    parse_array: Callable[..., Incomplete]
    parse_string: Callable[..., Incomplete]
    memo: dict[str, str]
    if sys.version_info >= (3, 15):
        def __init__(
            self,
            *,
            object_hook: Callable[[dict[str, Any]], Any] | None = None,
            parse_float: Callable[[str], Any] | None = None,
            parse_int: Callable[[str], Any] | None = None,
            parse_constant: Callable[[str], Any] | None = None,
            strict: bool = True,
            object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None = None,
            array_hook: Callable[[list[Any]], Any] | None = None,
        ) -> None: ...

    else:
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
