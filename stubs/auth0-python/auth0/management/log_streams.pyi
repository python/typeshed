from _typeshed import Incomplete
from builtins import list as _list

from ..rest import RestClientOptions
from ..types import TimeoutType

class LogStreams:
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
    def list(self) -> _list[dict[str, Incomplete]]: ...
    def get(self, id: str) -> dict[str, Incomplete]: ...
    def create(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def delete(self, id: str) -> dict[str, Incomplete]: ...
    def update(self, id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
