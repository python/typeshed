from _typeshed import Incomplete

from . import base_client

class Client(base_client.BaseClient):
    connection_url: Incomplete
    connection_headers: Incomplete
    connection_auth: Incomplete
    connection_transports: Incomplete
    connection_namespaces: Incomplete
    socketio_path: Incomplete
    namespaces: Incomplete
    connected: bool
    def connect(
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
    def wait(self) -> None: ...
    def emit(
        self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, callback: Incomplete | None = None
    ) -> None: ...
    def send(self, data, namespace: Incomplete | None = None, callback: Incomplete | None = None) -> None: ...
    def call(self, event, data: Incomplete | None = None, namespace: Incomplete | None = None, timeout: int = 60): ...
    def disconnect(self) -> None: ...
    def shutdown(self) -> None: ...
    def start_background_task(self, target, *args, **kwargs): ...
    def sleep(self, seconds: int = 0): ...
