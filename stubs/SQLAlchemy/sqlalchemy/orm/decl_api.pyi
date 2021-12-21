from collections.abc import Callable
from typing import Any, ClassVar, Type, TypeVar, overload

from ..engine.interfaces import Connectable
from ..sql.schema import MetaData
from ..util import hybridproperty
from . import interfaces

_ClsT = TypeVar("_ClsT", bound=Type[Any])
_DeclT = TypeVar("_DeclT", bound=Type[_DeclarativeBase])

# Dynamic class as created by registry.generate_base() via DeclarativeMeta
# or another metaclass. This class does not exist at runtime.
class _DeclarativeBase(Any):  # super classes are dynamic
    registry: ClassVar[registry]
    metadata: ClassVar[MetaData]
    __abstract__: ClassVar[bool]
    # not always existing:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __mapper_cls__: ClassVar[Any]
    __class_getitem__: ClassVar[Any]

# Meta class (or function) that creates a _DeclarativeBase class.
_DeclarativeBaseMeta = Callable[[str, tuple[Type[Any], ...], dict[str, Any]], _DeclT]

def has_inherited_table(cls: Type[Any]) -> bool: ...

class DeclarativeMeta(type):
    def __init__(cls, classname: str, bases: tuple[Type[Any], ...], dict_: dict[str, Any], **kw: object) -> None: ...
    def __setattr__(cls, key: str, value: Any) -> None: ...
    def __delattr__(cls, key: str) -> None: ...

def synonym_for(name, map_column: bool = ...): ...

class declared_attr(interfaces._MappedAttribute, property):
    def __init__(self, fget, cascading: bool = ...) -> None: ...
    def __get__(self, self_, cls): ...
    @hybridproperty
    def cascading(self): ...

class _stateful_declared_attr(declared_attr):
    kw: Any
    def __init__(self, **kw) -> None: ...
    def __call__(self, fn): ...

def declarative_mixin(cls: _ClsT) -> _ClsT: ...
@overload
def declarative_base(
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    mapper: Any | None = ...,
    cls: Type[Any] | tuple[Type[Any], ...] = ...,
    name: str = ...,
    constructor: Callable[..., None] = ...,
    class_registry: dict[str, Type[Any]] | None = ...,
) -> Type[_DeclarativeBase]: ...
@overload
def declarative_base(
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    mapper: Any | None = ...,
    cls: Type[Any] | tuple[Type[Any], ...] = ...,
    name: str = ...,
    constructor: Callable[..., None] = ...,
    class_registry: dict[str, Type[Any]] | None = ...,
    *,
    metaclass: _DeclarativeBaseMeta[_DeclT],
) -> _DeclT: ...
@overload
def declarative_base(
    bind: Connectable | None,
    metadata: MetaData | None,
    mapper: Any | None,
    cls: Type[Any] | tuple[Type[Any], ...],
    name: str,
    constructor: Callable[..., None],
    class_registry: dict[str, Type[Any]] | None,
    metaclass: _DeclarativeBaseMeta[_DeclT],
) -> _DeclT: ...

class registry:
    metadata: MetaData
    constructor: Callable[..., None]
    def __init__(
        self,
        metadata: MetaData | None = ...,
        class_registry: dict[str, Type[Any]] | None = ...,
        constructor: Callable[..., None] = ...,
        _bind: Connectable | None = ...,
    ) -> None: ...
    @property
    def mappers(self) -> frozenset[Any]: ...
    def configure(self, cascade: bool = ...) -> None: ...
    def dispose(self, cascade: bool = ...) -> None: ...
    @overload
    def generate_base(
        self, mapper: Any | None = ..., cls: Type[Any] | tuple[Type[Any], ...] = ..., name: str = ...
    ) -> Type[_DeclarativeBase]: ...
    @overload
    def generate_base(
        self,
        mapper: Any | None = ...,
        cls: Type[Any] | tuple[Type[Any], ...] = ...,
        name: str = ...,
        *,
        metaclass: _DeclarativeBaseMeta[_DeclT],
    ) -> _DeclT: ...
    @overload
    def generate_base(
        self, mapper: Any | None, cls: Type[Any] | tuple[Type[Any], ...], name: str, metaclass: _DeclarativeBaseMeta[_DeclT]
    ) -> Type[_DeclarativeBase]: ...
    def mapped(self, cls: _ClsT) -> _ClsT: ...
    # Return type of the callable is a _DeclarativeBase class with the passed in class as base.
    # This could be better approximated with Intersection[PassedInClass, _DeclarativeBase].
    def as_declarative_base(
        self, *, mapper: Any | None = ..., metaclass: _DeclarativeBaseMeta[_DeclT] = ...
    ) -> Callable[[_ClsT], _ClsT | _DeclT | Any]: ...
    def map_declaratively(self, cls): ...
    def map_imperatively(self, class_, local_table: Any | None = ..., **kw): ...

def as_declarative(
    *,
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    class_registry: dict[str, Type[Any]] | None = ...,
    mapper: Any | None = ...,
    metaclass: _DeclarativeBaseMeta[_DeclT] = ...,
) -> Callable[[_ClsT], _ClsT | _DeclT | Any]: ...
