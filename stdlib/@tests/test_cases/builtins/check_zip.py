from typing import Tuple
from typing_extensions import assert_type

assert_type(zip((1, 2)), zip[Tuple[int]])
assert_type(zip([1, 2], ("3", "4")), zip[Tuple[int, str]])
assert_type(zip([1], ["2"], [3.0]), zip[Tuple[int, str, float]])
assert_type(zip(["1"], [2], [3.0], [4]), zip[Tuple[str, int, float, int]])
assert_type(zip(["1"], [2], [3.0], [4], [("5",)]), zip[Tuple[str, int, float, int, Tuple[str]]])
