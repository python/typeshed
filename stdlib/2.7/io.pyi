# Stubs for io

# Based on https://docs.python.org/2/library/io.html

# Only a subset of functionality is included.

DEFAULT_BUFFER_SIZE = 0

from typing import List, BinaryIO, TextIO, IO, overload, Iterator, Iterable, Any, Union

def open(file: Union[str, unicode, int],
         mode: unicode = ..., buffering: int = ..., encoding: unicode = ...,
         errors: unicode = ..., newline: unicode = ...,
         closefd: bool = ...) -> IO[Any]: ...

class IOBase:
    # TODO
    ...

class BytesIO(BinaryIO):
    def __init__(self, initial_bytes: bytes = ...) -> None: ...
    # TODO getbuffer
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> bytes: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: bytes) -> None: ...
    def writelines(self, lines: Iterable[bytes]) -> None: ...
    def getvalue(self) -> bytes: ...
    def read1(self) -> bytes: ...

    def __iter__(self) -> Iterator[bytes]: ...
    def next(self) -> bytes: ...
    def __enter__(self) -> 'BytesIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class StringIO(TextIO):
    def __init__(self, initial_value: unicode = ...,
                 newline: unicode = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    name = ... # type: str
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> unicode: ...
    def readlines(self, hint: int = ...) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...
    def getvalue(self) -> unicode: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def next(self) -> unicode: ...
    def __enter__(self) -> 'StringIO': ...
    def __exit__(self, type, value, traceback) -> bool: ...

class TextIOWrapper(TextIO):
    # write_through is undocumented but used by subprocess
    def __init__(self, buffer: IO[bytes], encoding: unicode = ...,
                 errors: unicode = ..., newline: unicode = ...,
                 line_buffering: bool = ...,
                 write_through: bool = ...) -> None: ...
    # TODO see comments in BinaryIO for missing functionality
    def close(self) -> None: ...
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> unicode: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> unicode: ...
    def readlines(self, hint: int = ...) -> List[unicode]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = ...) -> int: ...
    def writable(self) -> bool: ...
    def write(self, s: unicode) -> None: ...
    def writelines(self, lines: Iterable[unicode]) -> None: ...

    def __iter__(self) -> Iterator[unicode]: ...
    def next(self) -> unicode: ...
    def __enter__(self) -> StringIO: ...
    def __exit__(self, type, value, traceback) -> bool: ...

class BufferedIOBase(IOBase): ...
