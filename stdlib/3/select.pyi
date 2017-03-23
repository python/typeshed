# Stubs for select

# NOTE: These are incomplete!

from typing import Any, Tuple, List, Sequence, TypeVar

class error(Exception): ...

POLLIN = 0
POLLPRI = 0
POLLOUT = 0
POLLERR = 0
POLLHUP = 0
POLLNVAL = 0

class poll:
    def __init__(self) -> None: ...
    def register(self, fd: Any,
                 eventmask: int = ...) -> None: ...
    def modify(self, fd: Any, eventmask: int) -> None: ...
    def unregister(self, fd: Any) -> None: ...
    def poll(self, timeout: int = ...) -> List[Tuple[int, int]]: ...

# Not the canonical naming choices, but these map to the select arguments. We
# need 3 because nothing in select prevents the read set from being socket
# objects and the write set from being file descriptors.
_R = TypeVar("_R")
_W = TypeVar("_W")
_X = TypeVar("_X")
def select(rlist: Sequence[_R], wlist: Sequence[_W], xlist: Sequence[_X], timeout: float = ...) -> Tuple[List[_R], List[_W], List[_X]]: ...
