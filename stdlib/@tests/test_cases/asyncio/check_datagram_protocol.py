from __future__ import annotations

import asyncio


class IPv4DatagramProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...


class IPv6DatagramProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[str, int, int, int]) -> None: ...
