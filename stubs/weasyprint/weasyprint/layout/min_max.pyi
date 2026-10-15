from collections.abc import Callable
from typing import ParamSpec, TypeVar

_T = TypeVar("_T")
_P = ParamSpec("_P")

def handle_min_max_width(function: Callable[_P, _T]) -> Callable[_P, _T]: ...
def handle_min_max_height(function: Callable[_P, _T]) -> Callable[_P, _T]: ...
