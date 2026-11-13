from _typeshed import FloatInt
from dataclasses import dataclass

from seaborn._stats.base import Stat
from seaborn.external.kde import _BwMethodType

@dataclass
class KDE(Stat):
    bw_adjust: FloatInt = 1
    bw_method: _BwMethodType = "scott"
    common_norm: bool | list[str] = True
    common_grid: bool | list[str] = True
    gridsize: int | None = 200
    cut: FloatInt = 3
    cumulative: bool = False
    def __post_init__(self) -> None: ...
