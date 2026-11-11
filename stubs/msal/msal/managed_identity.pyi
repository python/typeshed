from collections import UserDict
from collections.abc import MutableMapping
from logging import Logger
from typing import Any, Final, overload

from .oauth2cli.http import _HttpClientLike
from .throttled_http_client import ThrottledHttpClientBase
from .token_cache import TokenCache

logger: Logger

class ManagedIdentityError(ValueError): ...

class ManagedIdentity(UserDict[str, str | None]):
    ID_TYPE: Final = "ManagedIdentityIdType"
    ID: Final = "Id"
    CLIENT_ID: Final = "ClientId"
    RESOURCE_ID: Final = "ResourceId"
    OBJECT_ID: Final = "ObjectId"
    SYSTEM_ASSIGNED: Final = "SystemAssigned"
    @classmethod
    def is_managed_identity(cls, unknown: object): ...
    @classmethod
    def is_system_assigned(cls, unknown: object) -> bool: ...
    @classmethod
    def is_user_assigned(cls, unknown: object): ...
    def __init__(self, identifier: str | None = None, id_type: str | None = None) -> None: ...

class SystemAssignedManagedIdentity(ManagedIdentity):
    def __init__(self) -> None: ...

class UserAssignedManagedIdentity(ManagedIdentity):
    @overload
    def __init__(self, *, client_id: str, resource_id: None = None, object_id: None = None) -> None: ...
    @overload
    def __init__(self, *, client_id: None = None, resource_id: str, object_id: None = None) -> None: ...
    @overload
    def __init__(self, *, client_id: None = None, resource_id: None = None, object_id: str) -> None: ...

class _ThrottledHttpClient(ThrottledHttpClientBase):
    def __init__(self, *args, **kwargs) -> None: ...

class ManagedIdentityClient:
    def __init__(
        self,
        managed_identity: dict[str, Any] | ManagedIdentity,
        *,
        http_client: _HttpClientLike,
        token_cache: TokenCache | None = None,
        http_cache: MutableMapping[str, Any] | None = None,
        client_capabilities: list[str] | None = None,
    ) -> None: ...
    def acquire_token_for_client(self, *, resource: str, claims_challenge: str | None = None) -> dict[str, Any]: ...

APP_SERVICE: Final[object]
AZURE_ARC: Final[object]
CLOUD_SHELL: Final[object]
MACHINE_LEARNING: Final[object]
SERVICE_FABRIC: Final[object]
DEFAULT_TO_VM: Final[object]

def get_managed_identity_source() -> object: ...

class ArcPlatformNotSupportedError(ManagedIdentityError): ...
