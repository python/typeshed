from logging import Logger
from typing import Any
from urllib.parse import ParseResult

from .oauth2cli.http import _HttpClientLike

logger: Logger
AZURE_US_GOVERNMENT: str
DEPRECATED_AZURE_CHINA: str
AZURE_PUBLIC: str
AZURE_GOV_FR: str
AZURE_GOV_DE: str
AZURE_GOV_SG: str
WORLD_WIDE: str
WELL_KNOWN_AUTHORITY_HOSTS: frozenset[str]
WELL_KNOWN_B2C_HOSTS: list[str]

class AuthorityBuilder:
    def __init__(self, instance: str, tenant: str) -> None: ...

class Authority:
    instance: str
    tenant: str
    is_adfs: bool
    authorization_endpoint: str
    token_endpoint: str
    device_authorization_endpoint: str | None
    def __init__(
        self,
        authority_url: str | AuthorityBuilder | None,
        http_client: _HttpClientLike,
        validate_authority: bool = True,
        instance_discovery: bool | str | None = None,
        oidc_authority_url: str | None = None,
    ) -> None: ...
    def user_realm_discovery(self, username: str, correlation_id: str | None = None, response=None) -> dict[str, Any]: ...
    def has_valid_issuer(self) -> bool: ...

def canonicalize(authority_or_auth_endpoint: str) -> tuple[ParseResult, str, str]: ...
def tenant_discovery(tenant_discovery_endpoint: str, http_client: _HttpClientLike, **kwargs) -> dict[str, Any]: ...
