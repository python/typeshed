import collections
from _typeshed import Incomplete

from ijson import compat

class utf8reader_async(compat.utf8reader):
    async def read(self, n): ...

class sendable_deque(collections.deque):
    send: Incomplete

class async_iterable:
    events: Incomplete
    coro: Incomplete
    coro_finished: bool
    f: Incomplete
    buf_size: Incomplete
    read: Incomplete
    def __init__(self, f, buf_size, *coro_pipeline) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
