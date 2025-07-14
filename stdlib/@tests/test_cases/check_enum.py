from __future__ import annotations

import enum
import sys
from typing import Literal, Type
from typing_extensions import assert_type

A = enum.Enum("A", "spam eggs bacon")
B = enum.Enum("B", ["spam", "eggs", "bacon"])
C = enum.Enum("C", [("spam", 1), ("eggs", 2), ("bacon", 3)])
D = enum.Enum("D", {"spam": 1, "eggs": 2})

assert_type(A, Type[A])
assert_type(B, Type[B])
assert_type(C, Type[C])
assert_type(D, Type[D])


class EnumOfTuples(enum.Enum):
    X = 1, 2, 3
    Y = 4, 5, 6


assert_type(EnumOfTuples((1, 2, 3)), EnumOfTuples)

# TODO: ideally this test would pass:
#
# if sys.version_info >= (3, 12):
#     assert_type(EnumOfTuples(1, 2, 3), EnumOfTuples)


if sys.version_info >= (3, 11):

    class Foo(enum.StrEnum):
        X = enum.auto()

    assert_type(Foo.X, Literal[Foo.X])
    assert_type(Foo.X.value, str)


if sys.version_info >= (3, 13):
    
    class MultiValueEnum(enum.Enum):
        def __new__(cls, value, *values):
            self = object.__new__(cls)
            self._value_ = value
            for v in values:
                self._add_value_alias_(v)
            return self

    class DType(MultiValueEnum):
        float32 = 'f', 8
        double64 = 'd', 9

    # Test type inference for primary values
    assert_type(DType('f'), DType)
    assert_type(DType('d'), DType)
    
    # Test type inference for alias values
    assert_type(DType(8), DType)
    assert_type(DType(9), DType)
    
    # Test that the enum members have the correct literal types
    assert_type(DType.float32, Literal[DType.float32])
    assert_type(DType.double64, Literal[DType.double64])
