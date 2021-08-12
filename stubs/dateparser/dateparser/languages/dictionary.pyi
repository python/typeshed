from typing import Any, Optional

PARSER_HARDCODED_TOKENS: Any
PARSER_KNOWN_TOKENS: Any
ALWAYS_KEEP_TOKENS: Any
KNOWN_WORD_TOKENS: Any
PARENTHESES_PATTERN: Any
NUMERAL_PATTERN: Any
KEEP_TOKEN_PATTERN: Any

class UnknownTokenError(Exception): ...

class Dictionary:
    info: Any = ...
    def __init__(self, locale_info, settings: Optional[Any] = ...) -> None: ...
    def __contains__(self, key): ...
    def __getitem__(self, key): ...
    def __iter__(self) -> Any: ...
    def are_tokens_valid(self, tokens): ...
    def split(self, string, keep_formatting: bool = ...): ...

class NormalizedDictionary(Dictionary):
    def __init__(self, locale_info, settings: Optional[Any] = ...) -> None: ...
