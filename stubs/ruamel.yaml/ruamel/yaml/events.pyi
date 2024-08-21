from _typeshed import Incomplete
from typing import Any

SHOW_LINES: bool

def CommentCheck() -> None: ...

class Event:
    crepr: str
    start_mark: Incomplete
    end_mark: Incomplete
    comment: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, comment: Any = ...) -> None: ...
    def compact_repr(self) -> str: ...

class NodeEvent(Event):
    anchor: Incomplete
    def __init__(self, anchor: Any, start_mark: Any = None, end_mark: Any = None, comment: Any = None) -> None: ...

class CollectionStartEvent(NodeEvent):
    ctag: Incomplete
    implicit: Incomplete
    flow_style: Incomplete
    nr_items: Incomplete
    def __init__(
        self,
        anchor: Any,
        tag: Any,
        implicit: Any,
        start_mark: Any = None,
        end_mark: Any = None,
        flow_style: Any = None,
        comment: Any = None,
        nr_items: int | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...

class CollectionEndEvent(Event): ...

class StreamStartEvent(Event):
    crepr: str
    encoding: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, encoding: Any = None, comment: Any = None) -> None: ...

class StreamEndEvent(Event):
    crepr: str

class DocumentStartEvent(Event):
    crepr: str
    explicit: Incomplete
    version: Incomplete
    tags: Incomplete
    def __init__(
        self,
        start_mark: Any = None,
        end_mark: Any = None,
        explicit: Any = None,
        version: Any = None,
        tags: Any = None,
        comment: Any = None,
    ) -> None: ...
    def compact_repr(self) -> str: ...

class DocumentEndEvent(Event):
    crepr: str
    explicit: Incomplete
    def __init__(self, start_mark: Any = None, end_mark: Any = None, explicit: Any = None, comment: Any = None) -> None: ...
    def compact_repr(self) -> str: ...

class AliasEvent(NodeEvent):
    crepr: str
    style: Incomplete
    def __init__(
        self, anchor: Any, start_mark: Any = None, end_mark: Any = None, style: Any = None, comment: Any = None
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
        anchor: Any,
        tag: Any,
        implicit: Any,
        value: Any,
        start_mark: Any = None,
        end_mark: Any = None,
        style: Any = None,
        comment: Any = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val: Any) -> None: ...
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
