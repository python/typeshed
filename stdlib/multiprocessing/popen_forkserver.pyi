from multiprocessing.process import BaseProcess
from typing import ClassVar, Protocol

from . import popen_fork
from .util import Finalize

__all__ = ["Popen"]

class _SupportsDetach(Protocol):
    def detach(self) -> int: ...

class Popen(popen_fork.Popen):
    DupFd: ClassVar[_SupportsDetach]
    finalizer: Finalize
    sentinel: int

    def __init__(self, process_obj: BaseProcess) -> None: ...
    def duplicate_for_child(self, fd: int) -> int: ...
    def poll(self, flag: int = ...) -> int | None: ...
