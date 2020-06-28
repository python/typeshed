from queue import Queue
from typing import Any, List, Optional, Tuple, TypeVar

families: List[None]

_TConnection = TypeVar("_TConnection", bound=Connection)
_TListener = TypeVar("_TListener", bound=Listener)

class Connection(object):
    _in: Any
    _out: Any
    recv: Any
    recv_bytes: Any
    send: Any
    send_bytes: Any
    def __enter__(self: _TConnection) -> _TConnection: ...
    def __exit__(self, exc_type, exc_value, exc_tb) -> None: ...
    def __init__(self, _in, _out) -> None: ...
    def close(self) -> None: ...
    def poll(self, timeout: float = ...) -> bool: ...

class Listener(object):
    _backlog_queue: Optional[Queue[Any]]
    @property
    def address(self) -> Optional[Queue[Any]]: ...
    def __enter__(self: _TListener) -> _TListener: ...
    def __exit__(self, exc_type, exc_value, exc_tb) -> None: ...
    def __init__(self, address=..., family=..., backlog=...) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...

def Client(address) -> Connection: ...
def Pipe(duplex: bool = ...) -> Tuple[Connection, Connection]: ...
