import sys
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

if sys.version_info >= (3, 5):
    class JSONDecodeError(ValueError):
        msg: str
        doc: str
        pos: int
        lineno: int
        colno: int
        def __init__(self, msg: str, doc: str, pos: int) -> None: ...

# documentation for return type: https://docs.python.org/3.7/library/json.html#json-to-py-table
_LoadsReturnType = Union[Dict[Any,Any], List[Any], str, int, float, None]

class JSONDecoder:
    object_hook: Callable[[Dict[str, Any]], Any]
    parse_float: Callable[[str], Any]
    parse_int: Callable[[str], Any]
    parse_constant = ...  # Callable[[str], Any]
    strict: bool
    object_pairs_hook: Callable[[List[Tuple[str, Any]]], Any]

    def __init__(self, object_hook: Optional[Callable[[Dict[str, Any]], Any]] = ...,
                 parse_float: Optional[Callable[[str], Any]] = ...,
                 parse_int: Optional[Callable[[str], Any]] = ...,
                 parse_constant: Optional[Callable[[str], Any]] = ...,
                 strict: bool = ...,
                 object_pairs_hook: Optional[Callable[[List[Tuple[str, Any]]], Any]] = ...) -> None: ...
    def decode(self, s: str) -> _LoadsReturnType: ...
    def raw_decode(self, s: str, idx: int = ...) -> Tuple[Any, int]: ...
