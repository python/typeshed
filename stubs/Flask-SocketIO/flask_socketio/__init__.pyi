from collections.abc import Callable
from threading import Thread
from typing import Any
from typing_extensions import ParamSpec, TypeAlias

from flask import Flask
from flask.testing import FlaskClient

from .namespace import Namespace
from .test_client import SocketIOTestClient


_P = ParamSpec("_P")
_ExceptionHandler: TypeAlias = Callable[[Exception], Any]
_Handler: TypeAlias = Callable[[Any], Any]

_HandlerDecorator: TypeAlias = Callable[[_Handler], _Handler]

class SocketIO:
    def __init__(
        self,
        app: Flask | None = None,
        *,
        # SocketIO options
        manage_session: bool = True,
        message_queue: str | None = None,
        channel: str = "flask-socketio",
        path: str = "socket.io",
        resource: str = "socket.io",
        **kwargs,  # TODO: Socket.IO server options, Engine.IO server config
    ) -> None: ...
    def init_app(
        self,
        app: Flask,
        *,
        # SocketIO options
        manage_session: bool = True,
        message_queue: str | None = None,
        channel: str = "flask-socketio",
        path: str = "socket.io",
        resource: str = "socket.io",
        **kwargs,  # TODO: Socket.IO server options, Engine.IO server config: ...
    ) -> None: ...
    def on(self, message: str, namespace: str | None = None) -> _HandlerDecorator: ...
    def on_error(self, namespace: str | None = None) -> Callable[[_ExceptionHandler], _ExceptionHandler]: ...
    def on_error_default(self, exception_handler: _ExceptionHandler) -> Callable[[_ExceptionHandler], _ExceptionHandler]: ...
    def on_event(self, message: str, handler: _Handler, namespace: str | None = None) -> None: ...
    def event(self, namespace: str | None = None, *args, **kwargs) -> _Handler | Callable[[_Handler], _HandlerDecorator]: ...
    def on_namespace(self, namespace_handler: Namespace) -> None: ...
    def emit(
        self,
        event: str,
        *args,
        namespace: str = "/",  # / is the default (global) namespace
        to: str | None = None,
        include_self: bool = True,
        skip_sid: str | list[str] | None = None,
        callback: Callable[..., Any] | None = None,
    ) -> None: ...
    def call(
        self,
        event: str,
        *args,
        namespace: str = "/",  # / is the default (global) namespace
        to: str | None = None,
        timeout: int = 60,  # seconds
        ignore_queue: bool = False,
    ): ...
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
    def run(
        self,
        app,
        host: str | None = None,
        port: int | None = None,
        *,
        debug: bool = True,
        use_reloader: bool,
        reloader_options: dict[str, Any] = {},
        log_output: bool,
        allow_unsafe_werkzeug: bool = False,
        **kwargs,
    ) -> None: ...
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

def emit(
    event,
    *args,
    namespace: str = "/",  # / is the default (global) namespace
    to: str | None = None,
    include_self: bool = True,
    skip_sid: str | list[str] | None = None,
    callback: Callable[..., Any] | None = None,
    broadcast: bool = False,
) -> None: ...
def send(message: str, **kwargs) -> None: ...
def join_room(room, sid: str | None = None, namespace: str | None = None) -> None: ...
def leave_room(room, sid: str | None = None, namespace: str | None = None) -> None: ...
def close_room(room, namespace: str | None = None) -> None: ...
def rooms(sid: str | None = None, namespace: str | None = None) -> list[str]: ...
def disconnect(sid: str | None = None, namespace: str | None = None, silent: bool = False) -> None: ...
