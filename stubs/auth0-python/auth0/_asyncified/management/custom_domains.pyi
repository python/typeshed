# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from auth0.management.custom_domains import CustomDomains

@type_check_only
class _CustomDomainsAsync(CustomDomains):
    async def all_async(self) -> list[dict[str, Any]]: ...
    async def get_async(self, id: str) -> dict[str, Any]: ...
    async def delete_async(self, id: str) -> Any: ...
    async def create_new_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def verify_async(self, id: str) -> dict[str, Any]: ...
