from _typeshed import Incomplete
from typing import Optional

class ServerlessInferenceConfig:
    memory_size_in_mb: Incomplete
    max_concurrency: Incomplete
    provisioned_concurrency: Incomplete
    def __init__(
        self, memory_size_in_mb: int = 2048, max_concurrency: int = 5, provisioned_concurrency: Optional[int] = None
    ) -> None: ...
