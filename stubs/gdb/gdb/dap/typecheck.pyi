from collections.abc import Callable
from typing import Any, TypeVar

_T = TypeVar("_T", bound=Callable[..., Any])

def type_check(func: _T) -> _T: ...
