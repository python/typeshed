from _typeshed import SupportsWrite
from asyncio import Future
from collections.abc import AsyncIterator, Awaitable, Callable, Iterable, Iterator, Mapping
from typing import Generic, Literal, TypedDict, TypeVar, overload, type_check_only
from typing_extensions import Never, Self, Unpack

from .std import tqdm as std_tqdm

__all__ = ["tqdm_asyncio", "tarange", "tqdm", "trange"]

_T = TypeVar("_T")
_ResultT = TypeVar("_ResultT")

@type_check_only
class _GatherKwargs(TypedDict, Generic[_ResultT], total=False):
    iterable: Iterable[_ResultT]
    desc: str | None
    leave: bool | None
    file: SupportsWrite[str] | None
    ncols: int | None
    mininterval: float
    maxinterval: float
    miniters: float | None
    ascii: bool | str | None
    disable: bool | None
    unit: str
    unit_scale: bool | float
    dynamic_ncols: bool
    smoothing: float
    bar_format: str | None
    initial: float
    position: int | None
    postfix: Mapping[str, object] | str | None
    unit_divisor: float
    write_bytes: bool | None
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None
    nrows: int | None
    colour: str | None
    delay: float | None

class tqdm_asyncio(std_tqdm[_T]):
    iterable_awaitable: bool
    iterable_next: Callable[[], _T | Awaitable[_T]]
    iterable_iterator: Iterator[_T]

    def __aiter__(self) -> Self: ...
    async def __anext__(self) -> _T: ...
    def send(self, *args, **kwargs): ...
    @classmethod
    def as_completed(
        cls,
        fs: Iterable[Awaitable[_T]],
        *,
        loop: bool | None = None,
        timeout: float | None = None,
        total: int | None = None,
        desc: str | None = ...,
        leave: bool | None = ...,
        file: SupportsWrite[str] | None = ...,
        ncols: int | None = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: float | None = ...,
        ascii: bool | str | None = ...,
        disable: bool | None = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str | None = ...,
        initial: float = ...,
        position: int | None = ...,
        postfix: Mapping[str, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
    ) -> Iterator[Future[_T]]: ...

    @overload
    @classmethod
    async def gather(
        cls,
        *fs: Awaitable[_ResultT],
        loop: bool | None = None,
        timeout: float | None = None,
        total: int | None = None,
        return_exceptions: Literal[False] = False,
        **tqdm_kwargs: Unpack[_GatherKwargs[_ResultT]],
    ) -> list[_ResultT]: ...
    @overload
    @classmethod
    async def gather(
        cls,
        *fs: Awaitable[_ResultT],
        loop: bool | None = None,
        timeout: float | None = None,
        total: int | None = None,
        return_exceptions: Literal[True],
        **tqdm_kwargs: Unpack[_GatherKwargs[_ResultT]],
    ) -> list[_ResultT | Exception]: ...
    @overload
    @classmethod
    async def gather(
        cls,
        *fs: Awaitable[_ResultT],
        loop: bool | None = None,
        timeout: float | None = None,
        total: int | None = None,
        return_exceptions: bool,
        **tqdm_kwargs: Unpack[_GatherKwargs[_ResultT]],
    ) -> list[_ResultT] | list[_ResultT | Exception]: ...

    @overload
    def __init__(
        self,
        iterable: Iterable[_T] | AsyncIterator[_T],
        desc: str | None = ...,
        total: float | None = ...,
        leave: bool | None = ...,
        file: SupportsWrite[str] | None = ...,
        ncols: int | None = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: float | None = ...,
        ascii: bool | str | None = ...,
        disable: bool | None = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str | None = ...,
        initial: float = ...,
        position: int | None = ...,
        postfix: Mapping[str, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
        gui: bool = ...,
        **kwargs,
    ) -> None: ...
    @overload
    def __init__(
        self: tqdm_asyncio[Never],
        iterable: None = None,
        desc: str | None = ...,
        total: float | None = ...,
        leave: bool | None = ...,
        file: SupportsWrite[str] | None = ...,
        ncols: int | None = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: float | None = ...,
        ascii: bool | str | None = ...,
        disable: bool | None = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str | None = ...,
        initial: float = ...,
        position: int | None = ...,
        postfix: Mapping[str, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
        gui: bool = ...,
        **kwargs,
    ) -> None: ...

@overload
def tarange(
    start: int,
    stop: int,
    step: int | None = ...,
    *,
    desc: str | None = ...,
    total: float | None = ...,
    leave: bool | None = ...,
    file: SupportsWrite[str] | None = ...,
    ncols: int | None = ...,
    mininterval: float = ...,
    maxinterval: float = ...,
    miniters: float | None = ...,
    ascii: bool | str | None = ...,
    disable: bool | None = ...,
    unit: str = ...,
    unit_scale: bool | float = ...,
    dynamic_ncols: bool = ...,
    smoothing: float = ...,
    bar_format: str | None = ...,
    initial: float = ...,
    position: int | None = ...,
    postfix: Mapping[str, object] | str | None = ...,
    unit_divisor: float = ...,
    write_bytes: bool | None = ...,
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
    nrows: int | None = ...,
    colour: str | None = ...,
    delay: float | None = ...,
) -> tqdm_asyncio[int]: ...
@overload
def tarange(
    stop: int,
    *,
    desc: str | None = ...,
    total: float | None = ...,
    leave: bool | None = ...,
    file: SupportsWrite[str] | None = ...,
    ncols: int | None = ...,
    mininterval: float = ...,
    maxinterval: float = ...,
    miniters: float | None = ...,
    ascii: bool | str | None = ...,
    disable: bool | None = ...,
    unit: str = ...,
    unit_scale: bool | float = ...,
    dynamic_ncols: bool = ...,
    smoothing: float = ...,
    bar_format: str | None = ...,
    initial: float = ...,
    position: int | None = ...,
    postfix: Mapping[str, object] | str | None = ...,
    unit_divisor: float = ...,
    write_bytes: bool | None = ...,
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
    nrows: int | None = ...,
    colour: str | None = ...,
    delay: float | None = ...,
) -> tqdm_asyncio[int]: ...

tqdm = tqdm_asyncio
trange = tarange
