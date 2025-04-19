import sys
from types import TracebackType
from typing import ClassVar
from typing_extensions import Self

from setuptools._distutils.errors import DistutilsError

__all__ = ["AbstractSandbox", "DirectorySandbox", "SandboxViolation", "run_setup"]

class UnpickleableException(Exception):
    @staticmethod
    def dump(type, exc): ...

class ExceptionSaver:
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> bool: ...
    def resume(self) -> None: ...

def run_setup(setup_script, args): ...

class AbstractSandbox:
    def __enter__(self) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def run(self, func): ...
    # Dynamically created
    if sys.platform == "win32":
        def startfile(self, path, *args, **kw): ...
    else:
        def chown(self, path, *args, **kw): ...
        def chroot(self, path, *args, **kw): ...
        def lchown(self, path, *args, **kw): ...
        def mkfifo(self, path, *args, **kw): ...
        def mknod(self, path, *args, **kw): ...
        def pathconf(self, path, *args, **kw): ...

    def access(self, path, *args, **kw): ...
    def chdir(self, path, *args, **kw): ...
    def chmod(self, path, *args, **kw): ...
    def getcwd(self, *args, **kw): ...
    def link(self, src, dst, *args, **kw): ...
    def listdir(self, path, *args, **kw): ...
    def lstat(self, path, *args, **kw): ...
    def mkdir(self, path, *args, **kw): ...
    def open(self, path, *args, **kw): ...
    def readlink(self, path, *args, **kw): ...
    def remove(self, path, *args, **kw): ...
    def rename(self, src, dst, *args, **kw): ...
    def rmdir(self, path, *args, **kw): ...
    def stat(self, path, *args, **kw): ...
    def symlink(self, src, dst, *args, **kw): ...
    def unlink(self, path, *args, **kw): ...
    def utime(self, path, *args, **kw): ...

class DirectorySandbox(AbstractSandbox):
    write_ops: ClassVar[dict[str, None]]
    def __init__(self, sandbox, exceptions=...) -> None: ...
    def tmpnam(self) -> None: ...
    def open(self, file, flags, mode: int = 511, *args, **kw): ...  # type: ignore[override]

class SandboxViolation(DistutilsError):
    tmpl: str
