# Stub-only module, can't be imported at runtime.

from collections.abc import Collection
from typing import Any, Protocol, type_check_only
from typing_extensions import TypeAlias, TypeVar

import numpy as np

_ScalarT = TypeVar("_ScalarT", bound=bool | int | float | complex | str | bytes | np.generic)
_GenericT = TypeVar("_GenericT", bound=np.generic)
_GenericT_co = TypeVar("_GenericT_co", bound=np.generic, covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)

# numpy aliases
@type_check_only
class SupportsArray(Protocol[_GenericT_co, _ShapeT_co]):
    def __array__(self) -> np.ndarray[_ShapeT_co, np.dtype[_GenericT_co]]: ...

Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_GenericT]]
Array2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_GenericT]]
ArrayLike1D: TypeAlias = Collection[_ScalarT] | SupportsArray[_GenericT, tuple[int]]
Seed: TypeAlias = int | np.random.Generator | np.random.RandomState
