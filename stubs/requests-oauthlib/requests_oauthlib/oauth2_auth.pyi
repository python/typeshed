from _typeshed import Incomplete

from oauthlib.oauth2 import Client
from requests.auth import AuthBase

class OAuth2(AuthBase):
    def __init__(
        self, client_id: str | None = None, client: Client | None = None, token: dict[str, Incomplete] | None = None
    ) -> None: ...
