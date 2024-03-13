from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Ldap(VaultApiBase):
    def configure(
        self,
        userdn: Incomplete | None = ...,
        groupdn: Incomplete | None = ...,
        url: Incomplete | None = ...,
        case_sensitive_names: Incomplete | None = ...,
        starttls: Incomplete | None = ...,
        tls_min_version: Incomplete | None = ...,
        tls_max_version: Incomplete | None = ...,
        insecure_tls: Incomplete | None = ...,
        certificate: Incomplete | None = ...,
        binddn: Incomplete | None = ...,
        bindpass: Incomplete | None = ...,
        userattr: Incomplete | None = ...,
        discoverdn: Incomplete | None = ...,
        deny_null_bind: bool = ...,
        upndomain: Incomplete | None = ...,
        groupfilter: Incomplete | None = ...,
        groupattr: Incomplete | None = ...,
        use_token_groups: Incomplete | None = ...,
        token_ttl: Incomplete | None = ...,
        token_max_ttl: Incomplete | None = ...,
        mount_point=...,
        *,
        anonymous_group_search: Incomplete | None = ...,
        client_tls_cert: Incomplete | None = ...,
        client_tls_key: Incomplete | None = ...,
        connection_timeout: Incomplete | None = ...,
        dereference_aliases: Incomplete | None = ...,
        max_page_size: Incomplete | None = ...,
        request_timeout: Incomplete | None = ...,
        token_bound_cidrs: Incomplete | None = ...,
        token_explicit_max_ttl: Incomplete | None = ...,
        token_no_default_policy: Incomplete | None = ...,
        token_num_uses: Incomplete | None = ...,
        token_period: Incomplete | None = ...,
        token_policies: Incomplete | None = ...,
        token_type: Incomplete | None = ...,
        userfilter: Incomplete | None = ...,
        username_as_alias: Incomplete | None = ...,
    ): ...
    def read_configuration(self, mount_point=...): ...
    def create_or_update_group(self, name, policies: Incomplete | None = ..., mount_point=...): ...
    def list_groups(self, mount_point=...): ...
    def read_group(self, name, mount_point=...): ...
    def delete_group(self, name, mount_point=...): ...
    def create_or_update_user(
        self, username, policies: Incomplete | None = ..., groups: Incomplete | None = ..., mount_point=...
    ): ...
    def list_users(self, mount_point=...): ...
    def read_user(self, username, mount_point=...): ...
    def delete_user(self, username, mount_point=...): ...
    def login(self, username, password, use_token: bool = ..., mount_point=...): ...
