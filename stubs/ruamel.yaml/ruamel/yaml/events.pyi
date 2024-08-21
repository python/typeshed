from _typeshed import Incomplete

SHOW_LINES: bool

def CommentCheck() -> None: ...

class Event:
    crepr: str
    start_mark: Incomplete
    end_mark: Incomplete
    comment: Incomplete
    def __init__(self, start_mark: Incomplete | None = None, end_mark: Incomplete | None = None, comment=...) -> None: ...
    def compact_repr(self) -> str: ...

class NodeEvent(Event):
    anchor: Incomplete
    def __init__(
        self, anchor, start_mark: Incomplete | None = None, end_mark: Incomplete | None = None, comment: Incomplete | None = None
    ) -> None: ...

class CollectionStartEvent(NodeEvent):
    ctag: Incomplete
    implicit: Incomplete
    flow_style: Incomplete
    nr_items: Incomplete
    def __init__(
        self,
        anchor,
        tag,
        implicit,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        flow_style: Incomplete | None = None,
        comment: Incomplete | None = None,
        nr_items: int | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...

class CollectionEndEvent(Event): ...

class StreamStartEvent(Event):
    crepr: str
    encoding: Incomplete
    def __init__(
        self,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        encoding: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...

class StreamEndEvent(Event):
    crepr: str

class DocumentStartEvent(Event):
    crepr: str
    explicit: Incomplete
    version: Incomplete
    tags: Incomplete
    def __init__(
        self,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        explicit: Incomplete | None = None,
        version: Incomplete | None = None,
        tags: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class DocumentEndEvent(Event):
    crepr: str
    explicit: Incomplete
    def __init__(
        self,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        explicit: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class AliasEvent(NodeEvent):
    crepr: str
    style: Incomplete
    def __init__(
        self,
        anchor,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        style: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class ScalarEvent(NodeEvent):
    crepr: str
    ctag: Incomplete
    implicit: Incomplete
    value: Incomplete
    style: Incomplete
    def __init__(
        self,
        anchor,
        tag,
        implicit,
        value,
        start_mark: Incomplete | None = None,
        end_mark: Incomplete | None = None,
        style: Incomplete | None = None,
        comment: Incomplete | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val) -> None: ...
    def compact_repr(self) -> str: ...

class SequenceStartEvent(CollectionStartEvent):
    crepr: str
    def compact_repr(self) -> str: ...

class SequenceEndEvent(CollectionEndEvent):
    crepr: str

class MappingStartEvent(CollectionStartEvent):
    crepr: str
    def compact_repr(self) -> str: ...

class MappingEndEvent(CollectionEndEvent):
    crepr: str
