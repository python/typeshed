from typing import Any, Callable, TypedDict, TypeVar

from socketio import Namespace as _Namespace

from .socketio import SocketIO

_T = TypeVar("T")

class _Acks(TypedDict):
    args: Any
    namespace: Any

class Namespace(_Namespace):
    acks: Acks | None
    socketio: SocketIO | None

    def __init__(self, namespace=None) -> None: ...
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
        self, data: Any, room: str | None = None, include_self: bool = True, namespace=None, callback: Callable | None = None
    ) -> None: ...
    def close_room(self, room: str, namespace=None) -> None: ...
    def disconnect(self, namespace: str | None = None) -> None: ...
    def emit(self, event: str, *args, **kwargs): ...
    def send(self, data: Any, json: bool = False, callback=False, namespace=None) -> None: ...
