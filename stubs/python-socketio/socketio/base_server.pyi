from _typeshed import Incomplete
from typing import Callable, Final, ParamSpec, TypeVar, overload
from wsgiref.types import WSGIEnvironment

default_logger: Incomplete

HandlerParams = ParamSpec("HandlerParams")
HandlerReturn = TypeVar("HandlerReturn")
EventHandler = Callable[HandlerParams, HandlerReturn]

class BaseServer:
    handlers: dict[str, dict[str, Callable[..., Incomplete]]]
    namespace_handlers: dict[str, Incomplete]  # Incomplete is used here since base_namespace.BaseServerNamespace isn't imported
    reserved_events: Final[list[str]] = ["connect", "disconnect"]
    environ: WSGIEnvironment
    _binary_packet: dict[str, Incomplete]
    packet_class: Incomplete
    eio: Incomplete
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
    @overload
    def on(self, event: str, handler: None = None, namespace: str | None = None) -> Callable[[EventHandler], EventHandler]: ...
    @overload
    def on(
        self,
        event: str,
        handler: EventHandler,
        namespace: str | None = None,
    ) -> None: ...
    def on(
        self,
        event: str,
        handler: EventHandler | None = None,
        namespace: str | None = None,
    ) -> Callable[[EventHandler], EventHandler] | None: ...
    def event(self, *args, **kwargs): ...
    def register_namespace(self, namespace_handler) -> None: ...
    def rooms(self, sid, namespace: Incomplete | None = None): ...
    def transport(self, sid, namespace: Incomplete | None = None): ...
    def get_environ(self, sid, namespace: Incomplete | None = None): ...
