from os import PathLike, stat_result
import sys
from typing import Optional, Sequence, Union, overload

_AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
_FdOrAnyPath = Union[int, _AnyPath]

async def stat(path: _FdOrAnyPath, *, dir_fd: Optional[int] = ..., follow_symlinks: bool = ...) -> stat_result: ...
async def rename(src: _AnyPath, dst: _AnyPath, *, src_dir_fd: Optional[int] = ..., dst_dir_fd: Optional[int] = ...) -> None: ...
async def remove(path: _AnyPath, *, dir_fd: Optional[int] = ...) -> None: ...
async def mkdir(path: _AnyPath, mode: int = ..., *, dir_fd: Optional[int] = ...) -> None: ...
async def rmdir(path: _AnyPath, *, dir_fd: Optional[int] = ...) -> None: ...

if sys.platform != "win32":
    @overload
    async def sendfile(__out_fd: int, __in_fd: int, offset: Optional[int], count: int) -> int: ...
    @overload
    async def sendfile(
        __out_fd: int,
        __in_fd: int,
        offset: int,
        count: int,
        headers: Sequence[bytes] = ...,
        trailers: Sequence[bytes] = ...,
        flags: int = ...,
    ) -> int: ...
