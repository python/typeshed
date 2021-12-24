from _typeshed import StrOrBytesPath
from collections.abc import Callable
from typing import Any, TypeVar

def run(statement: str, filename: str | None = ..., sort: str | int = ...) -> None: ...
def runctx(
    statement: str, globals: dict[str, Any], locals: dict[str, Any], filename: str | None = ..., sort: str | int = ...
) -> None: ...

_SelfT = TypeVar("_SelfT", bound=Profile)
_T = TypeVar("_T")
_Label = tuple[str, int, str]

class Profile:
    bias: int
    stats: dict[_Label, tuple[int, int, int, int, dict[_Label, tuple[int, int, int, int]]]]  # undocumented
    def __init__(self, timer: Callable[[], float] | None = ..., bias: int | None = ...) -> None: ...
    def set_cmd(self, cmd: str) -> None: ...
    def simulate_call(self, name: str) -> None: ...
    def simulate_cmd_complete(self) -> None: ...
    def print_stats(self, sort: str | int = ...) -> None: ...
    def dump_stats(self, file: StrOrBytesPath) -> None: ...
    def create_stats(self) -> None: ...
    def snapshot_stats(self) -> None: ...
    def run(self: _SelfT, cmd: str) -> _SelfT: ...
    def runctx(self: _SelfT, cmd: str, globals: dict[str, Any], locals: dict[str, Any]) -> _SelfT: ...
    def runcall(self, __func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    def calibrate(self, m: int, verbose: int = ...) -> float: ...
