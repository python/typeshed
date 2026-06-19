from collections.abc import Callable
from typing import Any, TypeAlias, TypeVar, overload

import numpy as np

__all__ = ["resample", "resample_nu"]

_Floating = TypeVar("_Floating", bound=np.floating[Any])
_Shape = TypeVar("_Shape", bound=tuple[int, ...])
_FilterType: TypeAlias = str | Callable[[int], np.ndarray[tuple[int], np.dtype[np.float64]]]

@overload
def resample(
    x: np.ndarray[_Shape, np.dtype[np.integer[Any]]],
    sr_orig: float,
    sr_new: float,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]]: ...
@overload
def resample(
    x: np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: float,
    sr_new: float,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[_Floating]]: ...
@overload
def resample(
    x: np.ndarray[_Shape, np.dtype[np.integer[Any]]] | np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: float,
    sr_new: float,
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]] | np.ndarray[_Shape, np.dtype[_Floating]]: ...

@overload
def resample_nu(
    x: np.ndarray[_Shape, np.dtype[np.integer[Any]]],
    sr_orig: float,
    t_out: np.ndarray[_Shape, np.dtype[np.float32]],
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]]: ...
@overload
def resample_nu(
    x: np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: float,
    t_out: np.ndarray[_Shape, np.dtype[_Floating]],
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[_Floating]]: ...
@overload
def resample_nu(
    x: np.ndarray[_Shape, np.dtype[np.integer[Any]]] | np.ndarray[_Shape, np.dtype[_Floating]],
    sr_orig: float,
    t_out: np.ndarray[_Shape, np.dtype[np.float32]] | np.ndarray[_Shape, np.dtype[_Floating]],
    axis: int = -1,
    filter: _FilterType = "kaiser_best",
    parallel: bool = False,
    *,
    num_zeros: int = 64,
    precision: int = 9,
    rolloff: float = 0.945,
) -> np.ndarray[_Shape, np.dtype[np.float32]] | np.ndarray[_Shape, np.dtype[_Floating]]: ...
