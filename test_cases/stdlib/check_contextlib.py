from __future__ import annotations

from contextlib import ExitStack
from typing_extensions import assert_type


# See issue #7961
class Thing(ExitStack[bool | None]):
    pass


stack: ExitStack[bool | None] = ExitStack()
thing = Thing()
assert_type(stack.enter_context(Thing()), Thing)
assert_type(thing.enter_context(ExitStack()), ExitStack[bool | None])

with stack as cm:
    assert_type(cm, ExitStack[bool | None])
with thing as cm2:
    assert_type(cm2, Thing)
