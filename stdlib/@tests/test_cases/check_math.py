import math
from typing import Literal
from decimal import Decimal
from typing_extensions import assert_type


assert_type(math.prod([]), Literal[1])
assert_type(math.prod([1]), int)
assert_type(math.prod([34.34]), float | Literal[1])
assert_type(math.prod([34.34, 1]), float | int)
assert_type(math.prod([34.34, Decimal(1)]), float | Decimal | Literal[1])
assert_type(math.prod([Decimal(1)], start=Decimal(1)), Decimal)
