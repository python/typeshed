from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

logger: Incomplete

class Kv(VaultApiBase):
    allowed_kv_versions: Incomplete
    def __init__(self, adapter, default_kv_version: str = "2") -> None: ...
    @property
    def v1(self): ...
    @property
    def v2(self): ...
    @property
    def default_kv_version(self): ...
    @default_kv_version.setter
    def default_kv_version(self, default_kv_version) -> None: ...
    def __getattr__(self, item): ...
