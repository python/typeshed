from .base import AuthenticationBase as AuthenticationBase
from typing import Any

class RevokeToken(AuthenticationBase):
    def revoke_refresh_token(self, token: str) -> Any: ...
