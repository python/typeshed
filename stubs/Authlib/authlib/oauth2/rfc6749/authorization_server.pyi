from _typeshed import Incomplete

from .requests import JsonRequest, OAuth2Request

class AuthorizationServer:
    scopes_supported: Incomplete
    def __init__(self, scopes_supported: Incomplete | None = None) -> None: ...
    def query_client(self, client_id) -> None: ...
    def save_token(self, token, request) -> None: ...
    def generate_token(
        self,
        grant_type,
        client,
        user: Incomplete | None = None,
        scope: Incomplete | None = None,
        expires_in: Incomplete | None = None,
        include_refresh_token: bool = True,
    ): ...
    def register_token_generator(self, grant_type, func) -> None: ...
    def authenticate_client(self, request, methods, endpoint: str = "token"): ...
    def register_client_auth_method(self, method, func) -> None: ...
    def get_error_uri(self, request, error) -> None: ...
    def send_signal(self, name, *args, **kwargs) -> None: ...
    def create_oauth2_request(self, request) -> OAuth2Request: ...
    def create_json_request(self, request) -> JsonRequest: ...
    def handle_response(self, status, body, headers) -> None: ...
    def validate_requested_scope(self, scope, state: Incomplete | None = None) -> None: ...
    def register_grant(self, grant_cls, extensions: Incomplete | None = None) -> None: ...
    def register_endpoint(self, endpoint) -> None: ...
    def get_authorization_grant(self, request): ...
    def get_consent_grant(self, request: Incomplete | None = None, end_user: Incomplete | None = None): ...
    def get_token_grant(self, request): ...
    def create_endpoint_response(self, name, request: Incomplete | None = None): ...
    def create_authorization_response(self, request: Incomplete | None = None, grant_user: Incomplete | None = None): ...
    def create_token_response(self, request: Incomplete | None = None): ...
    def handle_error_response(self, request, error): ...
