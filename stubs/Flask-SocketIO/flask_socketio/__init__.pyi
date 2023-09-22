from collections.abc import Callable
from logging import Logger
from threading import Thread
from typing import Any
from typing_extensions import NotRequired, ParamSpec, TypeAlias, TypedDict, Unpack

from flask import Flask
from flask.testing import FlaskClient
from socketio.base_manager import BaseManager  # type: ignore[import]  # pyright: ignore[reportMissingImports]

from .namespace import Namespace
from .test_client import SocketIOTestClient

_P = ParamSpec("_P")
_ExceptionHandler: TypeAlias = Callable[[Exception], Any]
_Handler: TypeAlias = Callable[[Any], Any]

_HandlerDecorator: TypeAlias = Callable[[_Handler], _Handler]

gevent_socketio_found: bool

class _SocketIOConfig(TypedDict, total=False):
    manage_session: NotRequired[bool]
    message_queue: NotRequired[str]
    channel: NotRequired[str]
    path: NotRequired[str]
    resource: NotRequired[str]

    # SocketIO.Server options
    client_manager: NotRequired[BaseManager]
    logger: NotRequired[bool | Logger]
    json: NotRequired[Any]
    async_handlers: NotRequired[bool]
    always_connect: NotRequired[bool]

class _SocketIOCallArgs(TypedDict, total=False):
    namespace: NotRequired[str]
    to: NotRequired[str]
    room: NotRequired[str]

class _SocketIOEmitArgs(_SocketIOCallArgs, total=False):
    include_self: NotRequired[bool]
    skip_sid: NotRequired[str | list[str]]
    callback: NotRequired[Callable[..., Any]]

class _SocketIORunArgs(TypedDict, total=False):
    debug: NotRequired[bool]
    use_reloader: NotRequired[bool]
    reloader_options: dict[str, Any]
    log_output: NotRequired[bool]
    allow_unsafe_werkzeug: NotRequired[bool]

class SocketIO:
    def __init__(self, app: Flask | None = None, **kwargs: Unpack[_SocketIOConfig]) -> None: ...  # type: ignore
    def init_app(self, app: Flask, **kwargs: Unpack[_SocketIOConfig]): ...  # type: ignore
    def on(self, message: str, namespace: str | None = None) -> _HandlerDecorator: ...
    def on_error(self, namespace: str | None = None) -> Callable[[_ExceptionHandler], _ExceptionHandler]: ...
    def on_error_default(self, exception_handler: _ExceptionHandler) -> Callable[[_ExceptionHandler], _ExceptionHandler]: ...
    def on_event(self, message: str, handler: _Handler, namespace: str | None = None) -> None: ...
    def event(self, namespace: str | None = None, *args, **kwargs) -> _Handler | Callable[[_Handler], _HandlerDecorator]: ...
    def on_namespace(self, namespace_handler: Namespace) -> None: ...
    def emit(self, event: str, *args, **kwargs: Unpack[_SocketIOEmitArgs]) -> None: ...  # type: ignore
    def call(self, event: str, *args, **kwargs: Unpack[_SocketIOCallArgs]): ...  # type: ignore
    def send(
        self,
        data: Any,
        json: bool = False,
        namespace: str | None = None,
        to: str | None = None,
        callback: Callable[..., Any] | None = None,
        include_self: bool = True,
        skip_sid: list[str] | str | None = None,
        **kwargs,
    ) -> None: ...
    def close_room(self, room: str, namespace: str | None = None) -> None: ...
    def run(self, app, host: str | None = None, port: int | None = None, **kwargs: _SocketIORunArgs) -> None: ...
    def stop(self) -> None: ...
    def start_background_task(self, target: Callable[_P, None], *args: _P.args, **kwargs: _P.kwargs) -> Thread: ...
    def sleep(self, seconds: int = 0): ...
    def test_client(
        self,
        app: Flask,
        namespace: str | None = None,
        query_string: str | None = None,
        headers: dict[str, Any] | None = None,
        auth: dict[str, Any] | None = None,
        flask_test_client: FlaskClient | None = None,
    ) -> SocketIOTestClient: ...

def emit(event, *args, **kwargs: Unpack[_SocketIOEmitArgs]) -> None: ...  # type: ignore
def call(event, *args, **kwargs: Unpack[_SocketIOCallArgs]): ...  # type: ignore
def send(message: str, **kwargs) -> None: ...
def join_room(room, sid: str | None = None, namespace: str | None = None) -> None: ...
def leave_room(room, sid: str | None = None, namespace: str | None = None) -> None: ...
def close_room(room, namespace: str | None = None) -> None: ...
def rooms(sid: str | None = None, namespace: str | None = None) -> list[str]: ...
def disconnect(sid: str | None = None, namespace: str | None = None, silent: bool = False) -> None: ...
