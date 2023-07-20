import _typeshed
import sys
from _typeshed import SupportsWrite
from collections.abc import Callable
from typing import Any, TypeVar
from typing_extensions import Concatenate, Literal, ParamSpec

_T = TypeVar("_T")
_R_co = TypeVar("_R_co", covariant=True)
_FuncT = TypeVar("_FuncT", bound=Callable[..., Any])
_P = ParamSpec("_P")

# These definitions have special processing in mypy
class ABCMeta(type):
    __abstractmethods__: frozenset[str]
    if sys.version_info >= (3, 11):
        def __new__(
            __mcls: type[_typeshed.Self], __name: str, __bases: tuple[type, ...], __namespace: dict[str, Any], **kwargs: Any
        ) -> _typeshed.Self: ...
    else:
        def __new__(
            mcls: type[_typeshed.Self], name: str, bases: tuple[type, ...], namespace: dict[str, Any], **kwargs: Any
        ) -> _typeshed.Self: ...

    def __instancecheck__(cls: ABCMeta, instance: Any) -> bool: ...
    def __subclasscheck__(cls: ABCMeta, subclass: type) -> bool: ...
    def _dump_registry(cls: ABCMeta, file: SupportsWrite[str] | None = None) -> None: ...
    def register(cls: ABCMeta, subclass: type[_T]) -> type[_T]: ...

def abstractmethod(funcobj: _FuncT) -> _FuncT: ...

class abstractclassmethod(classmethod[_T, _P, _R_co]):
    __isabstractmethod__: Literal[True]
    def __init__(self, callable: Callable[Concatenate[type[_T], _P], _R_co]) -> None: ...

class abstractstaticmethod(staticmethod[_P, _R_co]):
    __isabstractmethod__: Literal[True]
    def __init__(self, callable: Callable[_P, _R_co]) -> None: ...

class abstractproperty(property):
    __isabstractmethod__: Literal[True]

class ABC(metaclass=ABCMeta): ...

def get_cache_token() -> object: ...

if sys.version_info >= (3, 10):
    def update_abstractmethods(cls: type[_T]) -> type[_T]: ...
