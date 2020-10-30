from _typeshed import AnyPath, OpenBinaryMode, OpenBinaryModeReading, OpenBinaryModeUpdating, OpenBinaryModeWriting, OpenTextMode
from asyncio import AbstractEventLoop
from typing import Any, Callable, Literal, Optional, TypeVar, Union, overload

from ..base import AiofilesContextManager
from .binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO
from .text import AsyncTextIOWrapper

_OpenFile = TypeVar("_OpenFile", AnyPath, int)
_Opener = Callable[[str, int], int]

# Text mode: always returns AsyncTextIOWrapper
@overload
def open(
    file: _OpenFile,
    mode: OpenTextMode = ...,
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[AbstractEventLoop] = ...,
    executor: Optional[Any] = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper[_OpenFile]]: ...

# Unbuffered binary: returns a FileIO
@overload
def open(
    file: _OpenFile,
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[AbstractEventLoop] = ...,
    executor: Optional[Any] = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO[_OpenFile]]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def open(
    file: _OpenFile,
    mode: Union[OpenBinaryModeUpdating, OpenBinaryModeReading],
    buffering: int = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[AbstractEventLoop] = ...,
    executor: Optional[Any] = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader[_OpenFile]]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def open(
    file: _OpenFile,
    mode: OpenBinaryModeWriting,
    buffering: int = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[AbstractEventLoop] = ...,
    executor: Optional[Any] = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase[_OpenFile]]: ...
