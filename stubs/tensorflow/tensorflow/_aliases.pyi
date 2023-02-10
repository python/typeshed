# Commonly used type aliases.
# Everything in this module is private for stubs. There is no runtime
# equivalent.

from collections.abc import Mapping, Sequence
from typing import Any, TypeVar
from typing_extensions import TypeAlias

import numpy

_T1 = TypeVar("_T1")
_ContainerGeneric: TypeAlias = Mapping[str, _ContainerGeneric[_T1]] | Sequence[_ContainerGeneric[_T1]] | _T1

_AnyArray: TypeAlias = numpy.ndarray[Any, Any]  # noqa: Y047
