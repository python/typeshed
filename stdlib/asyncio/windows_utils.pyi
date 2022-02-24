import subprocess
import sys
from _typeshed import Self
from types import TracebackType
from typing import Callable, Protocol
from typing_extensions import Literal

if sys.platform == "win32":
    if sys.version_info >= (3, 7):
        __all__ = ("pipe", "Popen", "PIPE", "PipeHandle")
    else:
        __all__ = ["socketpair", "pipe", "Popen", "PIPE", "PipeHandle"]
        import socket
        socketpair = socket.socketpair

    class _WarnFunction(Protocol):
        def __call__(
            self, message: str, category: type[Warning] = ..., stacklevel: int = ..., source: PipeHandle = ...
        ) -> None: ...
    BUFSIZE: Literal[8192]
    PIPE = subprocess.PIPE
    STDOUT = subprocess.STDOUT
    def pipe(*, duplex: bool = ..., overlapped: tuple[bool, bool] = ..., bufsize: int = ...) -> tuple[int, int]: ...

    class PipeHandle:
        def __init__(self, handle: int) -> None: ...
        if sys.version_info >= (3, 8):
            def __del__(self, _warn: _WarnFunction = ...) -> None: ...
        else:
            def __del__(self) -> None: ...

        def __enter__(self: Self) -> Self: ...
        def __exit__(self, t: type | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
        @property
        def handle(self) -> int: ...
        def fileno(self) -> int: ...
        def close(self, *, CloseHandle: Callable[[int], None] = ...) -> None: ...
