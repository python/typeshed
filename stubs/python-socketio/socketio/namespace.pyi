from _typeshed import Incomplete

from . import base_namespace

class Namespace(base_namespace.BaseServerNamespace):
    def trigger_event(self, event, *args): ...
    def emit(
        self,
        event,
        data: Incomplete | None = None,
        to: Incomplete | None = None,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        callback: Incomplete | None = None,
        ignore_queue: bool = False,
    ): ...
    def send(
        self,
        data,
        to: Incomplete | None = None,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        callback: Incomplete | None = None,
        ignore_queue: bool = False,
    ): ...
    def call(
        self,
        event,
        data: Incomplete | None = None,
        to: Incomplete | None = None,
        sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        timeout: Incomplete | None = None,
        ignore_queue: bool = False,
    ): ...
    def enter_room(self, sid, room, namespace: Incomplete | None = None): ...
    def leave_room(self, sid, room, namespace: Incomplete | None = None): ...
    def close_room(self, room, namespace: Incomplete | None = None): ...
    def get_session(self, sid, namespace: Incomplete | None = None): ...
    def save_session(self, sid, session, namespace: Incomplete | None = None): ...
    def session(self, sid, namespace: Incomplete | None = None): ...
    def disconnect(self, sid, namespace: Incomplete | None = None): ...

class ClientNamespace(base_namespace.BaseClientNamespace):
    def trigger_event(self, event, *args): ...
    def emit(
        self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, callback: Incomplete | None = None
    ): ...
    def send(
        self, data, room: Incomplete | None = None, namespace: Incomplete | None = None, callback: Incomplete | None = None
    ): ...
    def call(
        self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, timeout: Incomplete | None = None
    ): ...
    def disconnect(self): ...
