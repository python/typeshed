from collections.abc import Mapping, MutableMapping
from logging import Logger
from typing import Any, Final, Protocol, type_check_only
from typing_extensions import deprecated

from .auth_scheme import PopAuthScheme
from .authority import Authority, AuthorityBuilder
from .oauth2cli import Client
from .oauth2cli.http import _HttpClientLike
from .throttled_http_client import ThrottledHttpClient
from .token_cache import TokenCache
from .wstrust_response import *

logger: Logger

@type_check_only
class _OnBeforeLaunchingUI(Protocol):
    # Called as on_before_launching_ui(ui="browser") or on_before_launching_ui(ui="broker").
    def __call__(self, *, ui: str) -> object: ...

def extract_certs(public_cert_content: str) -> list[str]: ...

class ClientApplication:
    ACQUIRE_TOKEN_SILENT_ID: str
    ACQUIRE_TOKEN_BY_REFRESH_TOKEN: str
    ACQUIRE_TOKEN_BY_USERNAME_PASSWORD_ID: str
    ACQUIRE_TOKEN_ON_BEHALF_OF_ID: str
    ACQUIRE_TOKEN_BY_DEVICE_FLOW_ID: str
    ACQUIRE_TOKEN_FOR_CLIENT_ID: str
    ACQUIRE_TOKEN_BY_AUTHORIZATION_CODE_ID: str
    ACQUIRE_TOKEN_INTERACTIVE: str
    ACQUIRE_TOKEN_BY_USER_FIC_ID: str
    GET_ACCOUNTS_ID: str
    REMOVE_ACCOUNT_ID: str
    ATTEMPT_REGION_DISCOVERY: bool
    DISABLE_MSAL_FORCE_REGION: bool
    client_id: str
    client_credential: str | dict[str, Any] | None
    client_claims: Mapping[str, Any] | None
    http_client: ThrottledHttpClient
    app_name: str | None
    app_version: str | None
    authority: Authority
    token_cache: TokenCache
    client: Client
    authority_groups: dict[str, list[set[str]]]
    def __init__(
        self,
        client_id: str,
        client_credential: str | dict[str, Any] | None = None,
        authority: str | AuthorityBuilder | None = None,
        validate_authority: bool = True,
        token_cache: TokenCache | None = None,
        http_client: _HttpClientLike | None = None,
        verify: bool | str = True,
        proxies: Mapping[str, str] | None = None,
        timeout: float | tuple[float, float] | tuple[float, None] | None = None,
        client_claims: Mapping[str, Any] | None = None,
        app_name: str | None = None,
        app_version: str | None = None,
        client_capabilities: list[str] | None = None,
        azure_region: str | bool | None = None,
        exclude_scopes: list[str] | None = None,
        http_cache: MutableMapping[str, Any] | None = None,
        instance_discovery: bool | None = None,
        allow_broker: bool | None = None,
        enable_pii_log: bool | None = None,
        oidc_authority: str | None = None,
    ) -> None: ...
    def is_pop_supported(self) -> bool: ...
    def initiate_auth_code_flow(
        self,
        scopes: list[str],
        redirect_uri: str | None = None,
        state: str | None = None,
        prompt: str | None = None,
        login_hint: str | None = None,
        domain_hint: str | None = None,
        claims_challenge: str | None = None,
        max_age: int | None = None,
        response_mode: str | None = None,
    ) -> dict[str, Any]: ...
    @deprecated("Change your get_authorization_request_url() to initiate_auth_code_flow()")
    def get_authorization_request_url(
        self,
        scopes: list[str],
        login_hint: str | None = None,
        state: str | None = None,
        redirect_uri: str | None = None,
        response_type: str = "code",
        prompt: str | None = None,
        nonce: str | None = None,
        domain_hint: str | None = None,
        claims_challenge: str | None = None,
        **kwargs: Any,
    ) -> str: ...
    def acquire_token_by_auth_code_flow(
        self, auth_code_flow: dict[str, Any], auth_response: dict[str, Any], scopes: list[str] | None = None, **kwargs: Any
    ) -> dict[str, Any]: ...
    @deprecated("Change your acquire_token_by_authorization_code() to acquire_token_by_auth_code_flow()")
    def acquire_token_by_authorization_code(
        self,
        code: str,
        scopes: list[str],
        redirect_uri: str | None = None,
        nonce: str | None = None,
        claims_challenge: str | None = None,
        forwarded_client_claims: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    def get_accounts(self, username: str | None = None) -> list[dict[str, Any]]: ...
    def remove_account(self, account: Mapping[str, Any]) -> None: ...
    def acquire_token_silent(
        self,
        scopes: list[str],
        account: Mapping[str, Any] | None,
        authority: str | None = None,
        force_refresh: bool | None = False,
        claims_challenge: str | None = None,
        forwarded_client_claims: str | None = None,
        auth_scheme: PopAuthScheme | None = None,
        **kwargs: Any,
    ) -> dict[str, Any] | None: ...
    def acquire_token_silent_with_error(
        self,
        scopes: list[str],
        account: Mapping[str, Any] | None,
        authority: str | None = None,
        force_refresh: bool | None = False,
        claims_challenge: str | None = None,
        forwarded_client_claims: str | None = None,
        auth_scheme: PopAuthScheme | None = None,
        **kwargs: Any,
    ) -> dict[str, Any] | None: ...
    def acquire_token_by_refresh_token(self, refresh_token: str, scopes: list[str], **kwargs: Any) -> dict[str, Any]: ...
    def acquire_token_by_username_password(
        self,
        username: str,
        password: str,
        scopes: list[str],
        claims_challenge: str | None = None,
        auth_scheme: PopAuthScheme | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...

class PublicClientApplication(ClientApplication):
    DEVICE_FLOW_CORRELATION_ID: Final = "_correlation_id"
    CONSOLE_WINDOW_HANDLE: Final[object]
    def __init__(
        self,
        client_id: str,
        client_credential: None = None,
        *,
        enable_broker_on_windows: bool | None = None,
        enable_broker_on_mac: bool | None = None,
        enable_broker_on_linux: bool | None = None,
        enable_broker_on_wsl: bool | None = None,
        authority: str | AuthorityBuilder | None = None,
        validate_authority: bool = True,
        token_cache: TokenCache | None = None,
        http_client: _HttpClientLike | None = None,
        verify: bool | str = True,
        proxies: Mapping[str, str] | None = None,
        timeout: float | tuple[float, float] | tuple[float, None] | None = None,
        client_claims: Mapping[str, Any] | None = None,
        app_name: str | None = None,
        app_version: str | None = None,
        client_capabilities: list[str] | None = None,
        azure_region: str | bool | None = None,
        exclude_scopes: list[str] | None = None,
        http_cache: MutableMapping[str, Any] | None = None,
        instance_discovery: bool | None = None,
        allow_broker: bool | None = None,
        enable_pii_log: bool | None = None,
        oidc_authority: str | None = None,
    ) -> None: ...
    def acquire_token_interactive(
        self,
        scopes: list[str],
        prompt: str | None = None,
        login_hint: str | None = None,
        domain_hint: str | None = None,
        claims_challenge: str | None = None,
        timeout: float | None = None,
        port: int | None = None,
        extra_scopes_to_consent: list[str] | None = None,
        max_age: int | None = None,
        parent_window_handle: object | None = None,
        on_before_launching_ui: _OnBeforeLaunchingUI | None = None,
        auth_scheme: PopAuthScheme | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    def initiate_device_flow(
        self, scopes: list[str] | None = None, *, claims_challenge: str | None = None, **kwargs: Any
    ) -> dict[str, Any]: ...
    def acquire_token_by_device_flow(
        self, flow: dict[str, Any], claims_challenge: str | None = None, **kwargs: Any
    ) -> dict[str, Any]: ...
    @deprecated(
        "This API has been deprecated for public client flows, please use a more secure flow. "
        "See https://aka.ms/msal-ropc-migration for migration guidance"
    )
    def acquire_token_by_username_password(
        self,
        username: str,
        password: str,
        scopes: list[str],
        claims_challenge: str | None = None,
        auth_scheme: PopAuthScheme | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...

class ConfidentialClientApplication(ClientApplication):
    def acquire_token_for_client(
        self,
        scopes: list[str],
        claims_challenge: str | None = None,
        fmi_path: str | None = None,
        forwarded_client_claims: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    def remove_tokens_for_client(self) -> None: ...
    def acquire_token_on_behalf_of(
        self,
        user_assertion: str,
        scopes: list[str],
        claims_challenge: str | None = None,
        forwarded_client_claims: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
    def acquire_token_by_user_federated_identity_credential(
        self,
        scopes: list[str],
        assertion: str,
        username: str | None = None,
        user_object_id: str | None = None,
        claims_challenge: str | None = None,
        forwarded_client_claims: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]: ...
