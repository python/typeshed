from redis.asyncio.cluster import ClusterNode

class CommandsParser:
    __slots__ = ("commands", "node")

    async def initialize(self, node: ClusterNode | None = ...) -> None: ...
    async def get_keys(self, *args: Any) -> Tuple[str, ...] | None: ...
