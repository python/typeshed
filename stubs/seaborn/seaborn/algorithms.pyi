from collections.abc import Callable
from typing import Any

import numpy as np
from numpy.typing import ArrayLike, NDArray

def bootstrap(
    *args: ArrayLike,
    n_boot: int = 10000,
    func: str | Callable[..., Any] = "mean",
    axis: int | None = None,
    units: ArrayLike | None = None,
    seed: int | np.random.Generator | np.random.RandomState | None = None,
) -> NDArray[Any]: ...
