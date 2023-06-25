import datetime
from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

KeyType = TypeVar("KeyType")
ValType = TypeVar("ValType")

class LRUCache:
    class Element:
        value: Incomplete
        creation_time: Incomplete
        def __init__(self, value: ValType, creation_time: datetime.datetime) -> None: ...

    def __init__(
        self,
        max_cache_items: int,
        expiration_horizon: datetime.timedelta,
        retrieval_function: Callable[[KeyType, ValType], ValType],
    ) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: KeyType) -> bool: ...
    def clear(self) -> None: ...
    def get(self, key: KeyType, data_source_fallback: bool | None = True) -> ValType: ...
    def put(self, key: KeyType, value: ValType | None = None) -> None: ...
