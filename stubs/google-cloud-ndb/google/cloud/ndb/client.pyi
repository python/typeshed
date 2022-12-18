from _typeshed import Incomplete
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Callable, ClassVar

from google.cloud.ndb import context
from google.cloud.ndb import key

DATASTORE_API_HOST: str

class Client:
    SCOPE: ClassVar[tuple[str, ...]]
    namespace: str | None
    host: str
    client_info: Incomplete
    secure: bool
    stub: Incomplete
    def __init__(
        self,
        project: str | None = ...,
        namespace: str | None = ...,
        credentials: Incomplete | None = ...,
        client_options: Incomplete | None = ...,
    ) -> None: ...
    @contextmanager
    def context(
        self,
        namespace=...,
        cache_policy: Callable[[key.Key], bool] | None = ...,
        global_cache: Incomplete | None = ...,
        global_cache_policy: Callable[[key.Key], bool] | None = ...,
        global_cache_timeout_policy: Callable[[key.Key], int] | None = ...,
        legacy_data: bool = ...,
    ) -> Iterator[context.Context]: ...
