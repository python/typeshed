from collections.abc import Callable
from typing import Any, TypeVar

_T = TypeVar("_T")

class Namespace:
    def __init__(self, namespace: str | None = None) -> None: ...
    def trigger_event(self, event: str, *args): ...
    def emit(
        self,
        event: str,
        data: Any = None,
        room: str | None = None,
        include_self: bool = True,
        namespace: str | None = None,
        callback: Callable[..., _T] | None = None,
    ) -> _T | tuple[str, int]: ...
    def send(
        self,
        data: Any,
        room: str | None = None,
        include_self: bool = True,
        namespace: str | None = None,
        callback: Callable[..., Any] | None = None,
    ) -> None: ...
    def close_room(self, room: str, namespace: str | None = None) -> None: ...
