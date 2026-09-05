from _typeshed import Incomplete
from collections.abc import Generator
from typing import TypeAlias
from typing_extensions import Never

from authlib.oauth2.auth import ClientAuth, TokenAuth
from authlib.oauth2.client import OAuth2Client as _OAuth2Client

from ..base_client import OAuthError

USE_CLIENT_DEFAULT = Incomplete  # actual httpx2.USE_CLIENT_DEFAULT
Auth = Incomplete  # actual type is httpx2.Auth
Request: TypeAlias = Incomplete  # actual type is httpx2.Request
Response: TypeAlias = Incomplete  # actual type is httpx2.Response

__all__ = ["OAuth2Auth", "OAuth2ClientAuth", "AsyncOAuth2Client", "OAuth2Client"]

# Inherits from httpx2.Auth
class OAuth2Auth(TokenAuth):
    requires_request_body: bool
    def auth_flow(self, request: Request) -> Generator[Request, Response]: ...

# Inherits from httpx2.Auth
class OAuth2ClientAuth(ClientAuth):
    requires_request_body: bool
    def auth_flow(self, request: Request) -> Generator[Request, Response]: ...

# Inherits from httpx2.AsyncClient
class AsyncOAuth2Client(_OAuth2Client):
    SESSION_REQUEST_PARAMS: list[str]
    client_auth_class = OAuth2ClientAuth
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuthError  # type: ignore[assignment]
    def __init__(
        self,
        client_id=None,
        client_secret=None,
        token_endpoint_auth_method=None,
        revocation_endpoint_auth_method=None,
        scope=None,
        redirect_uri=None,
        token=None,
        token_placement="header",
        update_token=None,
        leeway=60,
        **kwargs,
    ) -> None: ...
    async def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
    async def stream(self, method, url, withhold_token: bool = False, auth=..., **kwargs) -> Generator[Incomplete]: ...
    async def ensure_active_token(self, token): ...  # type: ignore[override]

# Inherits from httpx2.Client
class OAuth2Client(_OAuth2Client):
    SESSION_REQUEST_PARAMS: list[str]
    client_auth_class = OAuth2ClientAuth
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuthError  # type: ignore[assignment]
    def __init__(
        self,
        client_id=None,
        client_secret=None,
        token_endpoint_auth_method=None,
        revocation_endpoint_auth_method=None,
        scope=None,
        redirect_uri=None,
        token=None,
        token_placement="header",
        update_token=None,
        **kwargs,
    ) -> None: ...
    @staticmethod
    def handle_error(error_type: str | None, error_description: str | None) -> Never: ...
    def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
    def stream(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
