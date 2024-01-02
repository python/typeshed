from collections.abc import Callable
from typing import Any, TypeVar, overload
from weakref import CallableProxyType as CallableProxyType, ProxyType as ProxyType, ReferenceType as ReferenceType, ref as ref

_C = TypeVar("_C", bound=Callable[..., Any])
_T = TypeVar("_T")

def getweakrefcount(__object: Any) -> int: ...
def getweakrefs(__object: Any) -> list[Any]: ...

# Return CallableProxyType if object is callable, ProxyType otherwise
@overload
def proxy(__object: _C, __callback: Callable[[_C], Any] | None = None) -> CallableProxyType[_C]: ...
@overload
def proxy(__object: _T, __callback: Callable[[_T], Any] | None = None) -> Any: ...
