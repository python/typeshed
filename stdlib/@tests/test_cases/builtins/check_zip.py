from __future__ import annotations

from collections.abc import Sequence
from typing_extensions import assert_type

ints: Sequence[int] = [1, 2, 3]
strs: Sequence[str] = ["one", "two", "three"]
floats: Sequence[float] = [1.0, 2.0, 3.0]
str_tuples: Sequence[tuple[str]] = list((x,) for x in strs)

assert_type(zip(ints), zip[tuple[int]])
assert_type(zip(ints, strs), zip[tuple[int, str]])
assert_type(zip(ints, strs, floats), zip[tuple[int, str, float]])
assert_type(zip(strs, ints, floats, ints), zip[tuple[str, int, float, int]])
assert_type(zip(strs, ints, floats, ints, str_tuples), zip[tuple[str, int, float, int, tuple[str]]])
