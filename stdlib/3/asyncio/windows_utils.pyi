
from typing import Tuple, Callable, Optional, Type, Protocol
from types import TracebackType


class _WarnFunction(Protocol):
    def __call__(self, message: str, category: Type[Warning], source: PipeHandle): ...


BUFSIZE: int
PIPE: int
STDOUT: int

def pipe(*, duplex: bool = ..., overlapped: Tuple[bool, bool] = ..., bufsize: int = ...) -> Tuple[int, int]: ...

class PipeHandle:

    def __init__(self, handle: int) -> None: ...
    def __repr__(self) -> str: ...
    def __del__(self, _warn: _WarnFunction = ...) -> None: ...
    def __enter__(self) -> PipeHandle: ...
    def __exit__(self, t: Optional[type], v: Optional[BaseException], tb: Optional[TracebackType]) -> None: ...
    @property
    def handle(self) -> int: ...
    def fileno(self) -> int: ...
    def close(self, *, CloseHandle: Callable[[int], None] = ...) -> None: ...
