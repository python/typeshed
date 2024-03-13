from _typeshed import Incomplete

from hvac.api.system_backend.system_backend_mixin import SystemBackendMixin

class Init(SystemBackendMixin):
    def read_init_status(self): ...
    def is_initialized(self): ...
    def initialize(
        self,
        secret_shares: Incomplete | None = ...,
        secret_threshold: Incomplete | None = ...,
        pgp_keys: Incomplete | None = ...,
        root_token_pgp_key: Incomplete | None = ...,
        stored_shares: Incomplete | None = ...,
        recovery_shares: Incomplete | None = ...,
        recovery_threshold: Incomplete | None = ...,
        recovery_pgp_keys: Incomplete | None = ...,
    ): ...
