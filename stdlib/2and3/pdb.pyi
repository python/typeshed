# NOTE: This stub is incomplete - only contains some global functions

from cmd import Cmd
import sys
from typing import Any, Dict, IO, Iterable, Optional

class Restart(Exception): ...

def run(statement: str, globals: Optional[Dict[str, Any]] = ...,
        locals: Optional[Dict[str, Any]] = ...) -> None: ...
def runeval(expression: str, globals: Optional[Dict[str, Any]] = ...,
            locals: Optional[Dict[str, Any]] = ...) -> Any: ...
def runctx(statement: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> None: ...
def runcall(*args: Any, **kwds: Any) -> Any: ...

if sys.version_info >= (3, 7):
    def set_trace(*, header: Optional[str] = ...) -> None: ...
else:
    def set_trace() -> None: ...

def post_mortem(t: Optional[Any] = ...) -> None: ...
def pm() -> None: ...

class Pdb(Cmd):
    if sys.version_info >= (3, 6):
        def __init__(
            self,
            completekey: str = ...,
            stdin: Optional[IO[str]] = ...,
            stdout: Optional[IO[str]] = ...,
            skip: Iterable[str] = ...,
            nosigint: bool = ...,
            readrc: bool = ...,
        ) -> None: ...
    elif sys.version_info >= (3, 2):
        def __init__(
            self,
            completekey: str = ...,
            stdin: Optional[IO[str]] = ...,
            stdout: Optional[IO[str]] = ...,
            skip: Iterable[str] = ...,
            nosigint: bool = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            completekey: str = ...,
            stdin: Optional[IO[str]] = ...,
            stdout: Optional[IO[str]] = ...,
            skip: Iterable[str] = ...,
        ) -> None: ...
    def run(self, statement: str, globals: Optional[Dict[str, Any]] = ...,
            locals: Optional[Dict[str, Any]] = ...) -> None: ...
    def runeval(self, expression: str, globals: Optional[Dict[str, Any]] = ...,
                locals: Optional[Dict[str, Any]] = ...) -> Any: ...
    def runcall(self, *args: Any, **kwds: Any) -> Any: ...
    if sys.version_info >= (3, 7):
        def set_trace(self, *, header: Optional[str] = ...) -> None: ...
    else:
        def set_trace(self) -> None: ...
