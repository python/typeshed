from _typeshed import SupportsRead, SupportsWrite
from collections.abc import Callable
from typing import Any, TypeAlias, TypeVar, overload

from .decoder import JSONDecodeError as JSONDecodeError, JSONDecoder as JSONDecoder
from .encoder import JSONEncoder as JSONEncoder

__all__ = ["dump", "dumps", "load", "loads", "JSONDecoder", "JSONDecodeError", "JSONEncoder"]

_T = TypeVar("_T")

_JSON: TypeAlias = dict[str, _JSON] | list[_JSON] | str | int | float | bool | None

@overload
def dumps(
    obj: _JSON,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: None | int | str = None,
    separators: tuple[str, str] | None = None,
    default: None = None,
    sort_keys: bool = False,
    **kwds: Any,
) -> str: ...
@overload
def dumps(
    obj: _T,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: None | int | str = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[_T], _JSON],
    sort_keys: bool = False,
    **kwds: Any,
) -> str: ...
@overload
def dump(
    obj: _JSON,
    fp: SupportsWrite[str],
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: None | int | str = None,
    separators: tuple[str, str] | None = None,
    default: None = None,
    sort_keys: bool = False,
    **kwds: Any,
) -> None: ...
@overload
def dump(
    obj: _T,
    fp: SupportsWrite[str],
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: None | int | str = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[_T], _JSON],
    sort_keys: bool = False,
    **kwds: Any,
) -> None: ...
def loads(
    s: str | bytes | bytearray,
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwds: Any,
) -> Any: ...
def load(
    fp: SupportsRead[str | bytes],
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwds: Any,
) -> Any: ...
def detect_encoding(b: bytes | bytearray) -> str: ...  # undocumented
