from __future__ import annotations

import asyncio
import sys
from asyncio.base_events import BaseEventLoop
from collections.abc import Coroutine
from typing import Any


class Waiter:
    def __init__(self) -> None:
        self.tasks: list[asyncio.Task[object]] = []

    def add(self, t: asyncio.Task[object]) -> None:
        self.tasks.append(t)

    async def join(self) -> None:
        await asyncio.wait(self.tasks)


async def foo() -> int:
    return 42


if sys.version_info >= (3, 13):

    def check_loop_create_task_eager_start(
        loop: asyncio.AbstractEventLoop, base_loop: BaseEventLoop, coro: Coroutine[Any, Any, int]
    ) -> None:
        loop.create_task(coro, eager_start=True)
        base_loop.create_task(coro, eager_start=True)


async def main() -> None:
    # asyncio.Task is covariant in its type argument, which is unusual since its parent class
    # asyncio.Future is invariant in its type argument. This is only sound because asyncio.Task
    # is not actually Liskov substitutable for asyncio.Future: it does not implement set_result.
    w = Waiter()
    t: asyncio.Task[int] = asyncio.create_task(foo())
    w.add(t)
    await w.join()
