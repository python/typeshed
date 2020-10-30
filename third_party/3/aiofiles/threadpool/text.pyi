from _typeshed import AnyPath
from io import BinaryIO
from typing import Generic, Iterable, List, Optional, Tuple, TypeVar, Union

from ..base import AsyncBase

_FileName = TypeVar("_FileName", AnyPath, int)

class AsyncTextIOWrapper(AsyncBase[str], Generic[_FileName]):
    async def close(self) -> None: ...
    async def flush(self) -> None: ...
    async def isatty(self) -> bool: ...
    async def read(self, __size: int = ...) -> str: ...
    async def readline(self, __size: Optional[int] = ...) -> str: ...
    async def readlines(self, __hint: int = ...) -> List[str]: ...
    async def seek(self, __offset: int, __whence: int = ...) -> int: ...
    async def seekable(self) -> bool: ...
    async def tell(self) -> int: ...
    async def truncate(self, __size: Optional[int] = ...) -> int: ...
    async def writable(self) -> bool: ...
    async def write(self, __b: str) -> Optional[int]: ...
    async def writelines(self, __lines: Iterable[str]) -> None: ...
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
    def errors(self) -> Optional[str]: ...
    @property
    def line_buffering(self) -> bool: ...
    @property
    def newlines(self) -> Union[str, Tuple[str, ...], None]: ...
    @property
    def name(self) -> _FileName: ...
    @property
    def mode(self) -> str: ...
