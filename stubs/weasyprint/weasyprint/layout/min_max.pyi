from collections.abc import Callable
from typing import ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")

def handle_min_max_width(function: Callable[P, T]) -> Callable[P, T]: ...
def handle_min_max_height(function: Callable[P, T]) -> Callable[P, T]: ...
