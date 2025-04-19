# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from .base import _AuthenticationBaseAsync

@type_check_only
class _SocialAsync(_AuthenticationBaseAsync):
    async def login_async(self, access_token: str, connection: str, scope: str = "openid") -> Any: ...
