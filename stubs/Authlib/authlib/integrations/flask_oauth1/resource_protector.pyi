from _typeshed import Incomplete

from authlib.oauth1 import ResourceProtector as _ResourceProtector

class ResourceProtector(_ResourceProtector):
    query_client: Incomplete
    query_token: Incomplete
    app: Incomplete
    def __init__(
        self,
        app: Incomplete | None = None,
        query_client: Incomplete | None = None,
        query_token: Incomplete | None = None,
        exists_nonce: Incomplete | None = None,
    ) -> None: ...
    SUPPORTED_SIGNATURE_METHODS: Incomplete
    def init_app(
        self,
        app,
        query_client: Incomplete | None = None,
        query_token: Incomplete | None = None,
        exists_nonce: Incomplete | None = None,
    ) -> None: ...
    def get_client_by_id(self, client_id): ...
    def get_token_credential(self, request): ...
    def exists_nonce(self, nonce, request): ...
    def acquire_credential(self): ...
    def __call__(self, scope: Incomplete | None = None): ...

current_credential: Incomplete
