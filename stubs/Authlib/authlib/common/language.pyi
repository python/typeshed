from typing import Final, Pattern

_LANGUAGE_TAG_RE: Final[Pattern[str]]

def is_valid_language_tag(tag: str) -> bool: ...
