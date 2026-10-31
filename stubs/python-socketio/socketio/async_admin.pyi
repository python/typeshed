from _typeshed import Incomplete

HOSTNAME: Incomplete
PID: Incomplete

class InstrumentedAsyncServer:
    sio: Incomplete
    auth: Incomplete
    admin_namespace: Incomplete
    read_only: Incomplete
    server_id: Incomplete
    mode: Incomplete
    server_stats_interval: Incomplete
    admin_queue: Incomplete
    event_buffer: Incomplete
    stop_stats_event: Incomplete
    stats_task: Incomplete
    def __init__(
        self,
        sio,
        auth: Incomplete | None = None,
        namespace: str = "/admin",
        read_only: bool = False,
        server_id: Incomplete | None = None,
        mode: str = "development",
        server_stats_interval: int = 2,
    ) -> None: ...
    def instrument(self) -> None: ...
    def uninstrument(self) -> None: ...
    async def admin_connect(self, sid, environ, client_auth) -> None: ...
    async def admin_emit(self, _, namespace, room_filter, event, *data) -> None: ...
    async def admin_enter_room(self, _, namespace, room, room_filter: Incomplete | None = None) -> None: ...
    async def admin_leave_room(self, _, namespace, room, room_filter: Incomplete | None = None) -> None: ...
    async def admin_disconnect(self, _, namespace, close, room_filter: Incomplete | None = None) -> None: ...
    async def shutdown(self) -> None: ...
    def serialize_socket(self, sid, namespace, eio_sid: Incomplete | None = None): ...
