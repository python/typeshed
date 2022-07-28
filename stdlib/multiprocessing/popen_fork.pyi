from .util import Finalize
from .process import BaseProcess

__all__ = ["Popen"]

class Popen(object):
    method: str
    pid: int | None
    returncode: int | None
    finalizer: Finalize | None
    sentinel: int | None

    def __init__(self, process_obj: BaseProcess): ...
    def duplicate_for_child(self, fd: int) -> int: ...
    def poll(self, flag: int = ...) -> int | None: ...
    def wait(self, timeout: float | None = ...) -> int | None: ...
    def _send_signal(self, sig: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def _launch(self, process_obj: BaseProcess) -> None: ...
    def close(self) -> None: ...
