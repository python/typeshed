from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from logging import Logger
from typing import Any
from typing_extensions import deprecated

from .authcode import AuthCodeReceiver
from .http import _HttpClientLike

string_types: tuple[type[str]]

class BrowserInteractionTimeoutError(RuntimeError): ...

class BaseClient:
    @staticmethod
    def encode_saml_assertion(assertion: bytes) -> bytes: ...
    CLIENT_ASSERTION_TYPE_JWT: str
    CLIENT_ASSERTION_TYPE_SAML2: str
    client_assertion_encoders: dict[str, Callable[[bytes], bytes]]

    @property
    @deprecated("Will be gone in next major release")
    def session(self): ...
    @session.setter
    @deprecated("Will be gone in next major release")
    def session(self, value) -> None: ...

    configuration: dict[str, Incomplete]
    client_id: str
    client_secret: str | None
    client_assertion: str | bytes | Callable[..., str | bytes] | None
    default_headers: dict[str, str]
    default_body: dict[str, Incomplete]
    logger: Logger
    def __init__(
        self,
        server_configuration: dict[str, Incomplete],
        client_id: str,
        http_client: _HttpClientLike | None = None,
        client_secret: str | None = None,
        client_assertion: str | bytes | Callable[..., str | bytes] | None = None,
        client_assertion_type: str | None = None,
        default_headers: dict[str, str] | None = None,
        default_body: dict[str, Incomplete] | None = None,
        verify: bool | str | None = None,
        proxies: Mapping[str, str] | None = None,
        timeout: float | tuple[float, float] | tuple[float, None] | None = None,
    ) -> None: ...
    def obtain_token_by_refresh_token(self, refresh_token: str, scope=None, **kwargs) -> dict[str, Any]: ...

class Client(BaseClient):
    DEVICE_FLOW: dict[str, str]
    DEVICE_FLOW_RETRIABLE_ERRORS: tuple[str, ...]
    GRANT_TYPE_SAML2: str
    GRANT_TYPE_JWT: str
    grant_assertion_encoders: dict[str, Callable[[bytes], bytes]]
    def initiate_device_flow(self, scope=None, *, data=None, **kwargs) -> dict[str, Any]: ...
    def obtain_token_by_device_flow(
        self, flow: dict[str, Any], exit_condition: Callable[[dict[str, Any]], bool] = ..., **kwargs
    ) -> dict[str, Any]: ...
    @deprecated("Use initiate_auth_code_flow() instead.")
    def build_auth_request_uri(self, response_type: str, redirect_uri=None, scope=None, state=None, **kwargs) -> str: ...
    def initiate_auth_code_flow(self, scope=None, redirect_uri=None, state=None, **kwargs) -> dict[str, Any]: ...
    def obtain_token_by_auth_code_flow(
        self, auth_code_flow: dict[str, Any], auth_response: dict[str, Any], scope=None, **kwargs
    ) -> dict[str, Any]: ...
    def obtain_token_by_browser(
        self, redirect_uri: str | None = None, auth_code_receiver: AuthCodeReceiver | None = None, **kwargs
    ) -> dict[str, Any]: ...
    @staticmethod
    @deprecated("Use obtain_token_by_auth_code_flow() instead")
    def parse_auth_response(params, state=None): ...
    @deprecated("Use obtain_token_by_auth_code_flow() instead")
    def obtain_token_by_authorization_code(self, code: str, redirect_uri=None, scope=None, **kwargs) -> dict[str, Any]: ...
    def obtain_token_by_username_password(self, username: str, password: str, scope=None, **kwargs) -> dict[str, Any]: ...
    def obtain_token_for_client(self, scope=None, **kwargs) -> dict[str, Any]: ...
    def obtain_token_by_user_fic(
        self, scope, assertion: str, username: str | None = None, user_object_id: str | None = None, **kwargs
    ) -> dict[str, Any]: ...
    on_obtaining_tokens: Callable[[dict[str, Any]], object]
    on_removing_rt: Callable[[dict[str, Any]], object]
    on_updating_rt: Callable[[dict[str, Any], str], object]
    def __init__(
        self,
        server_configuration: dict[str, Incomplete],
        client_id: str,
        on_obtaining_tokens: Callable[[dict[str, Any]], object] = ...,
        on_removing_rt: Callable[[dict[str, Any]], object] = ...,
        on_updating_rt: Callable[[dict[str, Any], str], object] = ...,
        **kwargs,
    ) -> None: ...
    def obtain_token_by_refresh_token(  # type: ignore[override]
        self, token_item, scope=None, rt_getter=..., on_removing_rt=None, on_updating_rt=None, **kwargs
    ) -> dict[str, Any]: ...
    def obtain_token_by_assertion(self, assertion, grant_type: str, scope=None, **kwargs) -> dict[str, Any]: ...
