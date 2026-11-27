from logging import Logger
from typing import Any

from oauthlib.oauth1 import Client
from requests.auth import AuthBase

CONTENT_TYPE_FORM_URLENCODED: str
CONTENT_TYPE_MULTI_PART: str
log: Logger

class OAuth1(AuthBase):
    client_class: type[Client]
    client: Client
    force_include_body: bool
    def __init__(
        self,
        client_key: str | bytes,
        client_secret: str | bytes | None = None,
        resource_owner_key: str | bytes | None = None,
        resource_owner_secret: str | bytes | None = None,
        callback_uri: str | bytes | None = None,
        signature_method: str | bytes = "HMAC-SHA1",
        signature_type: str | bytes = "AUTH_HEADER",
        rsa_key: str | bytes | None = None,
        verifier: str | bytes | None = None,
        decoding: str | None = "utf-8",
        client_class: type[Client] | None = None,
        force_include_body: bool = False,
        *,
        realm: str | bytes | None = None,
        encoding: str = "utf-8",
        nonce: str | bytes | None = None,
        timestamp: str | bytes | None = None,
        **kwargs: Any,  # passed to client_class's __init__
    ) -> None: ...
