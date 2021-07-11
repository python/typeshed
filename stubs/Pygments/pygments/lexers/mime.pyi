from pygments.lexer import RegexLexer
from typing import Any

class MIMELexer(RegexLexer):
    name: str = ...
    aliases: Any = ...
    mimetypes: Any = ...
    boundary: Any = ...
    content_transfer_encoding: Any = ...
    content_type: Any = ...
    max_nested_level: Any = ...
    def __init__(self, **options: Any) -> None: ...
    def get_header_tokens(self, match: Any) -> None: ...
    def get_body_tokens(self, match: Any) -> None: ...
    def get_bodypart_tokens(self, text: Any): ...
    def store_content_type(self, match: Any) -> None: ...
    def get_content_type_subtokens(self, match: Any) -> None: ...
    def store_content_transfer_encoding(self, match: Any) -> None: ...
    attention_headers: Any = ...
    tokens: Any = ...
