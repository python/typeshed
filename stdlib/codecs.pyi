import types
from _codecs import *
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from abc import abstractmethod
from collections.abc import Callable, Generator, Iterable
from typing import Any, BinaryIO, Final, Literal, Protocol, TextIO, type_check_only
from typing_extensions import Self

__all__ = [
    "register",
    "lookup",
    "open",
    "EncodedFile",
    "BOM",
    "BOM_BE",
    "BOM_LE",
    "BOM32_BE",
    "BOM32_LE",
    "BOM64_BE",
    "BOM64_LE",
    "BOM_UTF8",
    "BOM_UTF16",
    "BOM_UTF16_LE",
    "BOM_UTF16_BE",
    "BOM_UTF32",
    "BOM_UTF32_LE",
    "BOM_UTF32_BE",
    "CodecInfo",
    "Codec",
    "IncrementalEncoder",
    "IncrementalDecoder",
    "StreamReader",
    "StreamWriter",
    "StreamReaderWriter",
    "StreamRecoder",
    "getencoder",
    "getdecoder",
    "getincrementalencoder",
    "getincrementaldecoder",
    "getreader",
    "getwriter",
    "encode",
    "decode",
    "iterencode",
    "iterdecode",
    "strict_errors",
    "ignore_errors",
    "replace_errors",
    "xmlcharrefreplace_errors",
    "backslashreplace_errors",
    "namereplace_errors",
    "register_error",
    "lookup_error",
]

BOM32_BE: Final = b"\xfe\xff"
BOM32_LE: Final = b"\xff\xfe"
BOM64_BE: Final = b"\x00\x00\xfe\xff"
BOM64_LE: Final = b"\xff\xfe\x00\x00"

@type_check_only
class _WritableStream(SupportsWrite[bytes], Protocol):
    def seek(self, offset: int, whence: int, /) -> object: ...
    def close(self) -> object: ...

@type_check_only
class _ReadableStream(SupportsRead[bytes], Protocol):
    def seek(self, offset: int, whence: int, /) -> object: ...
    def close(self) -> object: ...

@type_check_only
class _Stream(_WritableStream, _ReadableStream, Protocol): ...

# TODO: this only satisfies the most common interface, where
# bytes is the raw form and str is the cooked form.
# In the long run, both should become template parameters maybe?
# There *are* bytes->bytes and str->str encodings in the standard library.
# They were much more common in Python 2 than in Python 3.

class _Encoder(Protocol):
    def __call__(self, input: str, errors: str = ..., /) -> tuple[bytes, int]: ...  # signature of Codec().encode

class _Decoder(Protocol):
    def __call__(self, input: bytes, errors: str = ..., /) -> tuple[str, int]: ...  # signature of Codec().decode

class _StreamReader(Protocol):
    def __call__(self, stream: _ReadableStream, errors: str = ..., /) -> StreamReader: ...

class _StreamWriter(Protocol):
    def __call__(self, stream: _WritableStream, errors: str = ..., /) -> StreamWriter: ...

class _IncrementalEncoder(Protocol):
    def __call__(self, errors: str = ...) -> IncrementalEncoder: ...

class _IncrementalDecoder(Protocol):
    def __call__(self, errors: str = ...) -> IncrementalDecoder: ...

class CodecInfo(tuple[_Encoder, _Decoder, _StreamReader, _StreamWriter]):
    _is_text_encoding: bool
    @property
    def encode(self) -> _Encoder: ...
    @property
    def decode(self) -> _Decoder: ...
    @property
    def streamreader(self) -> _StreamReader: ...
    @property
    def streamwriter(self) -> _StreamWriter: ...
    @property
    def incrementalencoder(self) -> _IncrementalEncoder: ...
    @property
    def incrementaldecoder(self) -> _IncrementalDecoder: ...
    name: str
    def __new__(
        cls,
        encode: _Encoder,
        decode: _Decoder,
        streamreader: _StreamReader | None = None,
        streamwriter: _StreamWriter | None = None,
        incrementalencoder: _IncrementalEncoder | None = None,
        incrementaldecoder: _IncrementalDecoder | None = None,
        name: str | None = None,
        *,
        _is_text_encoding: bool | None = None,
    ) -> Self: ...

def getencoder(encoding: str) -> _Encoder: ...
def getdecoder(encoding: str) -> _Decoder: ...
def getincrementalencoder(encoding: str) -> _IncrementalEncoder: ...
def getincrementaldecoder(encoding: str) -> _IncrementalDecoder: ...
def getreader(encoding: str) -> _StreamReader: ...
def getwriter(encoding: str) -> _StreamWriter: ...
def open(
    filename: str, mode: str = "r", encoding: str | None = None, errors: str = "strict", buffering: int = -1
) -> StreamReaderWriter: ...
def EncodedFile(file: _Stream, data_encoding: str, file_encoding: str | None = None, errors: str = "strict") -> StreamRecoder: ...
def iterencode(iterator: Iterable[str], encoding: str, errors: str = "strict") -> Generator[bytes, None, None]: ...
def iterdecode(iterator: Iterable[bytes], encoding: str, errors: str = "strict") -> Generator[str, None, None]: ...

BOM: Final[Literal[b"\xff\xfe", b"\xfe\xff"]]  # depends on `sys.byteorder`
BOM_BE: Final = b"\xfe\xff"
BOM_LE: Final = b"\xff\xfe"
BOM_UTF8: Final = b"\xef\xbb\xbf"
BOM_UTF16: Final[Literal[b"\xff\xfe", b"\xfe\xff"]]  # depends on `sys.byteorder`
BOM_UTF16_BE: Final = b"\xfe\xff"
BOM_UTF16_LE: Final = b"\xff\xfe"
BOM_UTF32: Final[Literal[b"\xff\xfe\x00\x00", b"\x00\x00\xfe\xff"]]  # depends on `sys.byteorder`
BOM_UTF32_BE: Final = b"\x00\x00\xfe\xff"
BOM_UTF32_LE: Final = b"\xff\xfe\x00\x00"

