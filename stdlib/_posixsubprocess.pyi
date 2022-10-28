from _typeshed import StrOrBytesPath
import sys
from collections.abc import Callable, Sequence
from typing_extensions import SupportsIndex

if sys.platform != "win32":
    def cloexec_pipe() -> tuple[int, int]: ...
    def fork_exec(
        __process_args: Sequence[StrOrBytesPath] | None,
        __executable_list: Sequence[bytes],
        __close_fds: bool,
        __fds_to_keep: tuple[int, ...],
        __cwd_obj: str,
        __env_list: Sequence[bytes] | None,
        __p2cread: int,
        __p2cwrite: int,
        __c2pred: int,
        __c2pwrite: int,
        __errread: int,
        __errwrite: int,
        __errpipe_read: int,
        __errpipe_write: int,
        __restore_signals: int,
        __call_setsid: int,
        __pgid_to_set: int,
        __gid_object: SupportsIndex | None,
        __groups_list: list[int] | None,
        __uid_object: SupportsIndex | None, 
        __child_umask: int,
        __preexec_fn: Callable[[], None],
        __allow_vfork: bool,
    ) -> int: ...
