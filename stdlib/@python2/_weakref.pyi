import sys
from typing import Any, Callable, Generic, List, Optional, TypeVar, overload

_C = TypeVar("_C", bound=Callable[..., Any])
_T = TypeVar("_T")

class CallableProxyType(Generic[_C]):  # "weakcallableproxy"
    def __getattr__(self, attr: str) -> Any: ...

class ProxyType(Generic[_T]):  # "weakproxy"
    def __getattr__(self, attr: str) -> Any: ...

class ReferenceType(Generic[_T]):
    def __init__(self, o: _T, callback: Optional[Callable[[ReferenceType[_T]], Any]] = ...) -> None: ...
    def __call__(self) -> Optional[_T]: ...
    def __hash__(self) -> int: ...

ref = ReferenceType

def getweakrefcount(__object: Any) -> int: ...
def getweakrefs(object: Any) -> List[Any]: ...
@overload
def proxy(object: _C, callback: Optional[Callable[[_C], Any]] = ...) -> CallableProxyType[_C]: ...

# Return CallableProxyType if object is callable, ProxyType otherwise
@overload
def proxy(object: _T, callback: Optional[Callable[[_T], Any]] = ...) -> Any: ...
