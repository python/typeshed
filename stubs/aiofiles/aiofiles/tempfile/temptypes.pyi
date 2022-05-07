from asyncio import AbstractEventLoop
from types import coroutine as coroutine
from typing import Any, TypeVar

from ..base import AsyncBase as AsyncBase
from ..threadpool.utils import (
    cond_delegate_to_executor as cond_delegate_to_executor,
    delegate_to_executor as delegate_to_executor,
    proxy_property_directly as proxy_property_directly,
)

_T = TypeVar("_T")

class AsyncSpooledTemporaryFile(AsyncBase[_T]):
    async def write(self, s): ...
    async def writelines(self, iterable): ...

class AsyncTemporaryDirectory:
    def __init__(self, file, loop: AbstractEventLoop | None, executor: Any | None) -> None: ...
    async def close(self) -> None: ...
