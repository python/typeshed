from typing_extensions import TypeAlias

from authlib.oauth2.rfc6749 import BaseGrant, TokenEndpointMixin, TokenMixin

_ServerResponse: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class RefreshTokenGrant(BaseGrant, TokenEndpointMixin):
    GRANT_TYPE: str
    INCLUDE_NEW_REFRESH_TOKEN: bool
    def validate_token_request(self) -> None: ...
    def create_token_response(self) -> _ServerResponse: ...
    def issue_token(self, user, refresh_token: TokenMixin) -> dict[str, str | int]: ...
    def authenticate_refresh_token(self, refresh_token: str) -> TokenMixin: ...
    def authenticate_user(self, refresh_token): ...
    def revoke_old_credential(self, refresh_token: TokenMixin) -> None: ...
