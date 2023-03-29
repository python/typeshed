from _typeshed import Incomplete, Unused
from collections.abc import Generator
from typing_extensions import Literal

from openpyxl.cell.text import Text
from openpyxl.comments.author import AuthorList
from openpyxl.descriptors.base import Typed
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable

class Properties(Serialisable):
    locked: Incomplete
    defaultSize: Incomplete
    disabled: Incomplete
    uiObject: Incomplete
    autoFill: Incomplete
    autoLine: Incomplete
    altText: Incomplete
    textHAlign: Incomplete
    textVAlign: Incomplete
    lockText: Incomplete
    justLastX: Incomplete
    autoScale: Incomplete
    rowHidden: Incomplete
    colHidden: Incomplete
    __elements__: Incomplete
    anchor: Incomplete
    def __init__(
        self,
        locked: Incomplete | None = None,
        defaultSize: Incomplete | None = None,
        _print: Incomplete | None = None,
        disabled: Incomplete | None = None,
        uiObject: Incomplete | None = None,
        autoFill: Incomplete | None = None,
        autoLine: Incomplete | None = None,
        altText: Incomplete | None = None,
        textHAlign: Incomplete | None = None,
        textVAlign: Incomplete | None = None,
        lockText: Incomplete | None = None,
        justLastX: Incomplete | None = None,
        autoScale: Incomplete | None = None,
        rowHidden: Incomplete | None = None,
        colHidden: Incomplete | None = None,
        anchor: Incomplete | None = None,
    ) -> None: ...

class CommentRecord(Serialisable):
    tagname: str
    ref: Incomplete
    authorId: Incomplete
    guid: Incomplete
    shapeId: Incomplete
    text: Typed[Text, Literal[False]]
    commentPr: Typed[Properties, Literal[True]]
    author: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    height: Incomplete
    width: Incomplete
    def __init__(
        self,
        ref: str = "",
        authorId: int = 0,
        guid: Incomplete | None = None,
        shapeId: int = 0,
        text: Text | None = None,
        commentPr: Properties | None = None,
        author: Incomplete | None = None,
        height: int = 79,
        width: int = 144,
    ) -> None: ...
    @classmethod
    def from_cell(cls, cell): ...
    @property
    def content(self): ...

class CommentSheet(Serialisable):
    tagname: str
    authors: Typed[AuthorList, Literal[False]]
    commentList: Incomplete
    extLst: Typed[ExtensionList, Literal[True]]
    mime_type: str
    __elements__: Incomplete
    def __init__(self, authors: AuthorList, commentList: Incomplete | None = None, extLst: Unused = None) -> None: ...
    def to_tree(self): ...
    @property
    def comments(self) -> Generator[Incomplete, None, None]: ...
    @classmethod
    def from_comments(cls, comments): ...
    def write_shapes(self, vml: Incomplete | None = None): ...
    @property
    def path(self): ...
