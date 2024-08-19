import sys
from collections.abc import Awaitable, Callable, Coroutine
from typing import Any, TypeVar, overload
from typing_extensions import ParamSpec, TypeGuard, TypeIs, deprecated

if sys.version_info >= (3, 11):
    __all__ = ("iscoroutinefunction", "iscoroutine")
else:
    __all__ = ("coroutine", "iscoroutinefunction", "iscoroutine")

_T = TypeVar("_T")
_FunctionT = TypeVar("_FunctionT", bound=Callable[..., Any])
_P = ParamSpec("_P")

if sys.version_info < (3, 11):
    def coroutine(func: _FunctionT) -> _FunctionT: ...

if sys.version_info < (3, 16):
    @overload
    @deprecated("Use inspect.iscoroutinefunction instead")
    def iscoroutinefunction(func: Callable[..., Coroutine[Any, Any, Any]]) -> bool: ...
    @overload
    @deprecated("Use inspect.iscoroutinefunction instead")
    def iscoroutinefunction(func: Callable[_P, Awaitable[_T]]) -> TypeGuard[Callable[_P, Coroutine[Any, Any, _T]]]: ...
    @overload
    @deprecated("Use inspect.iscoroutinefunction instead")
    def iscoroutinefunction(func: Callable[_P, object]) -> TypeGuard[Callable[_P, Coroutine[Any, Any, Any]]]: ...
    @overload
    @deprecated("Use inspect.iscoroutinefunction instead")
    def iscoroutinefunction(func: object) -> TypeGuard[Callable[..., Coroutine[Any, Any, Any]]]: ...

def iscoroutine(obj: object) -> TypeIs[Coroutine[Any, Any, Any]]: ...
