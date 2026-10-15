from _typeshed import Incomplete

from .async_manager import AsyncManager

class AsyncPubSubManager(AsyncManager):
    name: str
    channel: Incomplete
    write_only: Incomplete
    host_id: Incomplete
    logger: Incomplete
    def __init__(self, channel: str = "socketio", write_only: bool = False, logger: Incomplete | None = None) -> None: ...
    thread: Incomplete
    def initialize(self) -> None: ...
    async def emit(
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
    async def can_disconnect(self, sid, namespace): ...
    async def disconnect(self, sid, namespace, **kwargs): ...
    async def enter_room(self, sid, namespace, room, eio_sid: Incomplete | None = None): ...
    async def leave_room(self, sid, namespace, room): ...
    async def close_room(self, room, namespace: Incomplete | None = None) -> None: ...
