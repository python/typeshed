from _typeshed import Incomplete, Unused
from collections.abc import Iterator, Mapping, Set as AbstractSet
from typing import Generic, TypeVar, overload
from typing_extensions import Literal, Self

from networkx.classes.graph import Graph, _Edge, _NBunch, _Node

_D = TypeVar("_D")
_U = TypeVar("_U")

class NodeView(Mapping[_Node, _Node], AbstractSet[_Node]):
    def __init__(self, graph: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_Node]: ...
    def __getitem__(self, n: _Node) -> _Node: ...
    def __contains__(self, n: object) -> bool: ...
    @overload
    def __call__(self, data: Literal[False] = False, default: Incomplete = None) -> NodeView[_Node]: ...
    @overload
    def __call__(self, data: Literal[True] | str, default: Incomplete = None) -> NodeDataView[_Node]: ...
    def data(self, data: bool | str = True, default: Incomplete = None) -> NodeDataView[_Node]: ...

class NodeDataView(Generic[_Node]):
    def __init__(self, nodedict: dict[str, Incomplete], data: bool | str = False, default: Incomplete = None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, Incomplete]]: ...
    def __contains__(self, n: _Node) -> bool: ...
    def __getitem__(self, n: _Node): ...

class DiDegreeView(Generic[_Node]):
    def __init__(self, G: Graph[_Node], nbunch: _NBunch[_Node] = None, weight: None | bool | str = None) -> None: ...
    def __call__(self, nbunch: _NBunch[_Node] = None, weight: None | bool | str = None) -> DiDegreeView[_Node]: ...
    def __getitem__(self, n: _Node) -> float: ...
    def __iter__(self) -> Iterator[tuple[_Node, float]]: ...
    def __len__(self) -> int: ...

class DegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class OutDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class InDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class MultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class DiMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class InMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class OutMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...

class OutEdgeDataView(Generic[_Node, _D]):
    def __init__(self, viewer, nbunch: _NBunch[_Node] = None, data: bool = False, default: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_D]: ...
    def __contains__(self, e: _Edge[_Node]) -> bool: ...

class EdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class InEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...

class OutMultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]):
    def __init__(
        self, viewer, nbunch: _NBunch[_Node] = None, data: bool = False, keys: bool = False, default: Incomplete | None = None
    ) -> None: ...

class MultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class InMultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...

class OutEdgeView(AbstractSet[Incomplete], Mapping[Incomplete, Incomplete], Generic[_Node]):
    def __init__(self, G: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, _Node]]: ...
    def __contains__(self, e: _Edge[_Node]) -> bool: ...  # type: ignore[override]
    def __getitem__(self, e: _Edge[_Node]) -> dict[str, Incomplete]: ...
    @overload
    def __call__(self, nbunch: None = None, data: Literal[False] = False, default: Unused = None) -> Self: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], default: None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, default: _U | None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None) -> Self: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...

class EdgeView(OutEdgeView[_Node], Generic[_Node]): ...
class InEdgeView(OutEdgeView[_Node], Generic[_Node]): ...

class OutMultiEdgeView(OutEdgeView[_Node], Generic[_Node]):
    @overload  # type: ignore[override]  # Has an additional `keys` keyword argument
    def __call__(
        self, nbunch: None = None, data: Literal[False] = False, *, keys: Literal[True], default: Unused = None
    ) -> Self: ...
    @overload
    def __call__(self, nbunch: None, data: Literal[False], keys: Literal[True], default: Unused = None) -> Self: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], keys: bool = False, default: None = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], keys: bool = False, default: None = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, keys: bool = False, default: _U | None = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, keys: bool = False, default: _U | None = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload  # type: ignore[override]  # Has an additional `keys` keyword argument
    def data(self, data: Literal[False], keys: Literal[False] = False, default: Unused = None, nbunch: None = None) -> Self: ...
    @overload
    def data(
        self, data: Literal[True] = True, keys: bool = False, default: None = None, nbunch: _NBunch[_Node] = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str, keys: bool = False, default: _U | None = None, nbunch: _NBunch[_Node] = None
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...

class MultiEdgeView(OutMultiEdgeView[_Node], Generic[_Node]): ...
class InMultiEdgeView(OutMultiEdgeView[_Node], Generic[_Node]): ...
