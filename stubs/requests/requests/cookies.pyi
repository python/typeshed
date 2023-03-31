from collections.abc import MutableMapping
from http.cookiejar import CookieJar
from typing import Any

class MockRequest:
    type: Any
    def __init__(self, request) -> None: ...
    def get_type(self): ...
    def get_host(self): ...
    def get_origin_req_host(self): ...
    def get_full_url(self): ...
    def is_unverifiable(self): ...
    def has_header(self, name): ...
    def get_header(self, name, default=None): ...
    def add_header(self, key, val): ...
    def add_unredirected_header(self, name, value): ...
    def get_new_headers(self): ...
    @property
    def unverifiable(self): ...
    @property
    def origin_req_host(self): ...
    @property
    def host(self): ...

class MockResponse:
    def __init__(self, headers) -> None: ...
    def info(self): ...
    def getheaders(self, name): ...

def extract_cookies_to_jar(jar, request, response): ...
def get_cookie_header(jar, request): ...
def remove_cookie_by_name(cookiejar, name, domain=None, path=None): ...

class CookieConflictError(RuntimeError): ...

class RequestsCookieJar(CookieJar, MutableMapping[Any, Any]):
    def get(self, name, default=None, domain=None, path=None): ...
    def set(self, name, value, **kwargs): ...
    def iterkeys(self): ...
    def keys(self): ...
    def itervalues(self): ...
    def values(self): ...
    def iteritems(self): ...
    def items(self): ...
    def list_domains(self): ...
    def list_paths(self): ...
    def multiple_domains(self): ...
    def get_dict(self, domain=None, path=None): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __delitem__(self, name) -> None: ...
    def set_cookie(self, cookie, *args, **kwargs): ...
    def update(self, other): ...
    def copy(self): ...
    def get_policy(self): ...

def create_cookie(name, value, **kwargs): ...
def morsel_to_cookie(morsel): ...
def cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True): ...
def merge_cookies(cookiejar, cookies): ...
