import sys
import types
from _typeshed import SupportsAllComparisons, SupportsItems
from collections.abc import Callable, Hashable, Iterable, Sequence, Sized
from typing import Any, Generic, Literal, NamedTuple, Protocol, TypedDict, TypeVar, final, overload
from typing_extensions import Concatenate, ParamSpec, Self, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = [
    "update_wrapper",
    "wraps",
    "WRAPPER_ASSIGNMENTS",
    "WRAPPER_UPDATES",
    "total_ordering",
    "cmp_to_key",
    "lru_cache",
    "reduce",
    "partial",
    "partialmethod",
    "singledispatch",
    "cached_property",
    "singledispatchmethod",
]

if sys.version_info >= (3, 9):
    __all__ += ["cache"]

_T = TypeVar("_T")
_P = ParamSpec("_P")
_Pbound = ParamSpec("_Pbound")
_R = TypeVar("_R")
_T_co = TypeVar("_T_co", covariant=True)
_S = TypeVar("_S")
_PWrapped = ParamSpec("_PWrapped")
_RWrapped = TypeVar("_RWrapped")
_PWrapper = ParamSpec("_PWrapper")
_RWrapper = TypeVar("_RWrapper")

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T, /) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T], /) -> _T: ...

class _CacheInfo(NamedTuple):
    hits: int
    misses: int
    maxsize: int | None
    currsize: int

if sys.version_info >= (3, 9):
    class _CacheParameters(TypedDict):
        maxsize: int
        typed: bool

@final
class _lru_cache_wrapper(Generic[_P, _R]):
    __wrapped__: Callable[_P, _R]
    def __call__(self, *args: Any, **kwargs: Any) -> _R: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    if sys.version_info >= (3, 9):
        def cache_parameters(self) -> _CacheParameters: ...

    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Any, /) -> Self: ...

class _Function(Protocol[_P, _R]):  # type: ignore[misc]  # pyright: ignore reportInvalidTypeVarUse
    def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _R: ...

class _Method(Protocol[_T, _P, _R]):  # type: ignore[misc]  # pyright: ignore reportInvalidTypeVarUse
    def __call__(_self, self: _T, *args: _P.args, **kwds: _P.kwargs) -> _R: ...

class _Classmethod(Protocol[_T, _P, _R]):  # type: ignore[misc]  # pyright: ignore reportInvalidTypeVarUse
    def __call__(_self, cls: type[_T], *args: _P.args, **kwds: _P.kwargs) -> _R: ...

class _LruDescriptor(Protocol[_P, _R]):
    __wrapped__: Callable[_P, _R]
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    if sys.version_info >= (3, 9):
        def cache_parameters(self) -> _CacheParameters: ...

    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: Any, /) -> Self: ...

class _FunctionHasHashable(_LruDescriptor[_P, _R], Protocol[_P, _R]):
    def __call__(self, *args: Hashable, **kwds: Hashable) -> _R: ...

class _BoundHashableDescriptor(_LruDescriptor[_P, _R], Protocol[_P, _Pbound, _R]):
    def __call__(_self, *args: _Pbound.args, **kwds: _Pbound.kwargs) -> _R: ...

class _MethodHasHashableDescriptor(_LruDescriptor[Concatenate[_T, _P], _R], Protocol[_T, _P, _R]):  # type: ignore[misc]
    def __call__(_self, self: _T, *args: _P.args, **kwds: _P.kwargs) -> _R: ...
    @overload
    def __get__(self, instance: None, owner: type[_T]) -> Self: ...
    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _BoundHashableDescriptor[Concatenate[_T, _P], _P, _R]: ...

class _ClassmethodHasHashableDescriptor(_LruDescriptor[Concatenate[type[_T], _P], _R], Protocol[_T, _P, _R]):  # type: ignore[misc]
    def __call__(self, cls: type[_T], *args: Hashable, **kwds: Hashable) -> _R: ...
    @overload
    def __get__(self, instance: None, owner: type[_T]) -> _BoundHashableDescriptor[Concatenate[type[_T], _P], _P, _R]: ...
    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _BoundHashableDescriptor[Concatenate[type[_T], _P], _P, _R]: ...

class _BoundDescriptor(_LruDescriptor[_P, _R], Protocol[_P, _Pbound, _R]):
    def __call__(_self, *args: _Pbound.args, **kwds: _Pbound.kwargs) -> _R: ...

class _MethodDescriptor(_LruDescriptor[Concatenate[_T, _P], _R], Protocol[_T, _P, _R]):  # type: ignore[misc]
    def __call__(_self, self: _T, *args: _P.args, **kwds: _P.kwargs) -> _R: ...
    @overload
    def __get__(self, instance: None, owner: type[_T]) -> Self: ...
    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _BoundDescriptor[Concatenate[_T, _P], _P, _R]: ...

