import asyncio
from typing import Any, Awaitable, List, Tuple, Union
from typing_extensions import assert_type


async def coro1() -> int:
    ...


async def coro2() -> str:
    ...


async def coro3() -> int:
    ...


async def coro4() -> int:
    ...


async def coro5() -> int:
    ...


async def coro6() -> int:
    ...


async def test_gather(
    awaitable1: Awaitable[int],
    awaitable2: Awaitable[str],
    awaitable3: Awaitable[int],
    awaitable4: Awaitable[int],
    awaitable5: Awaitable[int],
    awaitable6: Awaitable[int],
) -> None:
    a = await asyncio.gather(awaitable1)
    assert_type(a, Tuple[int])

    b = await asyncio.gather(awaitable1, awaitable2, return_exceptions=True)
    assert_type(b, Tuple[Union[int, BaseException], Union[str, BaseException]])

    c = await asyncio.gather(awaitable1, awaitable2, awaitable3, awaitable4, awaitable5, awaitable6)
    assert_type(c, List[Any])

    awaitables_list: List[Awaitable[int]] = [awaitable1]
    d = await asyncio.gather(*awaitables_list)
    assert_type(d, List[Any])

    e = await asyncio.gather()
    assert_type(e, List[Any])


asyncio.run(test_gather(coro1(), coro2(), coro3(), coro4(), coro5(), coro6()))
