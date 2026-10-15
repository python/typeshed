from _typeshed import Incomplete

from .pubsub_manager import PubSubManager

logger: Incomplete

class KafkaManager(PubSubManager):
    name: str
    kafka_urls: Incomplete
    producer: Incomplete
    consumer: Incomplete
    def __init__(self, url: str = "kafka://localhost:9092", channel: str = "socketio", write_only: bool = False) -> None: ...
