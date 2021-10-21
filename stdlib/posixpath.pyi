import sys
from _typeshed import BytesPath, StrOrBytesPath, StrPath
from genericpath import (
    commonprefix as commonprefix,
    exists as exists,
    getatime as getatime,
    getctime as getctime,
    getmtime as getmtime,
    getsize as getsize,
    isdir as isdir,
    isfile as isfile,
    samefile as samefile,
    sameopenfile as sameopenfile,
    samestat as samestat,
)
from os import PathLike
from typing import AnyStr, Sequence, overload

supports_unicode_filenames: bool
# aliases (also in os)
curdir: str
pardir: str
sep: str
altsep: str | None
extsep: str
pathsep: str
defpath: str
devnull: str

# Overloads are necessary to work around python/mypy#3644.
@overload
def abspath(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def abspath(path: AnyStr) -> AnyStr: ...
@overload
def basename(p: PathLike[AnyStr]) -> AnyStr: ...
@overload
def basename(p: AnyStr) -> AnyStr: ...
@overload
def dirname(p: PathLike[AnyStr]) -> AnyStr: ...
@overload
def dirname(p: AnyStr) -> AnyStr: ...
@overload
def expanduser(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def expanduser(path: AnyStr) -> AnyStr: ...
@overload
def expandvars(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def expandvars(path: AnyStr) -> AnyStr: ...
@overload
def normcase(s: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normcase(s: AnyStr) -> AnyStr: ...
@overload
def normpath(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normpath(path: AnyStr) -> AnyStr: ...
@overload
def commonpath(paths: Sequence[StrPath]) -> str: ...
@overload
def commonpath(paths: Sequence[BytesPath]) -> bytes: ...
@overload
def join(a: StrPath, *paths: StrPath) -> str: ...
@overload
def join(a: BytesPath, *paths: BytesPath) -> bytes: ...

if sys.version_info >= (3, 10):
    @overload
    def realpath(filename: PathLike[AnyStr], *, strict: bool = ...) -> AnyStr: ...
    @overload
    def realpath(filename: AnyStr, *, strict: bool = ...) -> AnyStr: ...

else:
    @overload
    def realpath(filename: PathLike[AnyStr]) -> AnyStr: ...
    @overload
    def realpath(filename: AnyStr) -> AnyStr: ...

@overload
def relpath(path: BytesPath, start: BytesPath | None = ...) -> bytes: ...
@overload
def relpath(path: StrPath, start: StrPath | None = ...) -> str: ...
@overload
def split(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def split(p: AnyStr) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitdrive(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitdrive(p: AnyStr) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitext(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitext(p: AnyStr) -> tuple[AnyStr, AnyStr]: ...
def isabs(s: StrOrBytesPath) -> bool: ...
def islink(path: StrOrBytesPath) -> bool: ...
def ismount(path: StrOrBytesPath) -> bool: ...
def lexists(path: StrOrBytesPath) -> bool: ...
