from _typeshed import ReadableBuffer, StrOrBytesPath, WriteableBuffer
from compression._common import _streams
from compression.zstd import ZstdDict, _OptionsCompress, _OptionsDecompress
from typing import IO, Literal, TextIO, overload
from typing_extensions import TypeAlias

from _zstd import ZstdCompressor

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
        mode: _ReadBinaryMode = ...,
        *,
        level: None = ...,
        options: _OptionsDecompress | None = ...,
        zstd_dict: ZstdDict | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        file: _PathOrFileBinary,
        /,
        mode: _WriteBinaryMode,
        *,
        level: int | None = ...,
        options: _OptionsCompress | None = ...,
        zstd_dict: ZstdDict | None = ...,
    ) -> None: ...
    def write(self, data: ReadableBuffer, /) -> int: ...
    def flush(self, mode: Literal[1, 2] = ...) -> bytes: ...  # type: ignore[override]
    def read(self, size: int | None = ...) -> bytes: ...
    def read1(self, size: int | None = ...) -> bytes: ...
    def readinto(self, b: WriteableBuffer) -> int: ...
    def readinto1(self, b: WriteableBuffer) -> int: ...
    def readline(self, size: int | None = ...) -> bytes: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def peek(self, size: int = ...) -> bytes: ...
    @property
    def name(self) -> str | bytes: ...
    @property
    def mode(self) -> Literal["rb", "wb"]: ...

@overload
def open(
    file: _PathOrFileBinary,
    /,
    mode: _ReadBinaryMode = ...,
    *,
    level: None = ...,
    options: _OptionsDecompress | None = ...,
    zstd_dict: ZstdDict | None = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
) -> ZstdFile: ...
@overload
def open(
    file: _PathOrFileBinary,
    /,
    mode: _WriteBinaryMode,
    *,
    level: int | None = ...,
    options: _OptionsCompress | None = ...,
    zstd_dict: ZstdDict | None = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
) -> ZstdFile: ...
@overload
def open(
    file: _PathOrFileText,
    /,
    mode: _ReadTextMode,
    *,
    level: None = ...,
    options: _OptionsDecompress | None = ...,
    zstd_dict: ZstdDict | None = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
) -> TextIO: ...
@overload
def open(
    file: _PathOrFileText,
    /,
    mode: _WriteTextMode,
    *,
    level: int | None = ...,
    options: _OptionsCompress | None = ...,
    zstd_dict: ZstdDict | None = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
) -> TextIO: ...
