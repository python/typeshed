from typing import Any, Dict, Iterable, Iterator, TypeVar

from .utils import Comparable

_T = TypeVar("_T")

class tqdm(Comparable):
    monitor_interval: float
    @staticmethod
    def format_sizeof(num: float, suffix: str = ..., divisor: float = ...) -> str: ...
    @staticmethod
    def format_interval(t: float) -> str: ...
    @staticmethod
    def format_num(n: float) -> str: ...
    @staticmethod
    def format_meter(
        n: float,
        total: float | None,
        elapsed: float,
        ncols: int | None = ...,
        prefix: str = ...,
        ascii: bool | str = ...,
        unit: str = ...,
        unit_scale: bool | float = ...,
        rate: float | None = ...,
        bar_format: str | None = ...,
        postfix: Any | None = ...,
        unit_divisor: float = ...,
        initial: float = ...,
        colour: str | None = ...,
        **extra_kwargs: Any,
    ) -> str: ...
    @classmethod
    def write(cls, s: str, file: Any | None = ..., end: str = ..., nolock: bool = ...) -> None: ...
    @classmethod
    def external_write_mode(cls, file: Any | None = ..., nolock: bool = ...) -> None: ...
    @classmethod
    def set_lock(cls, lock: Any) -> None: ...
    @classmethod
    def get_lock(cls) -> Any: ...
    iterable: Iterable[_T]
    disable: bool | None
    pos: int
    n: float
    total: float | None
    leave: bool | None
    desc: str
    fp: Any
    ncols: int
    nrows: int
    mininterval: float
    maxinterval: float
    miniters: float
    dynamic_miniters: Any
    ascii: bool | str
    unit: str
    unit_scale: bool | float
    unit_divisor: float
    initial: float
    lock_args: Any
    delay: float
    gui: bool
    dynamic_ncols: Any
    smoothing: float
    bar_format: str | None
    postfix: Any | None
    colour: str | None
    last_print_n: float
    sp: Any
    last_print_t: float
    start_t: float
    def __init__(
        self,
        iterable: Iterable[_T] | None = ...,
        desc: str | None = ...,
        total: float | None = ...,
        leave: bool | None = ...,
        file: Any | None = ...,
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
        postfix: Any | None = ...,
        unit_divisor: float = ...,
        write_bytes: bool | None = ...,
        lock_args: Any | None = ...,
        nrows: int | None = ...,
        colour: str | None = ...,
        delay: float = ...,
        gui: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __len__(self) -> int | None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...
    def __hash__(self): ...
    def __iter__(self): ...
    def update(self, n: float = ...): ...
    def close(self) -> None: ...
    def clear(self, nolock: bool = ...) -> None: ...
    def refresh(self, nolock: bool = ..., lock_args: Any | None = ...) -> bool: ...
    def unpause(self) -> None: ...
    def reset(self, total: float | None = ...) -> None: ...
    def set_description(self, desc: str | None = ..., refresh: bool = ...) -> None: ...
    def set_description_str(self, desc: str | None = ..., refresh: bool = ...) -> None: ...
    def set_postfix(self, ordered_dict: Any | None = ..., refresh: bool = ..., **kwargs: Any) -> None: ...
    def set_postfix_str(self, s: str = ..., refresh: bool = ...) -> None: ...
    def moveto(self, n: int) -> None: ...
    @property
    def format_dict(self) -> Dict[str, Any]: ...
    def display(self, msg: str | None = ..., pos: int | None = ...): ...
    @classmethod
    def wrapattr(cls, stream: Any, method: str, total: float | None = ..., bytes: bool = ..., **tqdm_kwargs: Any) -> object: ...

def trange(*args: Any, **kwargs: Any) -> Iterator[int]: ...
