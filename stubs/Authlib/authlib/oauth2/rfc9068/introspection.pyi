from _typeshed import Incomplete

from authlib.oauth2.rfc7662 import IntrospectionEndpoint

class JWTIntrospectionEndpoint(IntrospectionEndpoint):
    ENDPOINT_NAME: str
    issuer: Incomplete
    def __init__(self, issuer, server: Incomplete | None = None, *args, **kwargs) -> None: ...
    def create_endpoint_response(self, request): ...
    def authenticate_token(self, request, client): ...
    def create_introspection_payload(self, token): ...
    def get_jwks(self) -> None: ...
    def get_username(self, user_id: str) -> str: ...
