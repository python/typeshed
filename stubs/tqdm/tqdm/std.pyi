import io
from _typeshed import Incomplete
from collections.abc import Iterable, Iterator, Mapping
from contextlib import AbstractContextManager
from typing import Generic, TypeVar, overload
from typing_extensions import Literal

class TqdmTypeError(TypeError): ...
class TqdmKeyError(KeyError): ...

class TqdmWarning(Warning):
    def __init__(self, msg, fp_write: Incomplete | None = ..., *a, **k) -> None: ...

class TqdmExperimentalWarning(TqdmWarning, FutureWarning): ...
class TqdmDeprecationWarning(TqdmWarning, DeprecationWarning): ...
class TqdmMonitorWarning(TqdmWarning, RuntimeWarning): ...

_T = TypeVar("_T")

class tqdm(Generic[_T], Iterable[_T], AbstractContextManager[tqdm[None]]):
    monitor_interval: int

    @staticmethod
    def format_sizeof(num: float, suffix: str = ..., divisor: int = ...) -> str: ...
    @staticmethod
    def format_interval(t: int) -> str: ...
    @staticmethod
    def format_num(n: int) -> str: ...
    @staticmethod
    def status_printer(file: io.TextIOWrapper | io.StringIO | None): ...
    # def status_printer(file: io.TextIOWrapper | io.StringIO | None, total: int | None = ..., desc: str | None = ..., ncols: int | None = ...): ...
    @staticmethod
    def format_meter(
        n: float,
        total: float,
        elapsed: float,
        ncols: int | None = ...,
        prefix: str | None = ...,
        ascii: bool | str | None = ...,
        unit: str | None = ...,
        unit_scale: bool | float | None = ...,
        rate: float | None = ...,
        bar_format: str | None = ...,
        postfix: str | Mapping[object, object] | None = ...,
        unit_divisor: float | None = ...,
        initial: float | None = ...,
        colour: str | None = ...,
    ) -> str: ...
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
        gui: bool = ...,
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
        gui: bool = ...,
    ) -> None: ...
    def __new__(cls, *_, **__): ...
    @classmethod
    def write(cls, s: str, file: io.TextIOWrapper | io.StringIO | None = ..., end: str = ..., nolock: bool = ...) -> None: ...
    @classmethod
    def external_write_mode(
        cls, file: io.TextIOWrapper | io.StringIO | None = ..., nolock: bool = ...
    ) -> AbstractContextManager[None]: ...
    @classmethod
    def set_lock(cls, lock) -> None: ...
    @classmethod
    def get_lock(cls): ...
    @classmethod
    def pandas(
        cls,
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
        postfix: Mapping[object, object] | str | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float | None = ...,
    ): ...

    iterable: Incomplete
    disable: Incomplete
    pos: Incomplete
    n: Incomplete
    total: Incomplete
    leave: Incomplete
    desc: Incomplete
    fp: Incomplete
    ncols: Incomplete
    nrows: Incomplete
    mininterval: Incomplete
    maxinterval: Incomplete
    miniters: Incomplete
    dynamic_miniters: Incomplete
    ascii: Incomplete
    unit: Incomplete
    unit_scale: Incomplete
    unit_divisor: Incomplete
    initial: Incomplete
    lock_args: Incomplete
    delay: Incomplete
    gui: Incomplete
    dynamic_ncols: Incomplete
    smoothing: Incomplete
    bar_format: Incomplete
    postfix: Incomplete
    colour: Incomplete
    last_print_n: Incomplete
    sp: Incomplete
    last_print_t: Incomplete
    start_t: Incomplete

    def __bool__(self): ...
    def __nonzero__(self): ...
    def __len__(self): ...
    def __reversed__(self): ...
    def __contains__(self, item) -> bool: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __del__(self) -> None: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def update(self, n: float | None = ...) -> bool | None: ...
    def close(self) -> None: ...
    def clear(self, nolock: bool = ...) -> None: ...
    def refresh(
        self, nolock: bool = ..., lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...
    ) -> None: ...
    def unpause(self) -> None: ...
    def reset(self, total: float | None = ...) -> None: ...
    def set_description(self, desc: str | None = ..., refresh: bool | None = ...) -> None: ...
    def set_description_str(self, desc: str | None = ..., refresh: bool | None = ...) -> None: ...
    def set_postfix(self, ordered_dict: Mapping[object, object] | None = ..., refresh: bool | None = ..., **kwargs) -> None: ...
    def set_postfix_str(self, s: str = ..., refresh: bool = ...) -> None: ...
    def moveto(self, n) -> None: ...
    @property
    def format_dict(self): ...
    def display(self, msg: str | None = ..., pos: int | None = ...) -> None: ...
    @classmethod
    def wrapattr(
        cls, stream, method: Literal["read", "write"], total: float | None = ..., bytes: bool | None = ..., **tqdm_kwargs
    ) -> AbstractContextManager[Incomplete]: ...

@overload
def trange(
    start: int,
    stop: int,
    step: int | None = ...,
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
    postfix: Mapping[object, object] | str | None = ...,
    unit_divisor: float = ...,
    write_bytes: bool | None = ...,
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
    nrows: int | None = ...,
    colour: str | None = ...,
    delay: float | None = ...,
) -> tqdm[int]: ...
@overload
def trange(
    stop: int,
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
    postfix: Mapping[object, object] | str | None = ...,
    unit_divisor: float = ...,
    write_bytes: bool | None = ...,
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None = ...,
    nrows: int | None = ...,
    colour: str | None = ...,
    delay: float | None = ...,
) -> tqdm[int]: ...
