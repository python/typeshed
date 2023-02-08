from typing_extensions import Self
import sys
from _typeshed import SupportsKeysAndGetItem
from _weakref import (
    CallableProxyType as CallableProxyType,
    ProxyType as ProxyType,
    ReferenceType as ReferenceType,
    getweakrefcount as getweakrefcount,
    getweakrefs as getweakrefs,
    proxy as proxy,
    ref as ref,
)
from _weakrefset import WeakSet as WeakSet
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableMapping
from typing import Any, Generic, TypeVar, overload
from typing_extensions import ParamSpec

__all__ = [
    "ref",
    "proxy",
    "getweakrefcount",
    "getweakrefs",
    "WeakKeyDictionary",
    "ReferenceType",
    "ProxyType",
    "CallableProxyType",
    "ProxyTypes",
    "WeakValueDictionary",
    "WeakSet",
    "WeakMethod",
    "finalize",
]

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_CallableT = TypeVar("_CallableT", bound=Callable[..., Any])
_P = ParamSpec("_P")

ProxyTypes: tuple[type[Any], ...]

class WeakMethod(ref[_CallableT], Generic[_CallableT]):
    def __new__(cls, meth: _CallableT, callback: Callable[[_CallableT], object] | None = None) -> Self: ...
    def __call__(self) -> _CallableT | None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class WeakValueDictionary(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self: WeakValueDictionary[_KT, _VT], __other: Mapping[_KT, _VT] | Iterable[tuple[_KT, _VT]]) -> None: ...
    @overload
    def __init__(
        self: WeakValueDictionary[str, _VT], __other: Mapping[str, _VT] | Iterable[tuple[str, _VT]] = ..., **kwargs: _VT
    ) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def copy(self) -> WeakValueDictionary[_KT, _VT]: ...
    __copy__ = copy
    def __deepcopy__(self, memo: Any) -> Self: ...
    # These are incompatible with Mapping
    def keys(self) -> Iterator[_KT]: ...  # type: ignore[override]
    def values(self) -> Iterator[_VT]: ...  # type: ignore[override]
    def items(self) -> Iterator[tuple[_KT, _VT]]: ...  # type: ignore[override]
    def itervaluerefs(self) -> Iterator[KeyedRef[_KT, _VT]]: ...
    def valuerefs(self) -> list[KeyedRef[_KT, _VT]]: ...
    def setdefault(self, key: _KT, default: _VT) -> _VT: ...  # type: ignore[override]
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T = ...) -> _VT | _T: ...
    if sys.version_info >= (3, 9):
        def __or__(self, other: Mapping[_T1, _T2]) -> WeakValueDictionary[_KT | _T1, _VT | _T2]: ...
        def __ror__(self, other: Mapping[_T1, _T2]) -> WeakValueDictionary[_KT | _T1, _VT | _T2]: ...
        # WeakValueDictionary.__ior__ should be kept roughly in line with MutableMapping.update()
        @overload  # type: ignore[misc]
        def __ior__(self, other: SupportsKeysAndGetItem[_KT, _VT]) -> Self: ...
        @overload
        def __ior__(self, other: Iterable[tuple[_KT, _VT]]) -> Self: ...

class KeyedRef(ref[_T], Generic[_KT, _T]):
    key: _KT
    # This __new__ method uses a non-standard name for the "cls" parameter
    def __new__(type, ob: _T, callback: Callable[[_T], Any], key: _KT) -> Self: ...
    def __init__(self, ob: _T, callback: Callable[[_T], Any], key: _KT) -> None: ...

class WeakKeyDictionary(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self, dict: None = None) -> None: ...
    @overload
    def __init__(self, dict: Mapping[_KT, _VT] | Iterable[tuple[_KT, _VT]]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def copy(self) -> WeakKeyDictionary[_KT, _VT]: ...
    __copy__ = copy
    def __deepcopy__(self, memo: Any) -> Self: ...
    # These are incompatible with Mapping
    def keys(self) -> Iterator[_KT]: ...  # type: ignore[override]
    def values(self) -> Iterator[_VT]: ...  # type: ignore[override]
    def items(self) -> Iterator[tuple[_KT, _VT]]: ...  # type: ignore[override]
    def keyrefs(self) -> list[ref[_KT]]: ...
    # Keep WeakKeyDictionary.setdefault in line with MutableMapping.setdefault, modulo positional-only differences
    @overload
    def setdefault(self: WeakKeyDictionary[_KT, _VT | None], key: _KT, default: None = None) -> _VT: ...
    @overload
    def setdefault(self, key: _KT, default: _VT) -> _VT: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _VT | _T = ...) -> _VT | _T: ...
    if sys.version_info >= (3, 9):
        def __or__(self, other: Mapping[_T1, _T2]) -> WeakKeyDictionary[_KT | _T1, _VT | _T2]: ...
        def __ror__(self, other: Mapping[_T1, _T2]) -> WeakKeyDictionary[_KT | _T1, _VT | _T2]: ...
        # WeakKeyDictionary.__ior__ should be kept roughly in line with MutableMapping.update()
        @overload  # type: ignore[misc]
        def __ior__(self, other: SupportsKeysAndGetItem[_KT, _VT]) -> Self: ...
        @overload
        def __ior__(self, other: Iterable[tuple[_KT, _VT]]) -> Self: ...

class finalize:  # TODO: This is a good candidate for to be a `Generic[_P, _T]` class
    def __init__(self, __obj: object, __func: Callable[_P, Any], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
    def __call__(self, _: Any = None) -> Any | None: ...
    def detach(self) -> tuple[Any, Any, tuple[Any, ...], dict[str, Any]] | None: ...
    def peek(self) -> tuple[Any, Any, tuple[Any, ...], dict[str, Any]] | None: ...
    @property
    def alive(self) -> bool: ...
    atexit: bool
