from typing import overload, Any, Callable, Dict, Generic, Iterable, Mapping, Optional, Tuple, Type, TypeVar, Union


_T = TypeVar('_T')

_DictType = TypeVar('_DictType', bound=dict)
_TupleType = TypeVar('_TupleType', bound=tuple)

class _MISSING_TYPE: ...

class _InitVarMeta(type): ...

def asdict(obj: Any, *, dict_factory: _DictType = ...) -> _DictType: ...

def astuple(obj: Any, *, tuple_factory: _TupleType = ...) -> _TupleType: ...

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


def field(*, default: Union[_T, _MISSING_TYPE] = ..., default_factory: Union[Callable[[], _T], _MISSING_TYPE] = ...,
    init: bool = ..., repr: bool = ..., hash: Optional[bool] = ..., compare: bool = ...,
    metadata: Optional[Mapping[str, Any]] = ...) -> Field: ...

def fields(class_or_instance: Type) -> Tuple[Field, ...]: ...

def is_dataclass(obj: Any) -> bool: ...

class FrozenInstanceError(AttributeError): ...

class InitVar(metaclass=_InitVarMeta): ...

def make_dataclass(cls_name: str, fields: Iterable[Union[str, Tuple[str, type], Tuple[str, type, Field]]], *,
    bases: Tuple[type, ...] = ..., namespace: Dict[str, Any] = ...,
    init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., hash: bool = ..., frozen: bool = ...): ...

def replace(obj: _T, **changes: Any) -> _T: ...
