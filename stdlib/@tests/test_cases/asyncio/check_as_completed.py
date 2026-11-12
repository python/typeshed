from __future__ import annotations

import asyncio
import sys
from collections.abc import Coroutine
from typing import Any
from typing_extensions import assert_type


async def result() -> int:
    return 42


if sys.version_info >= (3, 13):

    async def check_as_completed() -> None:
        task = asyncio.create_task(result())

        async for completed_task in asyncio.as_completed([task]):
            assert_type(completed_task, asyncio.Task[int])
            completed_task.cancelling()

        coroutine_for_async_iteration = result()
        async for completed_future in asyncio.as_completed([coroutine_for_async_iteration]):
            assert_type(completed_future, asyncio.Future[int])

        for completed_coroutine in asyncio.as_completed([task]):
            coroutine: Coroutine[Any, Any, int] = completed_coroutine
            assert_type(await coroutine, int)
