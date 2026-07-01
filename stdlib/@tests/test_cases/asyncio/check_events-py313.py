from __future__ import annotations

import asyncio
import sys
from collections.abc import Callable

if sys.version_info >= (3, 13):

    async def check_abstract_event_loop_create_unix_server_cleanup_socket(
        loop: asyncio.AbstractEventLoop, protocol_factory: Callable[[], asyncio.Protocol]
    ) -> None:
        await loop.create_unix_server(protocol_factory, cleanup_socket=False)
