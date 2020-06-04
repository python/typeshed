import sys
from asyncio import events
from asyncio import protocols
from asyncio import streams
from asyncio import transports
from typing import Any, Optional, Text, Tuple, Union, IO

if sys.version_info >= (3, 6):
    from os import PathLike
    _PathLike = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
    _PathLike = Union[str, bytes]

PIPE: int
STDOUT: int
DEVNULL: int

class SubprocessStreamProtocol(streams.FlowControlMixin,
                               protocols.SubprocessProtocol):
    stdin: Optional[streams.StreamWriter]
    stdout: Optional[streams.StreamReader]
    stderr: Optional[streams.StreamReader]
    def __init__(self, limit: int, loop: events.AbstractEventLoop) -> None: ...
    def connection_made(self, transport: transports.BaseTransport) -> None: ...
    def pipe_data_received(self, fd: int, data: Union[bytes, Text]) -> None: ...
    def pipe_connection_lost(self, fd: int, exc: Optional[Exception]) -> None: ...
    def process_exited(self) -> None: ...


class Process:
    stdin: Optional[streams.StreamWriter]
    stdout: Optional[streams.StreamReader]
    stderr: Optional[streams.StreamReader]
    pid: int
    def __init__(self,
                 transport: transports.BaseTransport,
                 protocol: protocols.BaseProtocol,
                 loop: events.AbstractEventLoop) -> None: ...
    @property
    def returncode(self) -> Optional[int]: ...
    async def wait(self) -> int: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    async def communicate(self, input: Optional[bytes] = ...) -> Tuple[bytes, bytes]: ...


async def create_subprocess_shell(
    # Seems that support for Path objects may depend on the loop implementation.
    # But, they seem to work with asyncio's default loop.
    cmd: _PathLike,
    stdin: Union[int, IO[Any], None] = ...,
    stdout: Union[int, IO[Any], None] = ...,
    stderr: Union[int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any
) -> Process: ...

async def create_subprocess_exec(
    # Seems that support for Path objects may depend on the loop implementation.
    # But, they seem to work with asyncio's default loop.
    program: _PathLike,
    *args: Union[str, bytes, _PathLike],
    stdin: Union[int, IO[Any], None] = ...,
    stdout: Union[int, IO[Any], None] = ...,
    stderr: Union[int, IO[Any], None] = ...,
    loop: Optional[events.AbstractEventLoop] = ...,
    limit: int = ...,
    **kwds: Any
) -> Process: ...
