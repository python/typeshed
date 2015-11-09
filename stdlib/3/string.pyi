# Stubs for string

# Based on http://docs.python.org/3.2/library/string.html

from typing import Mapping

ascii_letters = ...  # type: str
ascii_lowercase = ...  # type: str
ascii_uppercase = ...  # type: str
digits = ...  # type: str
hexdigits = ...  # type: str
octdigits = ...  # type: str
punctuation = ...  # type: str
printable = ...  # type: str
whitespace = ...  # type: str

def capwords(s: str, sep: str = ...) -> str: ...

class Template:
    template = ...  # type: str

    def __init__(self, template: str) -> None: ...
    def substitute(self, mapping: Mapping[str, str], **kwds: str) -> str: ...
    def safe_substitute(self, mapping: Mapping[str, str],
                        **kwds: str) -> str: ...

# TODO Formatter
