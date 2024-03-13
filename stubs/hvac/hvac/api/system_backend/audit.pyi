from _typeshed import Incomplete

from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Audit(SystemBackendMixin):
    def list_enabled_audit_devices(self): ...
    def enable_audit_device(
        self,
        device_type,
        description: Incomplete | None = ...,
        options: Incomplete | None = ...,
        path: Incomplete | None = ...,
        local: Incomplete | None = ...,
    ): ...
    def disable_audit_device(self, path): ...
    def calculate_hash(self, path, input_to_hash): ...
