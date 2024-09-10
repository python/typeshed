from _typeshed import Incomplete

from authlib.oauth1 import ClientAuth
from authlib.oauth1.client import OAuth1Client
from requests import Session
from requests.auth import AuthBase

class OAuth1Auth(AuthBase, ClientAuth):
    def __call__(self, req): ...

class OAuth1Session(OAuth1Client, Session):
    auth_class = OAuth1Auth
    def __init__(
        self,
        client_id,
        client_secret: Incomplete | None = None,
        token: Incomplete | None = None,
        token_secret: Incomplete | None = None,
        redirect_uri: Incomplete | None = None,
        rsa_key: Incomplete | None = None,
        verifier: Incomplete | None = None,
        signature_method="HMAC-SHA1",
        signature_type="HEADER",
        force_include_body: bool = False,
        **kwargs,
    ) -> None: ...
    def rebuild_auth(self, prepared_request, response) -> None: ...
    @staticmethod
    def handle_error(error_type, error_description) -> None: ...
