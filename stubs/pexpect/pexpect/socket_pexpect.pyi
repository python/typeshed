from socket import socket as Socket
from collections.abc import Iterable

from .spawnbase import SpawnBase, _Logfile

__all__ = ["SocketSpawn"]

class SocketSpawn(SpawnBase):
    args: None
    command: None
    socket: Socket
    child_fd: int
    closed: bool
    name: str
    use_poll: bool
    def __init__(
        self,
        socket: Socket,
        args: None = None,
        timeout: float = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def send(self, s: str | bytes) -> int: ...
    def sendline(self, s: str | bytes) -> int: ...
    def write(self, s: str | bytes) -> None: ...
    def writelines(self, sequence: Iterable[str | bytes]) -> None: ...
    def read_nonblocking(self, size: int = 1, timeout: float | None = -1) -> bytes: ...
