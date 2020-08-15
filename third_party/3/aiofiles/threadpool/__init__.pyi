from _typeshed import OpenBinaryMode, OpenBinaryModeReading, OpenBinaryModeUpdating, OpenBinaryModeWriting, OpenTextMode
from os import PathLike
from typing import Any, Callable, Optional, Union, overload
from typing_extensions import Literal

from .binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO
from .text import AsyncTextIOWrapper

_AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
_OpenFile = Union[_AnyPath, int]
_Opener = Callable[[str, int], int]
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
    loop: Optional[Any] = ...,
    executor: Optional[Any] = ...,
) -> AsyncTextIOWrapper: ...
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
    loop: Optional[Any] = ...,
    executor: Optional[Any] = ...,
) -> AsyncFileIO: ...
@overload
def open(
    file: _OpenFile,
    mode: OpenBinaryModeWriting,
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[Any] = ...,
    executor: Optional[Any] = ...,
) -> AsyncBufferedIOBase: ...
@overload
def open(
    file: _OpenFile,
    mode: Union[OpenBinaryModeReading, OpenBinaryModeUpdating],
    buffering: Literal[-1, 1] = ...,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[Any] = ...,
    executor: Optional[Any] = ...,
) -> AsyncBufferedReader: ...
@overload
def open(
    file: _OpenFile,
    mode: OpenBinaryMode,
    buffering: int,
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
    *,
    loop: Optional[Any] = ...,
    executor: Optional[Any] = ...,
) -> AsyncFileIO: ...
