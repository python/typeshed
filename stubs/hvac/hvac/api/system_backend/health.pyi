from _typeshed import Incomplete

from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Health(SystemBackendMixin):
    def read_health_status(
        self,
        standby_ok: Incomplete | None = ...,
        active_code: Incomplete | None = ...,
        standby_code: Incomplete | None = ...,
        dr_secondary_code: Incomplete | None = ...,
        performance_standby_code: Incomplete | None = ...,
        sealed_code: Incomplete | None = ...,
        uninit_code: Incomplete | None = ...,
        method: str = ...,
    ): ...
