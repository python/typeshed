from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class ResourceServers:
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
    def create(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_all(self, page: int | None = None, per_page: int | None = None, include_totals: bool = False): ...
    def get(self, id: str) -> dict[str, Incomplete]: ...
    def delete(self, id: str): ...
    def update(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
