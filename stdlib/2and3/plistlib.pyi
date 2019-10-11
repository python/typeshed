# Stubs for plistlib

from typing import (
    Any, IO, Mapping, MutableMapping, Optional, Union,
    Type, TypeVar,
)
from typing import Dict as DictT
import sys
if sys.version_info >= (3,):
    from enum import Enum

    class PlistFormat(Enum):
        FMT_XML: int
        FMT_BINARY: int
    FMT_XML = PlistFormat.FMT_XML
    FMT_BINARY = PlistFormat.FMT_BINARY

mm = MutableMapping[str, Any]
_D = TypeVar('_D', bound=mm)
if sys.version_info >= (3,):
    _Path = str
else:
    _Path = Union[str, unicode]

if sys.version_info >= (3, 4):
    def load(fp: IO[bytes], *, fmt: Optional[PlistFormat] = ...,
             use_builtin_types: bool = ..., dict_type: Type[_D] = ...) -> _D: ...
    def loads(data: bytes, *, fmt: Optional[PlistFormat] = ...,
              use_builtin_types: bool = ..., dict_type: Type[_D] = ...) -> _D: ...
    def dump(value: Mapping[str, Any], fp: IO[bytes], *,
             fmt: PlistFormat = ..., sort_keys: bool = ...,
             skipkeys: bool = ...) -> None: ...
    def dumps(value: Mapping[str, Any], *, fmt: PlistFormat = ...,
              skipkeys: bool = ..., sort_keys: bool = ...) -> bytes: ...

def readPlist(pathOrFile: Union[_Path, IO[bytes]]) -> DictT[str, Any]: ...
def writePlist(value: Mapping[str, Any], pathOrFile: Union[_Path, IO[bytes]]) -> None: ...
def readPlistFromBytes(data: bytes) -> DictT[str, Any]: ...
def writePlistToBytes(value: Mapping[str, Any]) -> bytes: ...
if sys.version_info < (3,):
    def readPlistFromResource(path: _Path, restype: str = ...,
                              resid: int = ...) -> DictT[str, Any]: ...
    def writePlistToResource(rootObject: Mapping[str, Any], path: _Path,
                             restype: str = ...,
                             resid: int = ...) -> None: ...
    def readPlistFromString(data: str) -> DictT[str, Any]: ...
    def writePlistToString(rootObject: Mapping[str, Any]) -> str: ...

if sys.version_info < (3, 7):
    class Dict(DictT[str, Any]):
        def __getattr__(self, attr: str) -> Any: ...
        def __setattr__(self, attr: str, value: Any) -> None: ...
        def __delattr__(self, attr: str) -> None: ...

class Data:
    data: bytes
    def __init__(self, data: bytes) -> None: ...
