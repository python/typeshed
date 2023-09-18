from typing import Any

from oauthlib.common import Request
from oauthlib.oauth2.rfc6749.clients import Client

log: Any

class RequestValidator:
    def client_authentication_required(self, request: Request, *args, **kwargs) -> bool: ...
    def authenticate_client(self, request: Request, *args, **kwargs) -> bool: ...
    def authenticate_client_id(self, client_id: str, request: Request, *args, **kwargs) -> bool: ...
    def confirm_redirect_uri(
        self, client_id: str, code: str, redirect_uri: str, client: Client, request: Request, *args, **kwargs
    ) -> bool: ...
    def get_default_redirect_uri(self, client_id: str, request: Request, *args, **kwargs) -> str: ...
    def get_default_scopes(self, client_id: str, request: Request, *args, **kwargs) -> list[str]: ...
    def get_original_scopes(self, refresh_token: str, request: Request, *args, **kwargs) -> list[str]: ...
    def is_within_original_scope(
        self, request_scopes: list[str], refresh_token: str, request: Request, *args, **kwargs
    ) -> bool: ...
    def introspect_token(self, token: str, token_type_hint: str, request: Request, *args, **kwargs) -> dict | None: ...
    def invalidate_authorization_code(self, client_id: str, code: str, request: Request, *args, **kwargs) -> None: ...
    def revoke_token(self, token: str, token_type_hint: str, request: Request, *args, **kwargs) -> None: ...
    def rotate_refresh_token(self, request: Request) -> bool: ...
    def save_authorization_code(self, client_id: str, code: str, request: Request, *args, **kwargs) -> None: ...
    def save_token(self, token: dict, request: Request, *args, **kwargs) -> None: ...
    def save_bearer_token(self, token: dict, request: Request, *args, **kwargs) -> str: ...
    def validate_bearer_token(self, token: str, scopes: list[str], request: Request) -> bool: ...
    def validate_client_id(self, client_id: str, request: Request, *args, **kwargs) -> bool: ...
    def validate_code(self, client_id: str, code: str, client: Client, request: Request, *args, **kwargs) -> bool: ...
    def validate_grant_type(self, client_id: str, grant_type: str, client: Client, request: Request, *args, **kwargs) -> bool: ...
    def validate_redirect_uri(self, client_id: str, redirect_uri: str, request: Request, *args, **kwargs) -> bool: ...
    def validate_refresh_token(self, refresh_token: str, client: Client, request: Request, *args, **kwargs) -> bool: ...
    def validate_response_type(
        self, client_id: str, response_type: str, client: Client, request: Request, *args, **kwargs
    ) -> bool: ...
    def validate_scopes(self, client_id: str, scopes: list[str], client: Client, request: Request, *args, **kwargs) -> bool: ...
    def validate_user(self, username: str, password: str, client: Client, request: Request, *args, **kwargs) -> bool: ...
    def is_pkce_required(self, client_id: str, request: Request) -> bool: ...
    def get_code_challenge(self, code: str, request: Request) -> str: ...
    def get_code_challenge_method(self, code: str, request: Request) -> str: ...
