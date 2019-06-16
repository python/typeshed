import _weakrefset
from typing import Any, Dict, Set, Tuple, Type

# NOTE: mypy has special processing for ABCMeta and abstractmethod.

def abstractmethod(funcobj: Any) -> Any: ...

class ABCMeta(type):
    # TODO: FrozenSet
    __abstractmethods__: Set[Any]
    _abc_cache: _weakrefset.WeakSet
    _abc_invalidation_counter: int
    _abc_negative_cache: _weakrefset.WeakSet
    _abc_negative_cache_version: int
    _abc_registry: _weakrefset.WeakSet
    def __init__(self, name: str, bases: Tuple[type, ...], namespace: Dict[Any, Any]) -> None: ...
    def __instancecheck__(cls: ABCMeta, instance: Any) -> Any: ...
    def __subclasscheck__(cls: ABCMeta, subclass: Any) -> Any: ...
    def _dump_registry(cls: ABCMeta, *args: Any, **kwargs: Any) -> None: ...
    def register(cls: ABCMeta, subclass: Type[Any]) -> None: ...

# TODO: The real abc.abstractproperty inherits from "property".
class abstractproperty(object):
    def __new__(cls, func: Any) -> Any: ...
    __isabstractmethod__: bool
    doc: Any
    fdel: Any
    fget: Any
    fset: Any
