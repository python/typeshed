import sys
from genericpath import commonprefix as commonprefix
from genericpath import exists as exists
from genericpath import getatime as getatime
from genericpath import getctime as getctime
from genericpath import getmtime as getmtime
from genericpath import getsize as getsize
from genericpath import isdir as isdir
from genericpath import isfile as isfile
from genericpath import samefile as samefile
from genericpath import sameopenfile as sameopenfile
from genericpath import samestat as samestat
from os import PathLike
# Re-export common definitions from posixpath to reduce duplication
from posixpath import abspath as abspath
from posixpath import basename as basename
from posixpath import commonpath as commonpath
from posixpath import curdir as curdir
from posixpath import defpath as defpath
from posixpath import devnull as devnull
from posixpath import dirname as dirname
from posixpath import expanduser as expanduser
from posixpath import expandvars as expandvars
from posixpath import extsep as extsep
from posixpath import isabs as isabs
from posixpath import islink as islink
from posixpath import ismount as ismount
from posixpath import lexists as lexists
from posixpath import normcase as normcase
from posixpath import normpath as normpath
from posixpath import pardir as pardir
from posixpath import pathsep as pathsep
from posixpath import relpath as relpath
from posixpath import sep as sep
from posixpath import split as split
from posixpath import splitdrive as splitdrive
from posixpath import splitext as splitext
from posixpath import supports_unicode_filenames as supports_unicode_filenames
from typing import AnyStr, Tuple, overload

from _typeshed import BytesPath, StrPath

altsep: str
if sys.version_info < (3, 7) and sys.platform == "win32":
    def splitunc(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...  # deprecated

# Similar to posixpath, but have slightly different argument names
@overload
def join(path: StrPath, *paths: StrPath) -> str: ...
@overload
def join(path: BytesPath, *paths: BytesPath) -> bytes: ...

if sys.platform == "win32":
    if sys.version_info >= (3, 10):
        @overload
        def realpath(path: PathLike[AnyStr], *, strict: bool = ...) -> AnyStr: ...
        @overload
        def realpath(path: AnyStr, *, strict: bool = ...) -> AnyStr: ...
    else:
        @overload
        def realpath(path: PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def realpath(path: AnyStr) -> AnyStr: ...

else:
    realpath = abspath
