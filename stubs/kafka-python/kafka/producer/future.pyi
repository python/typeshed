from _typeshed import Incomplete
from typing import NamedTuple

from kafka.future import Future

class FutureProduceResult(Future):
    topic_partition: Incomplete
    def __init__(self, topic_partition) -> None: ...
    def success(self, value): ...
    def failure(self, error): ...
    def wait(self, timeout=None): ...

class FutureRecordMetadata(Future):
    args: Incomplete
    def __init__(
        self,
        produce_future,
        batch_index,
        timestamp_ms,
        checksum,
        serialized_key_size,
        serialized_value_size,
        serialized_header_size,
    ) -> None: ...
    def get(self, timeout=None): ...

class RecordMetadata(NamedTuple):
    topic: Incomplete
    partition: Incomplete
    topic_partition: Incomplete
    offset: Incomplete
    timestamp: Incomplete
    checksum: Incomplete
    serialized_key_size: Incomplete
    serialized_value_size: Incomplete
    serialized_header_size: Incomplete
