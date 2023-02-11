from __future__ import annotations

import asyncio
from typing import Any, Awaitable, List, Tuple, Union
from typing_extensions import assert_type


async def coro1() -> int:
    return 42


async def coro2() -> str:
    return "spam"


async def test_gather(awaitable1: Awaitable[int], awaitable2: Awaitable[str]) -> None:
    a = await asyncio.gather(awaitable1)
    assert_type(a, Tuple[int])

    b = await asyncio.gather(awaitable1, awaitable2, return_exceptions=True)
    assert_type(b, Tuple[Union[int, BaseException], Union[str, BaseException]])

    c = await asyncio.gather(awaitable1, awaitable2, awaitable1, awaitable1, awaitable1, awaitable1)
    assert_type(c, Tuple[int, str, int, int, int, int])

    awaitables_list: list[Awaitable[int]] = [awaitable1]
    d = await asyncio.gather(*awaitables_list)
    assert_type(d, List[int])

    e = await asyncio.gather()
    assert_type(e, list[Any])


asyncio.run(test_gather(coro1(), coro2()))
