from _typeshed import Incomplete
from asyncio import AbstractEventLoop
from collections.abc import Generator, Iterable
from tempfile import TemporaryDirectory, _BytesMode
from types import coroutine as coroutine
from typing import TypeVar

from aiofiles.base import AsyncBase as AsyncBase
from aiofiles.threadpool.utils import (
    cond_delegate_to_executor as cond_delegate_to_executor,
    delegate_to_executor as delegate_to_executor,
    proxy_property_directly as proxy_property_directly,
)

_T = TypeVar("_T")

class AsyncSpooledTemporaryFile(AsyncBase[_T]):
    def fileno(self) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    def rollover(self) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    async def close(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    # All must return `AnyStr`:
    async def read(self, __n: int = ...) -> Incomplete: ...
    async def readline(self, __limit: int | None = ...) -> Incomplete: ...
    async def readlines(self, __hint: int = ...) -> list[Incomplete]: ...
    # ---
    async def seek(self, offset: int, whence: int = ...) -> int: ...
    async def tell(self) -> int: ...
    async def truncate(self, size: int | None = ...) -> None: ...
    @property
    def closed(self) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def mode(self) -> _BytesMode: ...
    @property
    def name(self) -> str: ...
    @property
    def newlines(self) -> str: ...
    @property
    def softspace(self) -> bool: ...
    # Both should work with `AnyStr`, like in `tempfile`:
    async def write(self, s: Incomplete) -> int: ...
    async def writelines(self, iterable: Iterable[Incomplete]) -> None: ...

class AsyncTemporaryDirectory:
    async def cleanup(self) -> None: ...
    @property
    def name(self) -> Incomplete: ...  # should be `AnyStr`
    def __init__(
        self, file: TemporaryDirectory[Incomplete], loop: AbstractEventLoop | None, executor: Incomplete | None
    ) -> None: ...
    async def close(self) -> None: ...
