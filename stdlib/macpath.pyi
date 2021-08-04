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
from posixpath import curdir as curdir
from posixpath import defpath as defpath
from posixpath import devnull as devnull
from posixpath import expanduser as expanduser
from posixpath import expandvars as expandvars
from posixpath import extsep as extsep
from posixpath import isabs as isabs
from posixpath import lexists as lexists
from posixpath import pardir as pardir
from posixpath import pathsep as pathsep
from posixpath import sep as sep
from posixpath import splitdrive as splitdrive
from posixpath import splitext as splitext
from posixpath import supports_unicode_filenames as supports_unicode_filenames
from typing import AnyStr, Optional, Tuple, overload

from _typeshed import BytesPath, StrOrBytesPath, StrPath

altsep: Optional[str]

@overload
def basename(s: PathLike[AnyStr]) -> AnyStr: ...
@overload
def basename(s: AnyStr) -> AnyStr: ...
@overload
def dirname(s: PathLike[AnyStr]) -> AnyStr: ...
@overload
def dirname(s: AnyStr) -> AnyStr: ...
@overload
def normcase(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normcase(path: AnyStr) -> AnyStr: ...
@overload
def normpath(s: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normpath(s: AnyStr) -> AnyStr: ...
@overload
def realpath(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def realpath(path: AnyStr) -> AnyStr: ...
def islink(s: StrOrBytesPath) -> bool: ...

# Mypy complains that the signatures overlap, but things seem to behave correctly anyway.
@overload
def join(s: StrPath, *paths: StrPath) -> str: ...
@overload
def join(s: BytesPath, *paths: BytesPath) -> bytes: ...
@overload
def split(s: PathLike[AnyStr]) -> Tuple[AnyStr, AnyStr]: ...
@overload
def split(s: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
