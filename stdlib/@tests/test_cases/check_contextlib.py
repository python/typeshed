from __future__ import annotations

from contextlib import AbstractContextManager, ExitStack
from typing_extensions import assert_type


class CM1(AbstractContextManager):
    def __exit__(self, *args) -> None:
        return None

with CM1() as cm1:
    assert_type(cm1, CM1)


# See issue #7961
class Thing(ExitStack):
    pass


stack = ExitStack()
thing = Thing()
assert_type(stack.enter_context(Thing()), Thing)
assert_type(thing.enter_context(ExitStack()), ExitStack)

with stack as cm:
    assert_type(cm, ExitStack)
with thing as cm2:
    assert_type(cm2, Thing)
