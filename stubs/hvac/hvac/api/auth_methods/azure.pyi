from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str
logger: Incomplete

class Azure(VaultApiBase):
    def configure(
        self,
        tenant_id,
        resource,
        environment: Incomplete | None = ...,
        client_id: Incomplete | None = ...,
        client_secret: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def read_config(self, mount_point=...): ...
    def delete_config(self, mount_point=...): ...
    def create_role(
        self,
        name,
        policies: Incomplete | None = ...,
        ttl: Incomplete | None = ...,
        max_ttl: Incomplete | None = ...,
        period: Incomplete | None = ...,
        bound_service_principal_ids: Incomplete | None = ...,
        bound_group_ids: Incomplete | None = ...,
        bound_locations: Incomplete | None = ...,
        bound_subscription_ids: Incomplete | None = ...,
        bound_resource_groups: Incomplete | None = ...,
        bound_scale_sets: Incomplete | None = ...,
        num_uses: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name, mount_point=...): ...
    def login(
        self,
        role,
        jwt,
        subscription_id: Incomplete | None = ...,
        resource_group_name: Incomplete | None = ...,
        vm_name: Incomplete | None = ...,
        vmss_name: Incomplete | None = ...,
        use_token: bool = ...,
        mount_point=...,
    ): ...
