from _typeshed import Incomplete

import httpx
from authlib.oauth2.rfc7521 import AssertionClient as _AssertionClient
from httpx import Response

from .oauth2_client import OAuth2Auth

__all__ = ["AsyncAssertionClient"]

from ...oauth2 import OAuth2Error

class AsyncAssertionClient(_AssertionClient, httpx.AsyncClient):
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuth2Error
    JWT_BEARER_GRANT_TYPE: Incomplete
    ASSERTION_METHODS: Incomplete
    DEFAULT_GRANT_TYPE = JWT_BEARER_GRANT_TYPE
    def __init__(
        self,
        token_endpoint,
        issuer,
        subject,
        audience: Incomplete | None = None,
        grant_type: Incomplete | None = None,
        claims: Incomplete | None = None,
        token_placement: str = "header",
        scope: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    async def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs) -> Response: ...

class AssertionClient(_AssertionClient, httpx.Client):
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuth2Error
    JWT_BEARER_GRANT_TYPE: Incomplete
    ASSERTION_METHODS: Incomplete
    DEFAULT_GRANT_TYPE = JWT_BEARER_GRANT_TYPE
    def __init__(
        self,
        token_endpoint,
        issuer,
        subject,
        audience: Incomplete | None = None,
        grant_type: Incomplete | None = None,
        claims: Incomplete | None = None,
        token_placement: str = "header",
        scope: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
