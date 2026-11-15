from _typeshed import Incomplete
from collections.abc import Collection
from typing import ClassVar, TypeAlias

from authlib.oauth2 import OAuth2Request
from authlib.oauth2.rfc6749.authorization_server import AuthorizationServer
from authlib.oauth2.rfc6749.hooks import Hookable
from authlib.oauth2.rfc6749.models import ClientMixin
from authlib.oauth2.rfc6750.token import _Token

_ServerResponse: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class BaseGrant(Hookable):
    TOKEN_ENDPOINT_AUTH_METHODS: ClassVar[list[str]]
    GRANT_TYPE: ClassVar[str | None]
    TOKEN_RESPONSE_HEADER: ClassVar[list[tuple[str, str]]]

    prompt: str
    redirect_uri: Incomplete
    request: OAuth2Request
    server: AuthorizationServer

    def __init__(self, request: OAuth2Request, server: AuthorizationServer) -> None: ...
    @property
    def client(self): ...
    def generate_token(
        self,
        user=None,
        scope: str | None = None,
        grant_type: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> _Token: ...
    def authenticate_token_endpoint_client(self) -> ClientMixin: ...
    def save_token(self, token): ...
    def validate_requested_scope(self) -> None: ...

class TokenEndpointMixin:
    TOKEN_ENDPOINT_HTTP_METHODS: ClassVar[list[str]]
    GRANT_TYPE: ClassVar[str | None]

    @classmethod
    def check_token_endpoint(cls, request: OAuth2Request) -> bool: ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> tuple[int, _Token, list[tuple[str, str]]]: ...

class AuthorizationEndpointMixin:
    RESPONSE_TYPES: Collection[str]
    ERROR_RESPONSE_FRAGMENT: bool
    @classmethod
    def check_authorization_endpoint(cls, request: OAuth2Request) -> bool: ...
    @staticmethod
    def validate_authorization_redirect_uri(request: OAuth2Request, client: ClientMixin) -> str: ...
    @staticmethod
    def validate_no_multiple_request_parameter(request: OAuth2Request): ...
    redirect_uri: str
    def validate_consent_request(self) -> str: ...
    def validate_authorization_request(self) -> str: ...
    def create_authorization_response(self, redirect_uri: str, grant_user) -> _ServerResponse: ...
