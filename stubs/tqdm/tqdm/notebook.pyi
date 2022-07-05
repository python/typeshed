import io
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from typing import Generic, TypeVar, overload

from .std import tqdm as std_tqdm

_T = TypeVar("_T")

class tqdm_notebook(Generic[_T], std_tqdm[_T]):
    @staticmethod
    def status_printer(_, total: float | None = ..., desc: str | None = ..., ncols: int | None = ...): ...
    displayed: bool
    def display(
        self,
        msg: str | None = ...,
        pos: Incomplete | None = ...,
        close: bool = ...,
        bar_style: Incomplete | None = ...,
        check_delay: bool = ...,
    ) -> None: ...
    @property
    def colour(self): ...
    @colour.setter
    def colour(self, bar_color) -> None: ...
    disp: Incomplete
    ncols: Incomplete
    container: Incomplete
    @overload
    def __init__(
        self,
        iterable: Iterable[_T] | None,
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
        postfix: Mapping[object, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
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
        postfix: Mapping[object, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
    ) -> None: ...
    def __iter__(self): ...
    def update(self, n: int = ...): ...  # type: ignore[override]
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def reset(self, total: Incomplete | None = ...): ...

def tnrange(*args, **kwargs): ...

tqdm = tqdm_notebook
trange = tnrange
