from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Hashable
from typing import Any, NoReturn

class OrderedMultiDict(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    def add(self, k, v) -> None: ...
    def addlist(self, k, v) -> None: ...
    def get(self, k, default: Incomplete | None = ...): ...
    def getlist(self, k, default=...): ...
    def clear(self) -> None: ...
    def setdefault(self, k, default=...): ...
    def copy(self): ...
    @classmethod
    def fromkeys(cls, keys, default: Incomplete | None = ...): ...
    def update(self, E, **F) -> None: ...
    def update_extend(self, E, **F) -> None: ...
    def __setitem__(self, k, v) -> None: ...
    def __getitem__(self, k): ...
    def __delitem__(self, k) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def pop(self, k, default=...): ...
    def popall(self, k, default=...): ...
    def poplast(self, k=..., default=...): ...
    def iteritems(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def iterkeys(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def itervalues(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def todict(self, multi: bool = ...): ...
    def sorted(self, key: Incomplete | None = ..., reverse: bool = ...): ...
    def sortedvalues(self, key: Incomplete | None = ..., reverse: bool = ...): ...
    def inverted(self): ...
    def counts(self): ...
    def keys(self, multi: bool = ...): ...
    def values(self, multi: bool = ...): ...
    def items(self, multi: bool = ...): ...
    def __iter__(self): ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...
    def viewkeys(self): ...
    def viewvalues(self): ...
    def viewitems(self): ...

OMD = OrderedMultiDict
MultiDict = OrderedMultiDict

class FastIterOrderedMultiDict(OrderedMultiDict):
    def iteritems(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def iterkeys(self, multi: bool = ...) -> Generator[Incomplete, None, None]: ...
    def __reversed__(self) -> Generator[Incomplete, None, None]: ...

class OneToOne(dict):
    inv: Incomplete
    def __init__(self, *a, **kw) -> None: ...
    @classmethod
    def unique(cls, *a, **kw): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def setdefault(self, key, default: Incomplete | None = ...): ...
    def update(self, dict_or_iterable, **kw) -> None: ...

class ManyToMany:
    def __getattr__(self, name: str) -> Any: ...  # incomplete
    data: dict[Hashable, object]
    inv: tuple[object]
    def add(self, key: Hashable, val: object) -> NoReturn: ...
    def get(self, key: Hashable, default: frozenset = ...) -> Any: ...
    def iteritems(self) -> Generator[tuple[Hashable, object], None, None]: ...
    def keys(self): ...  # incomplete
    def remove(self, key: Hashable, val: object) -> NoReturn: ...
    def replace(self, key: Hashable, newkey: Hashable) -> NoReturn: ...
    def update(self, iterable: Iterable) -> NoReturn: ...

def subdict(d: dict[Hashable, object], keep: Iterable[object] | None = ..., drop: Iterable[object] | None = ...) -> dict[Hashable, object]: ...

class FrozenHashError(TypeError): ...  # undocumented

class FrozenDict(dict):
    def clear(self, *a, **kw) -> NoReturn: ...
    @classmethod
    def fromkeys(cls, keys: Iterable[object], value: object | None = ...) -> FrozenDict: ...
    def pop(self, *a, **kw) -> NoReturn: ...
    def popitem(self, *a, **kw) -> NoReturn: ...
    def setdefault(self, *a, **kw) -> NoReturn: ...
    def updated(self, *a, **kw) -> FrozenDict: ...
