from asyncio import Future
from dataclasses import dataclass
from types import FrameType
from typing import Any, TextIO, TypeVar, overload

_T = TypeVar("_T")

__all__ = (
    "capture_call_graph",
    "format_call_graph",
    "print_call_graph",
    "FrameCallGraphEntry",
    "FutureCallGraph",
)

@dataclass(frozen=True, slots=True)
class FrameCallGraphEntry:
    frame: FrameType

@dataclass(frozen=True, slots=True)
class FutureCallGraph[_T]:
    future: Future[_T]
    call_stack: tuple[FrameCallGraphEntry, ...]
    awaited_by: tuple[FutureCallGraph[Any], ...]

@overload
def capture_call_graph(
    future: None = None,
    /,
    *,
    depth: int = 1,
    limit: int | None = None,
) -> FutureCallGraph[Any] | None: ...
@overload
def capture_call_graph(
    future: Future[_T],
    /,
    *,
    depth: int = 1,
    limit: int | None = None,
) -> FutureCallGraph[_T] | None: ...
def format_call_graph(
    future: Future[_T] | None = None,
    /,
    *,
    depth: int = 1,
    limit: int | None = None,
) -> str: ...
def print_call_graph(
    future: Future[_T] | None = None,
    /,
    *,
    file: TextIO | None = None,
    depth: int = 1,
    limit: int | None = None,
) -> None: ...
