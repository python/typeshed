import io
from _typeshed import ReadableBuffer, StrOrBytesPath
from collections.abc import Mapping, Sequence
from typing import IO, Any, TextIO, overload
from typing_extensions import Literal, Self, TypeAlias, final

__all__ = [
    "CHECK_NONE",
    "CHECK_CRC32",
    "CHECK_CRC64",
    "CHECK_SHA256",
    "CHECK_ID_MAX",
    "CHECK_UNKNOWN",
    "FILTER_LZMA1",
    "FILTER_LZMA2",
    "FILTER_DELTA",
    "FILTER_X86",
    "FILTER_IA64",
    "FILTER_ARM",
    "FILTER_ARMTHUMB",
    "FILTER_POWERPC",
    "FILTER_SPARC",
    "FORMAT_AUTO",
    "FORMAT_XZ",
    "FORMAT_ALONE",
    "FORMAT_RAW",
    "MF_HC3",
    "MF_HC4",
    "MF_BT2",
    "MF_BT3",
    "MF_BT4",
    "MODE_FAST",
    "MODE_NORMAL",
    "PRESET_DEFAULT",
    "PRESET_EXTREME",
    "LZMACompressor",
    "LZMADecompressor",
    "LZMAFile",
    "LZMAError",
    "open",
    "compress",
    "decompress",
    "is_check_supported",
]

_OpenBinaryWritingMode: TypeAlias = Literal["w", "wb", "x", "xb", "a", "ab"]
_OpenTextWritingMode: TypeAlias = Literal["wt", "xt", "at"]

_PathOrFile: TypeAlias = StrOrBytesPath | IO[bytes]

_FilterChain: TypeAlias = Sequence[Mapping[str, Any]]

FORMAT_AUTO: Literal[0]
FORMAT_XZ: Literal[1]
FORMAT_ALONE: Literal[2]
FORMAT_RAW: Literal[3]
CHECK_NONE: Literal[0]
CHECK_CRC32: Literal[1]
CHECK_CRC64: Literal[4]
CHECK_SHA256: Literal[10]
CHECK_ID_MAX: Literal[15]
CHECK_UNKNOWN: Literal[16]
FILTER_LZMA1: int  # v big number
FILTER_LZMA2: Literal[33]
FILTER_DELTA: Literal[3]
FILTER_X86: Literal[4]
FILTER_IA64: Literal[6]
FILTER_ARM: Literal[7]
FILTER_ARMTHUMB: Literal[8]
FILTER_SPARC: Literal[9]
FILTER_POWERPC: Literal[5]
MF_HC3: Literal[3]
MF_HC4: Literal[4]
MF_BT2: Literal[18]
MF_BT3: Literal[19]
MF_BT4: Literal[20]
MODE_FAST: Literal[1]
MODE_NORMAL: Literal[2]
PRESET_DEFAULT: Literal[6]
PRESET_EXTREME: int  # v big number

# from _lzma.c
@final
class LZMADecompressor:
    def __init__(self, format: int | None = ..., memlimit: int | None = ..., filters: _FilterChain | None = ...) -> None: ...
    def decompress(self, data: ReadableBuffer, max_length: int = -1) -> bytes: ...
    @property
    def check(self) -> int: ...
    @property
    def eof(self) -> bool: ...
    @property
    def unused_data(self) -> bytes: ...
    @property
    def needs_input(self) -> bool: ...

# from _lzma.c
@final
class LZMACompressor:
    def __init__(
        self, format: int | None = ..., check: int = ..., preset: int | None = ..., filters: _FilterChain | None = ...
    ) -> None: ...
    def compress(self, __data: ReadableBuffer) -> bytes: ...
    def flush(self) -> bytes: ...

class LZMAError(Exception): ...

class LZMAFile(io.BufferedIOBase, IO[bytes]):  # type: ignore[misc]  # incompatible definitions of writelines in the base classes
    def __init__(
        self,
        filename: _PathOrFile | None = None,
        mode: str = "r",
        *,
        format: int | None = None,
        check: int = -1,
        preset: int | None = None,
        filters: _FilterChain | None = None,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def peek(self, size: int = -1) -> bytes: ...
    def read(self, size: int | None = -1) -> bytes: ...
    def read1(self, size: int = -1) -> bytes: ...
    def readline(self, size: int | None = -1) -> bytes: ...
    def write(self, data: ReadableBuffer) -> int: ...
    def seek(self, offset: int, whence: int = 0) -> int: ...

@overload
def open(
    filename: _PathOrFile,
    mode: Literal["r", "rb"] = "rb",
    *,
    format: int | None = None,
    check: Literal[-1] = -1,
    preset: None = None,
    filters: _FilterChain | None = None,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
) -> LZMAFile: ...
@overload
def open(
    filename: _PathOrFile,
    mode: _OpenBinaryWritingMode,
    *,
    format: int | None = None,
    check: int = -1,
    preset: int | None = None,
    filters: _FilterChain | None = None,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
) -> LZMAFile: ...
@overload
def open(
    filename: StrOrBytesPath,
    mode: Literal["rt"],
    *,
    format: int | None = None,
    check: Literal[-1] = -1,
    preset: None = None,
    filters: _FilterChain | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> TextIO: ...
@overload
def open(
    filename: StrOrBytesPath,
    mode: _OpenTextWritingMode,
    *,
    format: int | None = None,
    check: int = -1,
    preset: int | None = None,
    filters: _FilterChain | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> TextIO: ...
@overload
def open(
    filename: _PathOrFile,
    mode: str,
    *,
    format: int | None = None,
    check: int = -1,
    preset: int | None = None,
    filters: _FilterChain | None = None,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
) -> LZMAFile | TextIO: ...
def compress(
    data: ReadableBuffer, format: int = 1, check: int = -1, preset: int | None = None, filters: _FilterChain | None = None
) -> bytes: ...
def decompress(
    data: ReadableBuffer, format: int = 0, memlimit: int | None = None, filters: _FilterChain | None = None
) -> bytes: ...
def is_check_supported(__check_id: int) -> bool: ...
