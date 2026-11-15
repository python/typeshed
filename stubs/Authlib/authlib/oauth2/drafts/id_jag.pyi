from _typeshed import Incomplete
from logging import Logger
from typing import Any, ClassVar, Final, Literal

from authlib.oauth2.rfc6749.grants.base import BaseGrant, TokenEndpointMixin
from authlib.oauth2.rfc6750.token import _Token
from joserfc import jwk

log: Logger

class IDJAGGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE: ClassVar[str]
    REQUIRED_TYP: Final[str]
    CLAIMS_OPTIONS: Final[dict[str, dict[str, Any]]]
    LEEWAY: int

    request: Incomplete

    @staticmethod
    def sign(
        key, issuer, audience, subject, client_id, jti=None, issued_at=None, expires_at=None, claims=None, *, header={}, **kwargs
    ): ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> tuple[Literal[200], _Token, list[tuple[str, str]]]: ...
    def get_audiences(self) -> list[Incomplete]: ...
    def resolve_issuer_key(self, issuer, headers) -> jwk.Key | jwk.KeySet: ...
    def authenticate_user(self, subject): ...
    def check_jti(self, claims, jti) -> bool: ...
    def check_id_jag_permission(self, client, user, scopes) -> bool: ...
