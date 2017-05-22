from typing import Any, MutableMapping, Generic, Iterator, List, TypeVar
from _weakref import (getweakrefcount, getweakrefs, ref, proxy,
                      CallableProxyType, ProxyType, ReferenceType)
from _weakrefset import WeakSet

ProxyTypes = ...  # type: Any

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

# Don't inherit from typing.Dict since
# isinstance(weakref.WeakValueDictionary(), dict) is False
class WeakValueDictionary(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    def itervaluerefs(self) -> Iterator[ReferenceType[_VT]]: ...
    def valuerefs(self) -> List[ReferenceType[_VT]]: ...

    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_KT]: ...

    def has_key(self, key: _KT) -> bool: ...
    def copy(self) -> WeakValueDictionary[_KT, _VT]: ...

class WeakKeyDictionary(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    def iterkeyrefs(self) -> Iterator[ReferenceType[_KT]]: ...
    def keyrefs(self) -> List[ReferenceType[_KT]]: ...

    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_KT]: ...

    def has_key(self, key: _KT) -> bool: ...
    def copy(self) -> WeakKeyDictionary[_KT, _VT]: ...

# TODO: make generic
class KeyedRef(ReferenceType):
    key = ...  # type: Any
    def __new__(type, ob, callback, key): ...
    def __init__(self, ob, callback, key): ...
