import sys
from typing import Any, IO, Union, Tuple, Callable, Optional, Iterator
# Imports used in type comments only.
from typing import Mapping  # noqa

HIGHEST_PROTOCOL = ...  # type: int
DEFAULT_PROTOCOL = ...  # type: int


def dump(obj: Any, file: IO[bytes], protocol: int = None, *,
         fix_imports: bool = ...) -> None: ...


def dumps(obj: Any, protocol: int = ..., *,
          fix_imports: bool = ...) -> bytes: ...


def loads(bytes_object: bytes, *, fix_imports: bool = ...,
          encoding: str = ..., errors: str = ...) -> Any: ...


def load(file: IO[bytes], *, fix_imports: bool = ..., encoding: str = ...,
         errors: str = ...) -> Any: ...


class PickleError(Exception):
    pass


class PicklingError(PickleError):
    pass


class UnpicklingError(PickleError):
    pass


_reducedtype = Union[str,
                     Tuple[Callable[..., Any], Tuple],
                     Tuple[Callable[..., Any], Tuple, Any],
                     Tuple[Callable[..., Any], Tuple, Any,
                           Optional[Iterator]],
                     Tuple[Callable[..., Any], Tuple, Any,
                           Optional[Iterator], Optional[Iterator]]]


class Pickler:
    dispatch_table = ...  # type: Mapping[type, Callable[[Any], _reducedtype]]

    def __init__(self, file: IO[bytes], protocol: int = None, *,
                 fix_imports: bool = ...) -> None: ...

    def dump(self, obj: Any) -> None: ...

    def persistent_id(self, obj: Any) -> Any: ...


class Unpickler:
    def __init__(self, file: IO[bytes], *, fix_imports: bool = ...,
                 encoding: str = ..., errors: str = ...) -> None: ...

    def load(self) -> Any: ...

    def persistent_load(self, pid: Any) -> Any: ...

    def find_class(self, module: str, name: str) -> Any: ...

MARK: bytes
STOP: bytes
POP: bytes
POP_MARK: bytes
DUP: bytes
FLOAT: bytes
INT: bytes
BININT: bytes
BININT1: bytes
LONG: bytes
BININT2: bytes
NONE: bytes
PERSID: bytes
BINPERSID: bytes
REDUCE: bytes
STRING: bytes
BINSTRING: bytes
SHORT_BINSTRING: bytes
UNICODE: bytes
BINUNICODE: bytes
APPEND: bytes
BUILD: bytes
GLOBAL: bytes
DICT: bytes
EMPTY_DICT: bytes
APPENDS: bytes
GET: bytes
BINGET: bytes
INST: bytes
LONG_BINGET: bytes
LIST: bytes
EMPTY_LIST: bytes
OBJ: bytes
PUT: bytes
BINPUT: bytes
LONG_BINPUT: bytes
SETITEM: bytes
TUPLE: bytes
EMPTY_TUPLE: bytes
SETITEMS: bytes
BINFLOAT: bytes

TRUE: bytes
FALSE: bytes

PROTO: bytes
NEWOBJ: bytes
EXT1: bytes
EXT2: bytes
EXT4: bytes
TUPLE1: bytes
TUPLE2: bytes
TUPLE3: bytes
NEWTRUE: bytes
NEWFALSE: bytes
LONG1: bytes
LONG4: bytes

BINBYTES: bytes
SHORT_BINBYTES: bytes

if sys.version_info >= (3, 4):
    SHORT_BINUNICODE: bytes
    BINUNICODE8: bytes
    BINBYTES8: bytes
    EMPTY_SET: bytes
    ADDITEMS: bytes
    FROZENSET: bytes
    NEWOBJ_EX: bytes
    STACK_GLOBAL: bytes
    MEMOIZE: bytes
    FRAME: bytes
