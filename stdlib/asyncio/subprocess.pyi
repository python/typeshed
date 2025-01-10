import subprocess
import sys
from _typeshed import StrOrBytesPath
from asyncio import events, protocols, streams, transports
from collections.abc import Callable, Collection
from typing import IO, Any, Literal, overload

# Keep asyncio.__all__ updated with any changes to __all__ here
__all__ = ("create_subprocess_exec", "create_subprocess_shell")

PIPE = subprocess.PIPE
STDOUT = subprocess.STDOUT
DEVNULL = subprocess.DEVNULL

class SubprocessStreamProtocol(streams.FlowControlMixin, protocols.SubprocessProtocol):
    stdin: streams.StreamWriter | None
    stdout: streams.StreamReader | None
    stderr: streams.StreamReader | None
    def __init__(self, limit: int, loop: events.AbstractEventLoop) -> None: ...
    def pipe_data_received(self, fd: int, data: bytes | str) -> None: ...

class Process[CommOut: (PIPE, int, IO[Any], None), CommErr: (PIPE, int, IO[Any], None)]:
    stdin: streams.StreamWriter | None
    stdout: streams.StreamReader | None
    stderr: streams.StreamReader | None
    pid: int
    def __init__(
        self, transport: transports.BaseTransport, protocol: protocols.BaseProtocol, loop: events.AbstractEventLoop
    ) -> None: ...
    @property
    def returncode(self) -> int | None: ...
    async def wait(self) -> int: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    @overload
    async def communicate(
        self: Process[PIPE, PIPE], input: bytes | bytearray | memoryview | None = None
    ) -> tuple[bytes, bytes]: ...
    @overload
    async def communicate(
        self: Process[PIPE, int | IO[Any] | None], input: bytes | bytearray | memoryview | None = None
    ) -> tuple[bytes, None]: ...
    @overload
    async def communicate(
        self: Process[int | IO[Any] | None, PIPE], input: bytes | bytearray | memoryview | None = None
    ) -> tuple[None, bytes]: ...
    @overload
    async def communicate(
        self: Process[int | IO[Any] | None, int | IO[Any] | None], input: bytes | bytearray | memoryview | None = None
    ) -> tuple[None, None]: ...

if sys.version_info >= (3, 11):
    async def create_subprocess_shell[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        cmd: str | bytes,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        limit: int = 65536,
        *,
        # These parameters are forced to these values by BaseEventLoop.subprocess_shell
        universal_newlines: Literal[False] = False,
        shell: Literal[True] = True,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
        process_group: int | None = None,
        pipesize: int = -1,
    ) -> Process[Out, Err]: ...
    async def create_subprocess_exec[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        program: StrOrBytesPath,
        *args: StrOrBytesPath,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        limit: int = 65536,
        # These parameters are forced to these values by BaseEventLoop.subprocess_exec
        universal_newlines: Literal[False] = False,
        shell: Literal[False] = False,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
        process_group: int | None = None,
        pipesize: int = -1,
    ) -> Process[Out, Err]: ...

elif sys.version_info >= (3, 10):
    async def create_subprocess_shell[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        cmd: str | bytes,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        limit: int = 65536,
        *,
        # These parameters are forced to these values by BaseEventLoop.subprocess_shell
        universal_newlines: Literal[False] = False,
        shell: Literal[True] = True,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
        pipesize: int = -1,
    ) -> Process[Out, Err]: ...
    async def create_subprocess_exec[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        program: StrOrBytesPath,
        *args: StrOrBytesPath,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        limit: int = 65536,
        # These parameters are forced to these values by BaseEventLoop.subprocess_exec
        universal_newlines: Literal[False] = False,
        shell: Literal[False] = False,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
        pipesize: int = -1,
    ) -> Process[Out, Err]: ...

else:  # >= 3.9
    async def create_subprocess_shell[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        cmd: str | bytes,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        loop: events.AbstractEventLoop | None = None,
        limit: int = 65536,
        *,
        # These parameters are forced to these values by BaseEventLoop.subprocess_shell
        universal_newlines: Literal[False] = False,
        shell: Literal[True] = True,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
    ) -> Process[Out, Err]: ...
    async def create_subprocess_exec[
        Out: (PIPE, int, IO[Any], None), Err: (PIPE, int, IO[Any], None)
    ](
        program: StrOrBytesPath,
        *args: StrOrBytesPath,
        stdin: int | IO[Any] | None = None,
        stdout: Out = None,
        stderr: Err = None,
        loop: events.AbstractEventLoop | None = None,
        limit: int = 65536,
        # These parameters are forced to these values by BaseEventLoop.subprocess_exec
        universal_newlines: Literal[False] = False,
        shell: Literal[False] = False,
        bufsize: Literal[0] = 0,
        encoding: None = None,
        errors: None = None,
        text: Literal[False] | None = None,
        # These parameters are taken by subprocess.Popen, which this ultimately delegates to
        executable: StrOrBytesPath | None = None,
        preexec_fn: Callable[[], Any] | None = None,
        close_fds: bool = True,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        startupinfo: Any | None = None,
        creationflags: int = 0,
        restore_signals: bool = True,
        start_new_session: bool = False,
        pass_fds: Collection[int] = ...,
        group: None | str | int = None,
        extra_groups: None | Collection[str | int] = None,
        user: None | str | int = None,
        umask: int = -1,
    ) -> Process[Out, Err]: ...
