from _typeshed import IdentityFunction
from collections.abc import Iterator, Sequence
from contextlib import AbstractContextManager
from typing import Any, Callable, Generic, MutableMapping, TypeVar, overload

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

class Cache(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    @overload  # type: ignore[override]
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T) -> _VT | _T: ...
    def setdefault(self, key: _KT, default: _VT | None = ...) -> _VT: ...
    @property
    def maxsize(self) -> float: ...
    @property
    def currsize(self) -> float: ...
    @staticmethod
    def getsizeof(value: _VT) -> float: ...

class FIFOCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...

class LFUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...

class LRUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...

class MRUCache(Cache[_KT, _VT]):
    def __init__(self, maxsize: float, getsizeof: Callable[[_VT], float] | None = ...) -> None: ...

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
    @property
    def currsize(self) -> float: ...
    @property
    def timer(self) -> Callable[[], float]: ...
    @property
    def ttl(self) -> float: ...
    def expire(self, time: float | None = ...) -> None: ...

def cached(
    cache: MutableMapping[_KT, Any] | None, key: Callable[..., _KT] = ..., lock: AbstractContextManager[Any] | None = ...
) -> IdentityFunction: ...
def cachedmethod(
    cache: Callable[[Any], MutableMapping[_KT, Any] | None],
    key: Callable[..., _KT] = ...,
    lock: Callable[[Any], AbstractContextManager[Any]] | None = ...,
) -> IdentityFunction: ...
