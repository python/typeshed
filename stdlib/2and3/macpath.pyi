# Stubs for os.path
# Ron Murawski <ron@horizonchess.com>

import os
import sys
from typing import overload, List, Any, AnyStr, Sequence, Tuple, TypeVar, Union, Text, Callable, Optional

if sys.version_info < (3, 8):
    _T = TypeVar('_T')

    if sys.version_info >= (3, 6):
        from builtins import _PathLike
        _PathType = Union[bytes, Text, _PathLike]
        _StrPath = Union[Text, _PathLike[Text]]
        _BytesPath = Union[bytes, _PathLike[bytes]]
    else:
        _PathType = Union[bytes, Text]
        _StrPath = Text
        _BytesPath = bytes

    # ----- os.path variables -----
    supports_unicode_filenames: bool
    # aliases (also in os)
    curdir: str
    pardir: str
    sep: str
    altsep: Optional[str]
    extsep: str
    pathsep: str
    defpath: str
    devnull: str

    # ----- os.path function stubs -----
    if sys.version_info >= (3, 6):
        # Overloads are necessary to work around python/mypy#3644.
        @overload
        def abspath(path: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def abspath(path: AnyStr) -> AnyStr: ...
        @overload
        def basename(s: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def basename(s: AnyStr) -> AnyStr: ...
        @overload
        def dirname(s: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def dirname(s: AnyStr) -> AnyStr: ...
        @overload
        def expanduser(path: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def expanduser(path: AnyStr) -> AnyStr: ...
        @overload
        def expandvars(path: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def expandvars(path: AnyStr) -> AnyStr: ...
        @overload
        def normcase(path: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def normcase(path: AnyStr) -> AnyStr: ...
        @overload
        def normpath(s: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def normpath(s: AnyStr) -> AnyStr: ...
        @overload
        def realpath(path: _PathLike[AnyStr]) -> AnyStr: ...
        @overload
        def realpath(path: AnyStr) -> AnyStr: ...

    else:
        def abspath(path: AnyStr) -> AnyStr: ...
        def basename(s: AnyStr) -> AnyStr: ...
        def dirname(s: AnyStr) -> AnyStr: ...
        def expanduser(path: AnyStr) -> AnyStr: ...
        def expandvars(path: AnyStr) -> AnyStr: ...
        def normcase(path: AnyStr) -> AnyStr: ...
        def normpath(s: AnyStr) -> AnyStr: ...
        def realpath(path: AnyStr) -> AnyStr: ...

    if sys.version_info >= (3, 6):
        # In reality it returns str for sequences of _StrPath and bytes for sequences
        # of _BytesPath, but mypy does not accept such a signature.
        def commonpath(paths: Sequence[_PathType]) -> Any: ...
    elif sys.version_info >= (3, 5):
        def commonpath(paths: Sequence[AnyStr]) -> AnyStr: ...

    # NOTE: Empty lists results in '' (str) regardless of contained type.
    # Also, in Python 2 mixed sequences of Text and bytes results in either Text or bytes
    # So, fall back to Any
    def commonprefix(m: Sequence[_PathType]) -> Any: ...

    if sys.version_info >= (3, 3):
        def exists(path: Union[_PathType, int]) -> bool: ...
    else:
        def exists(path: _PathType) -> bool: ...
    def lexists(path: _PathType) -> bool: ...

    # These return float if os.stat_float_times() == True,
    # but int is a subclass of float.
    def getatime(filename: _PathType) -> float: ...
    def getmtime(filename: _PathType) -> float: ...
    def getctime(filename: _PathType) -> float: ...

    def getsize(filename: _PathType) -> int: ...
    def isabs(s: _PathType) -> bool: ...
    def isfile(path: _PathType) -> bool: ...
    def isdir(s: _PathType) -> bool: ...
    def islink(s: _PathType) -> bool: ...
    def ismount(s: _PathType) -> bool: ...

    if sys.version_info < (3, 0):
        # Make sure signatures are disjunct, and allow combinations of bytes and unicode.
        # (Since Python 2 allows that, too)
        # Note that e.g. os.path.join("a", "b", "c", "d", u"e") will still result in
        # a type error.
        @overload
        def join(__p1: bytes, *p: bytes) -> bytes: ...
        @overload
        def join(__p1: bytes, __p2: bytes, __p3: bytes, __p4: Text, *p: _PathType) -> Text: ...
        @overload
        def join(__p1: bytes, __p2: bytes, __p3: Text, *p: _PathType) -> Text: ...
        @overload
        def join(__p1: bytes, __p2: Text, *p: _PathType) -> Text: ...
        @overload
        def join(__p1: Text, *p: _PathType) -> Text: ...
    elif sys.version_info >= (3, 6):
        # Mypy complains that the signatures overlap (same for relpath below), but things seem to behave correctly anyway.
        @overload
        def join(s: _StrPath, *paths: _StrPath) -> Text: ...
        @overload
        def join(s: _BytesPath, *paths: _BytesPath) -> bytes: ...
    else:
        def join(s: AnyStr, *paths: AnyStr) -> AnyStr: ...

    @overload
    def relpath(path: _BytesPath, start: Optional[_BytesPath] = ...) -> bytes: ...
    @overload
    def relpath(path: _StrPath, start: Optional[_StrPath] = ...) -> Text: ...

    def samefile(f1: _PathType, f2: _PathType) -> bool: ...
    def sameopenfile(fp1: int, fp2: int) -> bool: ...
    def samestat(s1: os.stat_result, s2: os.stat_result) -> bool: ...

    if sys.version_info >= (3, 6):
        @overload
        def split(s: _PathLike[AnyStr]) -> Tuple[AnyStr, AnyStr]: ...
        @overload
        def split(s: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
        @overload
        def splitdrive(p: _PathLike[AnyStr]) -> Tuple[AnyStr, AnyStr]: ...
        @overload
        def splitdrive(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
        @overload
        def splitext(p: _PathLike[AnyStr]) -> Tuple[AnyStr, AnyStr]: ...
        @overload
        def splitext(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
    else:
        def split(s: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
        def splitdrive(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...
        def splitext(p: AnyStr) -> Tuple[AnyStr, AnyStr]: ...

    if sys.version_info < (3,):
        def walk(path: AnyStr, visit: Callable[[_T, AnyStr, List[AnyStr]], Any], arg: _T) -> None: ...
