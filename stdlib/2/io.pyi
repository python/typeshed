# Stubs for io

# Based on https://docs.python.org/2/library/io.html

# Only a subset of functionality is included.

from typing import List, BinaryIO, TextIO, IO, overload, Iterator, Iterable, Any, Union, Optional
import _io

from _io import (DEFAULT_BUFFER_SIZE, BlockingIOError, UnsupportedOperation,
                 open, FileIO, BytesIO, StringIO, BufferedReader,
                 BufferedWriter, BufferedRWPair, BufferedRandom,
                 IncrementalNewlineDecoder, TextIOWrapper)

def _OpenWrapper(file: Union[str, unicode, int],
         mode: unicode = ..., buffering: int = ..., encoding: unicode = ...,
         errors: unicode = ..., newline: unicode = ...,
         closefd: bool = ...) -> IO[Any]: ...

SEEK_SET = ...  # type: int
SEEK_CUR = ...  # type: int
SEEK_END = ...  # type: int


class IOBase(_io._IOBase): ...

class RawIOBase(_io._RawIOBase, IOBase):
    pass

class BufferedIOBase(_io._BufferedIOBase, IOBase):
    pass

class TextIOBase(_io._TextIOBase, IOBase):  # type: ignore
    pass
