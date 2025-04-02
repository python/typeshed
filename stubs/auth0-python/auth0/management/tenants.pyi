from _typeshed import Incomplete
from typing import Any

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Tenants:
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
    def get(self, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Any]: ...
    async def get_async(self, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Any]: ...
    def update(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
