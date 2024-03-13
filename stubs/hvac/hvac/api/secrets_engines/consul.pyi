from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Consul(VaultApiBase):
    def configure_access(self, address, token, scheme: Incomplete | None = ..., mount_point=...): ...
    def create_or_update_role(
        self,
        name,
        policy: Incomplete | None = ...,
        policies: Incomplete | None = ...,
        token_type: Incomplete | None = ...,
        local: Incomplete | None = ...,
        ttl: Incomplete | None = ...,
        max_ttl: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name, mount_point=...): ...
    def generate_credentials(self, name, mount_point=...): ...
