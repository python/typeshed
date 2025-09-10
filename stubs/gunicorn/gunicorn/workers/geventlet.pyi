from types import FrameType
from typing import Any
from typing_extensions import override

from eventlet.greenio import GreenSocket  # type: ignore[import-not-found] # pyright: ignore[reportMissingTypeStubs]
from eventlet.wsgi import local  # type: ignore[import-not-found] # pyright: ignore[reportMissingTypeStubs]
from gunicorn.workers.base_async import AsyncWorker

from .._types import _AddressType

EVENTLET_WSGI_LOCAL: local | None
EVENTLET_ALREADY_HANDLED: bool | None

def patch_sendfile() -> None: ...

class EventletWorker(AsyncWorker):
    def patch(self) -> None: ...
    @override
    def is_already_handled(self, respiter: Any) -> bool: ...
    @override
    def init_process(self) -> None: ...
    @override
    def handle_quit(self, sig: int, frame: FrameType | None) -> None: ...
    @override
    def handle_usr1(self, sig: int, frame: FrameType | None) -> None: ...
    @override
    def timeout_ctx(self) -> None: ...
    @override
    def handle(self, listener: GreenSocket, client: GreenSocket, addr: _AddressType) -> None: ...
    @override
    def run(self) -> None: ...
