import sys
from collections.abc import Generator, Iterable, Mapping
from contextlib import AbstractContextManager
from io import BufferedWriter
from os import PathLike
from typing import Any, AnyStr
from typing_extensions import TypeAlias

from . import compat, cookies, exceptions, structures
from .models import PreparedRequest, Request

_Uri: TypeAlias = str | bytes
OrderedDict = compat.OrderedDict
cookiejar_from_dict = cookies.cookiejar_from_dict
CaseInsensitiveDict = structures.CaseInsensitiveDict
InvalidURL = exceptions.InvalidURL

NETRC_FILES: tuple[str, str]
DEFAULT_CA_BUNDLE_PATH: Any
DEFAULT_PORTS: dict[str, int]
DEFAULT_ACCEPT_ENCODING: str

def dict_to_sequence(d): ...
def super_len(o): ...
def get_netrc_auth(url: _Uri, raise_errors: bool = ...) -> tuple[str, str] | None: ...
def guess_filename(obj): ...
def extract_zipped_paths(path): ...
def atomic_open(filename: PathLike[AnyStr]) -> AbstractContextManager[BufferedWriter]: ...
def from_key_val_list(value): ...
def to_key_val_list(value): ...
def parse_list_header(value): ...
def parse_dict_header(value): ...
def unquote_header_value(value, is_filename: bool = ...): ...
def dict_from_cookiejar(cj): ...
def add_dict_to_cookiejar(cj, cookie_dict): ...
def get_encodings_from_content(content): ...
def get_encoding_from_headers(headers): ...
def stream_decode_response_unicode(iterator, r): ...
def iter_slices(string: str, slice_length: int | None) -> Generator[str, None, None]: ...
def get_unicode_from_response(r): ...

UNRESERVED_SET: frozenset[str]

def unquote_unreserved(uri: str) -> str: ...
def requote_uri(uri: str) -> str: ...
def address_in_network(ip: str, net: str) -> bool: ...
def dotted_netmask(mask: int) -> str: ...
def is_ipv4_address(string_ip: str) -> bool: ...
def is_valid_cidr(string_network: str) -> bool: ...
def set_environ(env_name: str, value: None) -> AbstractContextManager[None]: ...
def should_bypass_proxies(url: _Uri, no_proxy: Iterable[str] | None) -> bool: ...
def get_environ_proxies(url: _Uri, no_proxy: Iterable[str] | None = ...) -> dict[Any, Any]: ...
def select_proxy(url: _Uri, proxies: Mapping[Any, Any] | None): ...
def resolve_proxies(request: Request | PreparedRequest, proxies: Mapping[str, str], trust_env: bool = ...): ...
def default_user_agent(name: str = ...) -> str: ...
def default_headers() -> CaseInsensitiveDict[str]: ...
def parse_header_links(value: str) -> list[dict[str, str]]: ...
def guess_json_utf(data): ...
def prepend_scheme_if_needed(url, new_scheme): ...
def get_auth_from_url(url: _Uri) -> tuple[str, str]: ...
def to_native_string(string, encoding=...): ...
def urldefragauth(url: _Uri): ...
def rewind_body(prepared_request: PreparedRequest) -> None: ...
def check_header_validity(header: tuple[AnyStr, AnyStr]) -> None: ...

if sys.platform == "win32":
    def proxy_bypass_registry(host) -> bool: ...
    def proxy_bypass(host) -> bool: ...
