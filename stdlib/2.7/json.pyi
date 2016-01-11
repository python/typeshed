from typing import Any, IO, Optional, Tuple, Callable, Dict, List

class JSONDecodeError(object):
    def dumps(self, obj: Any) -> str: ...
    def dump(self, obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
    def loads(self, s: str) -> Any: ...
    def load(self, fp: IO[str]) -> Any: ...

def dumps(obj: Any,
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Any = ...,
    indent: Optional[int] = ...,
    separators: Optional[Tuple[str, str]] = ...,
    encoding: str = ...,
    default: Optional[Callable[[Any], Any]] = ...,
    sort_keys: bool = ...,
    **kwds: Any) -> str: ...

def dump(obj: Any,
    fp: IO[str],
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Any = ...,
    indent: Optional[int] = ...,
    separators: Optional[Tuple[str, str]] = ...,
    encoding: str = ...,
    default: Optional[Callable[[Any], Any]] = ...,
    sort_keys: bool = ...,
    **kwds: Any) -> None: ...

def loads(s: str,
    encoding: Any = ...,
    cls: Any = ...,
    object_hook: Callable[[Dict], Any] = ...,
    parse_float: Optional[Callable[[str], Any]] = ...,
    parse_int: Optional[Callable[[str], Any]] = ...,
    parse_constant: Optional[Callable[[str], Any]] = ...,
    object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
    **kwds: Any) -> Any: ...

def load(fp: IO[str],
    encoding: Optional[str] = ...,
    cls: Any = ...,
    object_hook: Callable[[Dict], Any] = ...,
    parse_float: Optional[Callable[[str], Any]] = ...,
    parse_int: Optional[Callable[[str], Any]] = ...,
    parse_constant: Optional[Callable[[str], Any]] = ...,
    object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
    **kwds: Any) -> Any: ...
