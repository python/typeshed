from collections.abc import Callable
from typing import Any, TypedDict

from flask import Flask
from flask.testing import FlaskClient

class _Packet(TypedDict, total=False):
    name: str
    args: Any
    namespace: str

class SocketIOTestClient:
    def __init__(
        self,
        app: Flask,
        socketio,
        namespace: str | None = None,
        query_string: str | None = None,
        headers: dict[str, Any] | None = None,
        auth: dict[str, Any] | None = None,
        flask_test_client: FlaskClient | None = None,
    ): ...
    def is_connected(self, namespace: str | None = None) -> bool: ...
    def connect(
        self,
        namespace: str | None = None,
        query_string: str | None = None,
        headers: dict[str, Any] | None = None,
        auth: dict[str, Any] | None = None,
    ) -> None: ...
    def disconnect(self, namespace: str | None = None) -> None: ...
    def emit(self, event: str, *args, callback: bool = True, namespace: str | None = None): ...
    def get_recieved(self, namespace: str | None = None) -> list[_Packet]: ...
    def send(
        self,
        data: Any,
        json: bool = False,
        namespace: str | None = None,
        include_self: bool = True,
        skip_sid: list[str] | str | None = None,
        callback: Callable[..., Any] | None = None,
        **kwargs,
    ): ...
