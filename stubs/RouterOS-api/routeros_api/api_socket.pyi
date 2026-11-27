import socket
import ssl
from _typeshed import ReadableBuffer
from typing import TypeAlias

# SocketWrapper's attribute socket hides the module in its class body.
_Socket: TypeAlias = socket.socket

EINTR: int  # undocumented

def get_socket(  # undocumented
    hostname: str,
    port: int,
    use_ssl: bool = False,
    ssl_verify: bool = True,
    ssl_verify_hostname: bool = True,
    ssl_context: ssl.SSLContext | None = None,
    timeout: float | None = 15.0,
) -> SocketWrapper: ...
def set_keepalive(  # undocumented
    sock: socket.socket, after_idle_sec: int = 1, interval_sec: int = 3, max_fails: int = 5
) -> None: ...

# A pool's socket while it isn't connected.
class DummySocket:  # undocumented
    def close(self) -> None: ...
    def settimeout(self, timeout: float | None) -> None: ...

class SocketWrapper:  # undocumented
    socket: _Socket
    def __init__(self, socket: _Socket) -> None: ...
    def send(self, bytes: ReadableBuffer) -> None: ...
    def receive(self, length: int) -> bytes: ...
    def close(self) -> None: ...
    def settimeout(self, timeout: float | None) -> None: ...
