from _typeshed import Incomplete

from authlib.oauth2.rfc6750.validator import BearerTokenValidator

class JWTBearerTokenValidator(BearerTokenValidator):
    issuer: Incomplete
    resource_server: Incomplete
    def __init__(self, issuer, resource_server, *args, **kwargs) -> None: ...
    def get_jwks(self) -> None: ...
    def validate_iss(self, claims, iss: str) -> bool: ...
    def authenticate_token(self, token_string): ...
    def validate_token(
        self,
        token,
        scopes,
        request,
        groups: Incomplete | None = None,
        roles: Incomplete | None = None,
        entitlements: Incomplete | None = None,
    ) -> None: ...
