from _typeshed import Incomplete
from collections.abc import Iterable

from ...common import Request

class RequestValidator:
    def __init__(self) -> None: ...
    @property
    def allowed_signature_methods(self) -> Iterable[str]: ...
    @property
    def safe_characters(self) -> set[str]: ...
    @property
    def client_key_length(self) -> tuple[int, int]: ...
    @property
    def request_token_length(self) -> tuple[int, int]: ...
    @property
    def access_token_length(self) -> tuple[int, int]: ...
    @property
    def timestamp_lifetime(self) -> int: ...
    @property
    def nonce_length(self) -> tuple[int, int]: ...
    @property
    def verifier_length(self) -> tuple[int, int]: ...
    @property
    def realms(self) -> list[str]: ...
    @property
    def enforce_ssl(self) -> bool: ...
    def check_client_key(self, client_key: str) -> bool: ...
    def check_request_token(self, request_token: str) -> bool: ...
    def check_access_token(self, request_token: str) -> bool: ...
    def check_nonce(self, nonce: str) -> bool: ...
    def check_verifier(self, verifier) -> bool: ...
    def check_realms(self, realms: list[str]) -> bool: ...
    @property
    def dummy_client(self) -> None: ...
    @property
    def dummy_request_token(self) -> None: ...
    @property
    def dummy_access_token(self) -> None: ...
    def get_client_secret(self, client_key: str, request: Request) -> str: ...
    def get_request_token_secret(self, client_key: str, token: str, request: Request) -> str: ...
    def get_access_token_secret(self, client_key: str, token: str, request: Request) -> str: ...
    def get_default_realms(self, client_key: str, request: Request) -> list[str]: ...
    def get_realms(self, token: str, request: Request) -> list[str]: ...
    def get_redirect_uri(self, token: str, request: Request) -> str: ...
    def get_rsa_key(self, client_key: str, request: Request) -> str: ...
    def invalidate_request_token(self, client_key: str, request_token: str, request: Request) -> None: ...
    def validate_client_key(self, client_key: str, request: Request) -> bool: ...
    def validate_request_token(self, client_key: str, token: str, request: Request) -> bool: ...
    def validate_access_token(self, client_key: str, token: str, request: Request) -> bool: ...
    def validate_timestamp_and_nonce(
        self,
        client_key: str,
        timestamp,
        nonce: str,
        request: Request,
        request_token: Incomplete | None = ...,
        access_token: Incomplete | None = ...,
    ) -> bool: ...
    def validate_redirect_uri(self, client_key: str, redirect_uri, request: Request) -> bool: ...
    def validate_requested_realms(self, client_key: str, realms: list[str], request: Request) -> bool: ...
    def validate_realms(
        self, client_key: str, token: str, request: Request, uri: str | None = None, realms: list[str] | None = None
    ) -> bool: ...
    def validate_verifier(self, client_key: str, token: str, verifier, request: Request) -> bool: ...
    def verify_request_token(self, token: str, request: Request) -> bool: ...
    def verify_realms(self, token: str, realms: list[str], request: Request) -> bool: ...
    def save_access_token(self, token: str, request: Request) -> None: ...
    def save_request_token(self, token: str, request: Request) -> None: ...
    def save_verifier(self, token: str, verifier, request: Request) -> None: ...
