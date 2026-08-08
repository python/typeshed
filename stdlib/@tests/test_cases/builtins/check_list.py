from __future__ import annotations

from typing import List, Union
from typing_extensions import assert_type


# list.__add__ example from #8292
class Foo:
    def asd(self) -> int:
        return 1


class Bar:
    def asd(self) -> int:
        return 2


combined = [Foo()] + [Bar()]
assert_type(combined, List[Union[Foo, Bar]])
for item in combined:
    assert_type(item.asd(), int)


def test_list_signature_overlapping_type(l: list[int], key: float) -> None:
    # list.{index, count, remove} allow any type for the key since
    # (a) the key may overlap with the list's element type, and
    # (b) these methods are equality-based anyway.
    l.index(key)
    l.count(key)
    l.remove(key)
