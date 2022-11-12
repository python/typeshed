import builtins
import types
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from typing import Any
from typing_extensions import TypeAlias

version: int

_Marshallable: TypeAlias = Union[
    int,
    float,
    complex,
    bytes,
    str,
    tuple[_Marshallable, ...],
    list[Any],
    dict[Any, Any],
    set[Any],
    frozenset[_Marshallable],
    types.CodeType,
    ReadableBuffer,
    None,
    bool,
    type[StopIteration],
    builtins.ellipsis,
    Any,  # TODO should be builtins.NotImplemented
]

def dump(__value: _Marshallable, __file: SupportsWrite[bytes], __version: int = ...) -> None: ...
def load(__file: SupportsRead[bytes]) -> Any: ...
def dumps(__value: _Marshallable, __version: int = ...) -> bytes: ...
def loads(__bytes: ReadableBuffer) -> Any: ...
