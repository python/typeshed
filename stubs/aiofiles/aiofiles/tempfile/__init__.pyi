from _typeshed import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    StrOrBytesPath,
)
from asyncio import AbstractEventLoop
from typing import Any, AnyStr, TypeVar, overload
from typing_extensions import Literal

from ..base import AiofilesContextManager
from ..threadpool.binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO
from ..threadpool.text import AsyncTextIOWrapper

_T_co = TypeVar("_T_co", covariant=True)
_V_co = TypeVar("_V_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

# Text mode: always returns AsyncTextIOWrapper
@overload
def NamedTemporaryFile(
    mode: OpenTextMode,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: returns a FileIO
@overload
def NamedTemporaryFile(
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def NamedTemporaryFile(
    mode: OpenBinaryModeReading | OpenBinaryModeUpdating = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def NamedTemporaryFile(
    mode: OpenBinaryModeWriting = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...

# Text mode: always returns AsyncTextIOWrapper
@overload
def TemporaryFile(
    mode: OpenTextMode,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: returns a FileIO
@overload
def TemporaryFile(
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def TemporaryFile(
    mode: OpenBinaryModeReading | OpenBinaryModeUpdating = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def TemporaryFile(
    mode: OpenBinaryModeWriting = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...

# Text mode: always returns AsyncTextIOWrapper
@overload
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: OpenTextMode = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: returns a FileIO
@overload
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: OpenBinaryMode = ...,
    buffering: Literal[0] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: OpenBinaryModeReading | OpenBinaryModeUpdating = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: OpenBinaryModeWriting = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    newline: None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...
def TemporaryDirectory(
    suffix: StrOrBytesPath | None = ...,
    prefix: StrOrBytesPath | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> StrOrBytesPath: ...

class AiofilesContextManagerTempDir(AiofilesContextManager[_T_co, _T_contra, _V_co]):
    async def __aenter__(self): ...
