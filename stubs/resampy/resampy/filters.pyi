from collections.abc import Callable
from typing import Any

import numpy as np

__all__ = ["get_filter", "clear_cache", "sinc_window"]

# Dictionary to cache loaded filters
FILTER_CACHE: dict[str, tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]]

# List of filter functions available
FILTER_FUNCTIONS: list[str]

def sinc_window(
    num_zeros: int = 64,
    precision: int = 9,
    window: Callable[..., np.ndarray[tuple[int, ...], np.dtype[np.floating]]] | None = None,
    rolloff: float = 0.945,
) -> tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]: ...
def get_filter(
    name_or_function: str | Callable[..., tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]],
    **kwargs,
) -> tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]: ...
def load_filter(filter_name: str) -> tuple[np.ndarray[tuple[int, ...], np.dtype[np.floating]], int, float]: ...
def clear_cache() -> None: ...
