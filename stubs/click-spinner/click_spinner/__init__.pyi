import threading
from _typeshed import SupportsFlush
from collections.abc import Iterator
from types import TracebackType
from typing import Literal, Protocol, type_check_only
from typing_extensions import Self

__version__: str

@type_check_only
class _Stream(SupportsFlush, Protocol):
    def isatty(self) -> bool: ...
    def write(self, s: str, /) -> int: ...

class Spinner:
    spinner_cycle: Iterator[str]
    disable: bool
    beep: bool
    force: bool
    stream: _Stream
    stop_running: threading.Event | None
    spin_thread: threading.Thread | None
    def __init__(self, beep: bool = False, disable: bool = False, force: bool = False, stream: _Stream = ...) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def init_spin(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> Literal[False]: ...

def spinner(beep: bool = False, disable: bool = False, force: bool = False, stream: _Stream = ...) -> Spinner: ...
