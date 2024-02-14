import abc
import builtins
import codecs
import sys
from _typeshed import FileDescriptorOrPath, ReadableBuffer, WriteableBuffer
from collections.abc import Callable, Iterable, Iterator
from os import _Opener
from types import TracebackType
from typing import IO, Any, BinaryIO, Literal, Protocol, TextIO, TypeVar, overload, type_check_only
from typing_extensions import Self

__all__ = [
    "BlockingIOError",
    "open",
    "open_code",
    "IOBase",
    "RawIOBase",
    "FileIO",
    "BytesIO",
    "StringIO",
    "BufferedIOBase",
    "BufferedReader",
    "BufferedWriter",
    "BufferedRWPair",
    "BufferedRandom",
    "TextIOBase",
    "TextIOWrapper",
    "UnsupportedOperation",
    "SEEK_SET",
    "SEEK_CUR",
    "SEEK_END",
]

if sys.version_info >= (3, 11):
    __all__ += ["DEFAULT_BUFFER_SIZE", "IncrementalNewlineDecoder", "text_encoding"]

_T = TypeVar("_T")

DEFAULT_BUFFER_SIZE: Literal[8192]

SEEK_SET: Literal[0]
SEEK_CUR: Literal[1]
SEEK_END: Literal[2]

open = builtins.open

def open_code(path: str) -> IO[bytes]: ...

BlockingIOError = builtins.BlockingIOError

class UnsupportedOperation(OSError, ValueError): ...

class IOBase(metaclass=abc.ABCMeta):
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    read: Callable[..., Any]
    def readlines(self, __hint: int = -1) -> list[bytes]: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, __size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    write: Callable[..., Any]
    def writelines(self, __lines: Iterable[ReadableBuffer]) -> None: ...
    def readline(self, __size: int | None = -1) -> bytes: ...
    def __del__(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self, msg: str | None = ...) -> None: ...  # undocumented

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    def readinto(self, __buffer: WriteableBuffer) -> int | None: ...
    def write(self, __b: ReadableBuffer) -> int | None: ...
    def read(self, __size: int = -1) -> bytes | None: ...

class BufferedIOBase(IOBase):
    raw: RawIOBase  # This is not part of the BufferedIOBase API and may not exist on some implementations.
    def detach(self) -> RawIOBase: ...
    def readinto(self, __buffer: WriteableBuffer) -> int: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...
    def readinto1(self, __buffer: WriteableBuffer) -> int: ...
    def read(self, __size: int | None = ...) -> bytes: ...
    def read1(self, __size: int = ...) -> bytes: ...

class FileIO(RawIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    mode: str
    name: FileDescriptorOrPath
    def __init__(
        self, file: FileDescriptorOrPath, mode: str = ..., closefd: bool = ..., opener: _Opener | None = ...
    ) -> None: ...
    @property
    def closefd(self) -> bool: ...
    def write(self, __b: ReadableBuffer) -> int: ...
    def read(self, __size: int = -1) -> bytes: ...
    def __enter__(self) -> Self: ...

class BytesIO(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __init__(self, initial_bytes: ReadableBuffer = ...) -> None: ...
    # BytesIO does not contain a "name" field. This workaround is necessary
    # to allow BytesIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def __enter__(self) -> Self: ...
    def getvalue(self) -> bytes: ...
    def getbuffer(self) -> memoryview: ...
    def read1(self, __size: int | None = -1) -> bytes: ...

class BufferedReader(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = 0) -> bytes: ...

class BufferedWriter(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def write(self, __buffer: ReadableBuffer) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __enter__(self) -> Self: ...
    def seek(self, __target: int, __whence: int = 0) -> int: ...  # stubtest needs this

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = ...) -> bytes: ...

class TextIOBase(IOBase):
    encoding: str
    errors: str | None
    newlines: str | tuple[str, ...] | None
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def detach(self) -> BinaryIO: ...
    def write(self, __s: str) -> int: ...
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = ...) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = -1) -> list[str]: ...  # type: ignore[override]
    def read(self, __size: int | None = ...) -> str: ...

@type_check_only
class _WrappedBuffer(Protocol):
    name: str
    closed: bool
    def read(self, size: int = ...) -> bytes: ...
    # Optional: def read1(size: int, /) -> bytes: ...
    def write(self, b: bytes, /) -> object: ...
    def flush(self) -> object: ...
    def close(self) -> object: ...
    def seekable(self) -> bool: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def truncate(self, size: int, /) -> int: ...
    def fileno(self) -> int: ...
    def isatty(self) -> int: ...
    # Optional: Only needs to be present if seekable() returns True.
    # def seek(self, offset: Literal[0], whence: Literal[2]) -> int: ...
    # def tell(self) -> int: ...

class TextIOWrapper(TextIOBase, TextIO):  # type: ignore[misc]  # incompatible definitions of write in the base classes
    def __init__(
        self,
        buffer: _WrappedBuffer,
        encoding: str | None = ...,
        errors: str | None = ...,
        newline: str | None = ...,
        line_buffering: bool = ...,
        write_through: bool = ...,
    ) -> None: ...
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def closed(self) -> bool: ...
    @property
    def line_buffering(self) -> bool: ...
    @property
    def write_through(self) -> bool: ...
    def reconfigure(
        self,
        *,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        line_buffering: bool | None = None,
        write_through: bool | None = None,
    ) -> None: ...
    # These are inherited from TextIOBase, but must exist in the stub to satisfy mypy.
    def __enter__(self) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def writelines(self, __lines: Iterable[str]) -> None: ...  # type: ignore[override]
    def readline(self, __size: int = -1) -> str: ...  # type: ignore[override]
    def readlines(self, __hint: int = -1) -> list[str]: ...  # type: ignore[override]
    @overload
    def seek(self, __cookie: int, __whence: Literal[0] = 0) -> int: ...
    @overload
    def seek(self, __cookie: Literal[0], __whence: Literal[1, 2]) -> int: ...

class StringIO(TextIOWrapper):
    def __init__(self, initial_value: str | None = ..., newline: str | None = ...) -> None: ...
    # StringIO does not contain a "name" field. This workaround is necessary
    # to allow StringIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def getvalue(self) -> str: ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    def __init__(self, decoder: codecs.IncrementalDecoder | None, translate: bool, errors: str = ...) -> None: ...
    def decode(self, input: ReadableBuffer | str, final: bool = False) -> str: ...
    @property
    def newlines(self) -> str | tuple[str, ...] | None: ...
    def setstate(self, __state: tuple[bytes, int]) -> None: ...

if sys.version_info >= (3, 10):
    @overload
    def text_encoding(__encoding: None, __stacklevel: int = 2) -> Literal["locale", "utf-8"]: ...
    @overload
    def text_encoding(__encoding: _T, __stacklevel: int = 2) -> _T: ...
