from typing import Any

from ..util import hybridproperty
from . import interfaces

def has_inherited_table(cls): ...

class DeclarativeMeta(type):
    def __init__(cls, classname, bases, dict_, **kw) -> None: ...
    def __setattr__(cls, key, value) -> None: ...
    def __delattr__(cls, key) -> None: ...

def synonym_for(name, map_column: bool = ...): ...

class declared_attr(interfaces._MappedAttribute, property):
    __doc__: Any
    def __init__(self, fget, cascading: bool = ...) -> None: ...
    def __get__(self, self_, cls): ...
    @hybridproperty
    def cascading(self): ...

class _stateful_declared_attr(declared_attr):
    kw: Any
    def __init__(self, **kw) -> None: ...
    def __call__(self, fn): ...

def declarative_mixin(cls): ...
def declarative_base(
    bind: Any | None = ...,
    metadata: Any | None = ...,
    mapper: Any | None = ...,
    cls=...,
    name: str = ...,
    constructor=...,
    class_registry: Any | None = ...,
    metaclass=...,
): ...

class registry:
    metadata: Any
    constructor: Any
    def __init__(
        self, metadata: Any | None = ..., class_registry: Any | None = ..., constructor=..., _bind: Any | None = ...
    ) -> None: ...
    @property
    def mappers(self): ...
    def configure(self, cascade: bool = ...) -> None: ...
    def dispose(self, cascade: bool = ...) -> None: ...
    def generate_base(self, mapper: Any | None = ..., cls=..., name: str = ..., metaclass=...): ...
    def mapped(self, cls): ...
    def as_declarative_base(self, **kw): ...
    def map_declaratively(self, cls): ...
    def map_imperatively(self, class_, local_table: Any | None = ..., **kw): ...

def as_declarative(**kw): ...
