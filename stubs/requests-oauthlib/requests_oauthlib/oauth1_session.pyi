from _typeshed import Incomplete
from collections.abc import Iterable
from logging import Logger
from typing import Any, TypeAlias, TypedDict, type_check_only

import requests
from oauthlib.oauth1 import Client

from . import OAuth1

# should be dict[str, str] but could look different
_ParsedToken: TypeAlias = dict[str, Incomplete]

@type_check_only
class _TokenDict(TypedDict, total=False):
    oauth_token: Incomplete  # oauthlib.oauth1.Client.resource_owner_key
    oauth_token_secret: Incomplete  # oauthlib.oauth1.Client.resource_token_secret
    oauth_verifier: Incomplete  # oauthlib.oauth1.Client.oauth_verifier

log: Logger

def urldecode(body: str | bytes | bytearray) -> Any: ...

class TokenRequestDenied(ValueError):
    response: requests.Response
    def __init__(self, message: str, response: requests.Response) -> None: ...
    @property
    def status_code(self) -> int: ...

class TokenMissing(ValueError):
    response: requests.Response
    def __init__(self, message: str, response: requests.Response) -> None: ...

class VerifierMissing(ValueError): ...

class OAuth1Session(requests.Session):
    auth: OAuth1
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
        client_class: type[Client] | None = None,
        force_include_body: bool = False,
        *,
        decoding: str | None = "utf-8",
        realm: str | bytes | None = None,
        encoding: str = "utf-8",
        nonce: str | bytes | None = None,
        timestamp: str | bytes | None = None,
        **kwargs: Any,  # passed to client_class's __init__
    ) -> None: ...

    @property
    def token(self) -> _TokenDict: ...
    @token.setter
    def token(self, value: _TokenDict) -> None: ...

    @property
    def authorized(self) -> bool: ...
    def authorization_url(self, url: str, request_token: str | None = None, **kwargs: Any) -> str: ...
    def fetch_request_token(self, url: str, realm: Iterable[str] | None = None, **request_kwargs: Any) -> _ParsedToken: ...
    def fetch_access_token(self, url: str, verifier: str | None = None, **request_kwargs: Any) -> _ParsedToken: ...
    def parse_authorization_response(self, url: str) -> _ParsedToken: ...
    def rebuild_auth(self, prepared_request: requests.PreparedRequest, response: requests.Response) -> None: ...
