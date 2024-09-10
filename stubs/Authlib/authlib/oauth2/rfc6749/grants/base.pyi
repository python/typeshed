from _typeshed import Incomplete
from collections.abc import Callable, Collection
from typing import Any
from typing_extensions import TypeAlias

from .. import ClientMixin
from ..requests import OAuth2Request

_SERVER_RESPONSE: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class BaseGrant:
    TOKEN_ENDPOINT_AUTH_METHODS: Collection[str]
    GRANT_TYPE: str | None
    TOKEN_RESPONSE_HEADER = Collection[tuple[str, str]]  # noqa: Y026
    prompt: Incomplete
    redirect_uri: Incomplete
    request: OAuth2Request
    server: Any
    def __init__(self, request: OAuth2Request, server: Any) -> None: ...
    @property
    def client(self): ...
    def generate_token(
        self,
        user: Any | None = None,
        scope: str | None = None,
        grant_type: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> dict[str, str | int]: ...
    def authenticate_token_endpoint_client(self) -> ClientMixin: ...
    def save_token(self, token): ...
    def validate_requested_scope(self) -> None: ...
    def register_hook(self, hook_type: str, hook: Callable[..., Incomplete]) -> None: ...
    def execute_hook(self, hook_type: str, *args: object, **kwargs: object) -> None: ...

class TokenEndpointMixin:
    TOKEN_ENDPOINT_HTTP_METHODS: Incomplete
    GRANT_TYPE: Incomplete
    @classmethod
    def check_token_endpoint(cls, request: OAuth2Request): ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> _SERVER_RESPONSE: ...

class AuthorizationEndpointMixin:
    RESPONSE_TYPES: Collection[str]
    ERROR_RESPONSE_FRAGMENT: bool
    @classmethod
    def check_authorization_endpoint(cls, request: OAuth2Request) -> bool: ...
    @staticmethod
    def validate_authorization_redirect_uri(request: OAuth2Request, client: ClientMixin) -> str: ...
    @staticmethod
    def validate_no_multiple_request_parameter(request: OAuth2Request): ...
    redirect_uri: Incomplete
    def validate_consent_request(self) -> None: ...
    def validate_authorization_request(self) -> str: ...
    def create_authorization_response(self, redirect_uri: str, grant_user: Any) -> _SERVER_RESPONSE: ...
