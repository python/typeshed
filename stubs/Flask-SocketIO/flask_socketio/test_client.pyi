from __future__ import annotations

from typing import Any

from flask import Flask
from flask.testing import FlaskClient


class SocketIOTestClient:
    clients: dict[str, SocketIOTestClient]

    def __init__(
        self,
        app: Flask,
        socketio,
        namespace: str | None = None,
        query_string: str | None = None,
        headers: dict[str, Any] = None,
        auth: dict[str, Any] | None = None,
        flask_test_client: FlaskClient | None = None,
    ): ...
    def is_connected(self, namespace: str | None = None) -> bool: ...
    def connect(
        self,
        namespace: str | None = None,
        query_string: str | None = None,
        headers: dict[str, Any] = None,
        auth: dict[str, Any] | None = None,
    ) -> None: ...
