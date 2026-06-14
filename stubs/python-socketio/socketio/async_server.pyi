from _typeshed import Incomplete

from . import base_server

task_reference_holder: Incomplete

class AsyncServer(base_server.BaseServer):
    def __init__(
        self,
        client_manager: Incomplete | None = None,
        logger: bool = False,
        json: Incomplete | None = None,
        async_handlers: bool = True,
        namespaces: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def is_asyncio_based(self): ...
    def attach(self, app, socketio_path: str = "socket.io") -> None: ...
    async def emit(
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
    async def send(
        self,
        data,
        to: Incomplete | None = None,
        room: Incomplete | None = None,
        skip_sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        callback: Incomplete | None = None,
        ignore_queue: bool = False,
    ) -> None: ...
    async def call(
        self,
        event,
        data: Incomplete | None = None,
        to: Incomplete | None = None,
        sid: Incomplete | None = None,
        namespace: Incomplete | None = None,
        timeout: int = 60,
        ignore_queue: bool = False,
    ): ...
    async def enter_room(self, sid, room, namespace: Incomplete | None = None) -> None: ...
    async def leave_room(self, sid, room, namespace: Incomplete | None = None) -> None: ...
    async def close_room(self, room, namespace: Incomplete | None = None) -> None: ...
    async def get_session(self, sid, namespace: Incomplete | None = None): ...
    async def save_session(self, sid, session, namespace: Incomplete | None = None) -> None: ...
    server: Incomplete
    sid: Incomplete
    namespace: Incomplete
    def session(self, sid, namespace: Incomplete | None = None): ...
    async def disconnect(self, sid, namespace: Incomplete | None = None, ignore_queue: bool = False) -> None: ...
    async def shutdown(self) -> None: ...
    async def handle_request(self, *args, **kwargs): ...
    def start_background_task(self, target, *args, **kwargs): ...
    async def sleep(self, seconds: int = 0): ...
    def instrument(
        self,
        auth: Incomplete | None = None,
        mode: str = "development",
        read_only: bool = False,
        server_id: Incomplete | None = None,
        namespace: str = "/admin",
        server_stats_interval: int = 2,
    ): ...
