import re
from collections.abc import Iterable, Iterator
from typing import Any

# We don't re-export any `html5lib` types / values here, because they are not
# really public and may change at any time. This is just a helper module,
# import things directly from `html5lib` instead!
from html5lib import HTMLParser
from html5lib._inputstream import HTMLUnicodeInputStream
from html5lib._tokenizer import HTMLTokenizer
from html5lib.serializer import HTMLSerializer

HTML_TAGS: list[str]
HTML_TAGS_BLOCK_LEVEL: frozenset[str]
AMP_SPLIT_RE: re.Pattern[str]
ENTITIES: dict[str, str]
TAG_TOKEN_TYPES: set[int]
TAG_TOKEN_TYPE_CHARACTERS: int
TAG_TOKEN_TYPE_END: int
TAG_TOKEN_TYPE_PARSEERROR: int
TAG_TOKEN_TYPE_START: int

class InputStreamWithMemory:
    position: int
    def __init__(self, inner_stream: HTMLUnicodeInputStream) -> None: ...
    def reset(self) -> None: ...
    @property
    def errors(self) -> list[str]: ...
    @property
    def charEncoding(self) -> tuple[str, str]: ...
    # Is a property returning a method, simplified:
    def changeEncoding(self, newEncoding: str) -> None: ...
    def char(self) -> str: ...
    def charsUntil(self, characters: str, opposite: bool = ...) -> str: ...
    def unget(self, char: str | None) -> None: ...
    def get_tag(self) -> str: ...
    def start_tag(self) -> None: ...

class BleachHTMLTokenizer(HTMLTokenizer):
    consume_entities: bool
    stream: InputStreamWithMemory
    emitted_last_token: dict[str, Any] | None
    def __init__(self, consume_entities: bool = ..., **kwargs: Any) -> None: ...

class BleachHTMLParser(HTMLParser):
    tags: list[str] | None
    strip: bool
    consume_entities: bool
    def __init__(self, tags: Iterable[str] | None, strip: bool, consume_entities: bool, **kwargs: Any) -> None: ...

class BleachHTMLSerializer(HTMLSerializer):
    escape_rcdata: bool
    def escape_base_amp(self, stoken: str) -> Iterator[str]: ...
    def serialize(self, treewalker, encoding: str | None = ...) -> Iterator[str]: ...  # type: ignore[override]

def convert_entity(value: str) -> str | None: ...
def convert_entities(text: str) -> str: ...
def match_entity(stream: str) -> str | None: ...
def next_possible_entity(text: str) -> Iterator[str]: ...
