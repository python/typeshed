from __future__ import annotations

import asyncio
import socket
from typing_extensions import assert_type


async def check_create_server(loop: asyncio.AbstractEventLoop, base_loop: asyncio.BaseEventLoop) -> None:
    # `port` is optional whenever a host is given: the runtime passes it straight
    # to getaddrinfo, which treats None as "any port".
    assert_type(await loop.create_server(asyncio.Protocol, "localhost"), asyncio.Server)
    assert_type(await loop.create_server(asyncio.Protocol, "localhost", 8080), asyncio.Server)
    assert_type(await loop.create_server(asyncio.Protocol, "localhost", None), asyncio.Server)
    assert_type(await loop.create_server(asyncio.Protocol, ["localhost", "127.0.0.1"], 8080), asyncio.Server)

    # A port with no host binds every interface.
    assert_type(await loop.create_server(asyncio.Protocol, None, 8080), asyncio.Server)
    assert_type(await loop.create_server(asyncio.Protocol, port=8080), asyncio.Server)

    assert_type(await base_loop.create_server(asyncio.Protocol, "localhost", None), asyncio.Server)
    assert_type(await base_loop.create_server(asyncio.Protocol, port=8080), asyncio.Server)


async def check_create_server_sock(loop: asyncio.AbstractEventLoop, sock: socket.socket) -> None:
    assert_type(await loop.create_server(asyncio.Protocol, sock=sock), asyncio.Server)

    # The runtime rejects host/port together with sock:
    # ValueError: host/port and sock can not be specified at the same time
    await loop.create_server(asyncio.Protocol, "localhost", sock=sock)  # type: ignore
    await loop.create_server(asyncio.Protocol, None, 8080, sock=sock)  # type: ignore
