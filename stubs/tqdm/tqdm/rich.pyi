from _typeshed import Incomplete
from typing import Any, Generic, TypeVar
from typing_extensions import TypeAlias

from .std import tqdm as std_tqdm

_ProgressColumn: TypeAlias = Any  # Actually rich.progress.ProgressColumn

class FractionColumn(_ProgressColumn):
    unit_scale: bool
    unit_divisor: int

    def __init__(self, unit_scale: bool = ..., unit_divisor: int = ...) -> None: ...
    def render(self, task): ...

class RateColumn(_ProgressColumn):
    unit: str
    unit_scale: bool
    unit_divisor: int

    def __init__(self, unit: str = ..., unit_scale: bool = ..., unit_divisor: int = ...) -> None: ...
    def render(self, task): ...

_T = TypeVar("_T")

class tqdm_rich(Generic[_T], std_tqdm[_T]):
    def __init__(self, *args, **kwargs) -> None: ...
    def close(self) -> None: ...
    def clear(self, *_, **__) -> None: ...
    def display(self, *_, **__) -> None: ...
    def reset(self, total: Incomplete | None = ...) -> None: ...

def trrange(*args, **kwargs): ...

tqdm = tqdm_rich
trange = trrange
