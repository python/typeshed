from _typeshed import Incomplete

from .async_pubsub_manager import AsyncPubSubManager

class AsyncRedisManager(AsyncPubSubManager):
    name: str
    redis_url: Incomplete
    redis_options: Incomplete
    def __init__(
        self,
        url: str = "redis://localhost:6379/0",
        channel: str = "socketio",
        write_only: bool = False,
        logger: Incomplete | None = None,
        redis_options: Incomplete | None = None,
    ) -> None: ...
