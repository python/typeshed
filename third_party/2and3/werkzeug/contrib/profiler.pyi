from typing import Any, AnyStr, Generic, Optional, Protocol, Tuple

from ..middleware.profiler import *

class _Writable(Protocol[AnyStr]):
    def write(self, __s: AnyStr) -> Any: ...

class MergeStream(Generic[AnyStr]):
    streams: Tuple[_Writable[AnyStr]]
    def __init__(self, *streams: _Writable[AnyStr]) -> None: ...
    def write(self, data: AnyStr) -> None: ...
