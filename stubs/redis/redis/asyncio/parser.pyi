from typing import Any

# TODO: define and use:
# from redis.asyncio.cluster import ClusterNode

class CommandsParser:
    __slots__ = ("commands", "node")

    async def initialize(self, node: Any | None = ...) -> None: ...  # TODO: ClusterNode
    async def get_keys(self, *args: Any) -> tuple[str, ...] | None: ...
