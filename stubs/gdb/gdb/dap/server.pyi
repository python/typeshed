import threading
from _typeshed import Incomplete
from collections.abc import Callable
from contextlib import AbstractContextManager
from typing import Any, BinaryIO, Generic, TypeVar, type_check_only

from .startup import DAPQueue

_T = TypeVar("_T")

class NotStoppedException(Exception): ...

class CancellationHandler:
    lock: threading.Lock
    reqs: list[int]
    in_flight_dap_thread: int | None
    def starting(self, req: int) -> None: ...
    def done(self, req: int) -> None: ...  # req argument is not used
    def cancel(self, req: int) -> None: ...
    def interruptable_region(self, req: int) -> AbstractContextManager[None]: ...

class Server:
    in_stream: BinaryIO
    out_stream: BinaryIO
    child_stream: BinaryIO
    delay_events: list[tuple[str, Any]]  # second tuple item is an arbitrary object
    write_queue: DAPQueue[Any | None]  # objects in queue must be passable to json.dumps
    read_queue: DAPQueue[Any | None]  # objects in queue are returned from json.loads
    done: bool
    canceller: CancellationHandler
    config: dict[str, Incomplete]
    def __init__(self, in_stream, out_stream, child_stream) -> None: ...
    def main_loop(self) -> None: ...
    def send_event(self, event: str, body: Any | None = None) -> None: ...  # body is an arbitrary object
    def send_event_later(self, event: str, body: Any | None = None) -> None: ...  # body is an arbitrary object
    def shutdown(self) -> None: ...

def send_event(event: str, body: Any | None = None) -> None: ...  # body is an arbitrary object
@type_check_only
class _Wrapper:
    def __call__(self, func: _T) -> _T: ...

def request(name: str, *, response: bool = True, on_dap_thread: bool = False, expect_stopped: bool = True) -> _Wrapper: ...
def capability(name: str, value: bool = True) -> _Wrapper: ...
def client_bool_capability(name: str) -> bool: ...
def initialize(**args) -> dict[str, bool]: ...  # args is arbitrary values for Server.config
def terminate(**args) -> None: ...  # args argument is unused
def disconnect(*, terminateDebuggee: bool = False, **args): ...  # args argument is unused
def cancel(**args) -> None: ...  # args argument is unused

class Invoker:
    def __init__(self, cmd: str) -> None: ...
    def __call__(self) -> None: ...

class Cancellable(Generic[_T]):
    def __init__(self, fn: Callable[[], _T], result_q: DAPQueue[_T] | None = None) -> None: ...
    def __call__(self) -> None: ...

def send_gdb(cmd: str | Callable[[], object]) -> None: ...
def send_gdb_with_response(fn: str | Callable[[], _T]) -> _T: ...
