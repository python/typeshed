from collections.abc import Callable
from typing import AnyStr

def html_escape(s: object) -> str: ...
def header_docstring(header: str, rfc_section: str) -> str: ...
def warn_deprecation(text: str, version: str, stacklevel: int) -> None: ...

status_reasons: dict[int, str]
status_generic_reasons: dict[int, str]

def strings_differ(string1: AnyStr, string2: AnyStr, compare_digest: Callable[[AnyStr, AnyStr], bool] = ...) -> bool: ...
