from typing import Any, Callable, Dict, Optional, TypeVar

def run(statement: str, filename: Optional[str] = ..., sort: int = ...) -> None: ...
def runctx(statement: str, globals: Dict[str, Any], locals: Dict[str, Any], filename: Optional[str] = ..., sort: int = ...) -> None: ...

_SelfT = TypeVar('_SelfT', bound='Profile')
_T = TypeVar('_T')

class Profile:
    def __init__(self, custom_timer: Callable[[], float] = ..., time_unit: float = ..., subcalls: bool = ..., builtins: bool = ...) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def print_stats(self, sort: int = ...) -> None: ...
    def dump_stats(self, file: str) -> None: ...
    def create_stats(self) -> None: ...
    def run(self: _SelfT, cmd: str) -> _SelfT: ...
    def runctx(self: _SelfT, cmd: str, globals: Dict[str, Any], locals: Dict[str, Any]) -> _SelfT: ...
    def runcall(self, func: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
