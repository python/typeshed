import threading
from _typeshed import Self, Unused
from collections.abc import Iterator
from typing import Protocol
from typing_extensions import Literal

__version__: str

class _Stream(Protocol):
    def isatty(self) -> bool: ...
    def flush(self) -> None: ...
    def write(self, s: str) -> int: ...

class Spinner:
    spinner_cycle: Iterator[str]
    disable: bool
    beep: bool
    force: bool
    stream: _Stream
    stop_running: threading.Event | None
    spin_thread: threading.Thread | None
    def __init__(self, beep: bool = ..., disable: bool = ..., force: bool = ..., stream: _Stream = ...) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def init_spin(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, exc_type: Unused, exc_val: Unused, exc_tb: Unused) -> Literal[False]: ...

def spinner(beep: bool = ..., disable: bool = ..., force: bool = ..., stream: _Stream = ...) -> Spinner: ...
