# Stubs for struct

# Based on http://docs.python.org/3.2/library/struct.html
# Based on http://docs.python.org/2/library/struct.html

import sys
from typing import Any, Tuple, Text, Union, Iterator
from array import array

class error(Exception): ...

_FmtType = Union[bytes, Text]
if sys.version_info >= (3,):
    _BufferType = Union[bytes, bytearray, memoryview]
    _WriteBufferType = Union[array, bytearray, memoryview]
else:
    _BufferType = Union[bytes, bytearray, buffer, memoryview]
    _WriteBufferType = Union[array, bytearray, buffer, memoryview]

def pack(fmt: _FmtType, *v: Any) -> bytes: ...
def pack_into(fmt: _FmtType, buffer: _WriteBufferType, offset: int, *v: Any) -> None: ...
def unpack(fmt: _FmtType, buffer: _BufferType) -> Tuple[Any, ...]: ...
def unpack_from(fmt: _FmtType, buffer: _BufferType, offset: int = ...) -> Tuple[Any, ...]: ...
if sys.version_info >= (3, 4):
    def iter_unpack(fmt: _FmtType, buffer: _BufferType) -> Iterator[Tuple[Any, ...]]: ...

def calcsize(fmt: _FmtType) -> int: ...

class Struct:
    format = ...  # type: bytes
    size = ...  # type: int

    def __init__(self, format: _FmtType) -> None: ...

    def pack(self, *v: Any) -> bytes: ...
    def pack_into(self, buffer: _WriteBufferType, offset: int, *v: Any) -> None: ...
    def unpack(self, buffer: _BufferType) -> Tuple[Any, ...]: ...
    def unpack_from(self, buffer: _BufferType, offset: int = ...) -> Tuple[Any, ...]: ...
    if sys.version_info >= (3, 4):
        def iter_unpack(self, buffer: _BufferType) -> Iterator[Tuple[Any, ...]]: ...
