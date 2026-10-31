from _typeshed import Incomplete

class SimpleClient:
    client_args: Incomplete
    client_kwargs: Incomplete
    client: Incomplete
    namespace: str
    connected_event: Incomplete
    connected: bool
    input_event: Incomplete
    input_buffer: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def connect(
        self,
        url,
        headers={},
        auth: Incomplete | None = None,
        transports: Incomplete | None = None,
        namespace: str = "/",
        socketio_path: str = "socket.io",
        wait_timeout: int = 5,
    ) -> None: ...
    @property
    def sid(self): ...
    @property
    def transport(self): ...
    def emit(self, event, data: Incomplete | None = None): ...
    def call(self, event, data: Incomplete | None = None, timeout: int = 60): ...
    def receive(self, timeout: Incomplete | None = None): ...
    def disconnect(self) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...
