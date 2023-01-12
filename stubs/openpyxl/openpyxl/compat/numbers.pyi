from _typeshed import Incomplete
from decimal import Decimal
from typing import Type  # noqa: Y022 Work around mypy bug with unions
from typing_extensions import TypeAlias

import numpy

NUMERIC_TYPES: (
    tuple[type[int], type[float], Decimal]
    | tuple[
        type[int],
        type[float],
        Decimal,
        numpy.short,
        numpy.ushort,
        numpy.intc,
        numpy.uintc,
        numpy.int_,
        numpy.uint,
        numpy.longlong,
        numpy.ulonglong,
        numpy.half,
        numpy.float16,
        numpy.single,
        numpy.double,
        numpy.longdouble,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.intp,
        numpy.uintp,
        numpy.float32,
        numpy.float64,
        type[numpy.bool_],
        type[numpy.floating[Incomplete]],
        type[numpy.integer[Incomplete]],
    ]
)
# Referenced outside this module
_NumericTypes: TypeAlias = (  # noqa: Y047
    int
    | float
    | Decimal
    | numpy.short
    | numpy.ushort
    | numpy.intc
    | numpy.uintc
    | numpy.int_
    | numpy.uint
    | numpy.longlong
    | numpy.ulonglong
    | numpy.half
    | numpy.float16
    | numpy.single
    | numpy.double
    | numpy.longdouble
    | numpy.int8
    | numpy.int16
    | numpy.int32
    | numpy.int64
    | numpy.uint8
    | numpy.uint16
    | numpy.uint32
    | numpy.uint64
    | numpy.intp
    | numpy.uintp
    | numpy.float32
    | numpy.float64
    | Type[numpy.bool_]
    | Type[numpy.floating[Incomplete]]
    | Type[numpy.integer[Incomplete]]
)
NUMPY: bool
