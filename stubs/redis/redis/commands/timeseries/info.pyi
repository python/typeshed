from ..helpers import nativestr as nativestr
from .utils import list_to_dict as list_to_dict
from typing import Any

class TSInfo:
    rules: Any
    labels: Any
    sourceKey: Any
    chunk_count: Any
    memory_usage: Any
    total_samples: Any
    retention_msecs: Any
    last_time_stamp: Any
    first_time_stamp: Any
    max_samples_per_chunk: Any
    chunk_size: Any
    duplicate_policy: Any
    source_key: Any
    lastTimeStamp: Any
    def __init__(self, args) -> None: ...
