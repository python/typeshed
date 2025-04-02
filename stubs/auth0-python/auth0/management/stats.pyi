from _typeshed import Incomplete

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Stats:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def get_active_users(self) -> int: ...
    async def get_active_users_async(self) -> int: ...
    def get_daily_stats(self, from_date: str | None = None, to_date: str | None = None) -> list[dict[str, Incomplete]]: ...
    async def get_daily_stats_async(
        self, from_date: str | None = None, to_date: str | None = None
    ) -> list[dict[str, Incomplete]]: ...
