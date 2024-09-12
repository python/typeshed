from _typeshed import ReadableBuffer, SupportsRead
from re import Pattern
from typing import Final, Literal, Protocol

from .compat import StreamTextType
from .error import StreamMark, YAMLError
from .main import YAML

# One of codecs.{utf_16_le_decode, utf_16_be_decode, utf_8_decode}
class _BufferDecoder(Protocol):
    def __call__(data: ReadableBuffer, errors: str | None = None, final: bool = False, /) -> tuple[str, int]: ...

__all__ = ["Reader", "ReaderError"]

class ReaderError(YAMLError):
    name: str | None
    character: int
    position: int
    encoding: str
    reason: str
    def __init__(self, name: str | None, position: int, character: int, encoding: str, reason: str) -> None: ...

class Reader:
    loader: YAML | None
    def __init__(self, stream: StreamTextType | None, loader: YAML | None = None) -> None: ...
    name: str | None
    stream_pointer: int
    eof: bool
    buffer: str
    pointer: int
    raw_buffer: str | bytes | None
    raw_decode: _BufferDecoder | None
    encoding: Literal["utf-16-le", "utf-16-be", "utf-8"] | None
    index: int
    line: int
    column: int
    def reset_reader(self) -> None: ...
    @property
    def stream(self) -> SupportsRead[str | bytes] | None: ...
    @stream.setter
    def stream(self, val: StreamTextType | None, /) -> None: ...
    def peek(self, index: int = 0) -> str: ...
    def prefix(self, length: int = 1) -> str: ...
    def forward_1_1(self, length: int = 1) -> None: ...
    def forward(self, length: int = 1) -> None: ...
    def get_mark(self) -> StreamMark: ...
    def determine_encoding(self) -> None: ...
    NON_PRINTABLE: Final[Pattern[str]]
    def check_printable(self, data: str) -> None: ...
    def update(self, length: int) -> None: ...
    def update_raw(self, size: int | None = None) -> None: ...
