from _typeshed import Incomplete

from . import base_client

default_logger: Incomplete

class AsyncClient(base_client.BaseClient):
    def is_asyncio_based(self): ...
    connection_url: Incomplete
    connection_headers: Incomplete
    connection_auth: Incomplete
    connection_transports: Incomplete
    connection_namespaces: Incomplete
    socketio_path: Incomplete
    namespaces: Incomplete
    connected: bool
    async def connect(
        self,
        url,
        headers={},
        auth: Incomplete | None = None,
        transports: Incomplete | None = None,
        namespaces: Incomplete | None = None,
        socketio_path: str = "socket.io",
        wait: bool = True,
        wait_timeout: int = 1,
        retry: bool = False,
    ) -> None: ...
    async def wait(self) -> None: ...
    async def emit(
        self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, callback: Incomplete | None = None
    ) -> None: ...
    async def send(self, data, namespace: Incomplete | None = None, callback: Incomplete | None = None) -> None: ...
    async def call(self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, timeout: int = 60): ...
    async def disconnect(self) -> None: ...
    async def shutdown(self) -> None: ...
    def start_background_task(self, target, *args, **kwargs): ...
    async def sleep(self, seconds: int = 0): ...
