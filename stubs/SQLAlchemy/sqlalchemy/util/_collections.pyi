import collections.abc
import sys
from typing import Any

from ..cimmutabledict import immutabledict as immutabledict

collections_abc = collections.abc

EMPTY_SET: Any

class ImmutableContainer:
    __delitem__: Any
    __setitem__: Any
    __setattr__: Any

def coerce_to_immutabledict(d): ...

EMPTY_DICT: Any

class FacadeDict(ImmutableContainer, dict):
    clear: Any
    pop: Any
    popitem: Any
    setdefault: Any
    update: Any
    def __new__(cls, *args): ...
    def copy(self) -> None: ...  # type: ignore[override]
    def __reduce__(self): ...

class Properties:
    def __init__(self, data) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __dir__(self): ...
    def __add__(self, other): ...
    def __setitem__(self, key, obj) -> None: ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __setattr__(self, key, obj) -> None: ...
    def __getattr__(self, key): ...
    def __contains__(self, key): ...
    def as_immutable(self): ...
    def update(self, value) -> None: ...
    def get(self, key, default: Any | None = ...): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def has_key(self, key): ...
    def clear(self) -> None: ...

class OrderedProperties(Properties):
    def __init__(self) -> None: ...

class ImmutableProperties(ImmutableContainer, Properties): ...

if sys.version_info >= (3, 7):
    OrderedDict = dict
else:
    class OrderedDict(dict):
        def __reduce__(self): ...
        def __init__(self, ____sequence: Any | None = ..., **kwargs) -> None: ...
        def clear(self) -> None: ...
        def copy(self): ...
        def __copy__(self): ...
        def update(self, ____sequence: Any | None = ..., **kwargs) -> None: ...
        def setdefault(self, key, value): ...
        def __iter__(self): ...
        def keys(self): ...
        def values(self): ...
        def items(self): ...
        def itervalues(self): ...
        def iterkeys(self): ...
        def iteritems(self): ...
        def __setitem__(self, key, obj) -> None: ...
        def __delitem__(self, key) -> None: ...
        def pop(self, key, *default): ...
        def popitem(self): ...

def sort_dictionary(d, key: Any | None = ...): ...

class OrderedSet(set):
    def __init__(self, d: Any | None = ...) -> None: ...
    def add(self, element) -> None: ...
    def remove(self, element) -> None: ...
    def insert(self, pos, element) -> None: ...
    def discard(self, element) -> None: ...
    def clear(self) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __add__(self, other): ...
    def update(self, iterable): ...
    __ior__: Any
    def union(self, other): ...
    __or__: Any
    def intersection(self, other): ...
    __and__: Any
    def symmetric_difference(self, other): ...
    __xor__: Any
    def difference(self, other): ...
    __sub__: Any
    def intersection_update(self, other): ...
    __iand__: Any
    def symmetric_difference_update(self, other): ...
    __ixor__: Any
    def difference_update(self, other): ...
    __isub__: Any

class IdentitySet:
    def __init__(self, iterable: Any | None = ...) -> None: ...
    def add(self, value) -> None: ...
    def __contains__(self, value): ...
    def remove(self, value) -> None: ...
    def discard(self, value) -> None: ...
    def pop(self): ...
    def clear(self) -> None: ...
    def __cmp__(self, other) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def issubset(self, iterable): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def issuperset(self, iterable): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def union(self, iterable): ...
    def __or__(self, other): ...
    def update(self, iterable) -> None: ...
    def __ior__(self, other): ...
    def difference(self, iterable): ...
    def __sub__(self, other): ...
    def difference_update(self, iterable) -> None: ...
    def __isub__(self, other): ...
    def intersection(self, iterable): ...
    def __and__(self, other): ...
    def intersection_update(self, iterable) -> None: ...
    def __iand__(self, other): ...
    def symmetric_difference(self, iterable): ...
    def __xor__(self, other): ...
    def symmetric_difference_update(self, iterable) -> None: ...
    def __ixor__(self, other): ...
    def copy(self): ...
    __copy__: Any
    def __len__(self): ...
    def __iter__(self): ...
    def __hash__(self): ...

class WeakSequence:
    def __init__(self, __elements=...) -> None: ...
    def append(self, item) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, index): ...

class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable: Any | None = ...) -> None: ...

class PopulateDict(dict):
    creator: Any
    def __init__(self, creator) -> None: ...
    def __missing__(self, key): ...

class WeakPopulateDict(dict):
    creator: Any
    weakself: Any
    def __init__(self, creator_method) -> None: ...
    def __missing__(self, key): ...

column_set = set
column_dict = dict
ordered_column_set = OrderedSet

def unique_list(seq, hashfunc: Any | None = ...): ...

class UniqueAppender:
    data: Any
    def __init__(self, data, via: Any | None = ...) -> None: ...
    def append(self, item) -> None: ...
    def __iter__(self): ...

def coerce_generator_arg(arg): ...
def to_list(x, default: Any | None = ...): ...
def has_intersection(set_, iterable): ...
def to_set(x): ...
def to_column_set(x): ...
def update_copy(d, _new: Any | None = ..., **kw): ...
def flatten_iterator(x) -> None: ...

class LRUCache(dict):
    capacity: Any
    threshold: Any
    size_alert: Any
    def __init__(self, capacity: int = ..., threshold: float = ..., size_alert: Any | None = ...) -> None: ...
    def get(self, key, default: Any | None = ...): ...
    def __getitem__(self, key): ...
    def values(self): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value) -> None: ...
    @property
    def size_threshold(self): ...

class ScopedRegistry:
    createfunc: Any
    scopefunc: Any
    registry: Any
    def __init__(self, createfunc, scopefunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj) -> None: ...
    def clear(self) -> None: ...

class ThreadLocalRegistry(ScopedRegistry):
    createfunc: Any
    registry: Any
    def __init__(self, createfunc) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj) -> None: ...
    def clear(self) -> None: ...

def has_dupes(sequence, target): ...
