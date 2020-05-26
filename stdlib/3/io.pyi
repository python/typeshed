from typing import (
    List, BinaryIO, TextIO, Iterator, Union, Optional, Callable, Tuple, Type, Any, IO, Iterable
)
import builtins
import codecs
import sys
from mmap import mmap
from types import TracebackType
from typing import TypeVar

_bytearray_like = Union[bytearray, mmap]

DEFAULT_BUFFER_SIZE: int

SEEK_SET: int
SEEK_CUR: int
SEEK_END: int

_T = TypeVar('_T', bound=IOBase)

open = builtins.open

if sys.version_info >= (3, 8):
    def open_code(path: str) -> IO[bytes]: ...

BlockingIOError = builtins.BlockingIOError
class UnsupportedOperation(OSError, ValueError): ...

class IOBase:
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> Optional[bool]: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def readlines(self, __hint: int = ...) -> List[bytes]: ...
    def seek(self, __offset: int, __whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, __size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    def writelines(self, __lines: Iterable[Union[bytes, bytearray]]) -> None: ...
    def readline(self, __size: int = ...) -> bytes: ...
    def __del__(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self, msg: Optional[str] = ...) -> None: ...  # undocumented

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    def readinto(self, __buffer: bytearray) -> Optional[int]: ...
    def write(self, __b: Union[bytes, bytearray]) -> Optional[int]: ...
    def read(self, __size: int = ...) -> Optional[bytes]: ...

class BufferedIOBase(IOBase):
    raw: RawIOBase  # This is not part of the BufferedIOBase API and may not exist on some implementations.
    def detach(self) -> RawIOBase: ...
    def readinto(self, __buffer: _bytearray_like) -> int: ...
    def write(self, __buffer: Union[bytes, bytearray]) -> int: ...
    def readinto1(self, __buffer: _bytearray_like) -> int: ...
    def read(self, __size: Optional[int] = ...) -> bytes: ...
    def read1(self, __size: int = ...) -> bytes: ...


class FileIO(RawIOBase):
    mode: str
    name: Union[int, str]
    def __init__(
        self,
        file: Union[str, bytes, int],
        mode: str = ...,
        closefd: bool = ...,
        opener: Optional[Callable[[Union[int, str], str], int]] = ...
    ) -> None: ...

class BytesIO(BufferedIOBase):
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    # BytesIO does not contain a "name" field. This workaround is necessary
    # to allow BytesIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def getvalue(self) -> bytes: ...
    def getbuffer(self) -> memoryview: ...

class BufferedReader(BufferedIOBase):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def peek(self, __size: int = ...) -> bytes: ...

class BufferedWriter(BufferedIOBase):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def flush(self) -> None: ...
    def write(self, __buffer: Union[bytes, bytearray]) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def seek(self, __target: int, __whence: int = ...) -> int: ...
    def tell(self) -> int: ...

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase,
                 buffer_size: int = ...) -> None: ...


class TextIOBase(IOBase):
    encoding: str
    errors: Optional[str]
    newlines: Union[str, Tuple[str, ...], None]
    def __iter__(self) -> Iterator[str]: ...  # type: ignore
    def __next__(self) -> str: ...  # type: ignore
    def detach(self) -> BinaryIO: ...
    def write(self, s: str) -> int: ...
    def writelines(self, __lines: List[str]) -> None: ...  # type: ignore
    def readline(self, size: int = ...) -> str: ...  # type: ignore
    def readlines(self, __hint: int = ...) -> List[str]: ...  # type: ignore
    def read(self, size: Optional[int] = ...) -> str: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def tell(self) -> int: ...

# TODO should extend from TextIOBase
class TextIOWrapper(TextIO):
    line_buffering: bool
    # TODO uncomment after fixing mypy about using write_through
    # def __init__(self, buffer: IO[bytes], encoding: str = ...,
    #              errors: Optional[str] = ..., newline: Optional[str] = ...,
    #              line_buffering: bool = ..., write_through: bool = ...) \
    #              -> None: ...
    def __init__(
        self,
        buffer: BinaryIO,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        line_buffering: bool = ...,
        write_through: bool = ...
    ) -> None: ...
    @property
    def buffer(self) -> BinaryIO: ...
    if sys.version_info >= (3, 7):
        def reconfigure(
            self,
            *,
            encoding: Optional[str] = ...,
            errors: Optional[str] = ...,
            newline: Optional[str] = ...,
            line_buffering: Optional[bool] = ...,
            write_through: Optional[bool] = ...
        ) -> None: ...
    # copied from IOBase
    def __exit__(self, t: Optional[Type[BaseException]] = ..., value: Optional[BaseException] = ...,
                 traceback: Optional[TracebackType] = ...) -> Optional[bool]: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def readlines(self, __hint: int = ...) -> List[str]: ...
    def seekable(self) -> bool: ...
    def truncate(self, __size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    # TODO should be the next line instead
    # def writelines(self, lines: List[str]) -> None: ...
    def writelines(self, __lines: Any) -> None: ...
    def __del__(self) -> None: ...
    closed: bool
    # copied from TextIOBase
    encoding: str
    errors: Optional[str]
    newlines: Union[str, Tuple[str, ...], None]
    def __iter__(self) -> Iterator[str]: ...
    def __next__(self) -> str: ...
    def __enter__(self) -> TextIO: ...
    def detach(self) -> BinaryIO: ...
    def write(self, __text: str) -> int: ...
    def readline(self, __size: int = ...) -> str: ...
    def read(self, __size: Optional[int] = ...) -> str: ...
    def seek(self, __cookie: int, __whence: int = ...) -> int: ...
    def tell(self) -> int: ...

class StringIO(TextIOWrapper):
    def __init__(self, initial_value: Optional[str] = ...,
                 newline: Optional[str] = ...) -> None: ...
    # StringIO does not contain a "name" field. This workaround is necessary
    # to allow StringIO sub-classes to add this field, as it is defined
    # as a read-only property on IO[].
    name: Any
    def getvalue(self) -> str: ...
    def __enter__(self) -> StringIO: ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder):
    def __init__(self, decoder: Optional[codecs.IncrementalDecoder],
                 translate: bool, errors: str = ...) -> None: ...
    def decode(self, input: Union[bytes, str], final: bool = ...) -> str: ...
