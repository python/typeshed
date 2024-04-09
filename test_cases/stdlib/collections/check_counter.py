from __future__ import annotations

from collections import Counter
from typing import Any, cast
from typing_extensions import assert_type


class Foo: ...


# Test the constructor
# assert_type(Counter(), Counter[Never, int])  # pyright derives "Unknown" instead of "Never"
assert_type(Counter(), "Counter[Any, int]")
assert_type(next(iter(Counter().values())), int)
assert_type(Counter(foo=42.2), "Counter[str, float]")
assert_type(Counter({42: "bar"}), "Counter[int, str]")
assert_type(Counter([1, 2, 3]), "Counter[int, int]")

int_c: Counter[str] = Counter()
assert_type(int_c, "Counter[str, int]")
assert_type(int_c["a"], int)
int_c["a"] = 1
int_c["a"] += 3
int_c["a"] += 3.5  # type: ignore

float_c = Counter(foo=42.2)
assert_type(float_c, "Counter[str, float]")
assert_type(float_c["a"], float)
float_c["a"] = 1.0
float_c["a"] += 3.0
float_c["a"] += 42
float_c["a"] += "42"  # type: ignore

custom_c = cast("Counter[str, Foo]", Counter())
assert_type(custom_c, "Counter[str, Foo]")
assert_type(custom_c["a"], Foo)
custom_c["a"] = Foo()
custom_c["a"] += Foo()  # type: ignore
custom_c["a"] += 42  # type: ignore
