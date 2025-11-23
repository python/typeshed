from _typeshed import Incomplete

from ..rest import RestClient, RestClientOptions
from ..types import TimeoutType

class NetworkAcls:
    domain: str
    protocol: str
    client: RestClient
    def __init__(
        self,
        domain: str,
        token: str,
        telemetry: bool = True,
        timeout: TimeoutType = 5.0,
        protocol: str = "https",
        rest_options: RestClientOptions | None = None,
    ) -> None: ...
    def all(self, page: int = 0, per_page: int = 25, include_totals: bool = True) -> list[dict[str, Incomplete]]: ...
    def create(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get(self, id: str) -> dict[str, Incomplete]: ...
    def delete(self, id: str) -> None: ...
    def update(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def update_partial(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
