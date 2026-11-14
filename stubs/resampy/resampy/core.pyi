from _typeshed import FloatInt
from collections.abc import Callable
from typing import Any, TypeAlias, TypeVar, overload

import numpy as np

__all__ = ["resample", "resample_nu"]

# np.floating[Any] because precision is not important
_Floating = TypeVar("_Floating", bound=np.floating[Any])
_Shape = TypeVar("_Shape", bound=tuple[int, ...])
_FilterType: TypeAlias = str | Callable[[int], np.ndarray[tuple[int], np.dtype[np.float64]]]

@overload
def resample(
    x: np.ndarray[_Shape, np.dtype[np.integer]],
    sr_orig: FloatInt,
    sr_new: FloatInt,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]]: ...
@overload
def resample(
    x: np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: FloatInt,
    sr_new: FloatInt,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> np.ndarray[_Shape, np.dtype[_Floating]]: ...

@overload
def resample_nu(
    x: np.ndarray[_Shape, np.dtype[np.integer]],
    sr_orig: FloatInt,
    t_out: np.ndarray[_Shape, np.dtype[np.float32]],
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]]: ...
@overload
def resample_nu(
    x: np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: FloatInt,
    t_out: np.ndarray[_Shape, np.dtype[_Floating]],
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: FloatInt = 0.945,
) -> np.ndarray[_Shape, np.dtype[_Floating]]: ...
