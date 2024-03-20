from collections import Counter
from typing_extensions import Never, assert_type


class Foo: ...


# Test the constructor
assert_type(Counter(), Counter[Never, int])
assert_type(Counter(foo=42.2), Counter[str, float])
assert_type(Counter({42: "bar"}), Counter[int, str])
assert_type(Counter([1, 2, 3]), Counter[int, int])

int_c: Counter[str] = Counter()
assert_type(int_c, Counter[str, int])
int_c["a"] = 1
int_c["a"] += 3
int_c["a"] += 3.5  # type: ignore

float_c = Counter(foo=42.2)
assert_type(float_c, Counter[str, float])
float_c["a"] = 1.0
float_c["a"] += 3.0
float_c["a"] += 42
float_c["a"] += "42"  # type: ignore

custom_c: Counter[str, Foo] = Counter()
assert_type(custom_c, Counter[str, Foo])
custom_c["a"] = Foo()
custom_c["a"] += Foo()  # type: ignore
custom_c["a"] += 42  # type: ignore
