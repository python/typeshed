from collections.abc import Mapping
from logging import Logger
from typing import Any, Final, overload
from typing_extensions import deprecated

from . import oauth2

logger: Logger

@overload
def decode_part(raw: str, encoding: str = "utf-8") -> str: ...
@overload
def decode_part(raw: str, encoding: None) -> bytes: ...

base64decode = decode_part

class IdTokenError(RuntimeError):
    def __init__(self, reason: str, now: float, claims: Mapping[str, Any]) -> None: ...

class _IdTokenTimeError(IdTokenError):
    def __init__(self, reason: str, now: float, claims: Mapping[str, Any]) -> None: ...
    def log(self) -> None: ...

class IdTokenIssuerError(IdTokenError): ...
class IdTokenAudienceError(IdTokenError): ...
class IdTokenNonceError(IdTokenError): ...

@deprecated(
    "decode_id_token() is deprecated. MSAL's token acquisition no longer validates the ID token; "
    "validation is the application's responsibility."
)
def decode_id_token(
    id_token: str, client_id: str | None = None, issuer: str | None = None, nonce: str | None = None, now: float | None = None
) -> dict[str, Any]: ...

class Prompt:
    NONE: Final = "none"
    LOGIN: Final = "login"
    CONSENT: Final = "consent"
    SELECT_ACCOUNT: Final = "select_account"
    CREATE: Final = "create"

class Client(oauth2.Client):
    @deprecated(
        "decode_id_token() is deprecated. MSAL's token acquisition no longer validates the ID token; "
        "validation is the application's responsibility."
    )
    def decode_id_token(self, id_token: str, nonce: str | None = None) -> dict[str, Any]: ...
    @deprecated("Use initiate_auth_code_flow() instead")
    def build_auth_request_uri(self, response_type: str, nonce: str | None = None, **kwargs) -> str: ...  # type: ignore[override]
    @deprecated("Use obtain_token_by_auth_code_flow() instead")
    def obtain_token_by_authorization_code(self, code: str, nonce: str | None = None, **kwargs) -> dict[str, Any]: ...  # type: ignore[override]
    def initiate_auth_code_flow(self, scope=None, **kwargs) -> dict[str, Any]: ...  # type: ignore[override]
    def obtain_token_by_auth_code_flow(  # type: ignore[override]
        self, auth_code_flow: dict[str, Any], auth_response: dict[str, Any], **kwargs
    ) -> dict[str, Any]: ...
    def obtain_token_by_browser(  # type: ignore[override]
        self,
        display=None,
        prompt: str | list[str] | tuple[str, ...] | None = None,
        max_age: int | None = None,
        ui_locales=None,
        id_token_hint: str | None = None,
        login_hint: str | None = None,
        acr_values=None,
        **kwargs,
    ) -> dict[str, Any]: ...
