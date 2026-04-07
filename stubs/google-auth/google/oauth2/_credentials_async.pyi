from _typeshed import Incomplete
from collections.abc import Mapping

from google.auth.transport import Request as _Request
from google.oauth2 import credentials as oauth2_credentials

class Credentials(oauth2_credentials.Credentials):
    token: Incomplete
    expiry: Incomplete

    async def refresh(self, request: _Request) -> None: ...
    async def before_request(self, request: _Request, method: str, url: str, headers: Mapping[str, str]) -> None: ...

class UserAccessTokenCredentials(oauth2_credentials.UserAccessTokenCredentials): ...
