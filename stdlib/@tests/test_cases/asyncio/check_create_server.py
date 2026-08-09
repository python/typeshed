from __future__ import annotations

import asyncio
from collections.abc import Sequence


async def check_create_server(loop: asyncio.BaseEventLoop) -> None:
    await loop.create_server(asyncio.Protocol, "localhost", None)
    await loop.create_server(asyncio.Protocol, ["localhost", "127.0.0.1"], None)

    hosts: Sequence[str] = ["localhost"]
    await loop.create_server(asyncio.Protocol, hosts)
