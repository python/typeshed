import sys
from asyncio import events, protocols, streams, transports
from subprocess import _DEVNULL, _PIPE, _STDOUT, DEVNULL as DEVNULL, PIPE as PIPE, STDOUT as STDOUT
from typing import IO, Any, Generic, Optional, Tuple, TypeVar, Union, overload

if sys.version_info >= (3, 8):
    from os import PathLike

    _ExecArg = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
    _ExecArg = Union[str, bytes]  # Union used instead of AnyStr due to mypy issue  #1236

_S = TypeVar("_S")
_T = TypeVar("_T")
_U = TypeVar("_U")

class SubprocessStreamProtocol(streams.FlowControlMixin, protocols.SubprocessProtocol):
    stdin: Optional[streams.StreamWriter]
    stdout: Optional[streams.StreamReader]
    stderr: Optional[streams.StreamReader]
    def __init__(self, limit: int, loop: events.AbstractEventLoop) -> None: ...
    def connection_made(self, transport: transports.BaseTransport) -> None: ...
    def pipe_data_received(self, fd: int, data: Union[bytes, str]) -> None: ...
    def pipe_connection_lost(self, fd: int, exc: Optional[Exception]) -> None: ...
    def process_exited(self) -> None: ...

class Process(Generic[_S, _T, _U]):
    stdin: _S
    stdout: _T
    stderr: _U
    pid: int
    def __init__(
        self, transport: transports.BaseTransport, protocol: protocols.BaseProtocol, loop: events.AbstractEventLoop
    ) -> None: ...
    @property
    def returncode(self) -> Optional[int]: ...
    async def wait(self) -> int: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    async def communicate(self, input: Optional[bytes] = ...) -> Tuple[bytes, bytes]: ...

@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: _PIPE,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, None, None]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    *,
    stdout: _PIPE,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, streams.StreamReader, None]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    *,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, None, streams.StreamReader]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: _PIPE,
    stdout: _PIPE,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, streams.StreamReader, None]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: _PIPE,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    *,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, None, streams.StreamReader]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    *,
    stdout: _PIPE,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, streams.StreamReader, streams.StreamReader]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: _PIPE,
    stdout: _PIPE,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, streams.StreamReader, streams.StreamReader]: ...
@overload
async def create_subprocess_shell(
    cmd: Union[str, bytes],  # Union used instead of AnyStr due to mypy issue  #1236
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, None, None]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: _PIPE,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, None, None]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: _PIPE,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, streams.StreamReader, None]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, None, streams.StreamReader]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: _PIPE,
    stdout: _PIPE,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, streams.StreamReader, None]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: _PIPE,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, None, streams.StreamReader]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: _PIPE,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, streams.StreamReader, streams.StreamReader]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: _PIPE,
    stdout: _PIPE,
    stderr: _PIPE,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[streams.StreamWriter, streams.StreamReader, streams.StreamReader]: ...
@overload
async def create_subprocess_exec(
    program: _ExecArg,
    *args: _ExecArg,
    stdin: Union[_DEVNULL, int, IO[Any], None] = ...,
    stdout: Union[_DEVNULL, int, IO[Any], None] = ...,
    stderr: Union[_DEVNULL, _STDOUT, int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any,
) -> Process[None, None, None]: ...
