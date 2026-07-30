import asyncio

protocol = asyncio.DatagramProtocol()
protocol.datagram_received(b"", ("127.0.0.1", 80))
protocol.datagram_received(b"", ("::1", 80, 0, 0))
