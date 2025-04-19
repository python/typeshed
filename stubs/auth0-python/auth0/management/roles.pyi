from _typeshed import Incomplete
from builtins import list as _list

from ..rest import RestClientOptions
from ..types import TimeoutType

class Roles:
    domain: Incomplete
    protocol: Incomplete
    client: Incomplete
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def list(
        self, page: int = 0, per_page: int = 25, include_totals: bool = True, name_filter: str | None = None
    ) -> dict[str, Incomplete]: ...
    def create(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get(self, id: str) -> dict[str, Incomplete]: ...
    def delete(self, id: str): ...
    def update(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def list_users(
        self,
        id: str,
        page: int = 0,
        per_page: int = 25,
        include_totals: bool = True,
        from_param: str | None = None,
        take: int | None = None,
    ) -> dict[str, Incomplete]: ...
    def add_users(self, id: str, users: _list[str]) -> dict[str, Incomplete]: ...
    def list_permissions(
        self, id: str, page: int = 0, per_page: int = 25, include_totals: bool = True
    ) -> dict[str, Incomplete]: ...
    def remove_permissions(self, id: str, permissions: _list[dict[str, str]]): ...
    def add_permissions(self, id: str, permissions: _list[dict[str, str]]) -> dict[str, Incomplete]: ...
