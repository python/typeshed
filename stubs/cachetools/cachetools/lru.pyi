from typing import Callable, Iterator, TypeVar

from .cache import Cache as Cache

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class LRUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None: ...
    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
