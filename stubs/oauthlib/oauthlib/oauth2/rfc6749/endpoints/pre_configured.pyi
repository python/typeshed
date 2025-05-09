from collections.abc import Callable
from typing import Any

from oauthlib.common import Request

from ..grant_types import (
    AuthorizationCodeGrant,
    ClientCredentialsGrant,
    ImplicitGrant,
    RefreshTokenGrant,
    ResourceOwnerPasswordCredentialsGrant,
)
from ..request_validator import RequestValidator
from ..tokens import BearerToken
from .authorization import AuthorizationEndpoint
from .introspect import IntrospectEndpoint
from .resource import ResourceEndpoint
from .revocation import RevocationEndpoint
from .token import TokenEndpoint

class Server(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint):
    auth_grant: AuthorizationCodeGrant
    implicit_grant: ImplicitGrant
    password_grant: ResourceOwnerPasswordCredentialsGrant
    credentials_grant: ClientCredentialsGrant
    refresh_grant: RefreshTokenGrant
    bearer: BearerToken
    def __init__(
        self,
        request_validator: RequestValidator,
        token_expires_in: int | Callable[[Request], int] | None = None,
        token_generator: Callable[[Request], str] | None = None,
        refresh_token_generator: Callable[[Request], str] | None = None,
        *args: Any,  # actually, these are not used
        **kwargs: Any,  # actually, these are not used
    ) -> None: ...

class WebApplicationServer(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint):
    auth_grant: AuthorizationCodeGrant
    refresh_grant: RefreshTokenGrant
    bearer: BearerToken
    def __init__(
        self,
        request_validator: RequestValidator,
        token_generator: Callable[[Request], str] | None = None,
        token_expires_in: int | Callable[[Request], int] | None = None,
        refresh_token_generator: Callable[[Request], str] | None = None,
        **kwargs: Any,  # actually, these are not used
    ) -> None: ...

class MobileApplicationServer(AuthorizationEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    implicit_grant: ImplicitGrant
    bearer: BearerToken
    def __init__(
        self,
        request_validator: RequestValidator,
        token_generator: Callable[[Request], str] | None = None,
        token_expires_in: int | Callable[[Request], int] | None = None,
        refresh_token_generator: Callable[[Request], str] | None = None,
        **kwargs: Any,  # actually, these are not used
    ) -> None: ...

class LegacyApplicationServer(TokenEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    password_grant: ResourceOwnerPasswordCredentialsGrant
    refresh_grant: RefreshTokenGrant
    bearer: BearerToken
    def __init__(
        self,
        request_validator: RequestValidator,
        token_generator: Callable[[Request], str] | None = None,
        token_expires_in: int | Callable[[Request], int] | None = None,
        refresh_token_generator: Callable[[Request], str] | None = None,
        **kwargs: Any,  # actually, these are not used
    ) -> None: ...

class BackendApplicationServer(TokenEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint):
    credentials_grant: ClientCredentialsGrant
    bearer: BearerToken
    def __init__(
        self,
        request_validator: RequestValidator,
        token_generator: Callable[[Request], str] | None = None,
        token_expires_in: int | Callable[[Request], int] | None = None,
        refresh_token_generator: Callable[[Request], str] | None = None,
        **kwargs: Any,  # actually, these are not used
    ) -> None: ...
