import io
from _typeshed import Incomplete
from collections.abc import Iterable, AsyncIterator, Mapping
from typing import Awaitable, Generic, TypeVar, overload

from .std import tqdm as std_tqdm

_T = TypeVar("_T")


class tqdm_asyncio(Generic[_T], std_tqdm[_T]):
    iterable_awaitable: bool
    iterable_next: Incomplete
    iterable_iterator: Incomplete

    def __aiter__(self) -> AsyncIterator[_T]: ...

    async def __anext__(self) -> Awaitable[_T]: ...

    def send(self, *args, **kwargs): ...

    @classmethod
    def as_completed(
        cls, fs: Iterable[Awaitable], *,
        loop: bool | None = ...,
        timeout: float | None = ...,
        total: int | None = ...,
        desc: str | None = ...,
        leave: bool = ...,
        file: io.TextIOWrapper | io.StringIO | None = ...,
        ncols: int | None = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: float | None = ...,
        ascii: bool | str | None = ...,
        disable: bool = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str | None = ...,
        initial: float = ...,
        position: int | None = ...,
        postfix: Mapping | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
        gui: bool = ...,

    ) -> None: ...

    @classmethod
    async def gather(
        cls, *fs: Awaitable, loop: bool | None = ...,
        timeout: float | None = ...,
        total: int | None = ...,
        iterable: Iterable[_T] = ...,
        desc: str | None = ...,
        leave: bool = ...,
        file: io.TextIOWrapper | io.StringIO | None = ...,
        ncols: int | None = ...,
        mininterval: float = ...,
        maxinterval: float = ...,
        miniters: float | None = ...,
        ascii: bool | str | None = ...,
        disable: bool = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        dynamic_ncols: bool = ...,
        smoothing: float = ...,
        bar_format: str | None = ...,
        initial: float = ...,
        position: int | None = ...,
        postfix: Mapping | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
        gui: bool = ...,
    ): ...


@overload
def tarange(start: int, stop: int, step: int | None = ...,
            *,
            desc: str | None = ...,
            total: float | None = ...,
            leave: bool = ...,
            file: io.TextIOWrapper | io.StringIO | None = ...,
            ncols: int | None = ...,
            mininterval: float = ...,
            maxinterval: float = ...,
            miniters: float | None = ...,
            ascii: bool | str | None = ...,
            disable: bool = ...,
            unit: str = ...,
            unit_scale: bool | float = ...,
            dynamic_ncols: bool = ...,
            smoothing: float = ...,
            bar_format: str | None = ...,
            initial: float = ...,
            position: int | None = ...,
            postfix: Mapping | str | None = ...,
            unit_divisor: float = ...,
            write_bytes: bool | None = ...,
            lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
            nrows: int | None = ...,
            colour: str | None = ...,
            delay: float | None = ...,
            gui: bool = ...) -> tqdm_asyncio[int]: ...


@overload
def tarange(stop: int,
            *,
            desc: str | None = ...,
            total: float | None = ...,
            leave: bool = ...,
            file: io.TextIOWrapper | io.StringIO | None = ...,
            ncols: int | None = ...,
            mininterval: float = ...,
            maxinterval: float = ...,
            miniters: float | None = ...,
            ascii: bool | str | None = ...,
            disable: bool = ...,
            unit: str = ...,
            unit_scale: bool | float = ...,
            dynamic_ncols: bool = ...,
            smoothing: float = ...,
            bar_format: str | None = ...,
            initial: float = ...,
            position: int | None = ...,
            postfix: Mapping | str | None = ...,
            unit_divisor: float = ...,
            write_bytes: bool | None = ...,
            lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
            nrows: int | None = ...,
            colour: str | None = ...,
            delay: float | None = ...,
            gui: bool = ...) -> tqdm_asyncio[int]: ...


tqdm = tqdm_asyncio
trange = tarange
