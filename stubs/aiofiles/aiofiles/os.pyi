import sys
from _typeshed import StrOrBytesPath
from asyncio.events import AbstractEventLoop
from concurrent.futures._base import Executor
from os import stat_result
from typing import Sequence, Union, overload

_FdOrAnyPath = Union[int, StrOrBytesPath]

async def stat(
    path: _FdOrAnyPath,
    *,
    dir_fd: int | None = ...,
    follow_symlinks: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> stat_result: ...
async def rename(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = ...,
    dst_dir_fd: int | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def replace(
    src: StrOrBytesPath,
    dst: StrOrBytesPath,
    *,
    src_dir_fd: int | None = ...,
    dst_dir_fd: int | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def remove(
    path: StrOrBytesPath, *, dir_fd: int | None = ..., loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def mkdir(
    path: StrOrBytesPath,
    mode: int = ...,
    *,
    dir_fd: int | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def makedirs(
    name: StrOrBytesPath,
    mode: int = ...,
    exist_ok: bool = ...,
    *,
    loop: AbstractEventLoop | None = ...,
    executor: Executor | None = ...,
) -> None: ...
async def rmdir(
    path: StrOrBytesPath, *, dir_fd: int | None = ..., loop: AbstractEventLoop | None = ..., executor: Executor | None = ...
) -> None: ...
async def removedirs(name: StrOrBytesPath, *, loop: AbstractEventLoop | None = ..., executor: Executor | None = ...) -> None: ...

if sys.platform != "win32":
    @overload
    async def sendfile(
        out_fd: int,
        in_fd: int,
        offset: int | None,
        count: int,
        *,
        *,
        loop: AbstractEventLoop | None = ...,
        executor: Executor | None = ...,
    ) -> int: ...
    @overload
    async def sendfile(
        out_fd: int,
        in_fd: int,
        offset: int,
        count: int,
        headers: Sequence[bytes] = ...,
        trailers: Sequence[bytes] = ...,
        flags: int = ...,
        *,
        loop: AbstractEventLoop | None = ...,
        executor: Executor | None = ...,
    ) -> int: ...  # FreeBSD and Mac OS X only
