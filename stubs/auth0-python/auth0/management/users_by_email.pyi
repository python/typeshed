from _typeshed import Incomplete

from ..rest import RestClient as RestClient, RestClientOptions as RestClientOptions
from ..types import TimeoutType as TimeoutType

class UsersByEmail:
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
    def search_users_by_email(
        self,
        email: str,
        fields: list[str] | None = None,
        include_fields: bool = True,
        page: int = 0,
        per_page: int = 25,
        include_totals: bool = True,
        sort: str | None = None,
        connection: str | None = None,
        q: str | None = None,
    ) -> dict[str, Incomplete]: ...
    async def search_users_by_email_async(
        self,
        email: str,
        fields: list[str] | None = None,
        include_fields: bool = True,
        page: int = 0,
        per_page: int = 25,
        include_totals: bool = True,
        sort: str | None = None,
        connection: str | None = None,
        q: str | None = None,
    ) -> dict[str, Incomplete]: ...
