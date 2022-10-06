from re import Pattern
from typing import Any, overload

from markdown.core import Markdown

BLOCK_LEVEL_ELEMENTS: Any
STX: str
ETX: str
INLINE_PLACEHOLDER_PREFIX: Any
INLINE_PLACEHOLDER: Any
INLINE_PLACEHOLDER_RE: Pattern[str]
AMP_SUBSTITUTE: Any
HTML_PLACEHOLDER: Any
HTML_PLACEHOLDER_RE: Pattern[str]
TAG_PLACEHOLDER: Any
RTL_BIDI_RANGES: Any

def deprecated(message: str, stacklevel: int = ...): ...
def parseBoolValue(value: object, fail_on_errors: bool = ..., preserve_none: bool = ...) -> bool | None: ...
def code_escape(text: str) -> str: ...
def nearing_recursion_limit() -> bool: ...

class AtomicString(str): ...

class Processor:
    md: Markdown
    def __init__(self, md: Markdown | None = ...) -> None: ...

class HtmlStash:
    html_counter: int = ...
    rawHtmlBlocks: list[str]
    tag_counter: int = ...
    tag_data: list[dict[str, Any]]
    def __init__(self) -> None: ...
    def store(self, html: str) -> str: ...
    def reset(self) -> None: ...
    def get_placeholder(self, key: int) -> str: ...
    def store_tag(self, tag: str, attrs: list[Any], left_index: int, right_index: int) -> str: ...

class Registry:
    def __init__(self) -> None: ...
    def __contains__(self, item: object) -> bool: ...
    def __iter__(self) -> Any: ...
    @overload
    def __getitem__(self, key: slice) -> Registry: ...
    @overload
    def __getitem__(self, key: str | int) -> Any: ...
    def __len__(self) -> int: ...
    def get_index_for_name(self, name: str) -> int: ...
    def register(self, item: Any, name: str, priority: float) -> None: ...
    def deregister(self, name: str, strict: bool = ...) -> None: ...
