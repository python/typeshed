from __future__ import annotations

from asyncio import DatagramProtocol


class IPv4Protocol(DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None: ...


class IPv6Protocol(DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[str, int, int, int]) -> None: ...


class NetlinkProtocol(DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[int, int]) -> None: ...
