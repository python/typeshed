from typing import Any

from setuptools._distutils.errors import DistutilsError

class UnpickleableException(Exception):
    @staticmethod
    def dump(type, exc): ...

class ExceptionSaver:
    def __enter__(self): ...
    def __exit__(self, type, exc, tb): ...
    def resume(self) -> None: ...

def run_setup(setup_script, args): ...

class AbstractSandbox:
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def run(self, func): ...

class DirectorySandbox(AbstractSandbox):
    write_ops: Any
    def __init__(self, sandbox, exceptions=...) -> None: ...
    def tmpnam(self) -> None: ...
    def open(self, file, flags, mode: int = ..., *args, **kw): ...

class SandboxViolation(DistutilsError):
    tmpl: Any
