import types
from collections.abc import Callable, Mapping
from typing import Final, Literal, SupportsIndex, final
from typing_extensions import TypeAlias

_Configs: TypeAlias = Literal["default", "isolated", "legacy", "empty"]

class InterpreterError(Exception): ...
class InterpreterNotFoundError(InterpreterError): ...
class NotShareableError(Exception): ...

# Not-instantiable, so mark as final.
@final
class CrossInterpreterBufferView:
    def __buffer__(self, flags: int, /) -> memoryview: ...

def new_config(name: _Configs = "isolated", /, **overides: object) -> types.SimpleNamespace: ...
def create(config: types.SimpleNamespace | _Configs | None = "isolated", *, reqrefs: bool = False) -> int: ...
def destroy(id: SupportsIndex, *, restrict: bool = False) -> None: ...
def list_all(*, require_ready: bool) -> list[tuple[int, int]]: ...
def get_current() -> tuple[int, int]: ...
def get_main() -> tuple[int, int]: ...
def is_running(id: SupportsIndex, *, restrict: bool = False) -> bool: ...
def get_config(id: SupportsIndex, *, restrict: bool = False) -> types.SimpleNamespace: ...
def whence(id: SupportsIndex) -> int: ...
def exec(id: SupportsIndex, code: str, shared: bool | None = None, *, restrict: bool = False) -> None: ...
def call(
    id: SupportsIndex,
    callable: Callable[..., object],
    args: tuple[object, ...] | None = None,
    kwargs: dict[str, object] | None = None,
    *,
    restrict: bool = False,
) -> object: ...
def run_string(id: SupportsIndex, script: str, shared: bool | None = None, *, restrict: bool = False) -> None: ...
def run_func(id: SupportsIndex, func: Callable[..., object], shared: bool | None = None, *, restrict: bool = False) -> None: ...
def set___main___attrs(id: SupportsIndex, updates: Mapping[str, object], *, restrict: bool = False) -> None: ...
def incref(id: SupportsIndex, *, implieslink: bool = False, restrict: bool = False) -> None: ...
def decref(id: SupportsIndex, *, restrict: bool = False) -> None: ...
def is_shareable(obj: object) -> bool: ...
def capture_exception(exc: BaseException | None = None) -> types.SimpleNamespace: ...

WHENCE_UNKNOWN: Final = 0
WHENCE_RUNTIME: Final = 1
WHENCE_LEGACY_CAPI: Final = 2
WHENCE_CAPI: Final = 3
WHENCE_XI: Final = 4
WHENCE_STDLIB: Final = 5
