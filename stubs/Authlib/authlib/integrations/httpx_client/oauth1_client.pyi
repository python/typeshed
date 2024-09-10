from _typeshed import Incomplete
from collections.abc import Generator

import httpx
from authlib.oauth1 import ClientAuth
from authlib.oauth1.client import OAuth1Client as _OAuth1Client
from httpx import Auth, Request as Request, Response as Response

class OAuth1Auth(Auth, ClientAuth):
    requires_request_body: bool
    def auth_flow(self, request: Request) -> Generator[Request, Response, None]: ...

class AsyncOAuth1Client(_OAuth1Client, httpx.AsyncClient):
    auth_class = OAuth1Auth
    def __init__(
        self,
        client_id,
        client_secret: Incomplete | None = None,
        token: Incomplete | None = None,
        token_secret: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        rsa_key: Incomplete | None = None,
        verifier: Incomplete | None = None,
        signature_method="HMAC-SHA1",
        signature_type="HEADER",
        force_include_body: bool = False,
        **kwargs,
    ) -> None: ...
    async def fetch_access_token(self, url, verifier: Incomplete | None = None, **kwargs): ...
    @staticmethod
    def handle_error(error_type, error_description) -> None: ...

class OAuth1Client(_OAuth1Client, httpx.Client):
    auth_class = OAuth1Auth
    def __init__(
        self,
        client_id,
        client_secret: Incomplete | None = None,
        token: Incomplete | None = None,
        token_secret: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        rsa_key: Incomplete | None = None,
        verifier: Incomplete | None = None,
        signature_method="HMAC-SHA1",
        signature_type="HEADER",
        force_include_body: bool = False,
        **kwargs,
    ) -> None: ...
    @staticmethod
    def handle_error(error_type, error_description) -> None: ...
