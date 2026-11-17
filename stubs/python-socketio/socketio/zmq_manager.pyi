from _typeshed import Incomplete
from collections.abc import Generator

from .pubsub_manager import PubSubManager

class ZmqManager(PubSubManager):
    name: str
    sink: Incomplete
    sub: Incomplete
    channel: Incomplete
    def __init__(
        self,
        url: str = "zmq+tcp://localhost:5555+5556",
        channel: str = "socketio",
        write_only: bool = False,
        logger: Incomplete | None = None,
    ) -> None: ...
    def zmq_listen(self) -> Generator[Incomplete]: ...
