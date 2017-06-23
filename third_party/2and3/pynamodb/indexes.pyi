from typing import Any, Optional

class IndexMeta(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class Index:
    Meta = ...  # type: Any
    def __init__(self) -> None: ...
    @classmethod
    def count(cls, hash_key, consistent_read: bool = ..., **filters) -> int: ...
    @classmethod
    def query(self, hash_key, scan_index_forward: Optional[Any] = ..., consistent_read: bool = ..., limit: Optional[Any] = ..., last_evaluated_key: Optional[Any] = ..., attributes_to_get: Optional[Any] = ..., **filters): ...

class GlobalSecondaryIndex(Index): ...
class LocalSecondaryIndex(Index): ...

class Projection:
    projection_type = ...  # type: Any
    non_key_attributes = ...  # type: Any

class KeysOnlyProjection(Projection):
    projection_type = ...  # type: Any

class IncludeProjection(Projection):
    projection_type = ...  # type: Any
    non_key_attributes = ...  # type: Any
    def __init__(self, non_attr_keys: Optional[Any] = ...) -> None: ...

class AllProjection(Projection):
    projection_type = ...  # type: Any
