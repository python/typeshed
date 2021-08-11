from _typeshed import SupportsRead
from typing import IO, Any, Callable, Dict, List, Optional, Text, Tuple, Type, Union

def dumps(
    obj: Any,
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Type[JSONEncoder] | None = ...,
    indent: int | None = ...,
    separators: Tuple[str, str] | None = ...,
    encoding: str = ...,
    default: Callable[[Any], Any] | None = ...,
    sort_keys: bool = ...,
    **kwds: Any,
) -> str: ...
def dump(
    obj: Any,
    fp: IO[str] | IO[Text],
    skipkeys: bool = ...,
    ensure_ascii: bool = ...,
    check_circular: bool = ...,
    allow_nan: bool = ...,
    cls: Type[JSONEncoder] | None = ...,
    indent: int | None = ...,
    separators: Tuple[str, str] | None = ...,
    encoding: str = ...,
    default: Callable[[Any], Any] | None = ...,
    sort_keys: bool = ...,
    **kwds: Any,
) -> None: ...
def loads(
    s: Text | bytes,
    encoding: Any = ...,
    cls: Type[JSONDecoder] | None = ...,
    object_hook: Callable[[Dict[Any, Any]], Any] | None = ...,
    parse_float: Callable[[str], Any] | None = ...,
    parse_int: Callable[[str], Any] | None = ...,
    parse_constant: Callable[[str], Any] | None = ...,
    object_pairs_hook: Callable[[List[Tuple[Any, Any]]], Any] | None = ...,
    **kwds: Any,
) -> Any: ...
def load(
    fp: SupportsRead[Text | bytes],
    encoding: str | None = ...,
    cls: Type[JSONDecoder] | None = ...,
    object_hook: Callable[[Dict[Any, Any]], Any] | None = ...,
    parse_float: Callable[[str], Any] | None = ...,
    parse_int: Callable[[str], Any] | None = ...,
    parse_constant: Callable[[str], Any] | None = ...,
    object_pairs_hook: Callable[[List[Tuple[Any, Any]]], Any] | None = ...,
    **kwds: Any,
) -> Any: ...

class JSONDecoder(object):
    def __init__(
        self,
        encoding: Union[Text, bytes] = ...,
        object_hook: Callable[..., Any] = ...,
        parse_float: Callable[[str], float] = ...,
        parse_int: Callable[[str], int] = ...,
        parse_constant: Callable[[str], Any] = ...,
        strict: bool = ...,
        object_pairs_hook: Callable[..., Any] = ...,
    ) -> None: ...
    def decode(self, s: Union[Text, bytes], _w: Any = ...) -> Any: ...
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
    def __init__(
        self,
        skipkeys: bool = ...,
        ensure_ascii: bool = ...,
        check_circular: bool = ...,
        allow_nan: bool = ...,
        sort_keys: bool = ...,
        indent: Optional[int] = ...,
        separators: Tuple[Union[Text, bytes], Union[Text, bytes]] = ...,
        encoding: Union[Text, bytes] = ...,
        default: Callable[..., Any] = ...,
    ) -> None: ...
    def default(self, o: Any) -> Any: ...
    def encode(self, o: Any) -> str: ...
    def iterencode(self, o: Any, _one_shot: bool = ...) -> str: ...
