from typing import Any, AnyStr, Iterable, Optional, Protocol

from ..middleware.profiler import *

class _Writable(Protocol):
    def write(self, __s: AnyStr) -> Any: ...

class MergeStream(object):
    streams: Iterable[_Writable]
    def __init__(self, *streams: Iterable[_Writable]) -> None: ...
    def write(self, data: AnyStr) -> None: ...
