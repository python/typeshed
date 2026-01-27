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

# ignoring this so we can test mypy and pyright separately
# pyright: reportUnnecessaryTypeIgnoreComment=false

# defining separately so that the value is not inferred at the usage
l_int = [1, 2]
l_str = ["a", "b"]
combined1 = l_int + l_str
assert_type(combined1, List[Union[int, str]])

combined2: list[Union[int, str]]
# mypy doesn't support this case
combined2 = l_int + l_str  # type: ignore[operator]
assert_type(combined2, List[Union[int, str]])

combined2 = l_int + combined1
assert_type(combined2, List[Union[int, str]])

# mypy doesn't support this case
combined3: List[object] = l_int + l_str  # type: ignore[operator]
assert_type(combined3, List[object])
