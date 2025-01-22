import threading
from _typeshed import ReadableBuffer
from collections.abc import Callable
from types import TracebackType
from typing import Generic, TypeVar
from typing_extensions import Self

from serial import Serial

class Protocol:
    def connection_made(self, transport: ReaderThread[Self]) -> None: ...
    def data_received(self, data: bytes) -> None: ...
    def connection_lost(self, exc: BaseException | None) -> None: ...

class Packetizer(Protocol):
    TERMINATOR: bytes
    buffer: bytearray
    transport: ReaderThread[Self] | None
    def handle_packet(self, packet: bytes) -> None: ...

class FramedPacket(Protocol):
    START: bytes
    STOP: bytes
    packet: bytearray
    in_packet: bool
    transport: ReaderThread[Self] | None
    def handle_packet(self, packet: bytes) -> None: ...
    def handle_out_of_packet_data(self, data: bytes) -> None: ...

class LineReader(Packetizer):
    ENCODING: str
    UNICODE_HANDLING: str
    def handle_line(self, line: str) -> None: ...
    def write_line(self, text: str) -> None: ...

_T = TypeVar("_T", bound=Protocol)

class ReaderThread(threading.Thread, Generic[_T]):
    serial: Serial
    protocol_factory: Callable[[], _T]
    alive: bool
    protocol: _T
    def __init__(self, serial_instance: Serial, protocol_factory: Callable[[], _T]) -> None: ...
    def stop(self) -> None: ...
    def write(self, data: ReadableBuffer) -> int: ...
    def close(self) -> None: ...
    def connect(self) -> tuple[Self, _T]: ...
    def __enter__(self) -> _T: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None, /
    ) -> None: ...
