from _typeshed import ReadableBuffer, SupportsWrite
from collections.abc import Callable, Iterable, Iterator, Mapping
from typing import Any, ClassVar, Final, Protocol, SupportsBytes, SupportsIndex, final
from typing_extensions import TypeAlias

__all__ = [
    "PickleBuffer",
    "PickleError",
    "PicklingError",
    "UnpicklingError",
    "Pickler",
    "Unpickler",
    "dump",
    "dumps",
    "load",
    "loads",
    "ADDITEMS",
    "APPEND",
    "APPENDS",
    "BINBYTES",
    "BINBYTES8",
    "BINFLOAT",
    "BINGET",
    "BININT",
    "BININT1",
    "BININT2",
    "BINPERSID",
    "BINPUT",
    "BINSTRING",
    "BINUNICODE",
    "BINUNICODE8",
    "BUILD",
    "BYTEARRAY8",
    "DEFAULT_PROTOCOL",
    "DICT",
    "DUP",
    "EMPTY_DICT",
    "EMPTY_LIST",
    "EMPTY_SET",
    "EMPTY_TUPLE",
    "EXT1",
    "EXT2",
    "EXT4",
    "FALSE",
    "FLOAT",
    "FRAME",
    "FROZENSET",
    "GET",
    "GLOBAL",
    "HIGHEST_PROTOCOL",
    "INST",
    "INT",
    "LIST",
    "LONG",
    "LONG1",
    "LONG4",
    "LONG_BINGET",
    "LONG_BINPUT",
    "MARK",
    "MEMOIZE",
    "NEWFALSE",
    "NEWOBJ",
    "NEWOBJ_EX",
    "NEWTRUE",
    "NEXT_BUFFER",
    "NONE",
    "OBJ",
    "PERSID",
    "POP",
    "POP_MARK",
    "PROTO",
    "PUT",
    "READONLY_BUFFER",
    "REDUCE",
    "SETITEM",
    "SETITEMS",
    "SHORT_BINBYTES",
    "SHORT_BINSTRING",
    "SHORT_BINUNICODE",
    "STACK_GLOBAL",
    "STOP",
    "STRING",
    "TRUE",
    "TUPLE",
    "TUPLE1",
    "TUPLE2",
    "TUPLE3",
    "UNICODE",
]

HIGHEST_PROTOCOL: Final[int]
DEFAULT_PROTOCOL: Final[int]

bytes_types: tuple[type[Any], ...]  # undocumented

class _ReadableFileobj(Protocol):
    def read(self, n: int, /) -> bytes: ...
    def readline(self) -> bytes: ...

@final
class PickleBuffer:
    def __init__(self, buffer: ReadableBuffer) -> None: ...
    def raw(self) -> memoryview: ...
    def release(self) -> None: ...
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __release_buffer__(self, buffer: memoryview, /) -> None: ...

_BufferCallback: TypeAlias = Callable[[PickleBuffer], Any] | None

def dump(
    obj: Any,
    file: SupportsWrite[bytes],
    protocol: int | None = None,
    *,
    fix_imports: bool = True,
    buffer_callback: _BufferCallback = None,
) -> None: ...
def dumps(
    obj: Any, protocol: int | None = None, *, fix_imports: bool = True, buffer_callback: _BufferCallback = None
) -> bytes: ...
def load(
    file: _ReadableFileobj,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    buffers: Iterable[Any] | None = (),
) -> Any: ...
def loads(
    data: ReadableBuffer,
    /,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
    buffers: Iterable[Any] | None = (),
) -> Any: ...

class PickleError(Exception): ...
class PicklingError(PickleError): ...
class UnpicklingError(PickleError): ...

_ReducedType: TypeAlias = (
    str
    | tuple[Callable[..., Any], tuple[Any, ...]]
    | tuple[Callable[..., Any], tuple[Any, ...], Any]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Iterator[Any] | None]
    | tuple[Callable[..., Any], tuple[Any, ...], Any, Iterator[Any] | None, Iterator[Any] | None]
)

