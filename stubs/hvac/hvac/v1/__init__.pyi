from typing import Any, Literal, overload

from hvac.adapters import Adapter
from hvac.api import AuthMethods, SystemBackend
from hvac.api.secrets_engines import SecretsEngines
from requests import Session
from requests.models import Response

has_hcl_parser: bool

class Client:
    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        cert: tuple[str, str] | None = None,
        verify: bool | str | None = None,
        timeout: int = 30,
        proxies: dict[str, str] | None = None,
        allow_redirects: bool = True,
        session: Session | None = None,
        adapter: type[Adapter[Any]] = ...,
        namespace: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def adapter(self) -> Adapter[Any]: ...
    @adapter.setter
    def adapter(self, adapter: Adapter[Any]) -> None: ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, url: str) -> None: ...
    @property
    def token(self) -> str: ...
    @token.setter
    def token(self, token: str) -> None: ...
    @property
    def session(self) -> Session: ...
    @session.setter
    def session(self, session: Session) -> None: ...
    @property
    def allow_redirects(self) -> bool: ...
    @allow_redirects.setter
    def allow_redirects(self, allow_redirects: bool) -> None: ...
    @property
    def auth(self) -> AuthMethods: ...
    @property
    def secrets(self) -> SecretsEngines: ...
    @property
    def sys(self) -> SystemBackend: ...
    @property
    def generate_root_status(self) -> dict[str, Any] | Response: ...
    @property
    def key_status(self) -> dict[str, Any] | Response: ...
    @property
    def rekey_status(self) -> dict[str, Any] | Response: ...
    @property
    def ha_status(self) -> dict[str, Any] | Response: ...
    @property
    def seal_status(self) -> dict[str, Any] | Response: ...
    def read(self, path: str, wrap_ttl: int | str | None = None) -> dict[str, Any] | Response | None: ...
    def list(self, path: str) -> dict[str, Any] | Response | None: ...
    def write(self, path: str, wrap_ttl: int | str | None, **kwargs: Any) -> dict[str, Any] | Response: ...
    def write_data(
        self, path: str, *, data: dict[str, Any] | None = None, wrap_ttl: int | str | None = None
    ) -> dict[str, Any] | Response: ...
    def delete(self, path: str) -> None: ...
    @overload
    def get_policy(self, name: str, parse: Literal[False] = False) -> str | None: ...
    @overload
    def get_policy(self, name: str, parse: Literal[True]) -> dict[str, Any] | None: ...
    def lookup_token(
        self, token: str | None = None, accessor: bool = False, wrap_ttl: int | str | None = None
    ) -> dict[str, Any] | Response: ...
    def revoke_token(self, token: str, orphan: bool = False, accessor: bool = False) -> None: ...
    def renew_token(
        self, token: str, increment: bool | None = None, wrap_ttl: int | str | None = None
    ) -> dict[str, Any] | Response: ...
    def logout(self, revoke_token: bool = False) -> None: ...
    def is_authenticated(self) -> bool: ...
    def auth_cubbyhole(self, token: str) -> Response: ...
    def login(self, url: str, use_token: bool = True, **kwargs: Any) -> Response: ...
