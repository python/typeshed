# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from auth0.authentication.users import Users

@type_check_only
class _UsersAsync(Users):
    async def userinfo_async(self, access_token: str) -> dict[str, Any]: ...
