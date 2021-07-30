from typing import Any, Optional

UNDEFINED: Any

class Key:
    def __new__(cls, *path_args: Any, **kwargs: Any): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __getnewargs__(self): ...
    def parent(self): ...
    def root(self): ...
    def namespace(self): ...
    def project(self): ...
    app: Any = ...
    def id(self): ...
    def string_id(self): ...
    def integer_id(self): ...
    def pairs(self): ...
    def flat(self): ...
    def kind(self): ...
    def reference(self): ...
    def serialized(self): ...
    def urlsafe(self): ...
    def to_legacy_urlsafe(self, location_prefix: Any): ...
    def get(
        self,
        read_consistency: Optional[Any] = ...,
        read_policy: Optional[Any] = ...,
        transaction: Optional[Any] = ...,
        retries: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        deadline: Optional[Any] = ...,
        use_cache: Optional[Any] = ...,
        use_global_cache: Optional[Any] = ...,
        use_datastore: Optional[Any] = ...,
        global_cache_timeout: Optional[Any] = ...,
        use_memcache: Optional[Any] = ...,
        memcache_timeout: Optional[Any] = ...,
        max_memcache_items: Optional[Any] = ...,
        force_writes: Optional[Any] = ...,
        _options: Optional[Any] = ...,
    ): ...
    def get_async(
        self,
        read_consistency: Optional[Any] = ...,
        read_policy: Optional[Any] = ...,
        transaction: Optional[Any] = ...,
        retries: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        deadline: Optional[Any] = ...,
        use_cache: Optional[Any] = ...,
        use_global_cache: Optional[Any] = ...,
        use_datastore: Optional[Any] = ...,
        global_cache_timeout: Optional[Any] = ...,
        use_memcache: Optional[Any] = ...,
        memcache_timeout: Optional[Any] = ...,
        max_memcache_items: Optional[Any] = ...,
        force_writes: Optional[Any] = ...,
        _options: Optional[Any] = ...,
    ): ...
    def delete(
        self,
        retries: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        deadline: Optional[Any] = ...,
        use_cache: Optional[Any] = ...,
        use_global_cache: Optional[Any] = ...,
        use_datastore: Optional[Any] = ...,
        global_cache_timeout: Optional[Any] = ...,
        use_memcache: Optional[Any] = ...,
        memcache_timeout: Optional[Any] = ...,
        max_memcache_items: Optional[Any] = ...,
        force_writes: Optional[Any] = ...,
        _options: Optional[Any] = ...,
    ): ...
    def delete_async(
        self,
        retries: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        deadline: Optional[Any] = ...,
        use_cache: Optional[Any] = ...,
        use_global_cache: Optional[Any] = ...,
        use_datastore: Optional[Any] = ...,
        global_cache_timeout: Optional[Any] = ...,
        use_memcache: Optional[Any] = ...,
        memcache_timeout: Optional[Any] = ...,
        max_memcache_items: Optional[Any] = ...,
        force_writes: Optional[Any] = ...,
        _options: Optional[Any] = ...,
    ): ...
    @classmethod
    def from_old_key(cls, old_key: Any) -> None: ...
    def to_old_key(self) -> None: ...
