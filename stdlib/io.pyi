import abc
import sys
from _io import (
    DEFAULT_BUFFER_SIZE as DEFAULT_BUFFER_SIZE,
    BlockingIOError as BlockingIOError,
    BufferedRandom as BufferedRandom,
    BufferedReader as BufferedReader,
    BufferedRWPair as BufferedRWPair,
    BufferedWriter as BufferedWriter,
    BytesIO as BytesIO,
    FileIO as FileIO,
    IncrementalNewlineDecoder as IncrementalNewlineDecoder,
    StringIO as StringIO,
    TextIOWrapper as TextIOWrapper,
    _BufferedIOBase,
    _IOBase,
    _RawIOBase,
    _TextIOBase,
    open as open,
)
from typing_extensions import Literal

__all__ = [
    "BlockingIOError",
    "open",
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

if sys.version_info >= (3, 10):
    from _io import text_encoding as text_encoding

if sys.version_info >= (3, 8):
    from _io import open_code as open_code

    __all__ += ["open_code"]

if sys.version_info >= (3, 11):
    __all__ += ["DEFAULT_BUFFER_SIZE", "IncrementalNewlineDecoder", "text_encoding"]

SEEK_SET: Literal[0]
SEEK_CUR: Literal[1]
SEEK_END: Literal[2]

class UnsupportedOperation(OSError, ValueError): ...
class IOBase(_IOBase, metaclass=abc.ABCMeta): ...
class RawIOBase(_RawIOBase, IOBase): ...
class BufferedIOBase(_BufferedIOBase, IOBase): ...
class TextIOBase(_TextIOBase, IOBase): ...
