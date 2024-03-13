from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

class Aws(VaultApiBase):
    def configure_root_iam_credentials(
        self,
        access_key,
        secret_key,
        region: Incomplete | None = ...,
        iam_endpoint: Incomplete | None = ...,
        sts_endpoint: Incomplete | None = ...,
        max_retries: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def rotate_root_iam_credentials(self, mount_point=...): ...
    def configure_lease(self, lease, lease_max, mount_point=...): ...
    def read_lease_config(self, mount_point=...): ...
    def create_or_update_role(
        self,
        name,
        credential_type,
        policy_document: Incomplete | None = ...,
        default_sts_ttl: Incomplete | None = ...,
        max_sts_ttl: Incomplete | None = ...,
        role_arns: Incomplete | None = ...,
        policy_arns: Incomplete | None = ...,
        legacy_params: bool = ...,
        iam_tags: Incomplete | None = ...,
        mount_point=...,
    ): ...
    def read_role(self, name, mount_point=...): ...
    def list_roles(self, mount_point=...): ...
    def delete_role(self, name, mount_point=...): ...
    def generate_credentials(
        self,
        name,
        role_arn: Incomplete | None = ...,
        ttl: Incomplete | None = ...,
        endpoint: str = ...,
        mount_point=...,
        role_session_name: Incomplete | None = ...,
    ): ...
