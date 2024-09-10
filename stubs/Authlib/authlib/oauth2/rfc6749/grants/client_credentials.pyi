from _typeshed import Incomplete

from .base import BaseGrant, TokenEndpointMixin

log: Incomplete

class ClientCredentialsGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE: str
    def validate_token_request(self) -> None: ...
    def create_token_response(self): ...
