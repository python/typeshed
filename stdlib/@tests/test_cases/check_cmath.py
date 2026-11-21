import cmath
from typing_extensions import assert_type

assert_type(cmath.e, float)
assert_type(cmath.pi, float)
assert_type(cmath.inf, float)
assert_type(cmath.nan, float)
assert_type(cmath.tau, float)

assert_type(cmath.infj, complex)
assert_type(cmath.nanj, complex)
