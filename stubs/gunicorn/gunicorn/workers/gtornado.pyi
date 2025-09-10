from types import FrameType
from typing_extensions import override

from gunicorn.workers.base import Worker
from tornado.ioloop import IOLoop, PeriodicCallback  # type: ignore[import-not-found]

TORNADO5: bool

class TornadoWorker(Worker):
    alive: bool
    server_alive: bool
    ioloop: IOLoop
    callbacks: list[PeriodicCallback]

    @classmethod
    def setup(cls) -> None: ...
    @override
    def handle_exit(self, sig: int, frame: FrameType | None) -> None: ...
    def handle_request(self) -> None: ...
    def watchdog(self) -> None: ...
    def heartbeat(self) -> None: ...
    @override
    def init_process(self) -> None: ...
    @override
    def run(self) -> None: ...
