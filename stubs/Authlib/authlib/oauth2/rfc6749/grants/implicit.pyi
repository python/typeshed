from _typeshed import Incomplete
from logging import Logger
from typing import ClassVar

from authlib.oauth2.rfc6749 import AuthorizationEndpointMixin, BaseGrant

log: Logger

class ImplicitGrant(BaseGrant, AuthorizationEndpointMixin):
    AUTHORIZATION_ENDPOINT: bool
    TOKEN_ENDPOINT_AUTH_METHODS: ClassVar[list[str]]
    RESPONSE_TYPES: Incomplete
    GRANT_TYPE: ClassVar[str]
    ERROR_RESPONSE_FRAGMENT: bool
    def validate_authorization_request(self): ...
    def create_authorization_response(self, redirect_uri, grant_user): ...
