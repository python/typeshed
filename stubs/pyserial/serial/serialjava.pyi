from _typeshed import ReadableBuffer
from collections.abc import Iterable
from typing import Any

from serial.serialutil import *

def my_import(name: str) -> Any: ...  # Java object
def detect_java_comm(names: Iterable[str]) -> Any: ...  # Java object

comm: Any  # Java object

def device(portnumber: int) -> str: ...

class Serial(SerialBase):
    sPort: Any  # Java object
    def open(self) -> None: ...
    @property
    def in_waiting(self) -> int: ...
    def read(self, size: int = 1) -> bytes: ...
    def write(self, b: ReadableBuffer, /) -> int | None: ...
    def reset_input_buffer(self) -> None: ...
    def reset_output_buffer(self) -> None: ...
    @property
    def cts(self) -> bool: ...
    @property
    def dsr(self) -> bool: ...
    @property
    def ri(self) -> bool: ...
    @property
    def cd(self) -> bool: ...
