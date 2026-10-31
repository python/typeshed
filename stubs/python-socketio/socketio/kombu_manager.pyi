from _typeshed import Incomplete

from .pubsub_manager import PubSubManager

class KombuManager(PubSubManager):
    name: str
    url: Incomplete
    connection_options: Incomplete
    exchange_options: Incomplete
    queue_options: Incomplete
    producer_options: Incomplete
    publisher_connection: Incomplete
    def __init__(
        self,
        url: str = "amqp://guest:guest@localhost:5672//",
        channel: str = "socketio",
        write_only: bool = False,
        logger: Incomplete | None = None,
        connection_options: Incomplete | None = None,
        exchange_options: Incomplete | None = None,
        queue_options: Incomplete | None = None,
        producer_options: Incomplete | None = None,
    ) -> None: ...
    def initialize(self) -> None: ...
