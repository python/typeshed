from enum import Enum
from typing import Any

class IndexType(Enum):
    HASH: int
    JSON: int

class IndexDefinition:
    args: Any
    def __init__(self, prefix=..., filter: Any | None = ..., language_field: Any | None = ..., language: Any | None = ..., score_field: Any | None = ..., score: float = ..., payload_field: Any | None = ..., index_type: Any | None = ...) -> None: ...
