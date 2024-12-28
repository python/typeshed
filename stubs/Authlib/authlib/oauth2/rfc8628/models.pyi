class DeviceCredentialMixin:
    def get_client_id(self) -> None: ...
    def get_scope(self) -> None: ...
    def get_user_code(self) -> None: ...
    def is_expired(self) -> None: ...

class DeviceCredentialDict(dict[str, object], DeviceCredentialMixin):
    def get_client_id(self): ...
    def get_scope(self): ...
    def get_user_code(self): ...
    def get_nonce(self): ...
    def get_auth_time(self): ...
    def is_expired(self): ...
