from __future__ import annotations

from contextlib import ExitStack
from typing import Optional
from typing_extensions import assert_type


# See issue #7961
class Thing(ExitStack[Optional[bool]]):
    pass


stack: ExitStack[bool | None] = ExitStack()
thing = Thing()
assert_type(stack.enter_context(Thing()), Thing)
assert_type(thing.enter_context(ExitStack()), ExitStack[Optional[bool]])

with stack as cm:
    assert_type(cm, ExitStack[Optional[bool]])
with thing as cm2:
    assert_type(cm2, Thing)
