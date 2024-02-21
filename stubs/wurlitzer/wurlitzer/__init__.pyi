import contextlib
import io
from collections.abc import Iterator
from contextlib import contextmanager
from types import TracebackType
from typing import Final, Literal, TextIO
from typing_extensions import TypeAlias

from IPython.core.interactiveshell import InteractiveShell

STDOUT: Final = 2
PIPE: Final = 3
_STDOUT: TypeAlias = Literal[2]
_PIPE: TypeAlias = Literal[3]

class Wurlitzer:
    flush_interval: float = 0.2

    def __init__(
        self,
        stdout: TextIO | io.IOBase | None = None,
        stderr: _STDOUT | TextIO | io.IOBase | None = None,
        encoding: str = ...,
        bufsize: int | None = ...,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

def dup2(a: int, b: int, timeout: int = 3) -> int: ...
def sys_pipes(
    encoding: str = ..., bufsize: int | None = None
) -> contextlib._GeneratorContextManager[tuple[TextIO | io.BytesIO | io.StringIO, TextIO | io.BytesIO | io.StringIO | None]]: ...
@contextmanager
def pipes(
    stdout: _PIPE | TextIO = 3, stderr: _STDOUT | _PIPE | TextIO = 3, encoding: str = ..., bufsize: int | None = None
) -> Iterator[tuple[TextIO | io.BytesIO | io.StringIO, TextIO | io.BytesIO | io.StringIO | None]]: ...
def sys_pipes_forever(encoding: str = ..., bufsize: int | None = None): ...
def stop_sys_pipes() -> None: ...
def load_ipython_extension(ip: InteractiveShell) -> None: ...
def unload_ipython_extension(ip: InteractiveShell) -> None: ...

__all__ = ["STDOUT", "PIPE", "Wurlitzer", "pipes", "sys_pipes", "sys_pipes_forever", "stop_sys_pipes"]
