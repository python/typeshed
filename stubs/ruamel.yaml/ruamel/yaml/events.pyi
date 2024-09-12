from _typeshed import sentinel
from typing import ClassVar, Final, Literal

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
    crepr: Final = "+STR"
    encoding: str | None
    def __init__(
        self,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        encoding: str | None = None,
        comment: _CommentGroup | None = None,
    ) -> None: ...

class StreamEndEvent(Event):
    crepr: Final = "-STR"

class DocumentStartEvent(Event):
    crepr: Final = "+DOC"
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
    crepr: Final = "-DOC"
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
    crepr: Final = "=ALI"
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
    crepr: Final = "=VAL"
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
    crepr: Final = "+SEQ"
    def compact_repr(self) -> str: ...

class SequenceEndEvent(CollectionEndEvent):
    crepr: Final = "-SEQ"

class MappingStartEvent(CollectionStartEvent):
    crepr: Final = "+MAP"
    def compact_repr(self) -> str: ...

class MappingEndEvent(CollectionEndEvent):
    crepr: Final = "-MAP"
