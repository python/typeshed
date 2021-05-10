import sys
from _typeshed import BytesPath, StrPath
from genericpath import *
from os import PathLike
from os.path import (
    abspath as abspath,
    basename as basename,
    commonpath as commonpath,
    curdir as curdir,
    defpath as defpath,
    devnull as devnull,
    dirname as dirname,
    expanduser as expanduser,
    expandvars as expandvars,
    extsep as extsep,
    isabs as isabs,
    islink as islink,
    ismount as ismount,
    lexists as lexists,
    normcase as normcase,
    normpath as normpath,
    pardir as pardir,
    pathsep as pathsep,
    relpath as relpath,
    sep as sep,
    split as split,
    splitdrive as splitdrive,
    splitext as splitext,
    supports_unicode_filenames as supports_unicode_filenames,
)
from typing import AnyStr, overload

if sys.version_info < (3, 7) and sys.platform == "win32":
    from os.path import splitunc as splitunc

altsep: str

# Has different argument names from the os.path versions
@overload
def join(path: StrPath, *paths: StrPath) -> str: ...
@overload
def join(path: BytesPath, *paths: BytesPath) -> bytes: ...
@overload
def realpath(path: PathLike[AnyStr]) -> AnyStr: ...
@overload
def realpath(path: AnyStr) -> AnyStr: ...
