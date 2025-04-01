from _typeshed import Incomplete
from typing import Any

from auth0.rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from auth0.types import RequestData as RequestData

from .client_authentication import add_client_authentication as add_client_authentication

UNKNOWN_ERROR: str

class AuthenticationBase:
    domain: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    client_assertion_signing_key: Incomplete
    client_assertion_signing_alg: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        client_id: str,
        client_secret: str | None = None,
        client_assertion_signing_key: str | None = None,
        client_assertion_signing_alg: str | None = None,
        telemetry: bool = True,
        timeout: float | tuple[float, float] = 5.0,
        protocol: str = "https",
    ) -> None: ...
    def post(self, url: str, data: RequestData | None = None, headers: dict[str, str] | None = None) -> Any: ...
    def authenticated_post(self, url: str, data: dict[str, Any], headers: dict[str, str] | None = None) -> Any: ...
    def get(self, url: str, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> Any: ...
