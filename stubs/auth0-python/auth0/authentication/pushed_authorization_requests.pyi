from .base import AuthenticationBase as AuthenticationBase
from typing import Any

class PushedAuthorizationRequests(AuthenticationBase):
    def pushed_authorization_request(self, response_type: str, redirect_uri: str, **kwargs) -> Any: ...
