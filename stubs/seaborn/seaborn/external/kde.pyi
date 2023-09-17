from collections.abc import Callable
from typing_extensions import Literal, TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray

__all__ = ["gaussian_kde"]

_Scalar: TypeAlias = np.generic | bool | int | float | complex | bytes | memoryview  # see np.isscalar
_BwMethodType: TypeAlias = Literal["scott", "silverman"] | Callable[[gaussian_kde], object] | _Scalar | None

class gaussian_kde:
    dataset: NDArray[np.float64]
    def __init__(self, dataset: ArrayLike, bw_method: _BwMethodType = None, weights: ArrayLike | None = None) -> None: ...
    def evaluate(self, points: ArrayLike) -> NDArray[np.float64]: ...
    __call__ = evaluate
    def scotts_factor(self) -> float: ...
    def silverman_factor(self) -> float: ...
    covariance_factor = scotts_factor
    def set_bandwidth(self, bw_method: _BwMethodType = None) -> None: ...
    def pdf(self, x: ArrayLike) -> NDArray[np.float64]: ...
    @property
    def weights(self) -> NDArray[np.float64]: ...
    @property
    def neff(self) -> NDArray[np.float64]: ...
