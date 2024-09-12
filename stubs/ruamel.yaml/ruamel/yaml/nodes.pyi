from typing import Any, Final, Generic, Literal, TypeVar
from typing_extensions import TypeAlias

from .anchor import Anchor
from .error import _Mark
from .tag import Tag
from .tokens import _CommentGroup, _ScalarStyle

_T = TypeVar("_T")

_ScalarNodeStyle: TypeAlias = Literal["?", "-"] | _ScalarStyle

class Node:
    ctag: Tag
    value: Any
    start_mark: _Mark | None
    end_mark: _Mark | None
    comment: _CommentGroup | None
    anchor: Anchor | str | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: Any,
        start_mark: _Mark | None,
        end_mark: _Mark | None,
        *,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...
    @property
    def tag(self) -> str | None: ...
    @tag.setter
    def tag(self, val: Tag | str | None, /) -> None: ...
    def dump(self, *, indent: int = 0) -> None: ...

class ScalarNode(Node):
    id: Final = "scalar"
    value: str
    style: _ScalarNodeStyle | None
    def __init__(
        self,
        tag: Tag | str | None,
        value: str,
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        style: _ScalarNodeStyle | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...

class _CollectionNode(Generic[_T]):
    value: list[_T]
    flow_style: bool | None
    def __init__(
        self,
        tag: Tag | str,
        value: list[_T],
        start_mark: _Mark | None = None,
        end_mark: _Mark | None = None,
        *,
        flow_style: bool | None = None,
        comment: _CommentGroup | None = None,
        anchor: Anchor | str | None = None,
    ) -> None: ...

class CollectionNode(_CollectionNode[Any], Node): ...
class _SequenceNode(_CollectionNode[Node]): ...
class _MappingNode(_CollectionNode[tuple[Node, Node]]): ...

class SequenceNode(_SequenceNode, CollectionNode):
    id: Final = "sequence"

class MappingNode(_MappingNode, CollectionNode):
    id: Final = "mapping"
    merge: list[tuple[Node, Node]] | None
