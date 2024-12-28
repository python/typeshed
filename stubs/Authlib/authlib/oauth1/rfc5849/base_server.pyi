from _typeshed import Incomplete

class BaseServer:
    SIGNATURE_METHODS: Incomplete
    SUPPORTED_SIGNATURE_METHODS: Incomplete
    EXPIRY_TIME: int
    @classmethod
    def register_signature_method(cls, name, verify) -> None: ...
    def validate_timestamp_and_nonce(self, request) -> None: ...
    def validate_oauth_signature(self, request) -> None: ...
    def get_client_by_id(self, client_id) -> None: ...
    def exists_nonce(self, nonce, request) -> None: ...
