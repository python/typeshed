from collections.abc import Mapping

import google
import google.auth
import google.auth.transport
from google.auth import credentials

class Credentials(credentials.Credentials):
    token: str

    def __init__(self, token: str) -> None: ...
    @property
    def expired(self) -> bool: ...
    @property
    def valid(self) -> bool: ...
    def refresh(self, request: google.auth.transport.Request) -> None: ...
    def apply(self, headers: Mapping[str, str], token: str | None = None) -> None: ...
    def before_request(
        self, request: google.auth.transport.Request, method: str, url: str, headers: Mapping[str, str]
    ) -> None: ...
