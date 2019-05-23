from typing import Any, IO, Optional, Tuple, Callable, Dict, List, Union, Text, Protocol

# documentation for return type: https://docs.python.org/3.7/library/json.html#json-to-py-table
_LoadsReturnType = Union[Dict[Any,Any], List[Any], str, int, float, None]

class JSONDecodeError(ValueError):
    def dumps(self, obj: Any) -> str: ...
    def dump(self, obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
    def loads(self, s: str) -> _LoadsReturnType: ...
    def load(self, fp: IO[str]) -> _LoadsReturnType: ...

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
         fp: Union[IO[str], IO[Text]],
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

def loads(s: Union[Text, bytes],
          encoding: Any = ...,
          cls: Any = ...,
          object_hook: Optional[Callable[[Dict], Any]] = ...,
          parse_float: Optional[Callable[[str], Any]] = ...,
          parse_int: Optional[Callable[[str], Any]] = ...,
          parse_constant: Optional[Callable[[str], Any]] = ...,
          object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
          **kwds: Any) -> _LoadsReturnType: ...

class _Reader(Protocol):
    def read(self) -> Union[Text, bytes]: ...

def load(fp: _Reader,
         encoding: Optional[str] = ...,
         cls: Any = ...,
         object_hook: Optional[Callable[[Dict], Any]] = ...,
         parse_float: Optional[Callable[[str], Any]] = ...,
         parse_int: Optional[Callable[[str], Any]] = ...,
         parse_constant: Optional[Callable[[str], Any]] = ...,
         object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ...,
         **kwds: Any) -> _LoadsReturnType: ...

class JSONDecoder(object):
    def __init__(self,
                 encoding: Union[Text, bytes] = ...,
                 object_hook: Callable[..., Any] = ...,
                 parse_float: Callable[[str], float] = ...,
                 parse_int: Callable[[str], int] = ...,
                 parse_constant: Callable[[str], Any] = ...,
                 strict: bool = ...,
                 object_pairs_hook: Callable[..., Any] = ...) -> None: ...
    def decode(self, s: Union[Text, bytes], _w: Any = ...) -> _LoadsReturnType: ...
    def raw_decode(self, s: Union[Text, bytes], idx: int = ...) -> Tuple[Any, Any]: ...

class JSONEncoder(object):
    item_separator: str
    key_separator: str
    skipkeys: bool
    ensure_ascii: bool
    check_circular: bool
    allow_nan: bool
    sort_keys: bool
    indent: Optional[int]

    def __init__(self,
                 skipkeys: bool = ...,
                 ensure_ascii: bool = ...,
                 check_circular: bool = ...,
                 allow_nan: bool = ...,
                 sort_keys: bool = ...,
                 indent: Optional[int] = ...,
                 separators: Tuple[Union[Text, bytes], Union[Text, bytes]] = ...,
                 encoding: Union[Text, bytes] = ...,
                 default: Callable[..., Any] = ...) -> None: ...

    def default(self, o: Any) -> Any: ...

    def encode(self, o: Any) -> str: ...

    def iterencode(self, o: Any, _one_shot: bool = ...) -> str: ...
