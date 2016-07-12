from typing import AnyStr

__all__ = ... # type: str

from asyncio import transports

class BaseProtocol:
    def connection_made(self, transport: transports.BaseTransport) -> None: ...
    def connection_lost(self, exc: Exception) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...

class Protocol(BaseProtocol):
    def data_received(self, data: bytes) -> None: ...
    def eof_received(self) -> bool: ...

class DatagramProtocol(BaseProtocol):
    def datagram_received(self, data: AnyStr, addr: str) -> None: ...
    def error_received(self, exc: Exception) -> None: ...

class SubprocessProtocol(BaseProtocol):
    def pipe_data_received(self, fd: int, data: AnyStr) -> None: ...
    def pipe_connection_lost(self, fd: int, exc: Exception) -> None: ...
    def process_exited(self) -> None: ...
