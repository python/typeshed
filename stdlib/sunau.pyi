from _typeshed import Unused
from typing import IO, Any, Literal, NamedTuple, NoReturn, overload
from typing_extensions import Self, TypeAlias

_File: TypeAlias = str | IO[bytes]

class Error(Exception): ...

AUDIO_FILE_MAGIC: int
AUDIO_FILE_ENCODING_MULAW_8: int
AUDIO_FILE_ENCODING_LINEAR_8: int
AUDIO_FILE_ENCODING_LINEAR_16: int
AUDIO_FILE_ENCODING_LINEAR_24: int
AUDIO_FILE_ENCODING_LINEAR_32: int
AUDIO_FILE_ENCODING_FLOAT: int
AUDIO_FILE_ENCODING_DOUBLE: int
AUDIO_FILE_ENCODING_ADPCM_G721: int
AUDIO_FILE_ENCODING_ADPCM_G722: int
AUDIO_FILE_ENCODING_ADPCM_G723_3: int
AUDIO_FILE_ENCODING_ADPCM_G723_5: int
AUDIO_FILE_ENCODING_ALAW_8: int
AUDIO_UNKNOWN_SIZE: int

class _sunau_params(NamedTuple):
    nchannels: int
    sampwidth: int
    framerate: int
    nframes: int
    comptype: str
    compname: str

class Au_read:
    def __init__(self, f: _File) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def __del__(self) -> None: ...
    def getfp(self) -> IO[bytes] | None: ...
    def rewind(self) -> None: ...
    def close(self) -> None: ...
    def tell(self) -> int: ...
    def getnchannels(self) -> int: ...
    def getnframes(self) -> int: ...
    def getsampwidth(self) -> int: ...
    def getframerate(self) -> int: ...
    def getcomptype(self) -> str: ...
    def getcompname(self) -> str: ...
    def getparams(self) -> _sunau_params: ...
    def getmarkers(self) -> None: ...
    def getmark(self, id: Any) -> NoReturn: ...
    def setpos(self, pos: int) -> None: ...
    def readframes(self, nframes: int) -> bytes | None: ...

class Au_write:
    def __init__(self, f: _File) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def __del__(self) -> None: ...
    def setnchannels(self, nchannels: int) -> None: ...
    def getnchannels(self) -> int: ...
    def setsampwidth(self, sampwidth: int) -> None: ...
    def getsampwidth(self) -> int: ...
    def setframerate(self, framerate: float) -> None: ...
    def getframerate(self) -> int: ...
    def setnframes(self, nframes: int) -> None: ...
    def getnframes(self) -> int: ...
    def setcomptype(self, type: str, name: str) -> None: ...
    def getcomptype(self) -> str: ...
    def getcompname(self) -> str: ...
    def setparams(self, params: _sunau_params) -> None: ...
    def getparams(self) -> _sunau_params: ...
    def tell(self) -> int: ...
    # should be any bytes-like object after 3.4, but we don't have a type for that
    def writeframesraw(self, data: bytes) -> None: ...
    def writeframes(self, data: bytes) -> None: ...
    def close(self) -> None: ...

@overload
def open(f: _File, mode: Literal["r", "rb"]) -> Au_read: ...
@overload
def open(f: _File, mode: Literal["w", "wb"]) -> Au_write: ...
@overload
def open(f: _File, mode: str | None = None) -> Any: ...
