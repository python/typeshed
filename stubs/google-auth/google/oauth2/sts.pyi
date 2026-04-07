from collections.abc import Mapping, Sequence

from google.auth.transport import Request as _Request
from google.oauth2 import utils

class Client(utils.OAuthClientAuthHandler):
    def __init__(self, token_exchange_endpoint: str, client_authentication: utils.ClientAuthentication | None = None) -> None: ...
    def exchange_token(
        self,
        request: _Request,
        grant_type: str,
        subject_token: str,
        subject_token_type: str,
        resource: str | None = None,
        audience: str | None = None,
        scopes: Sequence[str] | None = None,
        requested_token_type: str | None = None,
        actor_token: str | None = None,
        actor_token_type: str | None = None,
        additional_options: Mapping[str, str] | None = None,
        additional_headers: Mapping[str, str] | None = None,
    ) -> Mapping[str, str]: ...
    def refresh_token(self, request: _Request, refresh_token: str) -> Mapping[str, str]: ...
    def revoke_token(self, request: _Request, token: str, token_type_hint: str, revoke_url: str) -> Mapping[str, str]: ...
