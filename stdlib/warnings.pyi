import sys
from _warnings import warn as warn, warn_explicit as warn_explicit
from collections.abc import Sequence
from types import ModuleType, TracebackType
from typing import Any, Generic, TextIO, TypeVar, overload
from typing_extensions import Literal, TypeAlias

__all__ = [
    "warn",
    "warn_explicit",
    "showwarning",
    "formatwarning",
    "filterwarnings",
    "simplefilter",
    "resetwarnings",
    "catch_warnings",
]

_W = TypeVar("_W", bound=list[WarningMessage] | None)
_ActionKind: TypeAlias = Literal["default", "error", "ignore", "always", "module", "once"]

filters: Sequence[tuple[str, str | None, type[Warning], str | None, int]]  # undocumented, do not mutate

def showwarning(
    message: Warning | str,
    category: type[Warning],
    filename: str,
    lineno: int,
    file: TextIO | None = None,
    line: str | None = None,
) -> None: ...
def formatwarning(
    message: Warning | str, category: type[Warning], filename: str, lineno: int, line: str | None = None
) -> str: ...
def filterwarnings(
    action: _ActionKind, message: str = "", category: type[Warning] = ..., module: str = "", lineno: int = 0, append: bool = False
) -> None: ...
def simplefilter(action: _ActionKind, category: type[Warning] = ..., lineno: int = 0, append: bool = False) -> None: ...
def resetwarnings() -> None: ...

class _OptionError(Exception): ...

class WarningMessage:
    message: Warning | str
    category: type[Warning]
    filename: str
    lineno: int
    file: TextIO | None
    line: str | None
    source: Any | None
    def __init__(
        self,
        message: Warning | str,
        category: type[Warning],
        filename: str,
        lineno: int,
        file: TextIO | None = None,
        line: str | None = None,
        source: Any | None = None,
    ) -> None: ...

class catch_warnings(Generic[_W]):
    if sys.version_info >= (3, 11):
        @overload
        def __init__(
            self: catch_warnings[None],
            *,
            record: Literal[False] = False,
            module: ModuleType | None = None,
            action: _ActionKind | None = None,
            category: type[Warning] = ...,
            lineno: int = 0,
            append: bool = False,
        ) -> None: ...
        @overload
        def __init__(
            self: catch_warnings[list[WarningMessage]],
            *,
            record: Literal[True],
            module: ModuleType | None = None,
            action: _ActionKind | None = None,
            category: type[Warning] = ...,
            lineno: int = 0,
            append: bool = False,
        ) -> None: ...
        @overload
        def __init__(
            self: catch_warnings[list[WarningMessage] | None],
            *,
            record: bool,
            module: ModuleType | None = None,
            action: _ActionKind | None = None,
            category: type[Warning] = ...,
            lineno: int = 0,
            append: bool = False,
        ) -> None: ...
    else:
        @overload
        def __init__(self: catch_warnings[None], *, record: Literal[False] = False, module: ModuleType | None = None) -> None: ...
        @overload
        def __init__(
            self: catch_warnings[list[WarningMessage]], *, record: Literal[True], module: ModuleType | None = None
        ) -> None: ...
        @overload
        def __init__(
            self: catch_warnings[list[WarningMessage] | None], *, record: bool, module: ModuleType | None = None
        ) -> None: ...

    def __enter__(self) -> _W: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
