from functools import lru_cache as lru_cache
from shutil import get_terminal_size as get_terminal_size, which as which
from typing import Any, NamedTuple

PY3: Any
long = int
xrange = range
unicode = str
basestring = str
range = range

def u(s): ...
def b(s): ...
super = super
FileNotFoundError = FileNotFoundError
PermissionError = PermissionError
ProcessLookupError = ProcessLookupError
InterruptedError = InterruptedError
ChildProcessError = ChildProcessError
FileExistsError = FileExistsError

class _CacheInfo(NamedTuple):
    hits: Any
    misses: Any
    maxsize: Any
    currsize: Any

class _HashedSeq(list):
    hashvalue: Any
    def __init__(self, tup, hash=...) -> None: ...
    def __hash__(self): ...
