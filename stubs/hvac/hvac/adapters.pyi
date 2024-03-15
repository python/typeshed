from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Mapping
from typing import Any
from typing_extensions import Self

class Adapter(metaclass=ABCMeta):
    @classmethod
    def from_adapter(cls, adapter: Adapter) -> Self: ...
    base_uri: str
    token: str | None
    namespace: str | None
    session: bool
    allow_redirects: bool
    ignore_exceptions: bool
    strict_http: bool
    request_header: bool
    def __init__(
        self,
        base_uri: str = "http://localhost:8200",
        token: str | None = None,
        cert: tuple[str, str] | None = None,
        verify: bool = True,
        timeout: int = 30,
        proxies: Mapping[str, str] | None = None,
        allow_redirects: bool = True,
        session: Incomplete | None = None,
        namespace: str | None = None,
        ignore_exceptions: bool = False,
        strict_http: bool = False,
        request_header: bool = True,
    ) -> None: ...
    @staticmethod
    def urljoin(*args: object) -> str: ...
    def close(self) -> None: ...
    def get(self, url: str, **kwargs: Any) -> Incomplete: ...
    def post(self, url: str, **kwargs: Any) -> Incomplete: ...
    def put(self, url: str, **kwargs: Any) -> Incomplete: ...
    def delete(self, url: str, **kwargs: Any) -> Incomplete: ...
    def list(self, url: str, **kwargs: Any) -> Incomplete: ...
    def head(self, url: str, **kwargs: Any) -> Incomplete: ...
    def login(self, url: str, use_token: bool = True, **kwargs: Any) -> Incomplete: ...
    @abstractmethod
    def get_login_token(self, response: Incomplete) -> str: ...
    @abstractmethod
    def request(
        self, method, url: str, headers: Mapping[str, str] | None = None, raise_exception: bool = True, **kwargs: Any
    ): ...

class RawAdapter(Adapter):
    def get_login_token(self, response: Incomplete) -> str: ...
    def request(
        self, method: str, url: str, headers: Mapping[str, str] | None = None, raise_exception: bool = True, **kwargs: Any
    ) -> Incomplete: ...

class JSONAdapter(RawAdapter):
    def get_login_token(self, response: Incomplete) -> str: ...
    def request(self, *args: Any, **kwargs: Any) -> Incomplete: ...

Request = RawAdapter
