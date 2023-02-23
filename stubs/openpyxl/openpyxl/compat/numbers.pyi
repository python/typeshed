from decimal import Decimal
from typing_extensions import TypeAlias

import numpy
import numpy._typing

NUMERIC_TYPES: tuple[
    Decimal | type[int | float | numpy.bool_ | numpy.floating[numpy._typing.NBitBase] | numpy.integer[numpy._typing.NBitBase]],
    ...,
]

# Referenced outside this module
_NumericTypes: TypeAlias = (  # noqa: Y047
    int
    | float
    | Decimal
    | type[numpy.bool_]
    | type[numpy.floating[numpy._typing.NBitBase]]
    | type[numpy.integer[numpy._typing.NBitBase]]
)
NUMPY: bool
