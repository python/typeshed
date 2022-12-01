from collections.abc import Callable, Container, Iterable, Iterator
from re import Pattern
from typing import Any
from typing_extensions import TypeAlias

from html5lib.filters.base import Filter
from html5lib.filters.sanitizer import Filter as SanitizerFilter
from html5lib.treewalkers.base import TreeWalker

from .css_sanitizer import CSSSanitizer
from .html5lib_shim import BleachHTMLParser, BleachHTMLSerializer
from .linkifier import _Token

ALLOWED_TAGS: list[str]
ALLOWED_ATTRIBUTES: dict[str, list[str]]
ALLOWED_PROTOCOLS: list[str]

INVISIBLE_CHARACTERS: str
INVISIBLE_CHARACTERS_RE: Pattern[str]
INVISIBLE_REPLACEMENT_CHAR: str

class Cleaner:
    tags: Container[str]
    attributes: _Attributes
    protocols: Container[str]
    strip: bool
    strip_comments: bool
    filters: Iterable[Filter]
    css_sanitizer: CSSSanitizer | None
    parser: BleachHTMLParser
    walker: Any
    serializer: BleachHTMLSerializer
    def __init__(
        self,
        tags: Container[str] = ...,
        attributes: _Attributes = ...,
        protocols: Container[str] = ...,
        strip: bool = ...,
        strip_comments: bool = ...,
        filters: Iterable[Filter] | None = ...,
        css_sanitizer: CSSSanitizer | None = ...,
    ) -> None: ...
    def clean(self, text: str) -> str: ...

_AttributeFilter: TypeAlias = Callable[[str, str, str], bool]
_AttributeDict: TypeAlias = dict[str, list[str] | _AttributeFilter] | dict[str, list[str]] | dict[str, _AttributeFilter]
_Attributes: TypeAlias = _AttributeFilter | _AttributeDict | list[str]

def attribute_filter_factory(attributes: _Attributes) -> _AttributeFilter: ...

class BleachSanitizerFilter(SanitizerFilter):
    attr_filter: _AttributeFilter
    strip_disallowed_elements: bool
    strip_html_comments: bool
    def __init__(
        self,
        source: TreeWalker,
        allowed_elements: Container[str] = ...,
        attributes: _Attributes = ...,
        allowed_protocols: Container[str] = ...,
        strip_disallowed_elements: bool = ...,
        strip_html_comments: bool = ...,
        css_sanitizer: CSSSanitizer | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def sanitize_stream(self, token_iterator: Iterable[_Token]) -> Iterator[_Token]: ...
    def merge_characters(self, token_iterator: Iterable[_Token]) -> Iterator[_Token]: ...
    def sanitize_characters(self, token: _Token) -> _Token | None: ...
    def sanitize_uri_value(self, value: str, allowed_protocols: Container[str]) -> str | None: ...
    def allow_token(self, token: _Token) -> _Token: ...
