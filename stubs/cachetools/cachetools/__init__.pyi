from collections.abc import Iterator, Sequence
from typing import Callable, Generic, TypeVar

from _typeshed import IdentityFunction
from typing import Any, Callable, ContextManager, MutableMapping, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class Cache(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    @property
    def maxsize(self) -> float: ...
    @property
    def currsize(self) -> float: ...
    @staticmethod
    def getsizeof(value: _VT) -> float: ...

class FIFOCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    # TODO: add types to these, currently using what is defined in superclass
    #def __setitem__(self, key, value, cache_setitem=...) -> None: ...
    #def __delitem__(self, key, cache_delitem=...) -> None: ...
    #def popitem(self): ...

class LFUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None: ...
    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None: ...

class LRUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None: ...
    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None: ...

class MRUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    # TODO: add types to these, currently using what is defined in superclass
    #def __getitem__(self, key, cache_getitem=...): ...
    #def __setitem__(self, key, value, cache_setitem=...) -> None: ...
    #def __delitem__(self, key, cache_delitem=...) -> None: ...
    #def popitem(self): ...

class RRCache(Cache[_KT, _VT]):
    def __init__(
        self, maxsize: float, choice: Callable[[Sequence[_KT]], _KT] | None = ..., getsizeof: Callable[[_VT], float] | None = ...
    ) -> None: ...
    @property
    def choice(self) -> Callable[[Sequence[_KT]], _KT]: ...

class TTLCache(Cache[_KT, _VT]):
    def __init__(
        self, maxsize: float, ttl: float, timer: Callable[[], float] = ..., getsizeof: Callable[[_VT], float] | None = ...
    ) -> None: ...
    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None: ...
    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    @property
    def currsize(self) -> float: ...
    @property
    def timer(self) -> Callable[[], float]: ...
    @property
    def ttl(self) -> float: ...
    def expire(self, time: float | None = ...) -> None: ...

def cached(
    cache: MutableMapping[_KT, Any] | None, key: Callable[..., _KT] = ..., lock: ContextManager[Any] | None = ...
) -> IdentityFunction: ...
def cachedmethod(
    cache: Callable[[Any], MutableMapping[_KT, Any] | None], key: Callable[..., _KT] = ..., lock: ContextManager[Any] | None = ...
) -> IdentityFunction: ...

