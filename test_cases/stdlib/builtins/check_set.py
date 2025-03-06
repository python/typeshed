from __future__ import annotations

from typing import FrozenSet, Set
from typing_extensions import assert_type

# We special case `AbstractSet[None] in set.__sub__ and frozenset.__sub__
# so that it can be used for narrowing `set[T|None]` to `set[T]`
x = {"foo", "bar", None}
y = frozenset(x)
assert_type(x - {None}, Set[str])
assert_type(y - {None}, FrozenSet[str])

# For most other cases of set subtraction, we're pretty restrictive about what's allowed.
# `set[T] - set[S]` is an error, even though it won't cause an exception at runtime,
# as it will always be a useless no-op
{"foo", "bar"} - {1, 2}  # type: ignore

# But subtracting set[T|None] from set[T] is allowed, as a convenience;
# this comes up a lot in real-life code:
assert_type({"foo", "bar"} - {"foo", None}, Set[str])
x = {"foo", "bar"}
x.difference_update({"foo", "bar", None})
name: str | None = "foo"
x.discard(name)
