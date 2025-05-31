from _typeshed import ReadableBuffer, StrOrBytesPath, WriteableBuffer
from collections.abc import Mapping
from compression._common import _streams
from compression.zstd import ZstdDict
from io import TextIOWrapper
from typing import IO, Literal, overload
from typing_extensions import TypeAlias

from _zstd import ZstdCompressor, _ZstdCompressorFlushBlock, _ZstdCompressorFlushFrame

__all__ = ("ZstdFile", "open")

_ReadBinaryMode: TypeAlias = Literal["r", "rb"]
_WriteBinaryMode: TypeAlias = Literal["w", "wb", "x", "xb", "a", "ab"]
_ReadTextMode: TypeAlias = Literal["rt"]
_WriteTextMode: TypeAlias = Literal["wt", "xt", "at"]
_PathOrFileBinary: TypeAlias = StrOrBytesPath | IO[bytes]
_PathOrFileText: TypeAlias = StrOrBytesPath | IO[str]

class ZstdFile(_streams.BaseStream):
    FLUSH_BLOCK = ZstdCompressor.FLUSH_BLOCK
    FLUSH_FRAME = ZstdCompressor.FLUSH_FRAME

    @overload
    def __init__(
        self,
        file: _PathOrFileBinary,
        /,
        mode: _ReadBinaryMode = "r",
        *,
        level: None = None,
        options: Mapping[int, int] | None = None,
        zstd_dict: ZstdDict | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        file: _PathOrFileBinary,
        /,
        mode: _WriteBinaryMode,
        *,
        level: int | None = None,
        options: Mapping[int, int] | None = None,
        zstd_dict: ZstdDict | None = None,
    ) -> None: ...
    def write(self, data: ReadableBuffer, /) -> int: ...
    def flush(self, mode: _ZstdCompressorFlushBlock | _ZstdCompressorFlushFrame = 1) -> bytes: ...  # type: ignore[override]
    def read(self, size: int | None = -1) -> bytes: ...
    def read1(self, size: int | None = -1) -> bytes: ...
    def readinto(self, b: WriteableBuffer) -> int: ...
    def readinto1(self, b: WriteableBuffer) -> int: ...
    def readline(self, size: int | None = -1) -> bytes: ...
    def seek(self, offset: int, whence: int = 0) -> int: ...
    def peek(self, size: int = -1) -> bytes: ...
    @property
    def name(self) -> str | bytes: ...
    @property
    def mode(self) -> Literal["rb", "wb"]: ...

@overload
def open(
    file: _PathOrFileBinary,
    /,
    mode: _ReadBinaryMode = "rb",
    *,
    level: None = None,
    options: Mapping[int, int] | None = None,
    zstd_dict: ZstdDict | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> ZstdFile: ...
@overload
def open(
    file: _PathOrFileBinary,
    /,
    mode: _WriteBinaryMode,
    *,
    level: int | None = None,
    options: Mapping[int, int] | None = None,
    zstd_dict: ZstdDict | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> ZstdFile: ...
@overload
def open(
    file: _PathOrFileText,
    /,
    mode: _ReadTextMode,
    *,
    level: None = None,
    options: Mapping[int, int] | None = None,
    zstd_dict: ZstdDict | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> TextIOWrapper: ...
@overload
def open(
    file: _PathOrFileText,
    /,
    mode: _WriteTextMode,
    *,
    level: int | None = None,
    options: Mapping[int, int] | None = None,
    zstd_dict: ZstdDict | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> TextIOWrapper: ...
