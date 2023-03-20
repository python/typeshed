import sys
import types
from _typeshed import SupportsAllComparisons, SupportsItems
from collections.abc import Callable, Hashable, Iterable, Sequence, Sized
from typing import Any, Generic, NamedTuple, TypeVar, overload
from typing_extensions import Literal, ParamSpec, Self, TypeAlias, final

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
]

if sys.version_info >= (3, 8):
    __all__ += ["cached_property", "singledispatchmethod"]

if sys.version_info >= (3, 9):
    __all__ += ["cache"]

_T = TypeVar("_T")
_S = TypeVar("_S")
_PWrapped = ParamSpec("_PWrapped")
_RWrapped = TypeVar("_RWrapped")
_PWrapper = ParamSpec("_PWrapper")
_RWapper = TypeVar("_RWapper")

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...

class _CacheInfo(NamedTuple):
    hits: int
    misses: int
    maxsize: int | None
    currsize: int

@final
class _lru_cache_wrapper(Generic[_T]):
    __wrapped__: Callable[..., _T]
    def __call__(self, *args: Hashable, **kwargs: Hashable) -> _T: ...
    def cache_info(self) -> _CacheInfo: ...
    def cache_clear(self) -> None: ...
    def __copy__(self) -> _lru_cache_wrapper[_T]: ...
    def __deepcopy__(self, __memo: Any) -> _lru_cache_wrapper[_T]: ...

if sys.version_info >= (3, 8):
    @overload
    def lru_cache(maxsize: int | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _lru_cache_wrapper[_T]]: ...
    @overload
    def lru_cache(maxsize: Callable[..., _T], typed: bool = False) -> _lru_cache_wrapper[_T]: ...

else:
    def lru_cache(maxsize: int | None = 128, typed: bool = False) -> Callable[[Callable[..., _T]], _lru_cache_wrapper[_T]]: ...

WRAPPER_ASSIGNMENTS: tuple[
    Literal["__module__"], Literal["__name__"], Literal["__qualname__"], Literal["__doc__"], Literal["__annotations__"]
]
WRAPPER_UPDATES: tuple[Literal["__dict__"]]

class _Wrapped(Generic[_PWrapped, _RWrapped, _PWrapper, _RWapper]):
    __wrapped__: Callable[_PWrapped, _RWrapped]
    def __call__(self, *args: _PWrapper.args, **kwargs: _PWrapper.kwargs) -> _RWapper: ...
    # as with ``Callable``, we'll assume that these attributes exist
    __name__: str
    __qualname__: str

class _Wrapper(Generic[_PWrapped, _RWrapped]):
    def __call__(self, f: Callable[_PWrapper, _RWapper]) -> _Wrapped[_PWrapped, _RWrapped, _PWrapper, _RWapper]: ...

def update_wrapper(
    wrapper: Callable[_PWrapper, _RWapper],
    wrapped: Callable[_PWrapped, _RWrapped],
    assigned: Sequence[str] = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'),
    updated: Sequence[str] = ('__dict__',),
) -> _Wrapped[_PWrapped, _RWrapped, _PWrapper, _RWapper]: ...
def wraps(
    wrapped: Callable[_PWrapped, _RWrapped], assigned: Sequence[str] = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated: Sequence[str] = ('__dict__',)
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
    def __new__(cls, __func: Callable[..., _T], *args: Any, **kwargs: Any) -> Self: ...
    def __call__(__self, *args: Any, **kwargs: Any) -> _T: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

# With protocols, this could change into a generic protocol that defines __get__ and returns _T
_Descriptor: TypeAlias = Any

class partialmethod(Generic[_T]):
    func: Callable[..., _T] | _Descriptor
    args: tuple[Any, ...]
    keywords: dict[str, Any]
    @overload
    def __init__(self, __func: Callable[..., _T], *args: Any, **keywords: Any) -> None: ...
    @overload
    def __init__(self, __func: _Descriptor, *args: Any, **keywords: Any) -> None: ...
    if sys.version_info >= (3, 8):
        def __get__(self, obj: Any, cls: type[Any] | None = None) -> Callable[..., _T]: ...
    else:
        def __get__(self, obj: Any, cls: type[Any] | None) -> Callable[..., _T]: ...

    @property
    def __isabstractmethod__(self) -> bool: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

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
    def __call__(__self, *args: Any, **kwargs: Any) -> _T: ...

def singledispatch(func: Callable[..., _T]) -> _SingleDispatchCallable[_T]: ...

if sys.version_info >= (3, 8):
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

    class cached_property(Generic[_T]):
        func: Callable[[Any], _T]
        attrname: str | None
        def __init__(self, func: Callable[[Any], _T]) -> None: ...
        @overload
        def __get__(self, instance: None, owner: type[Any] | None = None) -> cached_property[_T]: ...
        @overload
        def __get__(self, instance: object, owner: type[Any] | None = None) -> _T: ...
        def __set_name__(self, owner: type[Any], name: str) -> None: ...
        # __set__ is not defined at runtime, but @cached_property is designed to be settable
        def __set__(self, instance: object, value: _T) -> None: ...
        if sys.version_info >= (3, 9):
            def __class_getitem__(cls, item: Any) -> GenericAlias: ...

if sys.version_info >= (3, 9):
    def cache(__user_function: Callable[..., _T]) -> _lru_cache_wrapper[_T]: ...

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
