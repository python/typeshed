import collections
from _typeshed import SupportsRead
from collections.abc import Callable
from typing import Any, TypeVar

from ijson import compat
from ijson.utils import _CoroPipelineArgs

_T = TypeVar("_T")

class utf8reader_async(compat.utf8reader):
    async def read(self, n: int) -> bytes: ...  # type: ignore[override]

class sendable_deque(collections.deque[_T]):
    # send = collections.deque.append
    def send(self, x: _T, /) -> None: ...

class async_iterable:
    events: sendable_deque[Any]
    coro: list[Any]
    coro_finished: bool
    f: SupportsRead[Any]
    buf_size: int
    read: Callable[[int], bytes] | None
    def __init__(self, f: SupportsRead[Any], buf_size: int, *coro_pipeline: _CoroPipelineArgs) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
