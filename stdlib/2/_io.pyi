from typing import Any, AnyStr, BinaryIO, IO, TextIO, Iterable, Iterator, List, Optional, Type, Tuple, Union

DEFAULT_BUFFER_SIZE = ...  # type: int

class BlockingIOError(IOError):
    characters_written = ...  # type: int

class UnsupportedOperation(ValueError, IOError): ...

class _IOBase(BinaryIO):
    @property
    def closed(self) -> bool: ...
    def _checkClosed(self) -> None: ...
    def _checkReadable(self) -> None: ...
    def _checkSeekable(self) -> None: ...
    def _checkWritable(self) -> None: ...
    # All these methods are concrete here (you can instantiate this)
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: Optional[int] = ...) -> int: ...
    def writable(self) -> bool: ...
    def __exit__(self, type, value, traceback) -> bool: ...
    # This just returns self:
    def __iter__(self) -> Iterator[Any]: ...
    # The parameter type of writelines[s]() is determined by that of write():
    def writelines(self, lines: Iterable[AnyStr]) -> None: ...
    # The return type of readline[s]() and next() is determined by that of read():
    def readline(self, limit: int = ...) -> Any: ...
    def readlines(self, hint: int = ...) -> list[AnyStr]: ...
    def next(self) -> Any: ...

class _BufferedIOBase(_IOBase):
    def read1(self, size: int) -> Any: ...
    def read(self, size: int = ...) -> Any: ...
    def readinto(self, buffer: bytearray) -> int: ...
    def write(self, s: Any) -> int: ...
    def detach(self) -> "_BufferedIOBase": ...
    def __enter__(self) -> '_BufferedIOBase': ...

class BufferedRWPair(_BufferedIOBase):
    def __init__(self, reader: _RawIOBase, writer: _RawIOBase) -> None: ...
    def peek(self, n: int = ...) -> Any: ...
    def __enter__(self) -> 'BufferedRWPair': ...

class BufferedRandom(_BufferedIOBase):
    mode = ...  # type: str
    name = ...  # type: str
    raw = ...  # type: _IOBase
    def __init__(self, raw: _IOBase,
                 buffer_size: int = ...,
                 max_buffer_size: int = ...) -> None: ...
    def peek(self, n: int = ...) -> bytes: ...
    def __enter__(self) -> 'BufferedRandom': ...

class BufferedReader(_BufferedIOBase):
    mode = ...  # type: str
    name = ...  # type: str
    raw = ...  # type: _IOBase
    def __init__(self, raw: _IOBase, buffer_size: int = ...) -> None: ...
    def peek(self, n: int = ...) -> bytes: ...
    def __enter__(self) -> 'BufferedReader': ...

class BufferedWriter(_BufferedIOBase):
    name = ...  # type: str
    raw = ...  # type: _IOBase
    mode = ...  # type: str
    def __init__(self, raw: _IOBase,
                 buffer_size: int = ...,
                 max_buffer_size: int = ...) -> None: ...
    def __enter__(self) -> 'BufferedWriter': ...

class BytesIO(_BufferedIOBase):  # type: ignore
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    def __setstate__(self, tuple) -> None: ...
    def __getstate__(self) -> tuple: ...
    def getvalue(self) -> bytes: ...
    def write(self, s: bytes) -> int: ...
    def writelines(self, lines: Iterable[bytes]) -> None: ...  # type: ignore
    def read1(self, size: int) -> bytes: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def next(self) -> bytes: ...
    def __enter__(self) -> 'BytesIO': ...

class _RawIOBase(_IOBase):
    def readall(self) -> str: ...
    def read(self, size: int = ...) -> str: ...  # type: ignore
    def __enter__(self) -> '_RawIOBase': ...

class FileIO(_RawIOBase, BytesIO):  # type: ignore
    mode = ...  # type: str
    closefd = ...  # type: bool
    def __init__(self, file: str, mode: str = ...) -> None: ...
    def readinto(self, buffer: bytearray)-> int: ...
    def write(self, pbuf: str) -> int: ...
    def __enter__(self) -> 'FileIO': ...

class IncrementalNewlineDecoder(object):
    newlines = ...  # type: Union[str, unicode]
    def __init__(self, decoder, translate, z=...) -> None: ...
    def decode(self, input, final) -> Any: ...
    def getstate(self) -> Tuple[Any, int]: ...
    def setstate(self, state: Tuple[Any, int]) -> None: ...
    def reset(self) -> None: ...

class _TextIOBase(_IOBase, TextIO):  # type: ignore
    errors = ...  # type: Optional[str]
    newlines = ...  # type: Union[str, unicode]
    encoding = ...  # type: str
    def __iter__(self) -> Iterator[unicode]: ...  # type: ignore
    def next(self) -> unicode: ...  # type: ignore
    def read(self, size: int = ...) -> unicode: ...  # type: ignore
    def write(self, pbuf: unicode) -> int: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...  # type: ignore
    def detach(self) -> None: ...
    def __enter__(self) -> '_TextIOBase': ...

class StringIO(_TextIOBase):
    line_buffering = ...  # type: bool
    def __init__(self, initial_value: unicode = ...,
                 newline: unicode = ...) -> None: ...
    def __setstate__(self, state: tuple) -> None: ...
    def __getstate__(self) -> tuple: ...
    def getvalue(self) -> unicode: ...
    def __enter__(self) -> 'StringIO': ...

class TextIOWrapper(_TextIOBase):
    name = ...  # type: str
    line_buffering = ...  # type: bool
    buffer = ...  # type: BinaryIO
    _CHUNK_SIZE = ...  # type: int
    def __init__(self, buffer: IO, encoding: unicode = ...,
                 errors: unicode = ..., newline: unicode = ...,
                 line_buffering: bool = ...,
                 write_through: bool = ...) -> None: ...
    def __enter__(self) -> 'TextIOWrapper': ...

def open(file: Union[str, unicode, int],
         mode: unicode = ..., buffering: int = ..., encoding: unicode = ...,
         errors: unicode = ..., newline: unicode = ...,
         closefd: bool = ...) -> IO[Any]: ...
