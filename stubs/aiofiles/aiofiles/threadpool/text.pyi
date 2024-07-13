from _typeshed import FileDescriptorOrPath
from collections.abc import Iterable
from typing import BinaryIO, Literal

from ..base import AsyncBase, AsyncIndirectBase

class _UnknownAsyncTextIO(AsyncBase[str]):
    async def close(self) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    async def read(self, size: int | None = ..., /) -> str: ...
    async def readline(self, size: int = ..., /) -> str: ...
    async def readlines(self, hint: int = ..., /) -> list[str]: ...
    async def seek(self, offset: int, whence: Literal[0, 1, 2] = ..., /) -> int: ...
    async def seekable(self) -> bool: ...
    async def tell(self) -> int: ...
    async def truncate(self, size: int | None = ..., /) -> int: ...
    async def writable(self) -> bool: ...
    async def write(self, b: str, /) -> int: ...
    async def writelines(self, lines: Iterable[str], /) -> None: ...
    def detach(self) -> BinaryIO: ...
    def fileno(self) -> int: ...
    def readable(self) -> bool: ...
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def closed(self) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def errors(self) -> str | None: ...
    @property
    def line_buffering(self) -> bool: ...
    @property
    def newlines(self) -> str | tuple[str, ...] | None: ...
    @property
    def name(self) -> FileDescriptorOrPath: ...
    @property
    def mode(self) -> str: ...

class AsyncTextIOWrapper(_UnknownAsyncTextIO): ...
class AsyncTextIndirectIOWrapper(AsyncIndirectBase[str], _UnknownAsyncTextIO): ...
