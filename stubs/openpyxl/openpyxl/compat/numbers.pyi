import sys
from decimal import Decimal
from typing import Any
from typing_extensions import TypeAlias

import numpy

if sys.version_info < (3, 7):
    _NBitBase: Any
else:
    import numpy._typing

    _NBitBase: TypeAlias = numpy._typing.NBitBase

NUMERIC_TYPES: tuple[Decimal | type[int | float | numpy.bool_ | numpy.floating[_NBitBase] | numpy.integer[_NBitBase]], ...]

# Referenced outside this module
_NumericTypes: TypeAlias = (  # noqa: Y047
    int | float | Decimal | type[numpy.bool_] | type[numpy.floating[_NBitBase]] | type[numpy.integer[_NBitBase]]
)
NUMPY: bool
