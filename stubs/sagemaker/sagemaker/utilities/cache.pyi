import datetime
from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

_KeyType = TypeVar("_KeyType")
_ValType = TypeVar("_ValType")

class LRUCache:
    class Element:
        value: Incomplete
        creation_time: Incomplete
        def __init__(self, value: _ValType, creation_time: datetime.datetime) -> None: ...

    def __init__(
        self,
        max_cache_items: int,
        expiration_horizon: datetime.timedelta,
        retrieval_function: Callable[[_KeyType, _ValType], _ValType],
    ) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: _KeyType) -> bool: ...
    def clear(self) -> None: ...
    def get(self, key: _KeyType, data_source_fallback: bool | None = True) -> _ValType: ...
    def put(self, key: _KeyType, value: _ValType | None = None) -> None: ...
