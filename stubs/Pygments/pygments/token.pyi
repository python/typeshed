from typing import Any

class _TokenType(tuple):
    parent: Any
    def split(self): ...
    subtypes: Any
    def __init__(self, *args) -> None: ...
    def __contains__(self, val): ...
    def __getattr__(self, val): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

Token: Any
Text: Any
Whitespace: Any
Escape: Any
Error: Any
Other: Any
Keyword: Any
Name: Any
Literal: Any
String: Any
Number: Any
Punctuation: Any
Operator: Any
Comment: Any
Generic: Any

def is_token_subtype(ttype, other): ...
def string_to_tokentype(s): ...

STANDARD_TYPES: Any
