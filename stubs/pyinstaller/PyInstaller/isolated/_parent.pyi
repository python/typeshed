from collections.abc import Callable
from functools import _AnyCallable
from typing import TypeVar
from typing_extensions import ParamSpec

_AC = TypeVar("_AC", bound=_AnyCallable)
_R = TypeVar("_R")
_P = ParamSpec("_P")

class Python:
    def call(self, function: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

def call(function: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
def decorate(function: _AC) -> _AC: ...
