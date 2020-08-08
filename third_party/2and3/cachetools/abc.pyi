from abc import ABCMeta
from typing import Generic, MutableMapping, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class DefaultMapping(MutableMapping[_KT, _VT], Generic[_KT, _VT], metaclass=ABCMeta): ...
