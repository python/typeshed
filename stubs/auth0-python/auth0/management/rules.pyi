from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class Rules:
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
    def all(
        self,
        stage: str = "login_success",
        enabled: bool = True,
        fields: list[str] | None = None,
        include_fields: bool = True,
        page: int | None = None,
        per_page: int | None = None,
        include_totals: bool = False,
    ) -> dict[str, Incomplete]: ...
    def create(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get(self, id: str, fields: list[str] | None = None, include_fields: bool = True) -> dict[str, Incomplete]: ...
    def delete(self, id: str): ...
    def update(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
