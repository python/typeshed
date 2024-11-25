from _typeshed import Incomplete

default_logger: Incomplete

class BaseServer:
    reserved_events: Incomplete
    packet_class: Incomplete
    eio: Incomplete
    environ: Incomplete
    handlers: Incomplete
    namespace_handlers: Incomplete
    not_handled: Incomplete
    logger: Incomplete
    manager: Incomplete
    manager_initialized: bool
    async_handlers: Incomplete
    always_connect: Incomplete
    namespaces: Incomplete
    async_mode: Incomplete
    def __init__(
        self,
        client_manager: Incomplete | None = None,
        logger: bool = False,
        serializer: str = "default",
        json: Incomplete | None = None,
        async_handlers: bool = True,
        always_connect: bool = False,
        namespaces: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def is_asyncio_based(self): ...
    def on(self, event, handler: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def event(self, *args, **kwargs): ...
    def register_namespace(self, namespace_handler) -> None: ...
    def rooms(self, sid, namespace: Incomplete | None = None): ...
    def transport(self, sid, namespace: Incomplete | None = None): ...
    def get_environ(self, sid, namespace: Incomplete | None = None): ...
