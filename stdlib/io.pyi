import abc
import builtins
import codecs
import sys
from _typeshed import FileDescriptorOrPath, MaybeNone, ReadableBuffer, WriteableBuffer
from collections.abc import Callable, Iterable, Iterator
from os import _Opener
from types import TracebackType
from typing import IO, Any, BinaryIO, Final, Generic, Literal, Protocol, TextIO, TypeVar, overload, type_check_only
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

DEFAULT_BUFFER_SIZE: Final = 8192

SEEK_SET: Final = 0
SEEK_CUR: Final = 1
SEEK_END: Final = 2

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
    def readlines(self, hint: int = -1, /) -> list[bytes]: ...
    def seek(self, offset: int, whence: int = ..., /) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int | None = ..., /) -> int: ...
    def writable(self) -> bool: ...
    write: Callable[..., Any]
    def writelines(self, lines: Iterable[ReadableBuffer], /) -> None: ...
    def readline(self, size: int | None = -1, /) -> bytes: ...
    def __del__(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self) -> None: ...  # undocumented

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    # The following methods can return None if the file is in non-blocking mode
    # and no data is available.
    def readinto(self, buffer: WriteableBuffer, /) -> int | MaybeNone: ...
    def write(self, b: ReadableBuffer, /) -> int | MaybeNone: ...
    def read(self, size: int = -1, /) -> bytes | MaybeNone: ...

class BufferedIOBase(IOBase):
    def detach(self) -> RawIOBase: ...
    def readinto(self, buffer: WriteableBuffer, /) -> int: ...
    def write(self, buffer: ReadableBuffer, /) -> int: ...
    def readinto1(self, buffer: WriteableBuffer, /) -> int: ...
    def read(self, size: int | None = ..., /) -> bytes: ...
    def read1(self, size: int = ..., /) -> bytes: ...

class FileIO(RawIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    mode: str
    # The type of "name" equals the argument passed in to the constructor,
    # but that can make FileIO incompatible with other I/O types that assume
    # "name" is a str. In the future, making FileIO generic might help.
    name: Any
    def __init__(
        self, file: FileDescriptorOrPath, mode: str = ..., closefd: bool = ..., opener: _Opener | None = ...
    ) -> None: ...
    @property
    def closefd(self) -> bool: ...
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
    def read1(self, size: int | None = -1, /) -> bytes: ...

class BufferedReader(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    raw: RawIOBase
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, size: int = 0, /) -> bytes: ...

class BufferedWriter(BufferedIOBase, BinaryIO):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    raw: RawIOBase
    def __enter__(self) -> Self: ...
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def write(self, buffer: ReadableBuffer, /) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):  # type: ignore[misc]  # incompatible definitions of methods in the base classes
    def __enter__(self) -> Self: ...
    def seek(self, target: int, whence: int = 0, /) -> int: ...  # stubtest needs this

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, size: int = ..., /) -> bytes: ...

class TextIOBase(IOBase):
    encoding: str
    errors: str | None
    newlines: str | tuple[str, ...] | None
    def __iter__(self) -> Iterator[str]: ...  # type: ignore[override]
    def __next__(self) -> str: ...  # type: ignore[override]
    def detach(self) -> BinaryIO: ...
    def write(self, s: str, /) -> int: ...
    def writelines(self, lines: Iterable[str], /) -> None: ...  # type: ignore[override]
    def readline(self, size: int = ..., /) -> str: ...  # type: ignore[override]
    def readlines(self, hint: int = -1, /) -> list[str]: ...  # type: ignore[override]
    def read(self, size: int | None = ..., /) -> str: ...

@type_check_only
class _WrappedBuffer(Protocol):
    # "name" is wrapped by TextIOWrapper. Its type is inconsistent between
    # the various I/O types, see the comments on TextIOWrapper.name and
    # TextIO.name.
    @property
    def name(self) -> Any: ...
    @property
    def closed(self) -> bool: ...
    def read(self, size: int = ..., /) -> ReadableBuffer: ...
    # Optional: def read1(self, size: int, /) -> ReadableBuffer: ...
    def write(self, b: bytes, /) -> object: ...
    def flush(self) -> object: ...
    def close(self) -> object: ...
    def seekable(self) -> bool: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def truncate(self, size: int, /) -> int: ...
    def fileno(self) -> int: ...
    def isatty(self) -> bool: ...
    # Optional: Only needs to be present if seekable() returns True.
    # def seek(self, offset: Literal[0], whence: Literal[2]) -> int: ...
    # def tell(self) -> int: ...

_BufferT_co = TypeVar("_BufferT_co", bound=_WrappedBuffer, default=_WrappedBuffer, covariant=True)

class TextIOWrapper(TextIOBase, TextIO, Generic[_BufferT_co]):  # type: ignore[misc]  # incompatible definitions of write in the base classes
    def __init__(
        self,
        buffer: _BufferT_co,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        line_buffering: bool = False,
        write_through: bool = False,
    ) -> None: ...
    # Equals the "buffer" argument passed in to the constructor.
    @property
    def buffer(self) -> _BufferT_co: ...  # type: ignore[override]
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
    def writelines(self, lines: Iterable[str], /) -> None: ...  # type: ignore[override]
    def readline(self, size: int = -1, /) -> str: ...  # type: ignore[override]
    def readlines(self, hint: int = -1, /) -> list[str]: ...  # type: ignore[override]
    # Equals the "buffer" argument passed in to the constructor.
    def detach(self) -> _BufferT_co: ...  # type: ignore[override]
    # TextIOWrapper's version of seek only supports a limited subset of
    # operations.
    def seek(self, cookie: int, whence: int = 0, /) -> int: ...

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
    def setstate(self, state: tuple[bytes, int], /) -> None: ...

if sys.version_info >= (3, 10):
    @overload
    def text_encoding(encoding: None, stacklevel: int = 2, /) -> Literal["locale", "utf-8"]: ...
    @overload
    def text_encoding(encoding: _T, stacklevel: int = 2, /) -> _T: ...
