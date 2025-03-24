from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from _typeshed import Incomplete
from typing import Any

class Jobs:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(self, domain: str, token: str, telemetry: bool = True, timeout: TimeoutType = 5.0, protocol: str = 'https', rest_options: RestClientOptions | None = None) -> None: ...
    def get(self, id: str) -> dict[str, Any]: ...
    async def get_async(self, id: str) -> dict[str, Any]: ...
    def get_failed_job(self, id: str) -> dict[str, Any]: ...
    async def get_failed_job_async(self, id: str) -> dict[str, Any]: ...
    def export_users(self, body: dict[str, Any]): ...
    async def export_users_async(self, body: dict[str, Any]): ...
    def import_users(self, connection_id: str, file_obj: Any, upsert: bool = False, send_completion_email: bool = True, external_id: str | None = None) -> dict[str, Any]: ...
    async def import_users_async(self, connection_id: str, file_obj: Any, upsert: bool = False, send_completion_email: bool = True, external_id: str | None = None) -> dict[str, Any]: ...
    def send_verification_email(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def send_verification_email_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
