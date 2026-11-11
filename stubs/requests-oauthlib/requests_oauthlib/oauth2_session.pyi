from _typeshed import Incomplete
from collections.abc import Callable
from logging import Logger
from typing import Any, Literal, Protocol, TypeAlias, TypedDict, overload, type_check_only

import requests
from oauthlib.oauth2 import Client
from requests import _types
from requests.cookies import RequestsCookieJar

_Token: TypeAlias = dict[str, Incomplete]  # oauthlib.oauth2.Client.token

@type_check_only
class _AccessTokenResponseHook(Protocol):
    def __call__(self, response: requests.Response, /) -> requests.Response: ...

@type_check_only
class _RefreshTokenResponseHook(Protocol):
    def __call__(self, response: requests.Response, /) -> requests.Response: ...

@type_check_only
class _ProtectedRequestHook(Protocol):
    def __call__(self, url, headers, data, /) -> tuple[Incomplete, Incomplete, Incomplete]: ...

@type_check_only
class _ComplianceHooks(TypedDict):
    access_token_response: set[_AccessTokenResponseHook]
    refresh_token_response: set[_RefreshTokenResponseHook]
    protected_request: set[_ProtectedRequestHook]

log: Logger

class TokenUpdated(Warning):
    token: _Token
    def __init__(self, token: _Token) -> None: ...

class OAuth2Session(requests.Session):
    redirect_uri: str | None
    state: str | Callable[[], str]
    auto_refresh_url: str | None
    auto_refresh_kwargs: dict[str, Any]
    token_updater: Callable[[_Token], object] | None
    compliance_hook: _ComplianceHooks
    def __init__(
        self,
        client_id: str | None = None,
        client: Client | None = None,
        auto_refresh_url: str | None = None,
        auto_refresh_kwargs: dict[str, Any] | None = None,
        scope: str | list[str] | set[str] | tuple[str, ...] | None = None,
        redirect_uri: str | None = None,
        token: _Token | None = None,
        state: str | Callable[[], str] | None = None,
        token_updater: Callable[[_Token], object] | None = None,
        pkce: Literal["S256", "plain"] | None = None,
        **kwargs: Any,
    ) -> None: ...

    @property
    def scope(self) -> Incomplete | None: ...  # oauthlib.oauth2.Client.scope
    @scope.setter
    def scope(self, value: Incomplete | None) -> None: ...

    def new_state(self) -> str: ...

    @property
    def client_id(self) -> str | None: ...
    @client_id.setter
    def client_id(self, value: str | None) -> None: ...
    @client_id.deleter
    def client_id(self) -> None: ...

    @property
    def token(self) -> _Token: ...
    @token.setter
    def token(self, value: _Token) -> None: ...

    @property
    def access_token(self) -> str | None: ...
    @access_token.setter
    def access_token(self, value: str | None) -> None: ...
    @access_token.deleter
    def access_token(self) -> None: ...

    @property
    def authorized(self) -> bool: ...
    def authorization_url(self, url: str, state: str | None = None, **kwargs: Any) -> tuple[str, str]: ...
    def fetch_token(
        self,
        token_url: str,
        code: str | None = None,
        authorization_response: str | None = None,
        body: str = "",
        auth: _types.AuthType = None,
        username: str | None = None,
        password: str | None = None,
        method: str = "POST",
        force_querystring: bool = False,
        timeout: _types.TimeoutType = None,
        headers: _types.HeadersType = None,
        verify: _types.VerifyType | None = None,
        proxies: dict[str, str] | None = None,
        include_client_id: bool | None = None,
        client_secret: str | None = None,
        cert: _types.CertType = None,
        **kwargs: Any,
    ) -> _Token: ...
    def token_from_fragment(self, authorization_response: str) -> _Token: ...
    def refresh_token(
        self,
        token_url: str,
        refresh_token: str | None = None,
        body: str = "",
        auth: _types.AuthType = None,
        timeout: _types.TimeoutType = None,
        headers: _types.HeadersType = None,
        verify: _types.VerifyType | None = None,
        proxies: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> _Token: ...
    def request(  # type: ignore[override]
        self,
        method: str | bytes,
        url: str | bytes,
        data: _types.DataType = None,
        headers: _types.HeadersType = None,
        withhold_token: bool = False,
        client_id: str | None = None,
        client_secret: str | None = None,
        files: _types.FilesType = None,
        *,
        params: _types.ParamsType = None,
        cookies: RequestsCookieJar | dict[str, str] | None = None,
        auth: _types.AuthType = None,
        timeout: _types.TimeoutType = None,
        allow_redirects: bool = True,
        proxies: dict[str, str] | None = None,
        hooks: _types.HooksInputType | None = None,
        stream: bool | None = None,
        verify: _types.VerifyType | None = None,
        cert: _types.CertType = None,
        json: _types.JsonType = None,
    ) -> requests.Response: ...

    @overload
    def register_compliance_hook(self, hook_type: Literal["access_token_response"], hook: _AccessTokenResponseHook) -> None: ...
    @overload
    def register_compliance_hook(self, hook_type: Literal["refresh_token_response"], hook: _RefreshTokenResponseHook) -> None: ...
    @overload
    def register_compliance_hook(self, hook_type: Literal["protected_request"], hook: _ProtectedRequestHook) -> None: ...
