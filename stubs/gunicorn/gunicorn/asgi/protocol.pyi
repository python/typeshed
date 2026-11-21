import asyncio
from collections.abc import Iterable
from typing import Final, Literal, TypedDict, type_check_only
from typing_extensions import NotRequired

from gunicorn.asgi.parser import CallbackRequest
from gunicorn.config import Config
from gunicorn.glogging import Logger as GLogger
from gunicorn.workers.gasgi import ASGIWorker

from .._types import _ASGIAppType

def secure_scheme_names(secure_scheme_headers: Iterable[str]) -> frozenset[bytes]: ...

HIGH_WATER_LIMIT: Final = 65536

class ClientDisconnected(OSError): ...

class FlowControl:
    __slots__ = ("_transport", "read_paused", "write_paused", "_is_writable_event")
    read_paused: bool
    write_paused: bool

    def __init__(self, transport: asyncio.BaseTransport) -> None: ...
    async def drain(self) -> None: ...
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...

class ASGIResponseInfo:
    status: str | int
    sent: int
    headers: list[tuple[str, str]]

    def __init__(self, status: str | int, headers: Iterable[tuple[str | bytes, str | bytes]], sent: int) -> None: ...

@type_check_only
class _BodyReceieverReceiveReturnType(TypedDict):
    type: Literal["http.disconnect", "http.request"]
    body: NotRequired[bytes]
    more_body: NotRequired[bool]

class BodyReceiver:
    __slots__ = (
        "_chunks",
        "_complete",
        "_source",
        "_complete",
        "_body_finished",
        "_closed",
        "_body_wait_expired",
        "_waiter",
        "request",
        "protocol",
        "expect_continue",
    )

    request: CallbackRequest
    protocol: ASGIProtocol
    expect_continue: bool

    def __init__(self, request: CallbackRequest, protocol: ASGIProtocol) -> None: ...
    def feed(self, chunk: bytes) -> None: ...
    @property
    def buffered(self) -> int: ...
    def set_complete(self) -> None: ...
    def signal_disconnect(self) -> None: ...
    async def receive(self) -> _BodyReceieverReceiveReturnType: ...

class ASGIProtocol(asyncio.Protocol):
    worker: ASGIWorker
    cfg: Config
    log: GLogger
    app: _ASGIAppType
    transport: asyncio.BaseTransport | None
    reader: asyncio.StreamReader | None
    writer: asyncio.BaseTransport | None
    req_count: int

    def __init__(self, worker: ASGIWorker) -> None: ...
