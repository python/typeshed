from re import Pattern
from typing import Any

HEADER_VALIDATORS: dict[type, tuple[Pattern[Any], Pattern[Any]]]

def to_native_string(string: str | bytes, encoding: str = ...) -> str: ...
def unicode_is_ascii(u_string: str) -> bool: ...
