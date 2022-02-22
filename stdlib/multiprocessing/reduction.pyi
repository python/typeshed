import pickle
import sys
from abc import ABCMeta
from copyreg import _DispatchTableType
from typing import Any
from typing_extensions import Literal

if sys.platform == "win32":
    __all__ = ["send_handle", "recv_handle", "ForkingPickler", "register", "dump", "DupHandle", "duplicate", "steal_handle"]
else:
    __all__ = ["send_handle", "recv_handle", "ForkingPickler", "register", "dump", "DupFd", "sendfds", "recvfds"]

class ForkingPickler(pickle.Pickler):
    dispatch_table: _DispatchTableType
    def __init__(self, *args) -> None: ...
    @classmethod
    def register(cls, type, reduce) -> None: ...
    @classmethod
    def dumps(cls, obj, protocol: Any | None = ...): ...
    loads = pickle.loads

register = ForkingPickler.register

def dump(obj, file, protocol: Any | None = ...) -> None: ...

if sys.platform == "win32":
    def duplicate(handle, target_process: Any | None = ..., inheritable: bool = ..., *, source_process: Any | None = ...): ...
    def steal_handle(source_pid, handle): ...
    def send_handle(conn, handle, destination_pid) -> None: ...
    def recv_handle(conn): ...

    class DupHandle:
        def __init__(self, handle, access, pid: Any | None = ...) -> None: ...
        def detach(self): ...

else:
    if sys.platform == "darwin":
        ACKNOWLEDGE: Literal[True]
    else:
        ACKNOWLEDGE: Literal[False]

    def recvfds(sock, size): ...
    def send_handle(conn, handle, destination_pid) -> None: ...
    def recv_handle(conn) -> None: ...
    def sendfds(sock, fds) -> None: ... 
    def DupFd(fd): ...

class AbstractReducer(metaclass=ABCMeta):
    ForkingPickler = ForkingPickler
    register = register
    dump = dump
    send_handle = send_handle
    recv_handle = recv_handle
    if sys.platform == "win32":
        steal_handle = steal_handle
        duplicate = duplicate
        DupHandle = DupHandle
    else:
        sendfds = sendfds
        recvfds = recvfds
        DupFd = DupFd
    def __init__(self, *args) -> None: ...
