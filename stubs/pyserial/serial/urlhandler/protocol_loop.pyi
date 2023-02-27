import logging
import queue
from _typeshed import ReadableBuffer

from serial.serialutil import SerialBase

LOGGER_LEVELS: dict[str, int]

class Serial(SerialBase):
    buffer_size: int
    queue: queue.Queue[bytes | None] | None
    logger: logging.Logger | None
    def open(self) -> None: ...
    def from_url(self, url: str) -> None: ...
    @property
    def in_waiting(self) -> int: ...
    def read(self, size: int = 1) -> bytes: ...
    def cancel_read(self) -> None: ...
    def cancel_write(self) -> None: ...
    def write(self, __b: ReadableBuffer) -> int | None: ...
    def reset_input_buffer(self) -> None: ...
    def reset_output_buffer(self) -> None: ...
    @property
    def out_waiting(self) -> int: ...
    @property
    def cts(self) -> bool: ...
    @property
    def dsr(self) -> bool: ...
    @property
    def ri(self) -> bool: ...
    @property
    def cd(self) -> bool: ...
