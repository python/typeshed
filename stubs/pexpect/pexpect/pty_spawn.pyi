from _typeshed import Incomplete
from collections.abc import Callable
from io import TextIOWrapper
from os import _Environ

from .spawnbase import SpawnBase

PY3: Incomplete

class spawn(SpawnBase):
    use_native_pty_fork: bool
    STDIN_FILENO: Incomplete
    STDOUT_FILENO: Incomplete
    STDERR_FILENO: Incomplete
    str_last_chars: int
    env: Incomplete
    name: str
    def __init__(
        self,
        command: str,
        args: list[str] = [],
        timeout: int = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: TextIOWrapper | None = None,
        cwd: str | bytes | None = None,
        env: _Environ[Incomplete] | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        preexec_fn: Callable[[Incomplete], Incomplete] | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        dimensions: tuple[int, int] | None = None,
        use_poll: bool = False,
    ) -> None: ...
    child_fd: int
    closed: bool
    def close(self, force: bool = True) -> None: ...
    def isatty(self): ...
    def waitnoecho(self, timeout: int = -1): ...
    def getecho(self): ...
    def setecho(self, state: bool): ...
    def read_nonblocking(self, size: int = 1, timeout: int | None = -1): ...
    def write(self, s: str | bytes) -> None: ...
    def writelines(self, sequence: list[str | bytes]) -> None: ...
    def send(self, s: str | bytes): ...
    def sendline(self, s: str | bytes = ""): ...
    def sendcontrol(self, char: str): ...
    def sendeof(self) -> None: ...
    def sendintr(self) -> None: ...
    @property
    def flag_eof(self) -> bool: ...
    @flag_eof.setter
    def flag_eof(self, value: bool) -> None: ...
    def eof(self) -> bool: ...
    def terminate(self, force: bool = False): ...
    status: int | None
    exitstatus: bool | None
    signalstatus: int | None
    terminated: bool
    def wait(self) -> int: ...
    def isalive(self) -> bool: ...
    def kill(self, sig: int) -> None: ...
    def getwinsize(self) -> tuple[int, int]: ...
    def setwinsize(self, rows, cols) -> None: ...
    def interact(
        self,
        escape_character="\x1d",
        input_filter: Callable[[Incomplete], Incomplete] | None = None,
        output_filter: Callable[[Incomplete], Incomplete] | None = None,
    ) -> None: ...

def spawnu(*args: str, **kwargs: str): ...
