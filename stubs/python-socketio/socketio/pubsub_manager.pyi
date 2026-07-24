from _typeshed import Incomplete

from .manager import Manager

class PubSubManager(Manager):
    name: str
    channel: Incomplete
    write_only: Incomplete
    host_id: Incomplete
    logger: Incomplete
    def __init__(self, channel: str = "socketio", write_only: bool = False, logger: Incomplete | None = None) -> None: ...
    thread: Incomplete
    def initialize(self) -> None: ...
    def emit(
        self,
        event,
        data,
        namespace: Incomplete | None = None,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        callback: Incomplete | None = None,
        to: Incomplete | None = None,
        **kwargs,
    ): ...
    def can_disconnect(self, sid, namespace): ...
    def disconnect(self, sid, namespace: Incomplete | None = None, **kwargs): ...
    def enter_room(self, sid, namespace, room, eio_sid: Incomplete | None = None): ...
    def leave_room(self, sid, namespace, room): ...
    def close_room(self, room, namespace: Incomplete | None = None) -> None: ...
