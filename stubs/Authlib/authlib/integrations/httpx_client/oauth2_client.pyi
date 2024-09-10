from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import asynccontextmanager

import httpx
from authlib.oauth2 import OAuth2Error
from authlib.oauth2.auth import ClientAuth, TokenAuth
from authlib.oauth2.client import OAuth2Client as _OAuth2Client
from httpx import Auth, Request, Response

from .utils import HTTPX_CLIENT_KWARGS

__all__ = ["OAuth2Auth", "OAuth2ClientAuth", "AsyncOAuth2Client", "OAuth2Client"]

class OAuth2Auth(Auth, TokenAuth):
    requires_request_body: bool
    def auth_flow(self, request: Request) -> Generator[Request, Response, None]: ...

class OAuth2ClientAuth(Auth, ClientAuth):
    requires_request_body: bool
    def auth_flow(self, request: Request) -> Generator[Request, Response, None]: ...

class AsyncOAuth2Client(_OAuth2Client, httpx.AsyncClient):
    SESSION_REQUEST_PARAMS = HTTPX_CLIENT_KWARGS
    client_auth_class = OAuth2ClientAuth
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuth2Error
    def __init__(
        self,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        token_endpoint_auth_method: Incomplete | None = None,
        revocation_endpoint_auth_method: Incomplete | None = None,
        scope: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        token: Incomplete | None = None,
        token_placement: str = "header",
        update_token: Incomplete | None = None,
        leeway: int = 60,
        **kwargs,
    ) -> None: ...
    async def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
    @asynccontextmanager
    async def stream(self, *args, **kwargs): ...
    async def ensure_active_token(self, token=None): ...

class OAuth2Client(_OAuth2Client, httpx.Client):
    SESSION_REQUEST_PARAMS = HTTPX_CLIENT_KWARGS
    client_auth_class = OAuth2ClientAuth
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuth2Error
    def __init__(
        self,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        token_endpoint_auth_method: Incomplete | None = None,
        revocation_endpoint_auth_method: Incomplete | None = None,
        scope: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        token: Incomplete | None = None,
        token_placement: str = "header",
        update_token: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @staticmethod
    def handle_error(error_type, error_description) -> None: ...
    def request(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
    def stream(self, method, url, withhold_token: bool = False, auth=..., **kwargs): ...
