from typing import (IO, Any, Callable, Dict, List, Optional, Sequence, Tuple,
                    Union)

_Timer = Callable[[], float]
_Stmt = Union[str, Callable[[], Any]]

default_timer: _Timer

class Timer:
    def __init__(
        self, stmt: _Stmt = ..., setup: _Stmt = ..., timer: _Timer = ..., globals: Optional[Dict[str, Any]] = ...
    ) -> None: ...
    def print_exc(self, file: Optional[IO[str]] = ...) -> None: ...
    def timeit(self, number: int = ...) -> float: ...
    def repeat(self, repeat: int = ..., number: int = ...) -> List[float]: ...
    def autorange(self, callback: Optional[Callable[[int, float], Any]] = ...) -> Tuple[int, float]: ...

def timeit(
    stmt: _Stmt = ..., setup: _Stmt = ..., timer: _Timer = ..., number: int = ..., globals: Optional[Dict[str, Any]] = ...
) -> float: ...
def repeat(
    stmt: _Stmt = ...,
    setup: _Stmt = ...,
    timer: _Timer = ...,
    repeat: int = ...,
    number: int = ...,
    globals: Optional[Dict[str, Any]] = ...,
) -> List[float]: ...

_timerFunc = Callable[[], float]

def main(args: Optional[Sequence[str]] = ..., *, _wrap_timer: Optional[Callable[[_timerFunc], _timerFunc]] = ...) -> None: ...
