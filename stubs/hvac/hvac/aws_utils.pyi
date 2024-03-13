from _typeshed import Incomplete

class SigV4Auth:
    access_key: str
    secret_key: str
    session_token: str | None
    region: str
    def __init__(self, access_key: str, secret_key: str, session_token: str | None = ..., region: str = ...) -> None: ...
    def add_auth(self, request: Incomplete) -> None: ...

def generate_sigv4_auth_request(header_value: str | None = ...) -> Incomplete: ...
