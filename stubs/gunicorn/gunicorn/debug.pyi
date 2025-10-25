__all__ = ["spew", "unspew"]

from collections.abc import Container
from types import FrameType
from typing import Any, Literal
from typing_extensions import Self

class Spew:
    trace_names: Container[str] | None = None
    show_values: bool

    def __init__(self, trace_names: Container[str] | None = None, show_values: bool = True) -> None: ...
    def __call__(
        self,
        frame: FrameType,
        event: Literal["call"] | Literal["line"] | Literal["return"] | Literal["exception"] | Literal["opcode"],
        arg: Any,  # `arg` is not used inside the function, stub is set Any
    ) -> Self: ...

def spew(trace_names: Container[str] | None = None, show_values: bool = False) -> None: ...
def unspew() -> None: ...
