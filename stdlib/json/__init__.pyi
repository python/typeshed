from _typeshed import SupportsRead
from typing import IO, Any, Callable, Dict, List, Optional, Tuple, Type

from .decoder import JSONDecodeError as JSONDecodeError, JSONDecoder as JSONDecoder
from .encoder import JSONEncoder as JSONEncoder

def dumps(
    obj: Any,
    *,
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Type[JSONEncoder] | None = ...,
    indent: None | int | str = ...,
    separators: Tuple[str, str] | None = ...,
    default: Optional[Callable[[Any], Any]] = ...,
    sort_keys: bool = ...,
    **kwds: Any,
) -> str: ...
def dump(
    obj: Any,
    fp: IO[str],
    *,
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Type[JSONEncoder] | None = ...,
    indent: None | int | str = ...,
    separators: Tuple[str, str] | None = ...,
    default: Optional[Callable[[Any], Any]] = ...,
    sort_keys: bool = ...,
    **kwds: Any,
) -> None: ...
def loads(
    s: str | bytes,
    *,
    cls: Type[JSONDecoder] | None = ...,
    object_hook: Optional[Callable[[Dict[Any, Any]], Any]] = ...,
    parse_float: Optional[Callable[[str], Any]] = ...,
    parse_int: Optional[Callable[[str], Any]] = ...,
    parse_constant: Optional[Callable[[str], Any]] = ...,
    object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
    **kwds: Any,
) -> Any: ...
def load(
    fp: SupportsRead[str | bytes],
    *,
    cls: Type[JSONDecoder] | None = ...,
    object_hook: Optional[Callable[[Dict[Any, Any]], Any]] = ...,
    parse_float: Optional[Callable[[str], Any]] = ...,
    parse_int: Optional[Callable[[str], Any]] = ...,
    parse_constant: Optional[Callable[[str], Any]] = ...,
    object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
    **kwds: Any,
) -> Any: ...
def detect_encoding(b: bytes) -> str: ...  # undocumented
