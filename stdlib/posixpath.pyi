import sys
from _typeshed import AnyOrLiteralStr, BytesPath, StrOrBytesPath, StrPath
from collections.abc import Sequence
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
from typing import AnyStr, overload
from typing_extensions import LiteralString

__all__ = [
    "normcase",
    "isabs",
    "join",
    "splitdrive",
    "split",
    "splitext",
    "basename",
    "dirname",
    "commonprefix",
    "getsize",
    "getmtime",
    "getatime",
    "getctime",
    "islink",
    "exists",
    "lexists",
    "isdir",
    "isfile",
    "ismount",
    "expanduser",
    "expandvars",
    "normpath",
    "abspath",
    "samefile",
    "sameopenfile",
    "samestat",
    "curdir",
    "pardir",
    "sep",
    "pathsep",
    "defpath",
    "altsep",
    "extsep",
    "devnull",
    "realpath",
    "supports_unicode_filenames",
    "relpath",
    "commonpath",
]

supports_unicode_filenames: bool
# aliases (also in os)
curdir: LiteralString
pardir: LiteralString
sep: LiteralString
altsep: LiteralString | None
extsep: LiteralString
pathsep: LiteralString
defpath: LiteralString
devnull: LiteralString

# Overloads are necessary to work around python/mypy#3644.
@overload
def abspath(path: StrPath) -> str: ...
@overload
def abspath(path: BytesPath) -> bytes: ...
@overload
def basename(p: PathLike[AnyStr]) -> AnyStr: ...
@overload
def basename(p: AnyOrLiteralStr) -> AnyOrLiteralStr: ...
@overload
def dirname(p: PathLike[AnyStr]) -> AnyStr: ...
@overload
def dirname(p: AnyOrLiteralStr) -> AnyOrLiteralStr: ...
@overload
def expanduser(path: StrPath) -> str: ...
@overload
def expanduser(path: BytesPath) -> bytes: ...
@overload
def expandvars(path: StrPath) -> str: ...
@overload
def expandvars(path: BytesPath) -> bytes: ...
@overload
def normcase(s: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normcase(s: AnyOrLiteralStr) -> AnyOrLiteralStr: ...
@overload
def normpath(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def normpath(path: AnyOrLiteralStr) -> AnyOrLiteralStr: ...
@overload
def commonpath(paths: Sequence[LiteralString]) -> LiteralString: ...
@overload
def commonpath(paths: Sequence[StrPath]) -> str: ...
@overload
def commonpath(paths: Sequence[BytesPath]) -> bytes: ...

# First parameter is not actually pos-only,
# but must be defined as pos-only in the stub or cross-platform code doesn't type-check,
# as the parameter name is different in ntpath.join()
@overload
def join(__a: LiteralString, *paths: LiteralString) -> LiteralString: ...
@overload
def join(__a: StrPath, *paths: StrPath) -> str: ...
@overload
def join(__a: BytesPath, *paths: BytesPath) -> bytes: ...

if sys.version_info >= (3, 10):
    @overload
    def realpath(filename: StrPath, *, strict: bool = ...) -> str: ...
    @overload
    def realpath(filename: BytesPath, *, strict: bool = ...) -> bytes: ...

else:
    @overload
    def realpath(filename: StrPath) -> str: ...
    @overload
    def realpath(filename: BytesPath) -> bytes: ...

@overload
def relpath(path: LiteralString, start: LiteralString | None = ...) -> LiteralString: ...
@overload
def relpath(path: BytesPath, start: BytesPath | None = ...) -> bytes: ...
@overload
def relpath(path: StrPath, start: StrPath | None = ...) -> str: ...
@overload
def split(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def split(p: AnyOrLiteralStr) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
@overload
def splitdrive(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitdrive(p: AnyOrLiteralStr) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
@overload
def splitext(p: PathLike[AnyStr]) -> tuple[AnyStr, AnyStr]: ...
@overload
def splitext(p: AnyOrLiteralStr) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
def isabs(s: StrOrBytesPath) -> bool: ...
def islink(path: StrOrBytesPath | int) -> bool: ...
def ismount(path: StrOrBytesPath | int) -> bool: ...
def lexists(path: StrOrBytesPath | int) -> bool: ...
