from _typeshed import Incomplete

from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Mount(SystemBackendMixin):
    def list_mounted_secrets_engines(self): ...
    def retrieve_mount_option(self, mount_point, option_name, default_value: Incomplete | None = ...): ...
    def enable_secrets_engine(
        self,
        backend_type,
        path: Incomplete | None = ...,
        description: Incomplete | None = ...,
        config: Incomplete | None = ...,
        plugin_name: Incomplete | None = ...,
        options: Incomplete | None = ...,
        local: bool = ...,
        seal_wrap: bool = ...,
        **kwargs,
    ): ...
    def disable_secrets_engine(self, path): ...
    def read_mount_configuration(self, path): ...
    def tune_mount_configuration(
        self,
        path,
        default_lease_ttl: Incomplete | None = ...,
        max_lease_ttl: Incomplete | None = ...,
        description: Incomplete | None = ...,
        audit_non_hmac_request_keys: Incomplete | None = ...,
        audit_non_hmac_response_keys: Incomplete | None = ...,
        listing_visibility: Incomplete | None = ...,
        passthrough_request_headers: Incomplete | None = ...,
        options: Incomplete | None = ...,
        force_no_cache: Incomplete | None = ...,
        **kwargs,
    ): ...
    def move_backend(self, from_path, to_path): ...
