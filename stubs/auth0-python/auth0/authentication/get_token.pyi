from typing import Any

from .base import AuthenticationBase as AuthenticationBase

class GetToken(AuthenticationBase):
    def authorization_code(self, code: str, redirect_uri: str | None, grant_type: str = "authorization_code") -> Any: ...
    def authorization_code_pkce(
        self, code_verifier: str, code: str, redirect_uri: str | None, grant_type: str = "authorization_code"
    ) -> Any: ...
    def client_credentials(
        self, audience: str, grant_type: str = "client_credentials", organization: str | None = None
    ) -> Any: ...
    def login(
        self,
        username: str,
        password: str,
        scope: str | None = None,
        realm: str | None = None,
        audience: str | None = None,
        grant_type: str = "http://auth0.com/oauth/grant-type/password-realm",
        forwarded_for: str | None = None,
    ) -> Any: ...
    def refresh_token(self, refresh_token: str, scope: str = "", grant_type: str = "refresh_token") -> Any: ...
    def passwordless_login(self, username: str, otp: str, realm: str, scope: str, audience: str) -> Any: ...
    def backchannel_login(self, auth_req_id: str, grant_type: str = "urn:openid:params:grant-type:ciba") -> Any: ...
