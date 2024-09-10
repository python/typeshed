from collections.abc import Collection
from re import Pattern
from typing_extensions import TypeAlias

always_safe: str
urlencoded: Collection[str]
INVALID_HEX_PATTERN: Pattern[str]

_EXPLODED_QUERY_STRING: TypeAlias = list[tuple[str, str]]

def url_encode(params: _EXPLODED_QUERY_STRING) -> str: ...
def url_decode(query: str) -> _EXPLODED_QUERY_STRING: ...
def add_params_to_qs(query: str, params: _EXPLODED_QUERY_STRING) -> str: ...
def add_params_to_uri(uri: str, params: _EXPLODED_QUERY_STRING, fragment: bool = False): ...
def quote(s: str, safe: bytes = b"/") -> str: ...
def unquote(s: str) -> str: ...
def quote_url(s: str) -> str: ...
def extract_params(raw: dict[str, str] | _EXPLODED_QUERY_STRING) -> _EXPLODED_QUERY_STRING: ...
def is_valid_url(url: str) -> bool: ...