class _ClassmethodDescriptor(_LruDescriptor[Concatenate[type[_T], _P], _R], Protocol[_T, _P, _R]):  # type: ignore[misc]
    def __call__(self, cls: type[_T], *args: _P.args, **kwds: _P.kwargs) -> _R: ...
    @overload
    def __get__(self, instance: None, owner: type[_T]) -> _BoundDescriptor[Concatenate[type[_T], _P], _P, _R]: ...
    @overload
    def __get__(self, instance: _T, owner: type[_T]) -> _BoundDescriptor[Concatenate[type[_T], _P], _P, _R]: ...

class _FunctionDescriptor(_LruDescriptor[_P, _R], Protocol[_P, _R]):
    def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> _R: ...

_CachedMethod: TypeAlias = (
    _MethodDescriptor[_T, _P, _R] | _MethodHasHashableDescriptor[_T, _P, _R] | _lru_cache_wrapper[Concatenate[_T, _P], _R]
)
_CachedClassMethod: TypeAlias = (
    _ClassmethodDescriptor[_T, _P, _R]
    | _ClassmethodHasHashableDescriptor[_T, _P, _R]
    | _lru_cache_wrapper[Concatenate[type[_T], _P], _R]
)
_CachedFunction: TypeAlias = _FunctionDescriptor[_P, _R] | _FunctionHasHashable[_P, _R] | _lru_cache_wrapper[_P, _R]

class _LruInner(Protocol):
    @overload
    def __call__(self, fn: _Method[_T, _P, _R]) -> _CachedMethod[_T, _P, _R]: ...
    @overload
    def __call__(self, fn: _Classmethod[_T, _P, _R]) -> _CachedClassMethod[_T, _P, _R]: ...
    @overload
    def __call__(self, fn: _Function[_P, _R]) -> _CachedFunction[_P, _R]: ...

@overload
def lru_cache(maxsize: _Method[_T, _P, _R], typed: bool = False) -> _CachedMethod[_T, _P, _R]: ...
@overload
def lru_cache(maxsize: _Classmethod[_T, _P, _R], typed: bool = False) -> _CachedClassMethod[_T, _P, _R]: ...
@overload
def lru_cache(maxsize: _Function[_P, _R], typed: bool = False) -> _CachedFunction[_P, _R]: ...
@overload
def lru_cache(maxsize: int | None = 128, typed: bool = False) -> _LruInner: ...

if sys.version_info >= (3, 12):
    WRAPPER_ASSIGNMENTS: tuple[
        Literal["__module__"],
        Literal["__name__"],
        Literal["__qualname__"],
        Literal["__doc__"],
        Literal["__annotations__"],
        Literal["__type_params__"],
    ]
else:
    WRAPPER_ASSIGNMENTS: tuple[
        Literal["__module__"], Literal["__name__"], Literal["__qualname__"], Literal["__doc__"], Literal["__annotations__"]
    ]
WRAPPER_UPDATES: tuple[Literal["__dict__"]]

class _Wrapped(Generic[_PWrapped, _RWrapped, _PWrapper, _RWrapper]):
    __wrapped__: Callable[_PWrapped, _RWrapped]
    def __call__(self, *args: _PWrapper.args, **kwargs: _PWrapper.kwargs) -> _RWrapper: ...
    # as with ``Callable``, we'll assume that these attributes exist
    __name__: str
    __qualname__: str

class _Wrapper(Generic[_PWrapped, _RWrapped]):
    def __call__(self, f: Callable[_PWrapper, _RWrapper]) -> _Wrapped[_PWrapped, _RWrapped, _PWrapper, _RWrapper]: ...

if sys.version_info >= (3, 12):
    def update_wrapper(
        wrapper: Callable[_PWrapper, _RWrapper],
        wrapped: Callable[_PWrapped, _RWrapped],
        assigned: Sequence[str] = ("__module__", "__name__", "__qualname__", "__doc__", "__annotations__", "__type_params__"),
        updated: Sequence[str] = ("__dict__",),
    ) -> _Wrapped[_PWrapped, _RWrapped, _PWrapper, _RWrapper]: ...
    def wraps(
        wrapped: Callable[_PWrapped, _RWrapped],
        assigned: Sequence[str] = ("__module__", "__name__", "__qualname__", "__doc__", "__annotations__", "__type_params__"),
        updated: Sequence[str] = ("__dict__",),
    ) -> _Wrapper[_PWrapped, _RWrapped]: ...

else:
    def update_wrapper(
        wrapper: Callable[_PWrapper, _RWrapper],
        wrapped: Callable[_PWrapped, _RWrapped],
        assigned: Sequence[str] = ("__module__", "__name__", "__qualname__", "__doc__", "__annotations__"),
        updated: Sequence[str] = ("__dict__",),
    ) -> _Wrapped[_PWrapped, _RWrapped, _PWrapper, _RWrapper]: ...
    def wraps(
        wrapped: Callable[_PWrapped, _RWrapped],
        assigned: Sequence[str] = ("__module__", "__name__", "__qualname__", "__doc__", "__annotations__"),
        updated: Sequence[str] = ("__dict__",),
    ) -> _Wrapper[_PWrapped, _RWrapped]: ...

