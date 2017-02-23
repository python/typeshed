# Stubs for io

from typing import (
    List, BinaryIO, TextIO, Iterator, Union, Optional, Callable, Tuple, Any, IO, Iterable
)
import builtins
import codecs
import sys
from types import TracebackType

DEFAULT_BUFFER_SIZE = ...  # type: int

SEEK_SET = ...  # type: int
SEEK_CUR = ...  # type: int
SEEK_END = ...  # type: int

open = builtins.open

# FIXME when mypy handle condtional, we can uncomment the next block and remove
# the temporary fix
# if sys.version_info >= (3, 3):
#     BlockingIOError = BlockingIOError
#     class UnsupportedOperation(OSError, ValueError): ...
# else:
#     class BlockingIOError(IOError):
#         characters_written = ...  # type: int
#     class UnsupportedOperation(IOError, ValueError): ...
class BlockingIOError(OSError):
    characters_written = ...  # type: int
class UnsupportedOperation(OSError, ValueError): ...


class IOBase:
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self) -> 'IOBase': ...
    def __exit__(self, exc_type: Optional[type], exc_val: Optional[Exception],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def readlines(self, hint: int = ...) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    def writelines(self, lines: Iterable[Union[bytes, bytearray]]) -> None: ...
    if sys.version_info >= (3, 4):
        def readline(self, size: int = ...) -> bytes: ...
        def __del__(self) -> None: ...
    else:
        def readline(self, limit: int = ...) -> bytes: ...
    if sys.version_info >= (3, 2):
        closed = ...  # type: bool
    else:
        def closed(self) -> bool: ...

class RawIOBase(IOBase):
    def readall(self) -> bytes: ...
    def readinto(self, b: bytearray) -> Optional[int]: ...
    def write(self, b: Union[bytes, bytearray]) -> Optional[int]: ...
    if sys.version_info >= (3, 4):
        def read(self, size: int = ...) -> Optional[bytes]: ...
    else:
        def read(self, n: int = ...) -> Optional[bytes]: ...

class BufferedIOBase(IOBase):
    def detach(self) -> RawIOBase: ...
    def readinto(self, b: bytearray) -> int: ...
    def write(self, b: Union[bytes, bytearray]) -> int: ...
    if sys.version_info >= (3, 5):
        def readinto1(self, b: bytearray) -> int: ...
    if sys.version_info >= (3, 4):
        def read(self, size: Optional[int] = ...) -> bytes: ...
        def read1(self, size: int = ...) -> bytes: ...
    else:
        def read(self, n: Optional[int] = ...) -> bytes: ...
        def read1(self, n: int = ...) -> bytes: ...


class FileIO(RawIOBase):
    mode = ...  # type: str
    name = ...  # type: Union[int, str]
    if sys.version_info >= (3, 3):
        def __init__(
            self,
            name: Union[str, bytes, int],
            mode: str = ...,
            closefd: bool = ...,
            opener: Optional[Callable[[Union[int, str], str], int]] = ...
        ) -> None: ...
    else:
        def __init__(self, name: Union[str, bytes, int],
                     mode: str = ..., closefd: bool = ...) -> None: ...

# TODO should extend from BufferedIOBase
class BytesIO(BinaryIO):
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    def getvalue(self) -> bytes: ...
    if sys.version_info >= (3, 2):
        def getbuffer(self) -> memoryview: ...
    # copied from IOBase
    def __iter__(self) -> Iterator[bytes]: ...
    def __next__(self) -> bytes: ...
    def __enter__(self) -> 'BytesIO': ...
    def __exit__(self, t: type = None, value: BaseException = None,
                 traceback: Any = None) -> bool: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def readlines(self, hint: int = ...) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    # TODO should be the next line instead
    # def writelines(self, lines: List[Union[bytes, bytearray]]) -> None: ...
    def writelines(self, lines: Any) -> None: ...
    if sys.version_info >= (3, 4):
        def readline(self, size: int = ...) -> bytes: ...
        def __del__(self) -> None: ...
    else:
        def readline(self, limit: int = ...): ...
    if sys.version_info >= (3, 2):
        closed = ...  # type: bool
    else:
        def closed(self) -> bool: ...
    # copied from BufferedIOBase
    def detach(self) -> RawIOBase: ...
    def readinto(self, b: bytearray) -> int: ...
    def write(self, b: Union[bytes, bytearray]) -> int: ...
    if sys.version_info >= (3, 5):
        def readinto1(self, b: bytearray) -> int: ...
    if sys.version_info >= (3, 4):
        def read(self, size: Optional[int] = ...) -> bytes: ...
        def read1(self, size: int = ...) -> bytes: ...
    else:
        def read(self, n: Optional[int] = ...) -> bytes: ...
        def read1(self, n: int = ...) -> bytes: ...

class BufferedReader(BufferedIOBase):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    if sys.version_info >= (3, 4):
        def peek(self, size: int = ...) -> bytes: ...
    else:
        def peek(self, n: int = ...) -> bytes: ...

class BufferedWriter(BufferedIOBase):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def flush(self) -> None: ...
    def write(self, b: Union[bytes, bytearray]) -> int: ...

class BufferedRandom(BufferedReader, BufferedWriter):
    def __init__(self, raw: RawIOBase, buffer_size: int = ...) -> None: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def tell(self) -> int: ...

class BufferedRWPair(BufferedIOBase):
    def __init__(self, reader: RawIOBase, writer: RawIOBase,
                 buffer_size: int = ...) -> None: ...


class TextIOBase(IOBase):
    encoding = ...  # type: str
    errors = ...  # type: Optional[str]
    newlines = ...  # type: Union[str, Tuple[str, ...], None]
    def __iter__(self) -> Iterator[str]: ...  # type: ignore
    def __next__(self) -> str: ...  # type: ignore
    def __enter__(self) -> 'TextIOBase': ...
    def detach(self) -> IOBase: ...
    def write(self, s: str) -> int: ...
    if sys.version_info >= (3, 4):
        def readline(self, size: int = ...) -> str: ...  # type: ignore
        def read(self, size: Optional[int] = ...) -> str: ...
    elif sys.version_info >= (3, 2):
        def readline(self, limit: int = ...) -> str: ...  # type: ignore
    else:
        def readline(self) -> str: ...
    if sys.version_info >= (3, 2):
        def seek(self, offset: int, whence: int = ...) -> int: ...
        def tell(self) -> int: ...

# TODO should extend from TextIOBase
class TextIOWrapper(TextIO):
    line_buffering = ...  # type: bool
    # TODO uncomment after fixing mypy about using write_through
    # if sys.version_info >= (3, 3):
    #    def __init__(self, buffer: IO[bytes], encoding: str = ...,
    #                 errors: Optional[str] = ..., newline: Optional[str] = ...,
    #                 line_buffering: bool = ..., write_through: bool = ...) \
    #                 -> None: ...
    # else:
    #    def __init__(self, buffer: IO[bytes],
    #                 encoding: str = ..., errors: Optional[str] = ...,
    #                 newline: Optional[str] = ..., line_buffering: bool = ...) \
    #                 -> None: ...
    def __init__(
        self,
        buffer: IO[bytes],
        encoding: str = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
        line_buffering: bool = ...,
        write_through: bool = ...
    ) -> None: ...
    # copied from IOBase
    def __exit__(self, t: type = None, value: BaseException = None,
                 traceback: Any = None) -> bool: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def readlines(self, hint: int = ...) -> List[str]: ...
    def seekable(self) -> bool: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    # TODO should be the next line instead
    # def writelines(self, lines: List[str]) -> None: ...
    def writelines(self, lines: Any) -> None: ...
    if sys.version_info >= (3, 4):
        def __del__(self) -> None: ...
    if sys.version_info >= (3, 2):
        closed = ...  # type: bool
    else:
        def closed(self) -> bool: ...
    # copied from TextIOBase
    encoding = ...  # type: str
    errors = ...  # type: Optional[str]
    newlines = ...  # type: Union[str, Tuple[str, ...], None]
    def __iter__(self) -> Iterator[str]: ...
    def __next__(self) -> str: ...
    def __enter__(self) -> 'TextIO': ...
    def detach(self) -> IOBase: ...
    def write(self, s: str) -> int: ...
    if sys.version_info >= (3, 4):
        def readline(self, size: int = ...) -> str: ...
        def read(self, size: Optional[int] = ...) -> str: ...
    elif sys.version_info >= (3, 2):
        def readline(self, limit: int = ...) -> str: ...
    else:
        def readline(self) -> str: ...
    if sys.version_info >= (3, 2):
        def seek(self, offset: int, whence: int = ...) -> int: ...
        def tell(self) -> int: ...

class StringIO(TextIOWrapper):
    def __init__(self, initial_value: str = ...,
                 newline: Optional[str] = ...) -> None: ...
    name = ...  # type: str
    def getvalue(self) -> str: ...

class IncrementalNewlineDecoder(codecs.IncrementalDecoder): ...
