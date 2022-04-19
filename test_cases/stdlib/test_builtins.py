from decimal import Decimal
from fractions import Fraction
from typing import Any, NoReturn
from typing_extensions import Literal, assert_type

#
# REGRESSION TESTS FOR OBJECT.__REDUCE__
#
# The following should pass without error (see #6661):
class Diagnostic:
    def __reduce__(self) -> str | tuple[Any, ...]:
        res = super().__reduce__()
        if isinstance(res, tuple) and len(res) >= 3:
            res[2]["_info"] = 42

        return res

#
# REGRESSION TESTS FOR POW()
#
assert_type(pow(1, 0), Literal[1])  # See #7163
assert_type(pow(1, 0, None), Literal[1])  # See #7163
assert_type(pow(2, 4, 0), NoReturn)
assert_type(pow(2, 4), int)
assert_type(pow(5, -7), float)
assert_type(pow(2, 4, 5), int)  # pow(<smallint>, <smallint>, <smallint>)
assert_type(pow(2, 35, 3), int)  # pow(<smallint>, <bigint>, <smallint>)
assert_type(pow(4.6, 8), float)
assert_type(pow(5.1, 4, None), float)
assert_type(pow(complex(6), 6.2), complex)
assert_type(pow(complex(9), 7.3, None), complex)
assert_type(pow(Fraction(), 4, None), Fraction)
assert_type(pow(Fraction(3, 7), complex(1, 8)), complex)
assert_type(pow(complex(4, -8), Fraction(2, 3)), complex)
assert_type(pow(Decimal("1.0"), Decimal("1.6")), Decimal)
assert_type(pow(Decimal("1.0"), Decimal("1.0"), Decimal("1.0")), Decimal)
assert_type(pow(Decimal("4.6"), 7, None), Decimal)
assert_type((4).__pow__(7, 4), int)
assert_type((4).__pow__(6, None), int)
assert_type(complex(9).__pow__(3.1, None), complex)
assert_type(Decimal("2.6").__pow__(5, None), Decimal)

# These would ideally be more precise, but `Any` is acceptable
# They have to be `Any` due to the fact that type-checkers can't distinguish between positive and negative numbers for the second argument to `pow()`
#
# int for positive 2nd-arg, float otherwise
assert_type(pow(4, 65), Any)
assert_type(pow(3, 57, None), Any)
# float for positive 2nd-arg, complex otherwise
assert_type(pow(4.7, 7.4), Any)
assert_type(pow(4.7, 9.2, None), Any)
assert_type((6.2).__pow__(5.2, None), Any)
# See #7046 -- float for a positive 1st arg, complex otherwise
assert_type((-2) ** 0.5, Any)
