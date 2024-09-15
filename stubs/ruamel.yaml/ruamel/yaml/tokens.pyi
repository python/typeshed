from typing import ClassVar, Literal, overload
from typing_extensions import Self, TypeAlias

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
    id: ClassVar[Literal["<directive>"]]
    name: str
    value: _VersionTuple | _TagDirective | None
    @overload
    def __init__(self, name: Literal["YAML"], value: _VersionTuple, start_mark: _Mark, end_mark: _Mark) -> None: ...
    @overload
    def __init__(self, name: Literal["TAG"], value: _TagDirective, start_mark: _Mark, end_mark: _Mark) -> None: ...
    @overload
    def __init__(self, name: str, value: None, start_mark: _Mark, end_mark: _Mark) -> None: ...

class DocumentStartToken(Token):
    id: ClassVar[Literal["<document start>"]]

class DocumentEndToken(Token):
    id: ClassVar[Literal["<document end>"]]

class StreamStartToken(Token):
    id: ClassVar[Literal["<stream start>"]]
    encoding: str | None
    def __init__(self, start_mark: _Mark, end_mark: _Mark, encoding: str | None = None) -> None: ...

class StreamEndToken(Token):
    id: ClassVar[Literal["<stream end>"]]

class BlockSequenceStartToken(Token):
    id: ClassVar[Literal["<block sequence start>"]]

class BlockMappingStartToken(Token):
    id: ClassVar[Literal["<block mapping start>"]]

class BlockEndToken(Token):
    id: ClassVar[Literal["<block end>"]]

class FlowSequenceStartToken(Token):
    id: ClassVar[Literal["["]]

class FlowMappingStartToken(Token):
    id: ClassVar[Literal["{"]]

class FlowSequenceEndToken(Token):
    id: ClassVar[Literal["]"]]

class FlowMappingEndToken(Token):
    id: ClassVar[Literal["}"]]

class KeyToken(Token):
    id: ClassVar[Literal["?"]]

class ValueToken(Token):
    id: ClassVar[Literal[":"]]

class BlockEntryToken(Token):
    id: ClassVar[Literal["-"]]

class FlowEntryToken(Token):
    id: ClassVar[Literal[","]]

class AliasToken(Token):
    id: ClassVar[Literal["<alias>"]]
    value: str
    def __init__(self, value: str, start_mark: _Mark, end_mark: _Mark) -> None: ...

class AnchorToken(Token):
    id: ClassVar[Literal["<anchor>"]]
    value: str
    def __init__(self, value: str, start_mark: _Mark, end_mark: _Mark) -> None: ...

class TagToken(Token):
    id: ClassVar[Literal["<tag>"]]
    value: tuple[str | None, str]
    def __init__(self, value: tuple[str | None, str], start_mark: _Mark, end_mark: _Mark) -> None: ...

class ScalarToken(Token):
    id: ClassVar[Literal["<scalar>"]]
    value: str
    plain: bool
    style: _ScalarStyle | None
    def __init__(
        self, value: str, plain: bool, start_mark: _Mark, end_mark: _Mark, style: _ScalarStyle | None = None
    ) -> None: ...

class CommentToken(Token):
    id: ClassVar[Literal["<comment>"]]
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
    def __eq__(self, other: CommentToken, /) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: CommentToken, /) -> bool: ...  # type: ignore[override]
