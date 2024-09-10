from _typeshed import Incomplete

from authlib.oauth2.auth import ClientAuth, TokenAuth
from authlib.oauth2.client import OAuth2Client
from requests import Session
from requests.auth import AuthBase

from ..base_client import OAuthError

__all__ = ["OAuth2Session", "OAuth2Auth"]

class OAuth2Auth(AuthBase, TokenAuth):
    def ensure_active_token(self) -> None: ...
    def __call__(self, req): ...

class OAuth2ClientAuth(AuthBase, ClientAuth):
    def __call__(self, req): ...

class OAuth2Session(OAuth2Client, Session):
    client_auth_class = OAuth2ClientAuth
    token_auth_class = OAuth2Auth
    oauth_error_class = OAuthError
    SESSION_REQUEST_PARAMS: Incomplete
    default_timeout: Incomplete
    def __init__(
        self,
        client_id: Incomplete | None = None,
        client_secret: Incomplete | None = None,
        token_endpoint_auth_method: Incomplete | None = None,
        revocation_endpoint_auth_method: Incomplete | None = None,
        scope: Incomplete | None = None,
        state: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        token: Incomplete | None = None,
        token_placement: str = "header",
        update_token: Incomplete | None = None,
        leeway: int = 60,
        default_timeout: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def fetch_access_token(self, url: Incomplete | None = None, **kwargs): ...
    def request(self, method, url, withhold_token: bool = False, auth: Incomplete | None = None, **kwargs): ...
