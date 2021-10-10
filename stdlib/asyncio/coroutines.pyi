import types
from collections.abc import Callable, Coroutine
from typing import Any, TypeVar
from typing_extensions import TypeGuard

_F = TypeVar("_F", bound=Callable[..., Any])

def coroutine(func: _F) -> _F: ...
def iscoroutinefunction(func: object) -> bool: ...

def iscoroutine(obj: object) -> TypeGuard[types.GeneratorType | Coroutine[Any, Any, Any]]: ...
