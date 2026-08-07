from _typeshed import Incomplete

from . import base_server

default_logger: Incomplete

class Server(base_server.BaseServer):
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
    ) -> None: ...
    def send(
        self,
        data,
        to: Incomplete | None = None,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        callback: Incomplete | None = None,
        ignore_queue: bool = False,
    ) -> None: ...
    def call(
        self,
        event,
        data: Incomplete | None = None,
        to: Incomplete | None = None,
        sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        timeout: int = 60,
        ignore_queue: bool = False,
    ): ...
    def enter_room(self, sid, room, namespace: Incomplete | None = None) -> None: ...
    def leave_room(self, sid, room, namespace: Incomplete | None = None) -> None: ...
    def close_room(self, room, namespace: Incomplete | None = None) -> None: ...
    def get_session(self, sid, namespace: Incomplete | None = None): ...
    def save_session(self, sid, session, namespace: Incomplete | None = None) -> None: ...
    server: Incomplete
    sid: Incomplete
    namespace: Incomplete
    def session(self, sid, namespace: Incomplete | None = None): ...
    def disconnect(self, sid, namespace: Incomplete | None = None, ignore_queue: bool = False) -> None: ...
    def shutdown(self) -> None: ...
    def handle_request(self, environ, start_response): ...
    def start_background_task(self, target, *args, **kwargs): ...
    def sleep(self, seconds: int = 0): ...
    def instrument(
        self,
        auth: Incomplete | None = None,
        mode: str = "development",
        read_only: bool = False,
        server_id: Incomplete | None = None,
        namespace: str = "/admin",
        server_stats_interval: int = 2,
    ): ...
