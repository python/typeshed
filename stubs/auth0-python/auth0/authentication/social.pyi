from .base import AuthenticationBase as AuthenticationBase
from typing import Any

class Social(AuthenticationBase):
    def login(self, access_token: str, connection: str, scope: str = 'openid') -> Any: ...
