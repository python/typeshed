from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

class AppRole(VaultApiBase):
    def create_or_update_approle(
        self,
        role_name,
        bind_secret_id: Incomplete | None = ...,
        secret_id_bound_cidrs: Incomplete | None = ...,
        secret_id_num_uses: Incomplete | None = ...,
        secret_id_ttl: Incomplete | None = ...,
        enable_local_secret_ids: Incomplete | None = ...,
        token_ttl: Incomplete | None = ...,
        token_max_ttl: Incomplete | None = ...,
        token_policies: Incomplete | None = ...,
        token_bound_cidrs: Incomplete | None = ...,
        token_explicit_max_ttl: Incomplete | None = ...,
        token_no_default_policy: Incomplete | None = ...,
        token_num_uses: Incomplete | None = ...,
        token_period: Incomplete | None = ...,
        token_type: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def list_roles(self, mount_point=...): ...
    def read_role(self, role_name, mount_point=...): ...
    def delete_role(self, role_name, mount_point=...): ...
    def read_role_id(self, role_name, mount_point=...): ...
    def update_role_id(self, role_name, role_id, mount_point=...): ...
    def generate_secret_id(
        self,
        role_name,
        metadata: Incomplete | None = ...,
        cidr_list: Incomplete | None = ...,
        token_bound_cidrs: Incomplete | None = ...,
        mount_point=...,
        wrap_ttl: Incomplete | None = ...,
    ): ...
    def create_custom_secret_id(
        self,
        role_name,
        secret_id,
        metadata: Incomplete | None = ...,
        cidr_list: Incomplete | None = ...,
        token_bound_cidrs: Incomplete | None = ...,
        mount_point=...,
        wrap_ttl: Incomplete | None = ...,
    ): ...
    def read_secret_id(self, role_name, secret_id, mount_point=...): ...
    def destroy_secret_id(self, role_name, secret_id, mount_point=...): ...
    def list_secret_id_accessors(self, role_name, mount_point=...): ...
    def read_secret_id_accessor(self, role_name, secret_id_accessor, mount_point=...): ...
    def destroy_secret_id_accessor(self, role_name, secret_id_accessor, mount_point=...): ...
    def login(self, role_id, secret_id: Incomplete | None = ..., use_token: bool = ..., mount_point=...): ...
