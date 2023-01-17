from _typeshed import Incomplete
import abc
from _typeshed import Self
from typing import Any

ConnectionError: Any

class GlobalCache(metaclass=abc.ABCMeta):
    __metaclass__: Any
    transient_errors: Any
    strict_read: bool
    strict_write: bool
    @abc.abstractmethod
    def get(self, keys): ...
    @abc.abstractmethod
    def set(self, items, expires: Incomplete | None = ...): ...
    @abc.abstractmethod
    def delete(self, keys): ...
    @abc.abstractmethod
    def watch(self, items): ...
    @abc.abstractmethod
    def unwatch(self, keys): ...
    @abc.abstractmethod
    def compare_and_swap(self, items, expires: Incomplete | None = ...): ...
    @abc.abstractmethod
    def clear(self): ...

class _InProcessGlobalCache(GlobalCache):
    cache: Any
    def __init__(self) -> None: ...
    def get(self, keys): ...
    def set(self, items, expires: Incomplete | None = ...) -> None: ...
    def delete(self, keys) -> None: ...
    def watch(self, items) -> None: ...
    def unwatch(self, keys) -> None: ...
    def compare_and_swap(self, items, expires: Incomplete | None = ...): ...
    def clear(self) -> None: ...

class RedisCache(GlobalCache):
    transient_errors: Any
    @classmethod
    def from_environment(cls: type[Self], strict_read: bool = ..., strict_write: bool = ...) -> Self: ...
    redis: Any
    strict_read: Any
    strict_write: Any
    def __init__(self, redis, strict_read: bool = ..., strict_write: bool = ...) -> None: ...
    @property
    def pipes(self): ...
    def get(self, keys): ...
    def set(self, items, expires: Incomplete | None = ...) -> None: ...
    def delete(self, keys) -> None: ...
    def watch(self, items) -> None: ...
    def unwatch(self, keys) -> None: ...
    def compare_and_swap(self, items, expires: Incomplete | None = ...): ...
    def clear(self) -> None: ...

class MemcacheCache(GlobalCache):
    class KeyNotSet(Exception):
        key: Any
        def __init__(self, key) -> None: ...
        def __eq__(self, other): ...
    transient_errors: Any
    @classmethod
    def from_environment(
        cls: type[Self], max_pool_size: int = ..., strict_read: bool = ..., strict_write: bool = ...
    ) -> Self: ...
    client: Any
    strict_read: Any
    strict_write: Any
    def __init__(self, client, strict_read: bool = ..., strict_write: bool = ...) -> None: ...
    @property
    def caskeys(self): ...
    def get(self, keys): ...
    def set(self, items, expires: Incomplete | None = ...): ...
    def delete(self, keys) -> None: ...
    def watch(self, items) -> None: ...
    def unwatch(self, keys) -> None: ...
    def compare_and_swap(self, items, expires: Incomplete | None = ...): ...
    def clear(self) -> None: ...