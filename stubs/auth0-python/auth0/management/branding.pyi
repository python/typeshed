from _typeshed import Incomplete
from typing import Any

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class Branding:
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
    def get(self) -> dict[str, Any]: ...
    async def get_async(self) -> dict[str, Any]: ...
    def update(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def get_template_universal_login(self) -> dict[str, Any]: ...
    async def get_template_universal_login_async(self) -> dict[str, Any]: ...
    def delete_template_universal_login(self) -> Any: ...
    async def delete_template_universal_login_async(self) -> Any: ...
    def update_template_universal_login(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_template_universal_login_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def get_default_branding_theme(self) -> dict[str, Any]: ...
    async def get_default_branding_theme_async(self) -> dict[str, Any]: ...
    def get_branding_theme(self, theme_id: str) -> dict[str, Any]: ...
    async def get_branding_theme_async(self, theme_id: str) -> dict[str, Any]: ...
    def delete_branding_theme(self, theme_id: str) -> Any: ...
    async def delete_branding_theme_async(self, theme_id: str) -> Any: ...
    def update_branding_theme(self, theme_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_branding_theme_async(self, theme_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def create_branding_theme(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_branding_theme_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
