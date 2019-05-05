# Stubs for zipfile

from typing import Callable, Dict, IO, Iterable, List, Optional, Text, Tuple, Type, Union
from types import TracebackType
import os
import sys


if sys.version_info >= (3, 6):
    _Path = Union[os.PathLike[Text], Text]
else:
    _Path = Text
_SZI = Union[Text, ZipInfo]
_DT = Tuple[int, int, int, int, int, int]


if sys.version_info >= (3,):
    class BadZipFile(Exception): ...
    BadZipfile = BadZipFile
else:
    class BadZipfile(Exception): ...
error = BadZipfile

class LargeZipFile(Exception): ...

class ZipFile:
    debug: int
    comment: bytes
    filelist: List[ZipInfo]
    fp: IO[bytes]
    NameToInfo: Dict[Text, ZipInfo]
    def __init__(self, file: Union[_Path, IO[bytes]], mode: Text = ..., compression: int = ...,
                 allowZip64: bool = ...) -> None: ...
    def __enter__(self) -> ZipFile: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> bool: ...
    def close(self) -> None: ...
    def getinfo(self, name: Text) -> ZipInfo: ...
    def infolist(self) -> List[ZipInfo]: ...
    def namelist(self) -> List[Text]: ...
    def open(self, name: _SZI, mode: Text = ...,
             pwd: Optional[bytes] = ...) -> IO[bytes]: ...
    def extract(self, member: _SZI, path: Optional[_SZI] = ...,
                pwd: bytes = ...) -> str: ...
    def extractall(self, path: Optional[_Path] = ...,
                   members: Optional[Iterable[Text]] = ...,
                   pwd: Optional[bytes] = ...) -> None: ...
    def printdir(self) -> None: ...
    def setpassword(self, pwd: bytes) -> None: ...
    def read(self, name: _SZI, pwd: Optional[bytes] = ...) -> bytes: ...
    def testzip(self) -> Optional[str]: ...
    def write(self, filename: _Path, arcname: Optional[_Path] = ...,
              compress_type: Optional[int] = ...) -> None: ...
    if sys.version_info >= (3,):
        def writestr(self, zinfo_or_arcname: _SZI, data: Union[bytes, str],
                     compress_type: Optional[int] = ...) -> None: ...
    else:
        def writestr(self,
                     zinfo_or_arcname: _SZI, bytes: bytes,
                     compress_type: Optional[int] = ...) -> None: ...

class PyZipFile(ZipFile):
    if sys.version_info >= (3,):
        def __init__(self, file: Union[str, IO[bytes]], mode: str = ...,
                     compression: int = ..., allowZip64: bool = ...,
                     opimize: int = ...) -> None: ...
        def writepy(self, pathname: str, basename: str = ...,
                    filterfunc: Optional[Callable[[str], bool]] = ...) -> None: ...
    else:
        def writepy(self,
                    pathname: Text, basename: Text = ...) -> None: ...

class ZipInfo:
    filename: Text
    date_time: _DT
    compress_type: int
    comment: bytes
    extra: bytes
    create_system: int
    create_version: int
    extract_version: int
    reserved: int
    flag_bits: int
    volume: int
    internal_attr: int
    external_attr: int
    header_offset: int
    CRC: int
    compress_size: int
    file_size: int
    def __init__(self, filename: Optional[Text] = ...,
                 date_time: Optional[_DT] = ...) -> None: ...
    if sys.version_info >= (3, 6):
        def is_dir(self) -> bool: ...
    def FileHeader(self, zip64: Optional[bool] = ...) -> bytes: ...


def is_zipfile(filename: Union[_Path, IO[bytes]]) -> bool: ...

ZIP_STORED: int
ZIP_DEFLATED: int
if sys.version_info >= (3, 3):
    ZIP_BZIP2: int
    ZIP_LZMA: int