def total_ordering(cls: type[_T]) -> type[_T]: ...
def cmp_to_key(mycmp: Callable[[_T, _T], int]) -> Callable[[_T], SupportsAllComparisons]: ...

class partial(Generic[_T]):
    @property
    def func(self) -> Callable[..., _T]: ...
    @property
    def args(self) -> tuple[Any, ...]: ...
    @property
    def keywords(self) -> dict[str, Any]: ...
    def __new__(cls, func: Callable[..., _T], /, *args: Any, **kwargs: Any) -> Self: ...
    def __call__(self, /, *args: Any, **kwargs: Any) -> _T: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

# With protocols, this could change into a generic protocol that defines __get__ and returns _T
_Descriptor: TypeAlias = Any

class partialmethod(Generic[_T]):
    func: Callable[..., _T] | _Descriptor
    args: tuple[Any, ...]
    keywords: dict[str, Any]
    @overload
    def __init__(self, func: Callable[..., _T], /, *args: Any, **keywords: Any) -> None: ...
    @overload
    def __init__(self, func: _Descriptor, /, *args: Any, **keywords: Any) -> None: ...
    def __get__(self, obj: Any, cls: type[Any] | None = None) -> Callable[..., _T]: ...
    @property
    def __isabstractmethod__(self) -> bool: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

class _SingleDispatchCallable(Generic[_T]):
    registry: types.MappingProxyType[Any, Callable[..., _T]]
    def dispatch(self, cls: Any) -> Callable[..., _T]: ...
    # @fun.register(complex)
    # def _(arg, verbose=False): ...
    @overload
    def register(self, cls: type[Any], func: None = None) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    # @fun.register
    # def _(arg: int, verbose=False):
    @overload
    def register(self, cls: Callable[..., _T], func: None = None) -> Callable[..., _T]: ...
    # fun.register(int, lambda x: x)
    @overload
    def register(self, cls: type[Any], func: Callable[..., _T]) -> Callable[..., _T]: ...
    def _clear_cache(self) -> None: ...
    def __call__(self, /, *args: Any, **kwargs: Any) -> _T: ...

def singledispatch(func: Callable[..., _T]) -> _SingleDispatchCallable[_T]: ...

class singledispatchmethod(Generic[_T]):
    dispatcher: _SingleDispatchCallable[_T]
    func: Callable[..., _T]
    def __init__(self, func: Callable[..., _T]) -> None: ...
    @property
    def __isabstractmethod__(self) -> bool: ...
    @overload
    def register(self, cls: type[Any], method: None = None) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    @overload
    def register(self, cls: Callable[..., _T], method: None = None) -> Callable[..., _T]: ...
    @overload
    def register(self, cls: type[Any], method: Callable[..., _T]) -> Callable[..., _T]: ...
    def __get__(self, obj: _S, cls: type[_S] | None = None) -> Callable[..., _T]: ...

class cached_property(Generic[_T_co]):
    func: Callable[[Any], _T_co]
    attrname: str | None
    def __init__(self, func: Callable[[Any], _T_co]) -> None: ...
    @overload
    def __get__(self, instance: None, owner: type[Any] | None = None) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: type[Any] | None = None) -> _T_co: ...
    def __set_name__(self, owner: type[Any], name: str) -> None: ...
    # __set__ is not defined at runtime, but @cached_property is designed to be settable
    def __set__(self, instance: object, value: _T_co) -> None: ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

if sys.version_info >= (3, 9):
    @overload
    def cache(
        user_function: _Method[_T, _P, _R], /
    ) -> (
        _MethodDescriptor[_T, _P, _R] | _MethodHasHashableDescriptor[_T, _P, _R] | _lru_cache_wrapper[Concatenate[_T, _P], _R]
    ): ...
    @overload
    def cache(
        user_function: _Classmethod[_T, _P, _R], /
    ) -> (
        _ClassmethodDescriptor[_T, _P, _R]
        | _ClassmethodHasHashableDescriptor[_T, _P, _R]
        | _lru_cache_wrapper[Concatenate[type[_T], _P], _R]
    ): ...
    @overload
    def cache(
        user_function: _Function[_P, _R], /
    ) -> _FunctionDescriptor[_P, _R] | _FunctionHasHashable[_P, _R] | _lru_cache_wrapper[_P, _R]: ...

def _make_key(
    args: tuple[Hashable, ...],
    kwds: SupportsItems[Any, Any],
    typed: bool,
    kwd_mark: tuple[object, ...] = ...,
    fasttypes: set[type] = ...,
    tuple: type = ...,
    type: Any = ...,
    len: Callable[[Sized], int] = ...,
) -> Hashable: ...
