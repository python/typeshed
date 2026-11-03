from __future__ import annotations

import sys
from typing import Any
from typing_extensions import assert_type

if sys.version_info >= (3, 15):
    # Regression test for gh-15985: ``frozendict`` can be constructed from
    # keyword arguments, a mapping, or an iterable of pairs (not just with no
    # arguments).
    assert_type(frozendict(), frozendict[Any, Any])
    assert_type(frozendict(a=1), frozendict[str, int])
    assert_type(frozendict({"x": 1}), frozendict[str, int])
    assert_type(frozendict([("k", 2)]), frozendict[str, int])
    assert_type(frozendict({"x": 1}, y=2), frozendict[str, int])

    # gh-16668: like ``Mapping``, ``frozendict`` is covariant in its value type
    # (but not in its key type).
    def takes_optional_values(d: frozendict[str, int | None]) -> None: ...

    int_values: frozendict[str, int] = frozendict(a=1)
    takes_optional_values(int_values)
    assert_type(int_values.get("a"), int | None)
    assert_type(int_values.get("a", 0), int)
    assert_type(int_values.get("a", "x"), int | str)

    def takes_object_keys(d: frozendict[object, int]) -> None: ...

    takes_object_keys(int_values)  # type: ignore
