from _typeshed import Incomplete

from .async_pubsub_manager import AsyncPubSubManager

class AsyncAioPikaManager(AsyncPubSubManager):
    name: str
    url: Incomplete
    publisher_connection: Incomplete
    publisher_channel: Incomplete
    publisher_exchange: Incomplete
    def __init__(
        self,
        url: str = "amqp://guest:guest@localhost:5672//",
        channel: str = "socketio",
        write_only: bool = False,
        logger: Incomplete | None = None,
    ) -> None: ...
