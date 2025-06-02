from __future__ import annotations

from typing_extensions import assert_type

from decouple import Choices

assert_type(Choices()(""), str)
assert_type(Choices(cast=int)(""), int)
assert_type(Choices(flat=[1, 2])(""), int)
assert_type(Choices(cast=int, flat=[1, 2])(""), int)
assert_type(Choices(cast=int, choices=[(1, "one"), (2, "two")])(""), int)
assert_type(Choices(flat=[1, 2], choices=[(1, "one"), (2, "two")])(""), int)
assert_type(Choices(cast=int, flat=[1, 2], choices=[(1, "one"), (2, "two")])(""), int)
assert_type(Choices([1, 2])(""), int)
assert_type(Choices([1, 2], int)(""), int)
assert_type(Choices([1, 2], int, [(1, "one"), (2, "two")])(""), int)
