from _typeshed import Incomplete

from .base import AuthorizationEndpointMixin, BaseGrant

class ImplicitGrant(BaseGrant, AuthorizationEndpointMixin):
    AUTHORIZATION_ENDPOINT: bool
    TOKEN_ENDPOINT_AUTH_METHODS: Incomplete
    RESPONSE_TYPES: Incomplete
    GRANT_TYPE: str
    ERROR_RESPONSE_FRAGMENT: bool
    def validate_authorization_request(self): ...
    def create_authorization_response(self, redirect_uri, grant_user): ...
