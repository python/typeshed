from typing import Any, AnyStr, List
from genericpath import *  # noqa: F403

curdir = ...  # type: Any
pardir = ...  # type: Any
extsep = ...  # type: Any
sep = ...  # type: Any
pathsep = ...  # type: Any
defpath = ...  # type: Any
altsep = ...  # type: Any
devnull = ...  # type: Any

def normcase(s): ...
def isabs(s): ...
def join(a, *p): ...
def split(p): ...
def splitext(p): ...
def splitdrive(p): ...
def basename(p): ...
def dirname(p): ...
def islink(path): ...
def lexists(path): ...
def samefile(f1, f2): ...
def sameopenfile(fp1, fp2): ...
def samestat(s1, s2): ...
def ismount(path): ...
def walk(top, func, arg): ...
def expanduser(path): ...
def expandvars(path): ...
def normpath(path): ...
def abspath(path): ...
def realpath(filename): ...

supports_unicode_filenames = ...  # type: Any

def relpath(path, start=...): ...

# posixpath imports these from genericpath.py:
def commonprefix(list: List[AnyStr]) -> AnyStr: ...
def exists(path: unicode) -> bool: ...
def getatime(path: unicode) -> float: ...
def getmtime(path: unicode) -> float: ...
def getctime(path: unicode) -> float: ...
def getsize(path: unicode) -> int: ...
def isfile(path: unicode) -> bool: ...
def isdir(path: unicode) -> bool: ...
