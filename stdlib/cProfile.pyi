import sys
from _typeshed import Self, StrOrBytesPath
from collections.abc import Callable
from types import CodeType
from typing import Any, TypeVar

def run(statement: str, filename: str | None = ..., sort: str | int = ...) -> None: ...
def runctx(
    statement: str, globals: dict[str, Any], locals: dict[str, Any], filename: str | None = ..., sort: str | int = ...
) -> None: ...

_T = TypeVar("_T")
_Label = tuple[str, int, str]

class Profile:
    stats: dict[_Label, tuple[int, int, int, int, dict[_Label, tuple[int, int, int, int]]]]  # undocumented
    def __init__(
        self, timer: Callable[[], float] = ..., timeunit: float = ..., subcalls: bool = ..., builtins: bool = ...
    ) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def print_stats(self, sort: str | int = ...) -> None: ...
    def dump_stats(self, file: StrOrBytesPath) -> None: ...
    def create_stats(self) -> None: ...
    def snapshot_stats(self) -> None: ...
    def run(self: Self, cmd: str) -> Self: ...
    def runctx(self: Self, cmd: str, globals: dict[str, Any], locals: dict[str, Any]) -> Self: ...
    def runcall(self, __func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    if sys.version_info >= (3, 8):
        def __enter__(self: Self) -> Self: ...
        def __exit__(self, *exc_info: Any) -> None: ...

def label(code: str | CodeType) -> _Label: ...  # undocumented
