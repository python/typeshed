from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str
logger: Incomplete

class Gcp(VaultApiBase):
    def configure(self, credentials: Incomplete | None = ..., google_certs_endpoint=..., mount_point=...): ...
    def read_config(self, mount_point=...): ...
    def delete_config(self, mount_point=...): ...
    def create_role(
        self,
        name,
        role_type,
        project_id,
        ttl: Incomplete | None = ...,
        max_ttl: Incomplete | None = ...,
        period: Incomplete | None = ...,
        policies: Incomplete | None = ...,
        bound_service_accounts: Incomplete | None = ...,
        max_jwt_exp: Incomplete | None = ...,
        allow_gce_inference: Incomplete | None = ...,
        bound_zones: Incomplete | None = ...,
        bound_regions: Incomplete | None = ...,
        bound_instance_groups: Incomplete | None = ...,
        bound_labels: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def edit_service_accounts_on_iam_role(
        self, name, add: Incomplete | None = ..., remove: Incomplete | None = ..., mount_point=...
    ): ...
    def edit_labels_on_gce_role(self, name, add: Incomplete | None = ..., remove: Incomplete | None = ..., mount_point=...): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, role, mount_point=...): ...
    def login(self, role, jwt, use_token: bool = ..., mount_point=...): ...
