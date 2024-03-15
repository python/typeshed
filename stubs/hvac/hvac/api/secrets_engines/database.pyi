from _typeshed import Incomplete

from hvac.api.vault_api_base import VaultApiBase

DEFAULT_MOUNT_POINT: str

class Database(VaultApiBase):
    def configure(
        self,
        name,
        plugin_name,
        verify_connection: Incomplete | None = None,
        allowed_roles: Incomplete | None = None,
        root_rotation_statements: Incomplete | None = None,
        mount_point="database",
        *args,
        **kwargs,
    ): ...
    def rotate_root_credentials(self, name, mount_point="database"): ...
    def read_connection(self, name, mount_point="database"): ...
    def list_connections(self, mount_point="database"): ...
    def delete_connection(self, name, mount_point="database"): ...
    def reset_connection(self, name, mount_point="database"): ...
    def create_role(
        self,
        name,
        db_name,
        creation_statements,
        default_ttl: Incomplete | None = None,
        max_ttl: Incomplete | None = None,
        revocation_statements: Incomplete | None = None,
        rollback_statements: Incomplete | None = None,
        renew_statements: Incomplete | None = None,
        mount_point="database",
    ): ...
    def create_static_role(
        self, name, db_name, username, rotation_statements, rotation_period: int = 86400, mount_point="database"
    ): ...
    def read_role(self, name, mount_point="database"): ...
    def read_static_role(self, name, mount_point="database"): ...
    def list_roles(self, mount_point="database"): ...
    def list_static_roles(self, mount_point="database"): ...
    def delete_role(self, name, mount_point="database"): ...
    def delete_static_role(self, name, mount_point="database"): ...
    def generate_credentials(self, name, mount_point="database"): ...
    def get_static_credentials(self, name, mount_point="database"): ...
    def rotate_static_role_credentials(self, name, mount_point="database"): ...
