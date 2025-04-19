from _typeshed import Incomplete

from ..rest import RestClientOptions
from ..types import TimeoutType

class Branding:
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
    def get(self) -> dict[str, Incomplete]: ...
    def update(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_template_universal_login(self) -> dict[str, Incomplete]: ...
    def delete_template_universal_login(self): ...
    def update_template_universal_login(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def get_default_branding_theme(self) -> dict[str, Incomplete]: ...
    def get_branding_theme(self, theme_id: str) -> dict[str, Incomplete]: ...
    def delete_branding_theme(self, theme_id: str): ...
    def update_branding_theme(self, theme_id: str, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
    def create_branding_theme(self, body: dict[str, Incomplete]) -> dict[str, Incomplete]: ...
