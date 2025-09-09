import socket
from typing import Any

from gunicorn.http import Request
from gunicorn.workers import base

from .._types import _AddressType

ALREADY_HANDLED: object

class AsyncWorker(base.Worker):
    worker_connections: int
    alive: bool

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def timeout_ctx(self) -> None: ...
    def is_already_handled(self, respiter: Any) -> bool: ...
    def handle(self, listener: socket.socket, client: socket.socket, addr: _AddressType) -> None: ...
    def handle_request(self, listener_name: str, req: Request, sock: socket.socket, addr: _AddressType) -> bool: ...