class Pickler:
    fast: bool
    dispatch_table: Mapping[type, Callable[[Any], _ReducedType]]
    bin: bool  # undocumented
    dispatch: ClassVar[dict[type, Callable[[Unpickler, Any], None]]]  # undocumented, _Pickler only

    def __init__(
        self,
        file: SupportsWrite[bytes],
        protocol: int | None = ...,
        *,
        fix_imports: bool = ...,
        buffer_callback: _BufferCallback = ...,
    ) -> None: ...
    def reducer_override(self, obj: Any) -> Any: ...
    def dump(self, obj: Any, /) -> None: ...
    def clear_memo(self) -> None: ...
    def persistent_id(self, obj: Any) -> Any: ...

class Unpickler:
    dispatch: ClassVar[dict[int, Callable[[Unpickler], None]]]  # undocumented, _Unpickler only

    def __init__(
        self,
        file: _ReadableFileobj,
        *,
        fix_imports: bool = ...,
        encoding: str = ...,
        errors: str = ...,
        buffers: Iterable[Any] | None = ...,
    ) -> None: ...
    def load(self) -> Any: ...
    def find_class(self, module_name: str, global_name: str, /) -> Any: ...
    def persistent_load(self, pid: Any) -> Any: ...

MARK: Final[bytes]
STOP: Final[bytes]
POP: Final[bytes]
POP_MARK: Final[bytes]
DUP: Final[bytes]
FLOAT: Final[bytes]
INT: Final[bytes]
BININT: Final[bytes]
BININT1: Final[bytes]
LONG: Final[bytes]
BININT2: Final[bytes]
NONE: Final[bytes]
PERSID: Final[bytes]
BINPERSID: Final[bytes]
REDUCE: Final[bytes]
STRING: Final[bytes]
BINSTRING: Final[bytes]
SHORT_BINSTRING: Final[bytes]
UNICODE: Final[bytes]
BINUNICODE: Final[bytes]
APPEND: Final[bytes]
BUILD: Final[bytes]
GLOBAL: Final[bytes]
DICT: Final[bytes]
EMPTY_DICT: Final[bytes]
APPENDS: Final[bytes]
GET: Final[bytes]
BINGET: Final[bytes]
INST: Final[bytes]
LONG_BINGET: Final[bytes]
LIST: Final[bytes]
EMPTY_LIST: Final[bytes]
OBJ: Final[bytes]
PUT: Final[bytes]
BINPUT: Final[bytes]
LONG_BINPUT: Final[bytes]
SETITEM: Final[bytes]
TUPLE: Final[bytes]
EMPTY_TUPLE: Final[bytes]
SETITEMS: Final[bytes]
BINFLOAT: Final[bytes]

TRUE: Final[bytes]
FALSE: Final[bytes]

# protocol 2
PROTO: Final[bytes]
NEWOBJ: Final[bytes]
EXT1: Final[bytes]
EXT2: Final[bytes]
EXT4: Final[bytes]
TUPLE1: Final[bytes]
TUPLE2: Final[bytes]
TUPLE3: Final[bytes]
NEWTRUE: Final[bytes]
NEWFALSE: Final[bytes]
LONG1: Final[bytes]
LONG4: Final[bytes]

# protocol 3
BINBYTES: Final[bytes]
SHORT_BINBYTES: Final[bytes]

# protocol 4
SHORT_BINUNICODE: Final[bytes]
BINUNICODE8: Final[bytes]
BINBYTES8: Final[bytes]
EMPTY_SET: Final[bytes]
ADDITEMS: Final[bytes]
FROZENSET: Final[bytes]
NEWOBJ_EX: Final[bytes]
STACK_GLOBAL: Final[bytes]
MEMOIZE: Final[bytes]
FRAME: Final[bytes]

# protocol 5
BYTEARRAY8: Final[bytes]
NEXT_BUFFER: Final[bytes]
READONLY_BUFFER: Final[bytes]

def encode_long(x: int) -> bytes: ...  # undocumented
def decode_long(data: Iterable[SupportsIndex] | SupportsBytes | ReadableBuffer) -> int: ...  # undocumented

# pure-Python implementations
_Pickler = Pickler  # undocumented
_Unpickler = Unpickler  # undocumented
