from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Kubernetes(VaultApiBase):
    def configure(
        self,
        kubernetes_host,
        kubernetes_ca_cert: Incomplete | None = ...,
        token_reviewer_jwt: Incomplete | None = ...,
        pem_keys: Incomplete | None = ...,
        issuer: Incomplete | None = ...,
        mount_point=...,
        disable_local_ca_jwt: bool = ...,
    ): ...
    def read_config(self, mount_point=...): ...
    def create_role(
        self,
        name,
        bound_service_account_names,
        bound_service_account_namespaces,
        ttl: Incomplete | None = ...,
        max_ttl: Incomplete | None = ...,
        period: Incomplete | None = ...,
        policies: Incomplete | None = ...,
        token_type: str = ...,
        mount_point=...,
        alias_name_source: Incomplete | None = ...,
    ): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name, mount_point=...): ...
    def login(self, role, jwt, use_token: bool = ..., mount_point=...): ...
