from typing import Any, List, Optional, Dict

log: Any

class RequestValidator:
    def client_authentication_required(self, request, *args, **kwargs) -> bool: ...
    def authenticate_client(self, request, *args, **kwargs) -> bool: ...
    def authenticate_client_id(self, client_id, request, *args, **kwargs) -> bool: ...
    def confirm_redirect_uri(self, client_id, code, redirect_uri, client, request, *args, **kwargs) -> bool: ...
    def get_default_redirect_uri(self, client_id, request, *args, **kwargs) -> str: ...
    def get_default_scopes(self, client_id, request, *args, **kwargs) -> List[str]: ...
    def get_original_scopes(self, refresh_token, request, *args, **kwargs) -> List[str]: ...
    def is_within_original_scope(self, request_scopes, refresh_token, request, *args, **kwargs) -> bool: ...
    def introspect_token(self, token, token_type_hint, request, *args, **kwargs) -> Optional[Dict]: ...
    def invalidate_authorization_code(self, client_id, code, request, *args, **kwargs) -> None: ...
    def revoke_token(self, token, token_type_hint, request, *args, **kwargs) -> None: ...
    def rotate_refresh_token(self, request) -> bool: ...
    def save_authorization_code(self, client_id, code, request, *args, **kwargs) -> None: ...
    def save_token(self, token, request, *args, **kwargs) -> None: ...
    def save_bearer_token(self, token, request, *args, **kwargs) -> str: ...
    def validate_bearer_token(self, token, scopes, request) -> bool: ...
    def validate_client_id(self, client_id, request, *args, **kwargs) -> bool: ...
    def validate_code(self, client_id, code, client, request, *args, **kwargs) -> bool: ...
    def validate_grant_type(self, client_id, grant_type, client, request, *args, **kwargs) -> bool: ...
    def validate_redirect_uri(self, client_id, redirect_uri, request, *args, **kwargs) -> bool: ...
    def validate_refresh_token(self, refresh_token, client, request, *args, **kwargs) -> bool: ...
    def validate_response_type(self, client_id, response_type, client, request, *args, **kwargs) -> bool: ...
    def validate_scopes(self, client_id, scopes, client, request, *args, **kwargs) -> bool: ...
    def validate_user(self, username, password, client, request, *args, **kwargs) -> bool: ...
    def is_pkce_required(self, client_id, request) -> bool: ...
    def get_code_challenge(self, code, request) -> str: ...
    def get_code_challenge_method(self, code, request) -> str: ...
