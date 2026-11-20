import subprocess
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable
from typing import AnyStr

from .spawnbase import SpawnBase, _Logfile

class PopenSpawn(SpawnBase[AnyStr]):
    proc: subprocess.Popen[AnyStr]
    closed: bool
    def __init__(
        self,
        cmd,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], None] | None = None,
    ) -> None: ...
    flag_eof: bool
    def read_nonblocking(self, size, timeout): ...  # type: ignore[override]
    def write(self, s: str | bytes) -> None: ...
    def writelines(self, sequence: Iterable[str | bytes]) -> None: ...
    def send(self, s: str | bytes) -> int: ...
    def sendline(self, s: str | bytes = "") -> int: ...
    terminated: bool
    def wait(self): ...
    def kill(self, sig) -> None: ...
    def sendeof(self) -> None: ...
