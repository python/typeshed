import sys
from _typeshed import StrPath
from collections.abc import Iterable, Iterator, Sequence
from http.client import HTTPResponse
from re import Pattern
from typing import ClassVar, TypeVar, overload
from urllib.request import Request

__all__ = [
    "Cookie",
    "CookieJar",
    "CookiePolicy",
    "DefaultCookiePolicy",
    "FileCookieJar",
    "LWPCookieJar",
    "LoadError",
    "MozillaCookieJar",
]

_T = TypeVar("_T")

class LoadError(OSError): ...

class CookieJar(Iterable[Cookie]):
    non_word_re: ClassVar[Pattern[str]]  # undocumented
    quote_re: ClassVar[Pattern[str]]  # undocumented
    strict_domain_re: ClassVar[Pattern[str]]  # undocumented
    domain_re: ClassVar[Pattern[str]]  # undocumented
    dots_re: ClassVar[Pattern[str]]  # undocumented
    magic_re: ClassVar[Pattern[str]]  # undocumented
    def __init__(self, policy: CookiePolicy | None = None) -> None: ...
    def add_cookie_header(self, request: Request) -> None: ...
    def extract_cookies(self, response: HTTPResponse, request: Request) -> None: ...
    def set_policy(self, policy: CookiePolicy) -> None: ...
    def make_cookies(self, response: HTTPResponse, request: Request) -> Sequence[Cookie]: ...
    def set_cookie(self, cookie: Cookie) -> None: ...
    def set_cookie_if_ok(self, cookie: Cookie, request: Request) -> None: ...
    def clear(self, domain: str | None = None, path: str | None = None, name: str | None = None) -> None: ...
    def clear_session_cookies(self) -> None: ...
    def clear_expired_cookies(self) -> None: ...  # undocumented
    def __iter__(self) -> Iterator[Cookie]: ...
    def __len__(self) -> int: ...

class FileCookieJar(CookieJar):
    filename: str
    delayload: bool
    def __init__(self, filename: StrPath | None = None, delayload: bool = False, policy: CookiePolicy | None = None) -> None: ...
    def save(self, filename: str | None = None, ignore_discard: bool = False, ignore_expires: bool = False) -> None: ...
    def load(self, filename: str | None = None, ignore_discard: bool = False, ignore_expires: bool = False) -> None: ...
    def revert(self, filename: str | None = None, ignore_discard: bool = False, ignore_expires: bool = False) -> None: ...

class MozillaCookieJar(FileCookieJar):
    if sys.version_info < (3, 10):
        header: ClassVar[str]  # undocumented

class LWPCookieJar(FileCookieJar):
    def as_lwp_str(self, ignore_discard: bool = True, ignore_expires: bool = True) -> str: ...  # undocumented

class CookiePolicy:
    netscape: bool
    rfc2965: bool
    hide_cookie2: bool
    def set_ok(self, cookie: Cookie, request: Request) -> bool: ...
    def return_ok(self, cookie: Cookie, request: Request) -> bool: ...
    def domain_return_ok(self, domain: str, request: Request) -> bool: ...
    def path_return_ok(self, path: str, request: Request) -> bool: ...

class DefaultCookiePolicy(CookiePolicy):
    rfc2109_as_netscape: bool
    strict_domain: bool
    strict_rfc2965_unverifiable: bool
    strict_ns_unverifiable: bool
    strict_ns_domain: int
    strict_ns_set_initial_dollar: bool
    strict_ns_set_path: bool
    DomainStrictNoDots: ClassVar[int]
    DomainStrictNonDomain: ClassVar[int]
    DomainRFC2965Match: ClassVar[int]
    DomainLiberal: ClassVar[int]
    DomainStrict: ClassVar[int]
    def __init__(
        self,
        blocked_domains: Sequence[str] | None = None,
        allowed_domains: Sequence[str] | None = None,
        netscape: bool = True,
        rfc2965: bool = False,
        rfc2109_as_netscape: bool | None = None,
        hide_cookie2: bool = False,
        strict_domain: bool = False,
        strict_rfc2965_unverifiable: bool = True,
        strict_ns_unverifiable: bool = False,
        strict_ns_domain: int = 0,
        strict_ns_set_initial_dollar: bool = False,
        strict_ns_set_path: bool = False,
        secure_protocols: Sequence[str] = ("https", "wss"),
    ) -> None: ...
    def blocked_domains(self) -> tuple[str, ...]: ...
    def set_blocked_domains(self, blocked_domains: Sequence[str]) -> None: ...
    def is_blocked(self, domain: str) -> bool: ...
    def allowed_domains(self) -> tuple[str, ...] | None: ...
    def set_allowed_domains(self, allowed_domains: Sequence[str] | None) -> None: ...
    def is_not_allowed(self, domain: str) -> bool: ...
    def set_ok_version(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def set_ok_verifiability(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def set_ok_name(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def set_ok_path(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def set_ok_domain(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def set_ok_port(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_version(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_verifiability(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_secure(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_expires(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_port(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented
    def return_ok_domain(self, cookie: Cookie, request: Request) -> bool: ...  # undocumented

class Cookie:
    version: int | None
    name: str
    value: str | None
    port: str | None
    path: str
    path_specified: bool
    secure: bool
    expires: int | None
    discard: bool
    comment: str | None
    comment_url: str | None
    rfc2109: bool
    port_specified: bool
    domain: str  # undocumented
    domain_specified: bool
    domain_initial_dot: bool
    def __init__(
        self,
        version: int | None,
        name: str,
        value: str | None,  # undocumented
        port: str | None,
        port_specified: bool,
        domain: str,
        domain_specified: bool,
        domain_initial_dot: bool,
        path: str,
        path_specified: bool,
        secure: bool,
        expires: int | None,
        discard: bool,
        comment: str | None,
        comment_url: str | None,
        rest: dict[str, str],
        rfc2109: bool = False,
    ) -> None: ...
    def has_nonstandard_attr(self, name: str) -> bool: ...
    @overload
    def get_nonstandard_attr(self, name: str) -> str | None: ...
    @overload
    def get_nonstandard_attr(self, name: str, default: _T) -> str | _T: ...
    def set_nonstandard_attr(self, name: str, value: str) -> None: ...
    def is_expired(self, now: int | None = None) -> bool: ...
