from _typeshed import Incomplete
from typing import Any

class _PlainColumnGetter:
    cols: Any
    composite: Any
    def __init__(self, cols) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value): ...

class _SerializableColumnGetter:
    colkeys: Any
    composite: Any
    def __init__(self, colkeys) -> None: ...
    def __reduce__(self): ...
    def __call__(self, value): ...

class _SerializableColumnGetterV2(_PlainColumnGetter):
    colkeys: Any
    composite: Any
    def __init__(self, colkeys) -> None: ...
    def __reduce__(self): ...

def column_mapped_collection(mapping_spec): ...

class _SerializableAttrGetter:
    name: Any
    getter: Any
    def __init__(self, name) -> None: ...
    def __call__(self, target): ...
    def __reduce__(self): ...

def attribute_mapped_collection(attr_name): ...
def mapped_collection(keyfunc): ...

class collection:
    @staticmethod
    def appender(fn): ...
    @staticmethod
    def remover(fn): ...
    @staticmethod
    def iterator(fn): ...
    @staticmethod
    def internally_instrumented(fn): ...
    @staticmethod
    def converter(fn): ...
    @staticmethod
    def adds(arg): ...
    @staticmethod
    def replaces(arg): ...
    @staticmethod
    def removes(arg): ...
    @staticmethod
    def removes_return(): ...

collection_adapter: Any

class CollectionAdapter:
    attr: Any
    owner_state: Any
    invalidated: bool
    empty: bool
    def __init__(self, attr, owner_state, data) -> None: ...
    @property
    def data(self): ...
    def bulk_appender(self): ...
    def append_with_event(self, item, initiator: Incomplete | None = ...) -> None: ...
    def append_without_event(self, item) -> None: ...
    def append_multiple_without_event(self, items) -> None: ...
    def bulk_remover(self): ...
    def remove_with_event(self, item, initiator: Incomplete | None = ...) -> None: ...
    def remove_without_event(self, item) -> None: ...
    def clear_with_event(self, initiator: Incomplete | None = ...) -> None: ...
    def clear_without_event(self) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def fire_append_wo_mutation_event(self, item, initiator: Incomplete | None = ...): ...
    def fire_append_event(self, item, initiator: Incomplete | None = ...): ...
    def fire_remove_event(self, item, initiator: Incomplete | None = ...) -> None: ...
    def fire_pre_remove_event(self, initiator: Incomplete | None = ...) -> None: ...

class InstrumentedList(list[Any]): ...
class InstrumentedSet(set[Any]): ...
class InstrumentedDict(dict[Any, Any]): ...

class MappedCollection(dict[Any, Any]):
    keyfunc: Any
    def __init__(self, keyfunc) -> None: ...
    def set(self, value, _sa_initiator: Incomplete | None = ...) -> None: ...
    def remove(self, value, _sa_initiator: Incomplete | None = ...) -> None: ...