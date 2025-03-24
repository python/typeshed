from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from _typeshed import Incomplete
from typing import Any

class Actions:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(self, domain: str, token: str, telemetry: bool = True, timeout: TimeoutType = 5.0, protocol: str = 'https', rest_options: RestClientOptions | None = None) -> None: ...
    def get_actions(self, trigger_id: str | None = None, action_name: str | None = None, deployed: bool | None = None, installed: bool = False, page: int | None = None, per_page: int | None = None) -> Any: ...
    async def get_actions_async(self, trigger_id: str | None = None, action_name: str | None = None, deployed: bool | None = None, installed: bool = False, page: int | None = None, per_page: int | None = None) -> Any: ...
    def create_action(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_action_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def update_action(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_action_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def get_action(self, id: str) -> dict[str, Any]: ...
    async def get_action_async(self, id: str) -> dict[str, Any]: ...
    def delete_action(self, id: str, force: bool = False) -> Any: ...
    async def delete_action_async(self, id: str, force: bool = False) -> Any: ...
    def get_triggers(self) -> dict[str, Any]: ...
    async def get_triggers_async(self) -> dict[str, Any]: ...
    def get_execution(self, id: str) -> dict[str, Any]: ...
    async def get_execution_async(self, id: str) -> dict[str, Any]: ...
    def get_action_versions(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Any]: ...
    async def get_action_versions_async(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Any]: ...
    def get_trigger_bindings(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Any]: ...
    async def get_trigger_bindings_async(self, id: str, page: int | None = None, per_page: int | None = None) -> dict[str, Any]: ...
    def get_action_version(self, action_id: str, version_id: str) -> dict[str, Any]: ...
    async def get_action_version_async(self, action_id: str, version_id: str) -> dict[str, Any]: ...
    def deploy_action(self, id: str) -> dict[str, Any]: ...
    async def deploy_action_async(self, id: str) -> dict[str, Any]: ...
    def rollback_action_version(self, action_id: str, version_id: str) -> dict[str, Any]: ...
    async def rollback_action_version_async(self, action_id: str, version_id: str) -> dict[str, Any]: ...
    def update_trigger_bindings(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_trigger_bindings_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
