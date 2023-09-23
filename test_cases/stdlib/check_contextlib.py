from __future__ import annotations

from contextlib import ExitStack, asynccontextmanager
from typing import AsyncIterator, Awaitable
from typing_extensions import assert_type


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


@asynccontextmanager
async def async_context() -> AsyncGenerator[str, None]:
    yield "example"


async def async_gen() -> AsyncGenerator[str, None]:
    yield "async gen"


@asynccontextmanager
def async_cm_func() -> AsyncGenerator[str, None]:
    return async_gen()
