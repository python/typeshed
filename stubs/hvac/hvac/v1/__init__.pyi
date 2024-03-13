from _typeshed import Incomplete
from typing import Any

from hvac.adapters import Adapter

has_hcl_parser: bool

class Client:
    def __init__(
        self,
        url: str | None = ...,
        token: str | None = ...,
        cert: tuple[str, str] | None = ...,
        verify: bool | str | None = ...,
        timeout: int = ...,
        proxies: dict[str, str] | None = ...,
        allow_redirects: bool = ...,
        session: Incomplete | None = ...,
        adapter: type[Adapter] = ...,
        namespace: Incomplete | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def adapter(self) -> Adapter: ...
    @adapter.setter
    def adapter(self, adapter: Adapter) -> None: ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, url: str) -> None: ...
    @property
    def token(self) -> str: ...
    @token.setter
    def token(self, token: str) -> None: ...
    @property
    def session(self) -> Incomplete: ...
    @session.setter
    def session(self, session: Incomplete) -> None: ...
    @property
    def allow_redirects(self) -> bool: ...
    @allow_redirects.setter
    def allow_redirects(self, allow_redirects: bool) -> None: ...
    @property
    def auth(self): ...
    @property
    def secrets(self): ...
    @property
    def sys(self): ...
    @property
    def generate_root_status(self): ...
    @property
    def key_status(self): ...
    @property
    def rekey_status(self): ...
    @property
    def ha_status(self): ...
    @property
    def seal_status(self): ...
    def read(self, path: str, wrap_ttl: int | str | None = ...): ...
    def list(self, path: str): ...
    def write(self, path: str, wrap_ttl: int | str | None, **kwargs: Any): ...
    def write_data(self, path: str, *, data: dict[str, Any] | None = ..., wrap_ttl: int | str | None = ...): ...
    def delete(self, path: str) -> None: ...
    def get_policy(self, name: str, parse: bool = ...): ...
    def lookup_token(self, token: str | None = ..., accessor: bool = ..., wrap_ttl: int | str | None = ...): ...
    def revoke_token(self, token: str, orphan: bool = ..., accessor: bool = ...) -> None: ...
    def renew_token(self, token: str, increment: bool | None = ..., wrap_ttl: int | str | None = ...) -> Incomplete: ...
    def logout(self, revoke_token: bool = ...) -> None: ...
    def is_authenticated(self) -> bool: ...
    def auth_cubbyhole(self, token: str) -> Incomplete: ...
    def login(self, url: str, use_token: bool = ..., **kwargs: Any) -> Incomplete: ...
