from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias, TypeVar

import numpy as np

__all__ = ["resample", "resample_nu"]

_FloatArray = TypeVar("_FloatArray", bound=np.ndarray[tuple[int, ...], np.dtype[np.floating]])
_FilterType: TypeAlias = str | Callable[..., tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]]

def resample(
    x: _FloatArray,
    sr_orig: float,
    sr_new: float,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    **kwargs: Any,
) -> _FloatArray: ...
def resample_nu(
    x: _FloatArray,
    sr_orig: float,
    t_out: _FloatArray,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    **kwargs: Any,
) -> _FloatArray: ...
