from typing import overload, Any, Callable, Dict, Generic, Iterable, Mapping, Optional, Tuple, Type, TypeVar, Union


_T = TypeVar('_T')

_DictFactory = Callable[List[Tuple[str, Any]], _T]
_TupleFactory = Callable[List[Any], _T]

class _MISSING_TYPE: ...
MISSING: _MISSING_TYPE

class _InitVarMeta(type): ...

def asdict(obj: Any, *, dict_factory: _DictFactory = ...) -> _T: ...

def astuple(obj: Any, *, tuple_factory: _TupleFactory = ...) -> _T: ...


@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...

@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ...,
    unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...


class Field(Generic[_T]):
    name: str
    type: Type[_T]
    default: _T
    default_factory: Callable[[], _T]
    repr: bool
    hash: Optional[bool]
    init: bool
    compare: bool
    metadata: Optional[Mapping[str, Any]]


@overload # `default` and `default_factory` are optional and mutually exclusive.
def field(*, default: _T = ..., default_factory: _MISSING_TYPE = ...,
    init: bool = ..., repr: bool = ..., hash: Optional[bool] = ..., compare: bool = ...,
    metadata: Optional[Mapping[str, Any]] = ...) -> Field[_T]: ...

@overload
def field(*, default: _MISSING_TYPE = ..., default_factory: Callable[[], _T] = ...,
    init: bool = ..., repr: bool = ..., hash: Optional[bool] = ..., compare: bool = ...,
    metadata: Optional[Mapping[str, Any]] = ...) -> Field[_T]: ...

@overload
def field(*, default: _MISSING_TYPE = ..., default_factory: _MISSING_TYPE = ...,
    init: bool = ..., repr: bool = ..., hash: Optional[bool] = ..., compare: bool = ...,
    metadata: Optional[Mapping[str, Any]] = ...) -> Field[Any]: ...


def fields(class_or_instance: Any) -> Tuple[Field[Any], ...]: ...

def is_dataclass(obj: Any) -> bool: ...

class FrozenInstanceError(AttributeError): ...

class InitVar(metaclass=_InitVarMeta): ...

def make_dataclass(cls_name: str, fields: Iterable[Union[str, Tuple[str, type], Tuple[str, type, Field[Any]]]], *,
    bases: Tuple[type, ...] = ..., namespace: Optional[Dict[str, Any]] = ...,
    init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., hash: bool = ..., frozen: bool = ...): ...

def replace(obj: _T, **changes: Any) -> _T: ...
