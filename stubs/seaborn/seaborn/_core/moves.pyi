from _typeshed import FloatInt, Incomplete
from collections.abc import Callable
from dataclasses import dataclass
from typing import ClassVar

from pandas import DataFrame
from seaborn._core.groupby import GroupBy
from seaborn._core.scales import Scale
from seaborn._core.typing import Default

default: Default

@dataclass
class Move:
    group_by_orient: ClassVar[bool]
    def __call__(self, data: DataFrame, groupby: GroupBy, orient: str, scales: dict[str, Scale]) -> DataFrame: ...

@dataclass
class Jitter(Move):
    width: FloatInt | Default = ...
    x: FloatInt = 0
    y: FloatInt = 0
    seed: int | None = None

@dataclass
class Dodge(Move):
    empty: str = "keep"
    gap: FloatInt = 0
    by: list[str] | None = None

@dataclass
class Stack(Move): ...

@dataclass
class Shift(Move):
    x: FloatInt = 0
    y: FloatInt = 0

@dataclass
class Norm(Move):
    func: Callable[..., Incomplete] | str = "max"
    where: str | None = None
    by: list[str] | None = None
    percent: bool = False
