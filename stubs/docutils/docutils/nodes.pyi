import xml.dom.minidom
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from typing import Any, ClassVar, Protocol, TypeVar, overload
from typing_extensions import Literal, Self

from docutils.transforms import Transformer

_N = TypeVar("_N", bound=Node)

class _DomModule(Protocol):
    Document: type[xml.dom.minidom.Document]

class Node:
    # children is initialized by the subclasses
    children: Sequence[Node]
    parent: Node | None
    source: str | None
    line: int | None
    document: document | None
    def __bool__(self) -> Literal[True]: ...
    def asdom(self, dom: _DomModule | None = None) -> xml.dom.minidom.Element: ...
    # While docutils documents the Node class to be abstract it does not
    # actually use the ABCMeta metaclass. We still set @abstractmethod here
    # (although it's not used in the docutils implementation) because it
    # makes Mypy reject Node() with "Cannot instantiate abstract class".
    @abstractmethod
    def copy(self) -> Self: ...
    @abstractmethod
    def deepcopy(self) -> Self: ...
    @abstractmethod
    def pformat(self, indent: str = "    ", level: int = 0) -> str: ...
    @abstractmethod
    def astext(self) -> str: ...
    def setup_child(self, child: Node) -> None: ...
    def walk(self, visitor: NodeVisitor) -> bool: ...
    def walkabout(self, visitor: NodeVisitor) -> bool: ...
    @overload
    def findall(
        self, condition: type[_N], include_self: bool = True, descend: bool = True, siblings: bool = False, ascend: bool = False
    ) -> Generator[_N, None, None]: ...
    @overload
    def findall(
        self,
        condition: Callable[[Node], bool] | None = None,
        include_self: bool = True,
        descend: bool = True,
        siblings: bool = False,
        ascend: bool = False,
    ) -> Generator[Node, None, None]: ...
    @overload
    def traverse(
        self, condition: type[_N], include_self: bool = True, descend: bool = True, siblings: bool = False, ascend: bool = False
    ) -> list[_N]: ...
    @overload
    def traverse(
        self,
        condition: Callable[[Node], bool] | None = None,
        include_self: bool = True,
        descend: bool = True,
        siblings: bool = False,
        ascend: bool = False,
    ) -> list[Node]: ...
    @overload
    def next_node(
        self, condition: type[_N], include_self: bool = False, descend: bool = True, siblings: bool = False, ascend: bool = False
    ) -> _N: ...
    @overload
    def next_node(
        self,
        condition: Callable[[Node], bool] | None = None,
        include_self: bool = False,
        descend: bool = True,
        siblings: bool = False,
        ascend: bool = False,
    ) -> Node: ...
    def previous_sibling(self) -> Node | None: ...

class Element(Node):
    children: list[Node]
    def __init__(self, rawsource: str = "", *children: Node, **attributes): ...
    def __len__(self) -> int: ...
    def __contains__(self, key: str | Node) -> bool: ...
    # '__iter__' is added as workaround, since mypy doesn't support classes that are iterable via '__getitem__'
    # see https://github.com/python/typeshed/pull/10099#issuecomment-1528789395
    def __iter__(self) -> Iterator[Node]: ...
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
    def __iadd__(self, other: Node | Iterable[Node]) -> Self: ...
    def copy(self) -> Self: ...
    def deepcopy(self) -> Self: ...
    def pformat(self, indent: str = "    ", level: int = 0) -> str: ...
    def astext(self) -> str: ...
    def __getattr__(self, __name: str) -> Incomplete: ...

class Text(Node, str):
    tagname: ClassVar[str]
    children: tuple[()]

    # we omit the rawsource parameter because it has been deprecated and is ignored
    def __new__(cls, data: str) -> Self: ...
    def __init__(self, data: str) -> None: ...
    def shortrepr(self, maxlen: int = 18) -> str: ...
    def copy(self) -> Self: ...
    def deepcopy(self) -> Self: ...
    def pformat(self, indent: str = "    ", level: int = 0) -> str: ...
    def astext(self) -> str: ...
    def rstrip(self, chars: str | None = None) -> str: ...
    def lstrip(self, chars: str | None = None) -> str: ...

class Structural: ...
class Body: ...
class General(Body): ...
class Root: ...

class document(Root, Structural, Element):
    transformer: Transformer
    def copy(self) -> Self: ...
    def deepcopy(self) -> Self: ...
    def pformat(self, indent: str = "    ", level: int = 0) -> str: ...
    def astext(self) -> str: ...
    def __getattr__(self, __name: str) -> Incomplete: ...

class NodeVisitor:
    def __init__(self, document: document): ...
    def __getattr__(self, __name: str) -> Incomplete: ...

def __getattr__(name: str) -> Incomplete: ...
