from typing import Any

from ..orm import interfaces
from ..sql.operators import ColumnOperators
from ..util import memoized_property

def association_proxy(target_collection, attr, **kw): ...

ASSOCIATION_PROXY: Any

class AssociationProxy(interfaces.InspectionAttrInfo):
    is_attribute: bool
    extension_type: Any
    target_collection: Any
    value_attr: Any
    creator: Any
    getset_factory: Any
    proxy_factory: Any
    proxy_bulk_set: Any
    cascade_scalar_deletes: Any
    key: Any
    info: Any
    def __init__(
        self,
        target_collection,
        attr,
        creator: Any | None = ...,
        getset_factory: Any | None = ...,
        proxy_factory: Any | None = ...,
        proxy_bulk_set: Any | None = ...,
        info: Any | None = ...,
        cascade_scalar_deletes: bool = ...,
    ) -> None: ...
    def __get__(self, obj, class_): ...
    def __set__(self, obj: Any, values: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...
    def for_class(self, class_, obj: Any | None = ...): ...

class AssociationProxyInstance:
    parent: Any
    key: Any
    owning_class: Any
    target_collection: Any
    collection_class: Any
    target_class: Any
    value_attr: Any
    def __init__(self, parent, owning_class, target_class, value_attr) -> None: ...
    @classmethod
    def for_proxy(cls, parent, owning_class, parent_instance): ...
    def __clause_element__(self) -> None: ...
    @property
    def remote_attr(self): ...
    @property
    def local_attr(self): ...
    @property
    def attr(self): ...
    @memoized_property
    def scalar(self): ...
    @property
    def info(self): ...
    def get(self, obj): ...
    def set(self, obj, values) -> None: ...
    def delete(self, obj) -> None: ...
    def any(self, criterion: Any | None = ..., **kwargs): ...
    def has(self, criterion: Any | None = ..., **kwargs): ...

class AmbiguousAssociationProxyInstance(AssociationProxyInstance):
    def get(self, obj): ...
    def __eq__(self, obj): ...
    def __ne__(self, obj): ...
    def any(self, criterion: Any | None = ..., **kwargs) -> None: ...
    def has(self, criterion: Any | None = ..., **kwargs) -> None: ...

class ObjectAssociationProxyInstance(AssociationProxyInstance):
    def contains(self, obj): ...
    def __eq__(self, obj): ...
    def __ne__(self, obj): ...

class ColumnAssociationProxyInstance(ColumnOperators[Any], AssociationProxyInstance):
    def __eq__(self, other) -> ColumnOperators[Any]: ...  # type: ignore[override]
    def operate(self, op, *other, **kwargs): ...

class _lazy_collection:
    parent: Any
    target: Any
    def __init__(self, obj, target) -> None: ...
    def __call__(self): ...

class _AssociationCollection:
    lazy_collection: Any
    creator: Any
    getter: Any
    setter: Any
    parent: Any
    def __init__(self, lazy_collection, creator, getter, setter, parent) -> None: ...
    @property
    def col(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any

class _AssociationList(_AssociationCollection):
    def __getitem__(self, index): ...
    def __setitem__(self, index, value) -> None: ...
    def __delitem__(self, index) -> None: ...
    def __contains__(self, value): ...
    def __getslice__(self, start, end): ...
    def __setslice__(self, start, end, values) -> None: ...
    def __delslice__(self, start, end) -> None: ...
    def __iter__(self): ...
    def append(self, value) -> None: ...
    def count(self, value): ...
    def extend(self, values) -> None: ...
    def insert(self, index, value) -> None: ...
    def pop(self, index: int = ...): ...
    def remove(self, value) -> None: ...
    def reverse(self) -> None: ...
    def sort(self) -> None: ...
    def clear(self) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __cmp__(self, other): ...
    def __add__(self, iterable): ...
    def __radd__(self, iterable): ...
    def __mul__(self, n): ...
    __rmul__: Any
    def __iadd__(self, iterable): ...
    def __imul__(self, n): ...
    def index(self, item, *args): ...
    def copy(self): ...
    def __hash__(self) -> int: ...

class _AssociationDict(_AssociationCollection):
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key): ...
    def has_key(self, key): ...
    def __iter__(self): ...
    def clear(self) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __cmp__(self, other): ...
    def get(self, key, default: Any | None = ...): ...
    def setdefault(self, key, default: Any | None = ...): ...
    def keys(self): ...
    def items(self): ...
    def values(self): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def update(self, *a, **kw) -> None: ...
    def copy(self): ...
    def __hash__(self) -> int: ...

class _AssociationSet(_AssociationCollection):
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any
    def __contains__(self, value): ...
    def __iter__(self): ...
    def add(self, value) -> None: ...
    def discard(self, value) -> None: ...
    def remove(self, value) -> None: ...
    def pop(self): ...
    def update(self, other) -> None: ...
    def __ior__(self, other): ...  # type: ignore[misc]
    def union(self, other): ...
    __or__: Any
    def difference(self, other): ...
    __sub__: Any
    def difference_update(self, other) -> None: ...
    def __isub__(self, other): ...  # type: ignore[misc]
    def intersection(self, other): ...
    __and__: Any
    def intersection_update(self, other) -> None: ...
    def __iand__(self, other): ...  # type: ignore[misc]
    def symmetric_difference(self, other): ...
    __xor__: Any
    def symmetric_difference_update(self, other) -> None: ...
    def __ixor__(self, other): ...  # type: ignore[misc]
    def issubset(self, other): ...
    def issuperset(self, other): ...
    def clear(self) -> None: ...
    def copy(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self) -> int: ...
