from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType
from _typeshed import Incomplete
from typing import Any

class Organizations:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(self, domain: str, token: str, telemetry: bool = True, timeout: TimeoutType = 5.0, protocol: str = 'https', rest_options: RestClientOptions | None = None) -> None: ...
    def all_organizations(self, page: int | None = None, per_page: int | None = None, include_totals: bool = True, from_param: str | None = None, take: int | None = None): ...
    async def all_organizations_async(self, page: int | None = None, per_page: int | None = None, include_totals: bool = True, from_param: str | None = None, take: int | None = None): ...
    def get_organization_by_name(self, name: str | None = None) -> dict[str, Any]: ...
    async def get_organization_by_name_async(self, name: str | None = None) -> dict[str, Any]: ...
    def get_organization(self, id: str) -> dict[str, Any]: ...
    async def get_organization_async(self, id: str) -> dict[str, Any]: ...
    def create_organization(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_organization_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    def update_organization(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_organization_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_organization(self, id: str) -> Any: ...
    async def delete_organization_async(self, id: str) -> Any: ...
    def all_organization_connections(self, id: str, page: int | None = None, per_page: int | None = None) -> list[dict[str, Any]]: ...
    async def all_organization_connections_async(self, id: str, page: int | None = None, per_page: int | None = None) -> list[dict[str, Any]]: ...
    def get_organization_connection(self, id: str, connection_id: str) -> dict[str, Any]: ...
    async def get_organization_connection_async(self, id: str, connection_id: str) -> dict[str, Any]: ...
    def create_organization_connection(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_organization_connection_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def update_organization_connection(self, id: str, connection_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def update_organization_connection_async(self, id: str, connection_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_organization_connection(self, id: str, connection_id: str) -> Any: ...
    async def delete_organization_connection_async(self, id: str, connection_id: str) -> Any: ...
    def all_organization_members(self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = True, from_param: str | None = None, take: int | None = None, fields: list[str] | None = None, include_fields: bool = True): ...
    async def all_organization_members_async(self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = True, from_param: str | None = None, take: int | None = None, fields: list[str] | None = None, include_fields: bool = True): ...
    def create_organization_members(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_organization_members_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_organization_members(self, id: str, body: dict[str, Any]) -> Any: ...
    async def delete_organization_members_async(self, id: str, body: dict[str, Any]) -> Any: ...
    def all_organization_member_roles(self, id: str, user_id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False) -> list[dict[str, Any]]: ...
    async def all_organization_member_roles_async(self, id: str, user_id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False) -> list[dict[str, Any]]: ...
    def create_organization_member_roles(self, id: str, user_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_organization_member_roles_async(self, id: str, user_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_organization_member_roles(self, id: str, user_id: str, body: dict[str, Any]) -> Any: ...
    async def delete_organization_member_roles_async(self, id: str, user_id: str, body: dict[str, Any]) -> Any: ...
    def all_organization_invitations(self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False): ...
    async def all_organization_invitations_async(self, id: str, page: int | None = None, per_page: int | None = None, include_totals: bool = False): ...
    def get_organization_invitation(self, id: str, invitaton_id: str) -> dict[str, Any]: ...
    async def get_organization_invitation_async(self, id: str, invitaton_id: str) -> dict[str, Any]: ...
    def create_organization_invitation(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_organization_invitation_async(self, id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    def delete_organization_invitation(self, id: str, invitation_id: str) -> Any: ...
    async def delete_organization_invitation_async(self, id: str, invitation_id: str) -> Any: ...
    def get_client_grants(self, id: str, audience: str | None = None, client_id: str | None = None, page: int | None = None, per_page: int | None = None, include_totals: bool = False): ...
    async def get_client_grants_async(self, id: str, audience: str | None = None, client_id: str | None = None, page: int | None = None, per_page: int | None = None, include_totals: bool = False): ...
    def add_client_grant(self, id: str, grant_id: str) -> dict[str, Any]: ...
    async def add_client_grant_async(self, id: str, grant_id: str) -> dict[str, Any]: ...
    def delete_client_grant(self, id: str, grant_id: str) -> dict[str, Any]: ...
    async def delete_client_grant_async(self, id: str, grant_id: str) -> dict[str, Any]: ...
