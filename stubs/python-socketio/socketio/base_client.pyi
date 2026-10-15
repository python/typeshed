from _typeshed import Incomplete

default_logger: Incomplete
reconnecting_clients: Incomplete

def signal_handler(sig, frame): ...

original_signal_handler: Incomplete

class BaseClient:
    reserved_events: Incomplete
    reconnection: Incomplete
    reconnection_attempts: Incomplete
    reconnection_delay: Incomplete
    reconnection_delay_max: Incomplete
    randomization_factor: Incomplete
    handle_sigint: Incomplete
    packet_class: Incomplete
    eio: Incomplete
    logger: Incomplete
    connection_url: Incomplete
    connection_headers: Incomplete
    connection_auth: Incomplete
    connection_transports: Incomplete
    connection_namespaces: Incomplete
    socketio_path: Incomplete
    sid: Incomplete
    connected: bool
    namespaces: Incomplete
    handlers: Incomplete
    namespace_handlers: Incomplete
    callbacks: Incomplete
    def __init__(
        self,
        reconnection: bool = True,
        reconnection_attempts: int = 0,
        reconnection_delay: int = 1,
        reconnection_delay_max: int = 5,
        randomization_factor: float = 0.5,
        logger: bool = False,
        serializer: str = "default",
        json: Incomplete | None = None,
        handle_sigint: bool = True,
        **kwargs,
    ) -> None: ...
    def is_asyncio_based(self): ...
    def on(self, event, handler: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def event(self, *args, **kwargs): ...
    def register_namespace(self, namespace_handler) -> None: ...
    def get_sid(self, namespace: Incomplete | None = None): ...
    def transport(self): ...
