import sys
from abc import abstractmethod
from asyncio import transports
from typing import Protocol as TypingProtocol

class BaseProtocol(TypingProtocol):
    @abstractmethod
    def connection_made(self, transport: transports.BaseTransport) -> None: ...
    @abstractmethod
    def connection_lost(self, exc: Exception | None) -> None: ...
    @abstractmethod
    def pause_writing(self) -> None: ...
    @abstractmethod
    def resume_writing(self) -> None: ...

class Protocol(BaseProtocol, TypingProtocol):
    @abstractmethod
    def data_received(self, data: bytes) -> None: ...
    @abstractmethod
    def eof_received(self) -> bool | None: ...

if sys.version_info >= (3, 7):
    class BufferedProtocol(BaseProtocol, TypingProtocol):
        @abstractmethod
        def get_buffer(self, sizehint: int) -> bytearray: ...
        @abstractmethod
        def buffer_updated(self, nbytes: int) -> None: ...
        @abstractmethod
        def eof_received(self) -> bool | None: ...

class DatagramProtocol(BaseProtocol, TypingProtocol):
    @abstractmethod
    def connection_made(self, transport: transports.DatagramTransport) -> None: ...  # type: ignore[override]
    @abstractmethod
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...
    @abstractmethod
    def error_received(self, exc: Exception) -> None: ...

class SubprocessProtocol(BaseProtocol, TypingProtocol):
    @abstractmethod
    def pipe_data_received(self, fd: int, data: bytes) -> None: ...
    @abstractmethod
    def pipe_connection_lost(self, fd: int, exc: Exception | None) -> None: ...
    @abstractmethod
    def process_exited(self) -> None: ...
