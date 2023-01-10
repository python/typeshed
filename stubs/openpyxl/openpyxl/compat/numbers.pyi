from _typeshed import Incomplete
from decimal import Decimal
from typing_extensions import TypeAlias

# #5768
# import numpy

NUMERIC_TYPES: (
    tuple[type[int], type[float], Decimal]
    | tuple[
        type[int],
        type[float],
        Decimal,
        Incomplete,  # numpy.short,
        Incomplete,  # numpy.ushort,
        Incomplete,  # numpy.intc,
        Incomplete,  # numpy.uintc,
        Incomplete,  # numpy.int_,
        Incomplete,  # numpy.uint,
        Incomplete,  # numpy.longlong,
        Incomplete,  # numpy.ulonglong,
        Incomplete,  # numpy.half,
        Incomplete,  # numpy.float16,
        Incomplete,  # numpy.single,
        Incomplete,  # numpy.double,
        Incomplete,  # numpy.longdouble,
        Incomplete,  # numpy.int8,
        Incomplete,  # numpy.int16,
        Incomplete,  # numpy.int32,
        Incomplete,  # numpy.int64,
        Incomplete,  # numpy.uint8,
        Incomplete,  # numpy.uint16,
        Incomplete,  # numpy.uint32,
        Incomplete,  # numpy.uint64,
        Incomplete,  # numpy.intp,
        Incomplete,  # numpy.uintp,
        Incomplete,  # numpy.float32,
        Incomplete,  # numpy.float64,
        Incomplete,  # type[numpy.bool_],
        Incomplete,  # type[numpy.floating],
        Incomplete,  # type[numpy.integer],
    ]
)
# Referenced outside this module
_NumericTypes: TypeAlias = (  # noqa: Y047
    int
    | float
    | Decimal
    # | numpy.short
    # | numpy.ushort
    # | numpy.intc
    # | numpy.uintc
    # | numpy.int_
    # | numpy.uint
    # | numpy.longlong
    # | numpy.ulonglong
    # | numpy.half
    # | numpy.float16
    # | numpy.single
    # | numpy.double
    # | numpy.longdouble
    # | numpy.int8
    # | numpy.int16
    # | numpy.int32
    # | numpy.int64
    # | numpy.uint8
    # | numpy.uint16
    # | numpy.uint32
    # | numpy.uint64
    # | numpy.intp
    # | numpy.uintp
    # | numpy.float32
    # | numpy.float64
    # | type[numpy.bool_]
    # | type[numpy.floating]
    # | type[numpy.integer]
)
NUMPY: bool