def strict_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...
def replace_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...
def ignore_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...
def xmlcharrefreplace_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...
def backslashreplace_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...
def namereplace_errors(exception: UnicodeError, /) -> tuple[str | bytes, int]: ...

class Codec:
    # These are sort of @abstractmethod but sort of not.
    # The StreamReader and StreamWriter subclasses only implement one.
    def encode(self, input: str, errors: str = "strict") -> tuple[bytes, int]: ...
    def decode(self, input: bytes, errors: str = "strict") -> tuple[str, int]: ...

class IncrementalEncoder:
    errors: str
    def __init__(self, errors: str = "strict") -> None: ...
    @abstractmethod
    def encode(self, input: str, final: bool = False) -> bytes: ...
    def reset(self) -> None: ...
    # documentation says int but str is needed for the subclass.
    def getstate(self) -> int | str: ...
    def setstate(self, state: int | str) -> None: ...

class IncrementalDecoder:
    errors: str
    def __init__(self, errors: str = "strict") -> None: ...
    @abstractmethod
    def decode(self, input: ReadableBuffer, final: bool = False) -> str: ...
    def reset(self) -> None: ...
    def getstate(self) -> tuple[bytes, int]: ...
    def setstate(self, state: tuple[bytes, int]) -> None: ...

# These are not documented but used in encodings/*.py implementations.
class BufferedIncrementalEncoder(IncrementalEncoder):
    buffer: str
    def __init__(self, errors: str = "strict") -> None: ...
    @abstractmethod
    def _buffer_encode(self, input: str, errors: str, final: bool) -> tuple[bytes, int]: ...
    def encode(self, input: str, final: bool = False) -> bytes: ...

class BufferedIncrementalDecoder(IncrementalDecoder):
    buffer: bytes
    def __init__(self, errors: str = "strict") -> None: ...
    @abstractmethod
    def _buffer_decode(self, input: ReadableBuffer, errors: str, final: bool) -> tuple[str, int]: ...
    def decode(self, input: ReadableBuffer, final: bool = False) -> str: ...

# TODO: it is not possible to specify the requirement that all other
# attributes and methods are passed-through from the stream.
class StreamWriter(Codec):
    stream: _WritableStream
    errors: str
    def __init__(self, stream: _WritableStream, errors: str = "strict") -> None: ...
    def write(self, object: str) -> None: ...
    def writelines(self, list: Iterable[str]) -> None: ...
    def reset(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def __getattr__(self, name: str, getattr: Callable[[Any, str], Any] = ...) -> Any: ...

class StreamReader(Codec):
    stream: _ReadableStream
    errors: str
    def __init__(self, stream: _ReadableStream, errors: str = "strict") -> None: ...
    def read(self, size: int = -1, chars: int = -1, firstline: bool = False) -> str: ...
    def readline(self, size: int | None = None, keepends: bool = True) -> str: ...
    def readlines(self, sizehint: int | None = None, keepends: bool = True) -> list[str]: ...
    def reset(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> str: ...
    def __getattr__(self, name: str, getattr: Callable[[Any, str], Any] = ...) -> Any: ...

# Doesn't actually inherit from TextIO, but wraps a BinaryIO to provide text reading and writing
# and delegates attributes to the underlying binary stream with __getattr__.
class StreamReaderWriter(TextIO):
    stream: _Stream
    def __init__(self, stream: _Stream, Reader: _StreamReader, Writer: _StreamWriter, errors: str = "strict") -> None: ...
    def read(self, size: int = -1) -> str: ...
    def readline(self, size: int | None = None) -> str: ...
    def readlines(self, sizehint: int | None = None) -> list[str]: ...
    def __next__(self) -> str: ...
    def __iter__(self) -> Self: ...
    def write(self, data: str) -> None: ...  # type: ignore[override]
    def writelines(self, list: Iterable[str]) -> None: ...
    def reset(self) -> None: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...  # type: ignore[override]
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    # These methods don't actually exist directly, but they are needed to satisfy the TextIO
    # interface. At runtime, they are delegated through __getattr__.
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def truncate(self, size: int | None = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def writable(self) -> bool: ...

class StreamRecoder(BinaryIO):
    def __init__(
        self,
        stream: _Stream,
        encode: _Encoder,
        decode: _Decoder,
        Reader: _StreamReader,
        Writer: _StreamWriter,
        errors: str = "strict",
    ) -> None: ...
    def read(self, size: int = -1) -> bytes: ...
    def readline(self, size: int | None = None) -> bytes: ...
    def readlines(self, sizehint: int | None = None) -> list[bytes]: ...
    def __next__(self) -> bytes: ...
    def __iter__(self) -> Self: ...
    # Base class accepts more types than just bytes
    def write(self, data: bytes) -> None: ...  # type: ignore[override]
    def writelines(self, list: Iterable[bytes]) -> None: ...  # type: ignore[override]
    def reset(self) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...  # type: ignore[override]
    # These methods don't actually exist directly, but they are needed to satisfy the BinaryIO
    # interface. At runtime, they are delegated through __getattr__.
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def readable(self) -> bool: ...
    def truncate(self, size: int | None = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def writable(self) -> bool: ...
