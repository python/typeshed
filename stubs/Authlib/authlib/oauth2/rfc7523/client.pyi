from _typeshed import Incomplete

ASSERTION_TYPE: str

class JWTBearerClientAssertion:
    CLIENT_ASSERTION_TYPE = ASSERTION_TYPE
    CLIENT_AUTH_METHOD: str
    token_url: Incomplete
    def __init__(self, token_url, validate_jti: bool = True) -> None: ...
    def __call__(self, query_client, request): ...
    def create_claims_options(self): ...
    def process_assertion_claims(self, assertion, resolve_key): ...
    def authenticate_client(self, client): ...
    def create_resolve_key_func(self, query_client, request): ...
    def validate_jti(self, claims, jti) -> None: ...
    def resolve_client_public_key(self, client, headers) -> None: ...
