from re import Pattern
from typing import Final

_LANGUAGE_TAG_RE: Final[Pattern[str]]

def is_valid_language_tag(tag: str) -> bool: ...
