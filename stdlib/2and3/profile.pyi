from typing import Any, Callable, Dict, Optional, TypeVar, Union

def run(statement: str, filename: Optional[str] = ..., sort: Union[str, int] = ...) -> None: ...
def runctx(statement: str, globals: Dict[str, Any], locals: Dict[str, Any], filename: Optional[str] = ..., sort: Union[str, int] = ...) -> None: ...

_SelfT = TypeVar('_SelfT', bound='Profile')
_T = TypeVar('_T')

class Profile:
    def __init__(self, timer: Optional[Callable[[], float]] = ..., bias: Optional[int] = ...) -> None: ...
    def set_cmd(self, cmd: str) -> None: ...
    def simulate_call(self, name: str) -> None: ...
    def simulate_cmd_complete(self) -> None: ...
    def print_stats(self, sort: Union[str, int] = ...) -> None: ...
    def dump_stats(self, file: str) -> None: ...
    def create_stats(self) -> None: ...
    def snapshot_stats(self) -> None: ...
    def run(self: _SelfT, cmd: str) -> _SelfT: ...
    def runctx(self: _SelfT, cmd: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> _SelfT: ...
    def runcall(self, func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    def calibrate(self, m: int, verbose: int = ...) -> float: ...
