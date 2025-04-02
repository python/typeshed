from _typeshed import Incomplete
from typing import Any

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class EmailTemplates:
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
    def create(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def get(self, template_name: str) -> dict[str, Any]: ...
    async def get_async(self, template_name: str) -> dict[str, Any]: ...
    def update(self, template_name: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_async(self, template_name: str, body: dict[str, Any]) -> dict[str, Any]: ...
