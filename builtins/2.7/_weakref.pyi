from typing import Any, Callable

class CallableProxyType(object):  # "weakcallableproxy"
  pass

class ProxyType(object):  # "weakproxy"
  pass

class ReferenceType(object):  # "weakref"
  pass

ref = ReferenceType

def getweakrefcount(object: Any) -> int: ...
def getweakrefs(object: Any) -> int: ...
def proxy(object: Any, callback: Callable[[Any], Any] = ...) -> None: ...
