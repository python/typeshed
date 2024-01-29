from _typeshed import Incomplete
from collections.abc import Callable, Mapping
from typing import Any, Generic, TypeVar
from typing_extensions import ParamSpec, Self

_P = ParamSpec("_P")
_R = TypeVar("_R")
__all__ = ["_dispatch"]

class _dispatch(Generic[_P, _R]):
    __defaults__: Incomplete
    __kwdefaults__: Incomplete
    __module__: Incomplete
    __qualname__: Incomplete
    __wrapped__: Incomplete
    orig_func: Callable[_P, _R] | None
    name: str
    edge_attrs: dict[str, Any] | None
    node_attrs: dict[str, Any] | None
    preserve_edge_attrs: bool
    preserve_node_attrs: bool
    preserve_graph_attrs: bool
    optional_graphs: Incomplete
    list_graphs: Incomplete
    graphs: dict[str, int]
    backends: dict[str, Incomplete]
    # Incomplete: Ignoring the case where func=None returns a partial,
    # we only care about `_dispatch` used as a static-typing decorator
    def __new__(
        cls,
        func: Callable[_P, _R] | None = None,
        *,
        name: str | None = None,
        graphs: str | None | Mapping[str, int] = "G",
        edge_attrs: str | dict[str, Any] | None = None,
        node_attrs: str | dict[str, Any] | None = None,
        preserve_edge_attrs: bool = False,
        preserve_node_attrs: bool = False,
        preserve_graph_attrs: bool = False,
        preserve_all_attrs: bool = False,
    ) -> Self: ...
    @property
    def __doc__(self): ...
    @__doc__.setter
    def __doc__(self, val) -> None: ...
    @property
    def __signature__(self): ...
    def __call__(self, /, backend: str | None = None, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...
    def __reduce__(self): ...
