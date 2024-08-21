from _typeshed import Incomplete

from .compat import nprintf as nprintf
from .error import StreamMark

SHOW_LINES: bool

class Token:
    start_mark: Incomplete
    end_mark: Incomplete
    def __init__(self, start_mark: StreamMark, end_mark: StreamMark) -> None: ...
    @property
    def column(self) -> int: ...
    @column.setter
    def column(self, pos) -> None: ...
    def add_post_comment(self, comment) -> None: ...
    def add_pre_comments(self, comments) -> None: ...
    def add_comment_pre(self, comment) -> None: ...
    def add_comment_eol(self, comment, comment_type) -> None: ...
    def add_comment_post(self, comment) -> None: ...
    @property
    def comment(self): ...
    def move_old_comment(self, target, empty: bool = False): ...
    def split_old_comment(self): ...
    def move_new_comment(self, target, empty: bool = False): ...

class DirectiveToken(Token):
    id: str
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value, start_mark, end_mark) -> None: ...

class DocumentStartToken(Token):
    id: str

class DocumentEndToken(Token):
    id: str

class StreamStartToken(Token):
    id: str
    encoding: Incomplete
    def __init__(
        self, start_mark: Incomplete | None = None, end_mark: Incomplete | None = None, encoding: Incomplete | None = None
    ) -> None: ...

class StreamEndToken(Token):
    id: str

class BlockSequenceStartToken(Token):
    id: str

class BlockMappingStartToken(Token):
    id: str

class BlockEndToken(Token):
    id: str

class FlowSequenceStartToken(Token):
    id: str

class FlowMappingStartToken(Token):
    id: str

class FlowSequenceEndToken(Token):
    id: str

class FlowMappingEndToken(Token):
    id: str

class KeyToken(Token):
    id: str

class ValueToken(Token):
    id: str

class BlockEntryToken(Token):
    id: str

class FlowEntryToken(Token):
    id: str

class AliasToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value, start_mark, end_mark) -> None: ...

class AnchorToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value, start_mark, end_mark) -> None: ...

class TagToken(Token):
    id: str
    value: Incomplete
    def __init__(self, value, start_mark, end_mark) -> None: ...

class ScalarToken(Token):
    id: str
    value: Incomplete
    plain: Incomplete
    style: Incomplete
    def __init__(self, value, plain, start_mark, end_mark, style: Incomplete | None = None) -> None: ...

class CommentToken(Token):
    id: str
    def __init__(
        self, value, start_mark: Incomplete | None = None, end_mark: Incomplete | None = None, column: Incomplete | None = None
    ) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, val) -> None: ...
    def reset(self) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
