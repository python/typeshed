from _typeshed import FloatInt
from _typeshed import Incomplete, SupportsWrite
from collections.abc import Iterable, Iterator, Mapping
from typing import TypeVar, overload
from typing_extensions import Never

from .std import tqdm as std_tqdm, trange as trange

__all__ = ["tqdm_notebook", "tnrange", "tqdm", "trange"]

_T = TypeVar("_T")

class tqdm_notebook(std_tqdm[_T]):
    @staticmethod
    def status_printer(
        _: SupportsWrite[str] | None, total: FloatInt | None = None, desc: str | None = None, ncols: int | None = None
    ): ...
    displayed: bool
    def display(
        self,
        msg: str | None = None,
        pos: int | None = None,
        close: bool = False,
        bar_style: str | None = None,
        check_delay: bool = True,
    ) -> None: ...

    @property
    def colour(self) -> str | None: ...
    @colour.setter
    def colour(self, bar_color: str | None) -> None: ...

    disp: Incomplete
    ncols: Incomplete
    container: Incomplete

    @overload
    def __init__(
        self,
        iterable: Iterable[_T],
        desc: str | None = ...,
        total: FloatInt | None = ...,
        leave: bool | None = ...,
        file: SupportsWrite[str] | None = ...,
        ncols: int | None = ...,
        mininterval: FloatInt = ...,
        maxinterval: FloatInt = ...,
        miniters: FloatInt | None = ...,
        ascii: bool | str | None = ...,
        disable: bool = ...,
        unit: str = ...,
        unit_scale: bool | FloatInt = ...,
        dynamic_ncols: bool = ...,
        smoothing: FloatInt = ...,
        bar_format: str | None = ...,
        initial: FloatInt = ...,
        position: int | None = ...,
        postfix: Mapping[str, object] | str | None = ...,
        unit_divisor: FloatInt = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, FloatInt | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: FloatInt | None = ...,
        display: bool = ...,
        **kwargs,
    ) -> None: ...
    @overload
    def __init__(
        self: tqdm_notebook[Never],
        iterable: None = None,
        desc: str | None = ...,
        total: FloatInt | None = ...,
        leave: bool | None = ...,
        file: SupportsWrite[str] | None = ...,
        ncols: int | None = ...,
        mininterval: FloatInt = ...,
        maxinterval: FloatInt = ...,
        miniters: FloatInt | None = ...,
        ascii: bool | str | None = ...,
        disable: bool = ...,
        unit: str = ...,
        unit_scale: bool | FloatInt = ...,
        dynamic_ncols: bool = ...,
        smoothing: FloatInt = ...,
        bar_format: str | None = ...,
        initial: FloatInt = ...,
        position: int | None = ...,
        postfix: Mapping[str, object] | str | None = ...,
        unit_divisor: FloatInt = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, FloatInt | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: FloatInt | None = ...,
        display: bool = ...,
        **kwargs,
    ) -> None: ...

    def __iter__(self) -> Iterator[_T]: ...
    def update(self, n: int = 1): ...  # type: ignore[override]
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def reset(self, total: FloatInt | None = None): ...

tqdm = tqdm_notebook
tnrange = trange
