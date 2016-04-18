from typing import Any, Callable, Generic, Optional, TypeVar

_T = TypeVar('_T')

class CallableProxyType(object):  # "weakcallableproxy"
  pass

class ProxyType(object):  # "weakproxy"
  pass

class ReferenceType(Generic[_T]):
    # TODO rest of members
    def __call__(self) -> Optional[_T]:
        ...

def ref(o: _T, callback: Callable[[ReferenceType[_T]],
                                 Any] = ...) -> ReferenceType[_T]: ...

def getweakrefcount(object: Any) -> int: ...
def getweakrefs(object: Any) -> int: ...
def proxy(object: Any, callback: Callable[[Any], Any] = ...) -> None: ...
