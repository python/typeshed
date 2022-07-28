import sys
from .process import BaseProcess
from .util import Finalize

if sys.platform != "win32":
    __all__ = ["Popen"]

    class Popen:
        finalizer: Finalize | None
        method: str
        pid: int | None
        returncode: int | None
        sentinel: int | None

        def __init__(self, process_obj: BaseProcess) -> None: ...
        def duplicate_for_child(self, fd: int) -> int: ...
        def poll(self, flag: int = ...) -> int | None: ...
        def wait(self, timeout: float | None = ...) -> int | None: ...
        def terminate(self) -> None: ...
        def kill(self) -> None: ...
        def close(self) -> None: ...
