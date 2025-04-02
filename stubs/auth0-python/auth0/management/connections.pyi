from _typeshed import Incomplete
from typing import Any

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Connections:
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
    def all(
        self,
        strategy: str | None = None,
        fields: list[str] | None = None,
        include_fields: bool = True,
        page: int | None = None,
        per_page: int | None = None,
        extra_params: dict[str, Any] | None = None,
        name: str | None = None,
    ) -> list[dict[str, Any]]: ...
    async def all_async(
        self,
        strategy: str | None = None,
        fields: list[str] | None = None,
        include_fields: bool = True,
        page: int | None = None,
        per_page: int | None = None,
        extra_params: dict[str, Any] | None = None,
        name: str | None = None,
    ) -> list[dict[str, Any]]: ...
    def get(self, id: str, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Any]: ...
    async def get_async(self, id: str, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Any]: ...
    def delete(self, id: str) -> Any: ...
    async def delete_async(self, id: str) -> Any: ...
    def update(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def create(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_user_by_email(self, id: str, email: str) -> Any: ...
    async def delete_user_by_email_async(self, id: str, email: str) -> Any: ...
