import xml.dom.minidom
from _typeshed import Self
from collections.abc import Iterable
from types import ModuleType
from typing import Any, Callable, Generator, TypeVar, overload
from typing_extensions import Literal

from docutils.transforms import Transformer

class NodeVisitor:
    def __init__(self, document: document): ...
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

_N = TypeVar("_N", bound=Node)

class Node:
    parent: Node | None
    source: str | None
    line: int | None
    document: document | None
    def __bool__(self) -> Literal[True]: ...
    def asdom(self, dom: ModuleType | None = ...) -> xml.dom.minidom.Element: ...
    # ModuleType is inaccurate, you cannot pass any module, but it's the best we can express
    def pformat(self, indent: str = ..., level: int = ...) -> str: ...
    def copy(self: Self) -> Self: ...
    def deepcopy(self: Self) -> Self: ...
    def astext(self) -> str: ...
    def setup_child(self, child: Node) -> None: ...
    def walk(self, visitor: NodeVisitor) -> bool: ...
    def walkabout(self, visitor: NodeVisitor) -> bool: ...
    @overload
    def findall(
        self, condition: type[_N], include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...
    ) -> Generator[_N, None, None]: ...
    @overload
    def findall(
        self,
        condition: Callable[[Node], bool] | None = ...,
        include_self: bool = ...,
        descend: bool = ...,
        siblings: bool = ...,
        ascend: bool = ...,
    ) -> Generator[Node, None, None]: ...
    @overload
    def traverse(
        self, condition: type[_N], include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...
    ) -> list[_N]: ...
    @overload
    def traverse(
        self,
        condition: Callable[[Node], bool] | None = ...,
        include_self: bool = ...,
        descend: bool = ...,
        siblings: bool = ...,
        ascend: bool = ...,
    ) -> list[Node]: ...
    @overload
    def next_node(
        self, condition: type[_N], include_self: bool = ..., descend: bool = ..., siblings: bool = ..., ascend: bool = ...
    ) -> _N: ...
    @overload
    def next_node(
        self,
        condition: Callable[[Node], bool] | None = ...,
        include_self: bool = ...,
        descend: bool = ...,
        siblings: bool = ...,
        ascend: bool = ...,
    ) -> Node: ...
    def previous_sibling(self) -> Node | None: ...

class Element(Node):
    children: list[Node]
    def __init__(self, rawsource: str = ..., *children: Node, **attributes): ...
    def __len__(self) -> int: ...
    def __contains__(self, key: str | Node) -> bool: ...
    @overload
    def __getitem__(self, key: str) -> Any: ...
    @overload
    def __getitem__(self, key: int) -> Node: ...
    @overload
    def __getitem__(self, key: slice) -> list[Node]: ...
    @overload
    def __setitem__(self, key: str, item: Any) -> None: ...
    @overload
    def __setitem__(self, key: int, item: Node) -> None: ...
    @overload
    def __setitem__(self, key: slice, item: Iterable[Node]) -> None: ...
    def __delitem__(self, key: str | int | slice) -> None: ...
    def __add__(self, other: list[Node]) -> list[Node]: ...
    def __radd__(self, other: list[Node]) -> list[Node]: ...
    def __iadd__(self: Self, other: Node | Iterable[Node]) -> Self: ...
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

class Structural: ...
class Root: ...

class document(Root, Structural, Element):
    transformer: Transformer
    def __getattr__(self, __name: str) -> Any: ...  # incomplete

def __getattr__(name: str) -> Any: ...  # incomplete
