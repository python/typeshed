from typing import IO, Any, Callable, Iterator, MutableMapping
from typing_extensions import TypeAlias

__all__ = ["dis", "genops", "optimize"]

_Reader: TypeAlias = Callable[[IO[bytes]], Any]
bytes_types: tuple[type[Any], ...]

UP_TO_NEWLINE: int
TAKEN_FROM_ARGUMENT1: int
TAKEN_FROM_ARGUMENT4: int
TAKEN_FROM_ARGUMENT4U: int
TAKEN_FROM_ARGUMENT8U: int

class ArgumentDescriptor:
    name: str
    n: int
    reader: _Reader
    doc: str
    def __init__(self, name: str, n: int, reader: _Reader, doc: str) -> None: ...

def read_uint1(f: IO[bytes]) -> int: ...

uint1: ArgumentDescriptor

def read_uint2(f: IO[bytes]) -> int: ...

uint2: ArgumentDescriptor

def read_int4(f: IO[bytes]) -> int: ...

int4: ArgumentDescriptor

def read_uint4(f: IO[bytes]) -> int: ...

uint4: ArgumentDescriptor

def read_uint8(f: IO[bytes]) -> int: ...

uint8: ArgumentDescriptor

def read_stringnl(f: IO[bytes], decode: bool = ..., stripquotes: bool = ...) -> bytes | str: ...

stringnl: ArgumentDescriptor

def read_stringnl_noescape(f: IO[bytes]) -> str: ...

stringnl_noescape: ArgumentDescriptor

def read_stringnl_noescape_pair(f: IO[bytes]) -> str: ...

stringnl_noescape_pair: ArgumentDescriptor

def read_string1(f: IO[bytes]) -> str: ...

string1: ArgumentDescriptor

def read_string4(f: IO[bytes]) -> str: ...

string4: ArgumentDescriptor

def read_bytes1(f: IO[bytes]) -> bytes: ...

bytes1: ArgumentDescriptor

def read_bytes4(f: IO[bytes]) -> bytes: ...

bytes4: ArgumentDescriptor

def read_bytes8(f: IO[bytes]) -> bytes: ...

bytes8: ArgumentDescriptor

def read_unicodestringnl(f: IO[bytes]) -> str: ...

unicodestringnl: ArgumentDescriptor

def read_unicodestring1(f: IO[bytes]) -> str: ...

unicodestring1: ArgumentDescriptor

def read_unicodestring4(f: IO[bytes]) -> str: ...

unicodestring4: ArgumentDescriptor

def read_unicodestring8(f: IO[bytes]) -> str: ...

unicodestring8: ArgumentDescriptor

def read_decimalnl_short(f: IO[bytes]) -> int: ...
def read_decimalnl_long(f: IO[bytes]) -> int: ...

decimalnl_short: ArgumentDescriptor
decimalnl_long: ArgumentDescriptor

def read_floatnl(f: IO[bytes]) -> float: ...

floatnl: ArgumentDescriptor

def read_float8(f: IO[bytes]) -> float: ...

float8: ArgumentDescriptor

def read_long1(f: IO[bytes]) -> int: ...

long1: ArgumentDescriptor

def read_long4(f: IO[bytes]) -> int: ...

long4: ArgumentDescriptor

class StackObject:
    name: str
    obtype: type[Any] | tuple[type[Any], ...]
    doc: str
    def __init__(self, name: str, obtype: type[Any] | tuple[type[Any], ...], doc: str) -> None: ...

pyint: StackObject
pylong: StackObject
pyinteger_or_bool: StackObject
pybool: StackObject
pyfloat: StackObject
pybytes_or_str: StackObject
pystring: StackObject
pybytes: StackObject
pyunicode: StackObject
pynone: StackObject
pytuple: StackObject
pylist: StackObject
pydict: StackObject
pyset: StackObject
pyfrozenset: StackObject
anyobject: StackObject
markobject: StackObject
stackslice: StackObject

class OpcodeInfo:
    name: str
    code: str
    arg: ArgumentDescriptor | None
    stack_before: list[StackObject]
    stack_after: list[StackObject]
    proto: int
    doc: str
    def __init__(
        self,
        name: str,
        code: str,
        arg: ArgumentDescriptor | None,
        stack_before: list[StackObject],
        stack_after: list[StackObject],
        proto: int,
        doc: str,
    ) -> None: ...

opcodes: list[OpcodeInfo]

def genops(pickle: bytes | IO[bytes]) -> Iterator[tuple[OpcodeInfo, Any | None, int | None]]: ...
def optimize(p: bytes | IO[bytes]) -> bytes: ...
def dis(
    pickle: bytes | IO[bytes],
    out: IO[str] | None = ...,
    memo: MutableMapping[int, Any] | None = ...,
    indentlevel: int = ...,
    annotate: int = ...,
) -> None: ...
