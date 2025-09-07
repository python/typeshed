__all__ = ["spew", "unspew"]

from collections.abc import Container
from types import FrameType
from typing import Any, Self


class Spew:
    trace_names: Container[str] | None = None
    show_values: bool

    def __init__(self, trace_names: Container[str] | None = None, show_values: bool = True) -> None: ...
    def __call__(self, frame: FrameType, event: str, arg: Any) -> Self: ...


def spew(trace_names: Container[str] | None = None, show_values: bool = False) -> None: ...
def unspew() -> None: ...
