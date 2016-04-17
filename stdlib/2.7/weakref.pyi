# Stubs for weakref (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import UserDict
from _weakref import getweakrefcount as getweakrefcount, getweakrefs as getweakrefs, ref as ref, proxy as proxy, CallableProxyType as CallableProxyType, ProxyType as ProxyType, ReferenceType as ReferenceType
from _weakrefset import WeakSet as WeakSet
from exceptions import ReferenceError as ReferenceError

ProxyTypes = ... # type: Any

class WeakValueDictionary(UserDict.UserDict):
    def __init__(self, *args, **kw): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key): ...
    def __contains__(self, key): ...
    def has_key(self, key): ...
    def __setitem__(self, key, value): ...
    def clear(self): ...
    def copy(self): ...
    __copy__ = ... # type: Any
    def __deepcopy__(self, memo): ...
    def get(self, key, default=None): ...
    def items(self): ...
    def iteritems(self): ...
    def iterkeys(self): ...
    __iter__ = ... # type: Any
    def itervaluerefs(self): ...
    def itervalues(self): ...
    def popitem(self): ...
    def pop(self, key, *args): ...
    def setdefault(self, key, default=None): ...
    def update(self, dict=None, **kwargs): ...
    def valuerefs(self): ...
    def values(self): ...

class KeyedRef(ReferenceType):
    key = ... # type: Any
    def __new__(type, ob, callback, key): ...
    def __init__(self, ob, callback, key): ...

class WeakKeyDictionary(UserDict.UserDict):
    data = ... # type: Any
    def __init__(self, dict=None): ...
    def __delitem__(self, key): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def copy(self): ...
    __copy__ = ... # type: Any
    def __deepcopy__(self, memo): ...
    def get(self, key, default=None): ...
    def has_key(self, key): ...
    def __contains__(self, key): ...
    def items(self): ...
    def iteritems(self): ...
    def iterkeyrefs(self): ...
    def iterkeys(self): ...
    __iter__ = ... # type: Any
    def itervalues(self): ...
    def keyrefs(self): ...
    def keys(self): ...
    def popitem(self): ...
    def pop(self, key, *args): ...
    def setdefault(self, key, default=None): ...
    def update(self, dict=None, **kwargs): ...
