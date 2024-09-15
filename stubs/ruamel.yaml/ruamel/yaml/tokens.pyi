from typing import ClassVar, Final, Literal, Self, overload
from typing_extensions import TypeAlias

from .error import CommentMark, StreamMark, _Mark

_PostComment: TypeAlias = CommentToken
_PreComments: TypeAlias = list[CommentToken] | list[str]
_CommentGroup: TypeAlias = list[_PostComment | _PreComments | None]
_VersionTuple: TypeAlias = tuple[int, int]
_TagDirective: TypeAlias = tuple[str, str]
_FlowScalarStyle: TypeAlias = Literal['"', "'"]
_BlockScalarStyle: TypeAlias = Literal["|", ">"]
_ScalarStyle: TypeAlias = _FlowScalarStyle | _BlockScalarStyle | Literal[""]

SHOW_LINES: bool

class Token:
    id: ClassVar[str]
    start_mark: _Mark
    end_mark: _Mark
    def __init__(self, start_mark: _Mark, end_mark: _Mark) -> None: ...
    @property
    def column(self) -> int: ...
    @column.setter
    def column(self, pos: int, /) -> None: ...
    def add_post_comment(self, comment: _PostComment, /) -> None: ...
    def add_pre_comments(self, comments: _PreComments, /) -> None: ...
    def add_comment_pre(self, comment: int) -> None: ...  # RTSC
    def add_comment_eol(self, comment: int, comment_type: int) -> None: ...  # RTSC
    def add_comment_post(self, comment: int) -> None: ...  # RTSC
    @property
    def comment(self) -> _CommentGroup | None: ...
    def move_old_comment(self, target: Token, *, empty: bool = False) -> Self | None: ...
    def split_old_comment(self) -> list[CommentToken | None]: ...
    def move_new_comment(self, target: Token, *, empty: bool = False) -> Self | None: ...

class DirectiveToken(Token):
    id: Final = "<directive>"
    name: str
    value: _VersionTuple | _TagDirective | None
    @overload
    def __init__(self, name: Literal["YAML"], value: _VersionTuple, start_mark: _Mark, end_mark: _Mark) -> None: ...
    @overload
    def __init__(self, name: Literal["TAG"], value: _TagDirective, start_mark: _Mark, end_mark: _Mark) -> None: ...
    @overload
    def __init__(self, name: str, value: None, start_mark: _Mark, end_mark: _Mark) -> None: ...

class DocumentStartToken(Token):
    id: Final = "<document start>"

class DocumentEndToken(Token):
    id: Final = "<document end>"

class StreamStartToken(Token):
    id: Final = "<stream start>"
    encoding: str | None
    def __init__(self, start_mark: _Mark, end_mark: _Mark, encoding: str | None = None) -> None: ...

class StreamEndToken(Token):
    id: Final = "<stream end>"

class BlockSequenceStartToken(Token):
    id: Final = "<block sequence start>"

class BlockMappingStartToken(Token):
    id: Final = "<block mapping start>"

class BlockEndToken(Token):
    id: Final = "<block end>"

class FlowSequenceStartToken(Token):
    id: Final = "["

class FlowMappingStartToken(Token):
    id: Final = "{"

class FlowSequenceEndToken(Token):
    id: Final = "]"

class FlowMappingEndToken(Token):
    id: Final = "}"

class KeyToken(Token):
    id: Final = "?"

class ValueToken(Token):
    id: Final = ":"

class BlockEntryToken(Token):
    id: Final = "-"

class FlowEntryToken(Token):
    id: Final = ","

class AliasToken(Token):
    id: Final = "<alias>"
    value: str
    def __init__(self, value: str, start_mark: _Mark, end_mark: _Mark) -> None: ...

class AnchorToken(Token):
    id: Final = "<anchor>"
    value: str
    def __init__(self, value: str, start_mark: _Mark, end_mark: _Mark) -> None: ...

class TagToken(Token):
    id: Final = "<tag>"
    value: tuple[str | None, str]
    def __init__(self, value: tuple[str | None, str], start_mark: _Mark, end_mark: _Mark) -> None: ...

class ScalarToken(Token):
    id: Final = "<scalar>"
    value: str
    plain: bool
    style: _ScalarStyle | None
    def __init__(
        self, value: str, plain: bool, start_mark: _Mark, end_mark: _Mark, style: _ScalarStyle | None = None
    ) -> None: ...

class CommentToken(Token):
    id: Final = "<comment>"
    pre_done: bool
    def __init__(
        self,
        value: str,
        start_mark: CommentMark | StreamMark | None = None,
        end_mark: StreamMark | None = None,
        column: int | None = None,
    ) -> None: ...
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, val: str, /) -> None: ...
    def reset(self) -> None: ...
    def __eq__(self, other: CommentToken, /) -> bool: ...
    def __ne__(self, other: CommentToken, /) -> bool: ...
