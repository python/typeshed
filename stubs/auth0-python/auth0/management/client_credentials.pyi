from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class ClientCredentials:
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
    def all(self, client_id: str) -> list[dict[str, Incomplete]]: ...
    def get(self, client_id: str, id: str) -> dict[str, Incomplete]: ...
    def create(self, client_id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def delete(self, client_id: str, id: str) -> dict[str, Incomplete]: ...
