from _typeshed import Incomplete

from authlib.oauth2.rfc7521 import AssertionClient
from requests import Session

from .oauth2_session import OAuth2Auth

class AssertionAuth(OAuth2Auth):
    def ensure_active_token(self): ...

class AssertionSession(AssertionClient, Session):
    token_auth_class = AssertionAuth
    JWT_BEARER_GRANT_TYPE: Incomplete
    ASSERTION_METHODS: Incomplete
    DEFAULT_GRANT_TYPE = JWT_BEARER_GRANT_TYPE
    default_timeout: Incomplete
    def __init__(
        self,
        token_endpoint,
        issuer,
        subject,
        audience: Incomplete | None = None,
        grant_type: Incomplete | None = None,
        claims: Incomplete | None = None,
        token_placement: str = "header",
        scope: Incomplete | None = None,
        default_timeout: Incomplete | None = None,
        leeway: int = 60,
        **kwargs,
    ) -> None: ...
    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None,
        json=None,
        withhold_token: bool = False,
    ): ...
