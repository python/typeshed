from _typeshed import FileDescriptorLike, StrOrBytesPath
from collections.abc import Iterable, Mapping, Sequence
from signal import _HANDLER, _SIGNUM
from struct import Struct
from threading import Lock
from typing import Any

__all__ = ["ensure_running", "get_inherited_fds", "connect_to_new_process", "set_forkserver_preload"]

MAXFDS_TO_SEND: int
SIGNED_STRUCT: Struct

class ForkServer:
    def __init__(self) -> None: ...
    def set_forkserver_preload(self, modules_names: list[str]) -> None: ...
    def get_inherited_fds(self) -> Sequence[int] | None: ...
    def connect_to_new_process(self, fds: Sequence[int]) -> tuple[int, int]: ...
    def ensure_running(self) -> None: ...

def main(
    listener_fd: int | None,
    alive_r: FileDescriptorLike,
    preload: Sequence[str],
    main_path: str | None = ...,
    sys_path: object | None = ...,
) -> None: ...
def _serve_one(child_r: int, fds: Iterable[int], unused_fds: Iterable[int], handlers: Mapping[_SIGNUM, _HANDLER]) -> Any: ...
def read_signed(fd: int) -> Any: ...
def write_signed(fd: int, n: Any) -> None: ...

_forkserver: ForkServer = ...
ensure_running = _forkserver.ensure_running
get_inherited_fds = _forkserver.get_inherited_fds
connect_to_new_process = _forkserver.connect_to_new_process
set_forkserver_preload = _forkserver.set_forkserver_preload
