# Stubs for plistlib

from typing import Any, IO, MutableMapping, Optional, Type, TypeVar, Union
from typing import Dict as DictT
from enum import Enum
import sys

_D = TypeVar('_D', MutableMapping[str, Any])


class PlistFormat(Enum):
    FMT_XML = ...  # type: PlistFormat
    FMT_BINARY = ...  # type: PlistFormat

if sys.version_info >= (3, 4):
    def load(fp: IO[bytes], *, fmt: Optional[PlistFormat] = ...,
             use_builtin_types: bool, dict_type: Type[_D] =...) -> _D: ...
    def loads(data: bytes, *, fmt: Optional[PlistFormat] = ...,
              use_builtin_types: bool = ..., dict_type: Type[_D] = ...) -> _D: ...
    def dump(value: MutableMapping[str, Any], fp: IO[bytes], *,
             fmt: PlistFormat =..., sort_keys: bool = ...,
             skipkeys: bool = ...) -> None: ...
    def dumps(value: MutableMapping[str, Any], *, fmt: PlistFormat = ...,
              skipkeys: bool = ..., sort_keys: bool = ...) -> bytes: ...

def readPlist(pathOrFile: Union[str, IO[bytes]]) -> DictT[str, Any]: ...
def writePlist(value: DictT[str, Any], pathOrFile: Union[str, IO[bytes]]) -> None: ...
def readPlistFromBytes(data: bytes) -> DictT[str, Any]: ...
def writePlistToBytes(value: DictT[str, Any]) -> bytes: ...

class Dict(dict):
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def __delattr__(self, attr: str) -> None: ...

class Data:
    data = ...  # type: bytes
    def __init__(self, data: bytes) -> None: ...

FMT_XML = PlistFormat.FMT_XML
FMT_BINARY = PlistFormat.FMT_BINARY
