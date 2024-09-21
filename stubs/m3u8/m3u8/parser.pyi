from collections.abc import Callable
from re import Pattern
from typing import Any
from typing_extensions import TypeAlias

ATTRIBUTELISTPATTERN: Pattern[str]
CustomTagsParser: TypeAlias = Callable[[str, int, dict[str, Any], dict[str, Any]], object]

class ParseError(Exception):
    lineno: int
    line: str
    def __init__(self, lineno: int, line: str) -> None: ...

def parse(content: str, strict: bool = False, custom_tags_parser: CustomTagsParser | None = None) -> dict[str, Any]: ...
