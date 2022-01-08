import sys
import types
from collections.abc import Coroutine
from typing import Any
from typing_extensions import TypeGuard

if sys.version_info < (3, 11):
    from collections.abc import Callable
    from typing import TypeVar

    _F = TypeVar("_F", bound=Callable[..., Any])
    def coroutine(func: _F) -> _F: ...

def iscoroutinefunction(func: object) -> bool: ...
def iscoroutine(obj: object) -> TypeGuard[types.GeneratorType | Coroutine[Any, Any, Any]]: ...
