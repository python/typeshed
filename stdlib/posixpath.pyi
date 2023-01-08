import sys
from _typeshed import AnyOrLiteralStr, GenericPath, StrOrBytesPath
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
from typing import AnyStr
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
def abspath(path: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...
def basename(p: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...
def dirname(p: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...
def expanduser(path: GenericPath[AnyStr]) -> AnyStr: ...
def expandvars(path: GenericPath[AnyStr]) -> AnyStr: ...
def normcase(s: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...
def normpath(path: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...
def commonpath(paths: Sequence[GenericPath[AnyOrLiteralStr]]) -> AnyOrLiteralStr: ...

# First parameter is not actually pos-only,
# but must be defined as pos-only in the stub or cross-platform code doesn't type-check,
# as the parameter name is different in ntpath.join()
def join(__a: GenericPath[AnyOrLiteralStr], *paths: GenericPath[AnyOrLiteralStr]) -> AnyOrLiteralStr: ...

if sys.version_info >= (3, 10):
    def realpath(filename: GenericPath[AnyStr], *, strict: bool = ...) -> AnyStr: ...

else:
    def realpath(filename: GenericPath[AnyStr]) -> AnyStr: ...

def relpath(path: GenericPath[AnyOrLiteralStr], start: GenericPath[AnyOrLiteralStr] | None = ...) -> AnyOrLiteralStr: ...
def split(p: GenericPath[AnyOrLiteralStr]) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
def splitdrive(p: GenericPath[AnyOrLiteralStr]) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
def splitext(p: GenericPath[AnyOrLiteralStr]) -> tuple[AnyOrLiteralStr, AnyOrLiteralStr]: ...
def isabs(s: StrOrBytesPath) -> bool: ...
def islink(path: StrOrBytesPath | int) -> bool: ...
def ismount(path: StrOrBytesPath | int) -> bool: ...
def lexists(path: StrOrBytesPath | int) -> bool: ...
