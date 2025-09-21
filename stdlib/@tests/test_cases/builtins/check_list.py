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

l_int = [1, 2]
l_str = ["a", "b"]
# TODO: these pass pyright with the current stubs, but mypy erroneously emits errors:
# _1: List[object] = l_int + l_str
# _2: List[None] = l_int + l_str

# combined = l_int + l_str
# assert_type(combined, List[int | str])
