from _typeshed import AnyPath, ReadableBuffer, WriteableBuffer
from io import FileIO
from typing import Generic, Iterable, List, Optional, TypeVar, Union

from ..base import AsyncBase

_FileName = TypeVar("_FileName", bound=Union[AnyPath, int])

class _UnknownAsyncBinaryIO(AsyncBase[bytes], Generic[_FileName]):
    async def close(self) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    async def read(self, __size: int = ...) -> Optional[bytes]: ...
    async def readinto(self, __buffer: WriteableBuffer) -> Optional[int]: ...
    async def readline(self, __size: Optional[int] = ...) -> bytes: ...
    async def readlines(self, __hint: int = ...) -> List[bytes]: ...
    async def seek(self, __offset: int, __whence: int = ...) -> int: ...
    async def seekable(self) -> bool: ...
    async def tell(self) -> int: ...
    async def truncate(self, __size: Optional[int] = ...) -> int: ...
    async def writable(self) -> bool: ...
    async def write(self, __b: ReadableBuffer) -> Optional[int]: ...
    async def writelines(self, __lines: Iterable[ReadableBuffer]) -> None: ...
    def fileno(self) -> int: ...
    def readable(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> _FileName: ...

class AsyncBufferedIOBase(_UnknownAsyncBinaryIO[_FileName]):
    async def read1(self, __size: int = ...) -> bytes: ...
    def detach(self) -> FileIO: ...
    @property
    def raw(self) -> FileIO: ...

class AsyncBufferedReader(AsyncBufferedIOBase[_FileName]):
    async def peek(self, __size: int = ...) -> bytes: ...

class AsyncFileIO(_UnknownAsyncBinaryIO[_FileName]):
    async def readall(self) -> bytes: ...
