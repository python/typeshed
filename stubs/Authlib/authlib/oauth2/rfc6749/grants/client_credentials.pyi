from logging import Logger
from typing import ClassVar, Literal

from authlib.oauth2.rfc6749 import BaseGrant, TokenEndpointMixin
from authlib.oauth2.rfc6750.token import _Token

log: Logger

class ClientCredentialsGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE: ClassVar[str]
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> tuple[Literal[200], _Token, list[tuple[str, str]]]: ...
