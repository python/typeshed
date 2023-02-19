import re
from _typeshed import Incomplete
from collections.abc import Container, Iterable, Iterator, Sequence
from re import Pattern

from html5lib.filters.base import Filter
from html5lib.treewalkers.base import TreeWalker

from .callbacks import _Attrs, _Callback
from .html5lib_shim import Filter

DEFAULT_CALLBACKS: list[_Callback]

TLDS: list[str]

def build_url_re(tlds: Iterable[str] = ..., protocols: Iterable[str] = ...) -> Pattern[str]: ...

URL_RE: Pattern[str]
PROTO_RE: Pattern[str]

def build_email_re(tlds: Iterable[str] = ...) -> Pattern[str]: ...

EMAIL_RE: Pattern[str]

class Linker:
    def __init__(
        self,
        callbacks: Iterable[_Callback] = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
        recognized_tags: Container[str] | None = ...,
    ) -> None: ...
    def linkify(self, text: str) -> str: ...

# TODO: `_Token` might be converted into `TypedDict`
# or `html5lib` token might be reused
_Token: TypeAlias = dict[str, Any]

class LinkifyFilter(Filter):
    callbacks: Iterable[_Callback]
    skip_tags: Container[str]
    parse_email: bool
    url_re: Pattern[str]
    email_re: Pattern[str]
    def __init__(
        self,
        source,
        callbacks: Iterable[_Callback] | None = ...,
        skip_tags: Container[str] | None = None,
        parse_email: bool = False,
        url_re: Pattern[str] = ...,
        email_re: Pattern[str] = ...,
    ) -> None: ...
    def apply_callbacks(self, attrs: _Attrs, is_new: bool) -> _Attrs: ...
    def extract_character_data(self, token_list: _Token) -> str: ...
    def handle_email_addresses(self, src_iter: _Token) -> Iterator[_Token]: ...
    def strip_non_url_bits(self, fragment: str) -> tuple[str, str, str]: ...
    def handle_links(self, src_iter: Iterable[_Token]) -> Iterator[_Token]: ...
    def handle_a_tag(self, token_buffer: Sequence[_Token]) -> Iterator[_Token]: ...
    def extract_entities(self, token): ...
    def __iter__(self) -> Iterator[Incomplete]: ...
