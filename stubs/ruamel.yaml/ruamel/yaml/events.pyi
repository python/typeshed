from _typeshed import sentinel
from typing import ClassVar, Literal

from .error import _Mark
from .tag import Tag, _TagHandleToPrefix
from .tokens import _CommentGroup, _ScalarStyle, _VersionTuple

SHOW_LINES: bool

class Event:
    crepr: ClassVar[str]
    start_mark: _Mark | None
    end_mark: _Mark | None
    comment: _CommentGroup | None
    def __init__(
        self, start_mark: _Mark | None = None, end_mark: _Mark | None = None, comment: _CommentGroup | None = sentinel
    ) -> None: ...
    def compact_repr(self) -> str: ...

class NodeEvent(Event):
    anchor: str | None
    def __init__(
        self,
        anchor: str | None,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...

class CollectionStartEvent(NodeEvent):
    ctag: Tag | str | None
    implicit: bool
    flow_style: bool | None
    nr_items: int | None
    def __init__(
        self,
        anchor: str | None,
        tag: Tag | str | None,
        implicit: bool,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        flow_style: bool | None = None,
        comment: _CommentGroup | None = None,
        nr_items: int | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...

class CollectionEndEvent(Event): ...

# Implementations.

class StreamStartEvent(Event):
    crepr: ClassVar[Literal["+STR"]]
    encoding: str | None
    def __init__(
        self,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        encoding: str | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...

class StreamEndEvent(Event):
    crepr: ClassVar[Literal["-STR"]]

class DocumentStartEvent(Event):
    crepr: ClassVar[Literal["+DOC"]]
    explicit: bool | None
    version: _VersionTuple | None
    tags: _TagHandleToPrefix | None
    def __init__(
        self,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        explicit: bool | None = None,
        version: _VersionTuple | None = None,
        tags: _TagHandleToPrefix | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class DocumentEndEvent(Event):
    crepr: ClassVar[Literal["-DOC"]]
    explicit: bool | None
    def __init__(
        self,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        explicit: bool | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class AliasEvent(NodeEvent):
    crepr: ClassVar[Literal["=ALI"]]
    style: Literal["?"] | None
    def __init__(
        self,
        anchor: str,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        style: Literal["?"] | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class ScalarEvent(NodeEvent):
    crepr: ClassVar[Literal["=VAL"]]
    ctag: Tag | None
    implicit: tuple[bool, bool]
    value: str
    style: _ScalarStyle | None
    def __init__(
        self,
        anchor: str | None,
        tag: Tag | None,
        implicit: tuple[bool, bool],
        value: str,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        style: _ScalarStyle | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val: Tag | str) -> None: ...
    def compact_repr(self) -> str: ...

class SequenceStartEvent(CollectionStartEvent):
    crepr: ClassVar[Literal["+SEQ"]]
    def compact_repr(self) -> str: ...

class SequenceEndEvent(CollectionEndEvent):
    crepr: ClassVar[Literal["-SEQ"]]

class MappingStartEvent(CollectionStartEvent):
    crepr: ClassVar[Literal["+MAP"]]
    def compact_repr(self) -> str: ...

class MappingEndEvent(CollectionEndEvent):
    crepr: ClassVar[Literal["-MAP"]]
