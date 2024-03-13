from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Token(VaultApiBase):
    def create(
        self,
        id: Incomplete | None = ...,
        role_name: Incomplete | None = ...,
        policies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        no_parent: bool = ...,
        no_default_policy: bool = ...,
        renewable: bool = ...,
        ttl: Incomplete | None = ...,
        type: Incomplete | None = ...,
        explicit_max_ttl: Incomplete | None = ...,
        display_name: str = ...,
        num_uses: int = ...,
        period: Incomplete | None = ...,
        entity_alias: Incomplete | None = ...,
        wrap_ttl: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def create_orphan(
        self,
        id: Incomplete | None = ...,
        role_name: Incomplete | None = ...,
        policies: Incomplete | None = ...,
        meta: Incomplete | None = ...,
        no_default_policy: bool = ...,
        renewable: bool = ...,
        ttl: Incomplete | None = ...,
        type: Incomplete | None = ...,
        explicit_max_ttl: Incomplete | None = ...,
        display_name: str = ...,
        num_uses: int = ...,
        period: Incomplete | None = ...,
        entity_alias: Incomplete | None = ...,
        wrap_ttl: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def list_accessors(self, mount_point=...): ...
    def lookup(self, token, mount_point=...): ...
    def lookup_self(self, mount_point=...): ...
    def lookup_accessor(self, accessor, mount_point=...): ...
    def renew(self, token, increment: Incomplete | None = ..., wrap_ttl: Incomplete | None = ..., mount_point=...): ...
    def renew_self(self, increment: Incomplete | None = ..., wrap_ttl: Incomplete | None = ..., mount_point=...): ...
    def renew_accessor(
        self, accessor, increment: Incomplete | None = ..., wrap_ttl: Incomplete | None = ..., mount_point=...
    ): ...
    def revoke(self, token, mount_point=...): ...
    def revoke_self(self, mount_point=...): ...
    def revoke_accessor(self, accessor, mount_point=...): ...
    def revoke_and_orphan_children(self, token, mount_point=...): ...
    def read_role(self, role_name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def create_or_update_role(
        self,
        role_name,
        allowed_policies: Incomplete | None = ...,
        disallowed_policies: Incomplete | None = ...,
        orphan: bool = ...,
        renewable: bool = ...,
        path_suffix: Incomplete | None = ...,
        allowed_entity_aliases: Incomplete | None = ...,
        mount_point=...,
        token_period: Incomplete | None = ...,
        token_explicit_max_ttl: Incomplete | None = ...,
    ): ...
    def delete_role(self, role_name, mount_point=...): ...
    def tidy(self, mount_point=...): ...
