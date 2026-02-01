from collections.abc import Callable
from typing import TypedDict, type_check_only
from typing_extensions import TypeAlias, Unpack

import numpy as np

__all__ = ["get_filter", "clear_cache", "sinc_window"]

# Dictionary to cache loaded filters
FILTER_CACHE: dict[str, tuple[np.ndarray[tuple[int], np.dtype[np.float64]], int, float]]

# List of filter functions available
FILTER_FUNCTIONS: list[str]

_FilterType: TypeAlias = str | Callable[[int], np.ndarray[tuple[int], np.dtype[np.float64]]]

@type_check_only
class _FilterKwArgs(TypedDict, total=False):
    num_zeros: int
    precision: int
    rolloff: float

def sinc_window(
    num_zeros: int = 64,
    precision: int = 9,
    window: Callable[[int], np.ndarray[tuple[int], np.dtype[np.float64]]] | None = None,
    rolloff: float = 0.945,
) -> tuple[np.ndarray[tuple[int], np.dtype[np.float64]], int, float]: ...
def get_filter(
    name_or_function: _FilterType, **kwargs: Unpack[_FilterKwArgs]
) -> tuple[np.ndarray[tuple[int], np.dtype[np.float64]], int, float]: ...
def load_filter(filter_name: str) -> tuple[np.ndarray[tuple[int], np.dtype[np.float64]], int, float]: ...
def clear_cache() -> None: ...
