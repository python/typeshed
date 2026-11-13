from _typeshed import FloatInt
from collections.abc import Callable
from typing import Any, TypeAlias, TypeVar

import numpy as np

__all__ = ["resample", "resample_nu"]

# np.floating[Any] because precision is not important
_FloatArray = TypeVar("_FloatArray", bound=np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]])
_FilterType: TypeAlias = str | Callable[[int], np.ndarray[tuple[int], np.dtype[np.float64]]]

def resample(
    x: _FloatArray,
    sr_orig: FloatInt,
    sr_new: FloatInt,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> _FloatArray: ...
def resample_nu(
    x: _FloatArray,
    sr_orig: FloatInt,
    t_out: _FloatArray,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> _FloatArray: ...
