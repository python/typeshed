from typing import Any

import numba
import numpy as np
from numba import guvectorize

def _resample_loop(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
) -> None: ...

# JIT-compiled parallel version of _resample_loop
_resample_loop_p = ...

# JIT-compiled sequential version of _resample_loop
_resample_loop_s = ...

@guvectorize(
    (
        numba.float32[:, :, :],
        numba.float32[:, :],
        numba.float32[:],
        numba.float32[:],
        numba.int32,
        numba.float32,
        numba.float32[:, :],
    ),
    "(n),(m),(p),(p),(),()->(m)",
    nopython=True,
)
def resample_f_p(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
) -> None: ...
@guvectorize(
    (
        numba.float32[:, :, :],
        numba.float32[:, :],
        numba.float32[:],
        numba.float32[:],
        numba.int32,
        numba.float32,
        numba.float32[:, :],
    ),
    "(n),(m),(p),(p),(),()->(m)",
    nopython=True,
)
def resample_f_s(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating[Any]]],
) -> None: ...
