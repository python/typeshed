from _typeshed import Incomplete

from . import base_manager

default_logger: Incomplete

class Manager(base_manager.BaseManager):
    def can_disconnect(self, sid, namespace): ...
    def emit(
        self,
        event,
        data,
        namespace,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        callback: Incomplete | None = None,
        to: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def disconnect(self, sid, namespace, **kwargs): ...
    def enter_room(self, sid, namespace, room, eio_sid: Incomplete | None = None): ...
    def leave_room(self, sid, namespace, room): ...
    def close_room(self, room, namespace): ...
    def trigger_callback(self, sid, id, data) -> None: ...
