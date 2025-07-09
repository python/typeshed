from asyncio import BaseEventLoop
from collections.abc import Callable, Coroutine
from concurrent.futures import ThreadPoolExecutor
from typing import Any, TypeVar
from typing_extensions import ParamSpec

from asgiref.sync import SyncToAsync

_P = ParamSpec("_P")
_R = TypeVar("_R")

class DatabaseSyncToAsync(SyncToAsync[_P, _R]):
    def thread_handler(self, loop: BaseEventLoop, *args: Any, **kwargs: Any) -> Any: ...

# We define `database_sync_to_async` as a function instead of assigning
# `DatabaseSyncToAsync(...)` directly, to preserve both decorator and
# higher-order function behavior with correct type hints.
# A direct assignment would result in incorrect type inference for the wrapped function.
def database_sync_to_async(
    func: Callable[_P, _R], thread_sensitive: bool = True, executor: ThreadPoolExecutor | None = None
) -> Callable[_P, Coroutine[Any, Any, _R]]: ...
async def aclose_old_connections() -> None: ...
