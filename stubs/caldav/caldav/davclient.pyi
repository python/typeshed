from typing_extensions import Self
from collections.abc import Iterable, Mapping
from typing import Any
from typing_extensions import TypeAlias
from urllib.parse import ParseResult, SplitResult

from requests.auth import AuthBase
from requests.models import Response
from requests.sessions import _Timeout
from requests.structures import CaseInsensitiveDict

from .lib.url import URL
from .objects import Calendar, DAVObject, Principal

_Element: TypeAlias = Any  # actually lxml.etree._Element

class DAVResponse:
    reason: str
    tree: _Element | None
    status: int
    headers: CaseInsensitiveDict[str]
    objects: dict[str, dict[str, str]]  # only defined after call to find_objects_and_props()
    def __init__(self, response: Response) -> None: ...
    @property
    def raw(self) -> str: ...
    def validate_status(self, status: str) -> None: ...
    def find_objects_and_props(self) -> None: ...
    def expand_simple_props(
        self, props: Iterable[Any] = ..., multi_value_props: Iterable[Any] = ..., xpath: str | None = ...
    ) -> dict[str, dict[str, str]]: ...

class DAVClient:
    proxy: str | None
    url: URL
    headers: dict[str, str]
    username: str | None
    password: str | None
    auth: AuthBase | None
    timeout: _Timeout | None
    ssl_verify_cert: bool | str
    ssl_cert: str | tuple[str, str] | None
    def __init__(
        self,
        url: str,
        proxy: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
        auth: AuthBase | None = ...,
        timeout: _Timeout | None = ...,
        ssl_verify_cert: bool | str = ...,
        ssl_cert: str | tuple[str, str] | None = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None: ...
    def principal(self, *, url: str | ParseResult | SplitResult | URL | None = ...) -> Principal: ...
    def calendar(
        self,
        url: str | ParseResult | SplitResult | URL | None = ...,
        parent: DAVObject | None = ...,
        name: str | None = ...,
        id: str | None = ...,
        props: Mapping[Any, Any] = ...,
        **extra: Any,
    ) -> Calendar: ...
    def check_dav_support(self) -> str | None: ...
    def check_cdav_support(self) -> bool: ...
    def check_scheduling_support(self) -> bool: ...
    def propfind(self, url: str | None = ..., props: str = ..., depth: int = ...) -> DAVResponse: ...
    def proppatch(self, url: str, body: str, dummy: None = ...) -> DAVResponse: ...
    def report(self, url: str, query: str = ..., depth: int = ...) -> DAVResponse: ...
    def mkcol(self, url: str, body: str, dummy: None = ...) -> DAVResponse: ...
    def mkcalendar(self, url: str, body: str = ..., dummy: None = ...) -> DAVResponse: ...
    def put(self, url: str, body: str, headers: Mapping[str, str] = ...) -> DAVResponse: ...
    def post(self, url: str, body: str, headers: Mapping[str, str] = ...) -> DAVResponse: ...
    def delete(self, url: str) -> DAVResponse: ...
    def options(self, url: str) -> DAVResponse: ...
    def request(self, url: str, method: str = ..., body: str = ..., headers: Mapping[str, str] = ...) -> DAVResponse: ...
