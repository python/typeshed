from _typeshed import Incomplete
from typing import Any, Callable, TypedDict, TypeVar
from typing_extensions import TypeAlias

from socketio import Namespace as _Namespace

from .socketio import SocketIO

_T = TypeVar('T')
_Json: TypeAlias = dict[str, _Json] | list[_Json] | int | str | float | bool | None

class _Acks(TypedDict):
    args: Any
    namespace: Any

class Namespace(_Namespace):
    acks: Acks | None
    socketio: SocketIO | None

    def __init__(self, namespace=None) -> None: ...
    def trigger_event(self, event: Incomplete, *args): ...
    def emit(
        self,
        event: Incomplete,
        data: Incomplete | None = None,
        room: str | None = None,
        include_self: bool = True,
        namespace: str | None = None,
        callback: Callable[..., _T] | None = None,
    ) -> _T | tuple[str, int]: ...
    def send(
        self,
        data: str | list[_Json] | dict[str, _Json],
        room: str | None = None,
        include_self: bool = True,
        namespace=None,
        callback: Callable | None = None,
    ) -> None: ...
    def close_room(self, room: str, namespace=None) -> None: ...
    def disconnect(self, namespace: str | None = None) -> None: ...
    def emit(self, event: str, *args, **kwargs): ...
    def send(
        self,
        data: _Json,
        json: bool = False,
        callback=False, namespace=None) -> None:
