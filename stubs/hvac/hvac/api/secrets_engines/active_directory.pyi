from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class ActiveDirectory(VaultApiBase):
    def configure(
        self,
        binddn: Incomplete | None = ...,
        bindpass: Incomplete | None = ...,
        url: Incomplete | None = ...,
        userdn: Incomplete | None = ...,
        upndomain: Incomplete | None = ...,
        ttl: Incomplete | None = ...,
        max_ttl: Incomplete | None = ...,
        mount_point=...,
        *args,
        **kwargs,
    ): ...
    def read_config(self, mount_point=...): ...
    def create_or_update_role(
        self, name, service_account_name: Incomplete | None = ..., ttl: Incomplete | None = ..., mount_point=...
    ): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name, mount_point=...): ...
    def generate_credentials(self, name, mount_point=...): ...
