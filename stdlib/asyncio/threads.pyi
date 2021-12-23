import sys
from typing import Any, Callable, TypeVar
from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")

if sys.version_info >= (3, 9):
    async def to_thread(func: Callable[_P, _R], /, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
