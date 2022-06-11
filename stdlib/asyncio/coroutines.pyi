import sys
import types
from collections.abc import Callable, Coroutine
from typing import Any, overload
from typing_extensions import ParamSpec, TypeGuard

if sys.version_info >= (3, 11):
    __all__ = ("iscoroutinefunction", "iscoroutine")
elif sys.version_info >= (3, 7):
    __all__ = ("coroutine", "iscoroutinefunction", "iscoroutine")
else:
    __all__ = ["coroutine", "iscoroutinefunction", "iscoroutine"]

_P = ParamSpec("_P")

if sys.version_info < (3, 11):
    from typing import TypeVar

    _F = TypeVar("_F", bound=Callable[..., Any])
    def coroutine(func: _F) -> _F: ...

@overload
def iscoroutinefunction(func: Callable[_P, Any]) -> TypeGuard[Callable[_P, Coroutine[Any, Any, Any]]]: ...
@overload
def iscoroutinefunction(func: object) -> TypeGuard[Callable[..., Coroutine[Any, Any, Any]]]: ...

if sys.version_info >= (3, 8):
    def iscoroutine(obj: object) -> TypeGuard[Coroutine[Any, Any, Any]]: ...

else:
    def iscoroutine(obj: object) -> TypeGuard[types.GeneratorType[Any, Any, Any] | Coroutine[Any, Any, Any]]: ...
