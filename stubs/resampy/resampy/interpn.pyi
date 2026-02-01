import numpy as np

def _resample_loop(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
) -> None: ...
def resample_f_p(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
) -> None: ...
def resample_f_s(
    x: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    t_out: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_win: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    interp_delta: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
    num_table: int,
    scale: float,
    y: np.ndarray[tuple[int, ...], np.dtype[np.floating]],
) -> None: ...
