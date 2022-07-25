import sys
from collections.abc import Callable
from typing import Any, NamedTuple
from typing_extensions import TypeAlias

__all__ = ["scheduler"]

_ActionCallback: TypeAlias = Callable[..., Any]

if sys.version_info >= (3, 10):
    class Event(NamedTuple):
        time: float
        priority: Any
        sequence: int
        action: _ActionCallback
        argument: tuple[Any, ...]
        kwargs: dict[str, Any]

else:
    class Event(NamedTuple):
        time: float
        priority: Any
        action: _ActionCallback
        argument: tuple[Any, ...]
        kwargs: dict[str, Any]

class scheduler:
    timefunc: Callable[[], float]
    delayfunc: Callable[[float], Any]

    def __init__(self, timefunc: Callable[[], float] = ..., delayfunc: Callable[[float], Any] = ...) -> None: ...
    def enterabs(
        self, time: float, priority: Any, action: _ActionCallback, argument: tuple[Any, ...] = ..., kwargs: dict[str, Any] = ...
    ) -> Event: ...
    def enter(
        self, delay: float, priority: Any, action: _ActionCallback, argument: tuple[Any, ...] = ..., kwargs: dict[str, Any] = ...
    ) -> Event: ...
    def run(self, blocking: bool = ...) -> float | None: ...
    def cancel(self, event: Event) -> None: ...
    def empty(self) -> bool: ...
    @property
    def queue(self) -> list[Event]: ...
