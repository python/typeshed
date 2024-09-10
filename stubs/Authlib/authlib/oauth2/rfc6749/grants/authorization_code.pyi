from _typeshed import Incomplete

from .base import AuthorizationEndpointMixin, BaseGrant, TokenEndpointMixin

log: Incomplete

class AuthorizationCodeGrant(BaseGrant, AuthorizationEndpointMixin, TokenEndpointMixin):
    TOKEN_ENDPOINT_AUTH_METHODS: Incomplete
    AUTHORIZATION_CODE_LENGTH: int
    RESPONSE_TYPES: Incomplete
    GRANT_TYPE: str
    def validate_authorization_request(self): ...
    def create_authorization_response(self, redirect_uri: str, grant_user): ...
    def validate_token_request(self) -> None: ...
    def create_token_response(self): ...
    def generate_authorization_code(self): ...
    def save_authorization_code(self, code, request) -> None: ...
    def query_authorization_code(self, code, client) -> None: ...
    def delete_authorization_code(self, authorization_code) -> None: ...
    def authenticate_user(self, authorization_code) -> None: ...

def validate_code_authorization_request(grant): ...
