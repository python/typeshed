from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from types import FunctionType

from networkx.utils.backends import _dispatchable

__all__ = [
    "categorical_node_match",
    "categorical_edge_match",
    "categorical_multiedge_match",
    "numerical_node_match",
    "numerical_edge_match",
    "numerical_multiedge_match",
    "generic_node_match",
    "generic_edge_match",
    "generic_multiedge_match",
]

def copyfunc(f, name=None) -> FunctionType: ...
def allclose(x, y, rtol: float = 1.0000000000000001e-05, atol=1e-08) -> bool: ...
@_dispatchable
def categorical_node_match(attr: str | Iterable[str], default): ...

# Same as categorical_node_match, but not dispatchable
def categorical_edge_match(attr: str | Iterable[str], default): ...
@_dispatchable
def categorical_multiedge_match(attr: str | Iterable[str], default): ...
@_dispatchable
def numerical_node_match(attr: str | Iterable[str], default, rtol: float = 1e-05, atol: float = 1e-08): ...

# Same as numerical_node_match, but not dispatchable
def numerical_edge_match(attr: str | Iterable[str], default, rtol: float = 1e-05, atol: float = 1e-08): ...
@_dispatchable
def numerical_multiedge_match(attr: str | Iterable[str], default, rtol: float = 1e-05, atol: float = 1e-08): ...
@_dispatchable
def generic_node_match(attr: str | Iterable[str], default, op: Callable[[Incomplete, Incomplete], Incomplete]): ...

# Same as generic_node_match, but not dispatchable
def generic_edge_match(attr: str | Iterable[str], default, op: Callable[[Incomplete, Incomplete], Incomplete]): ...
@_dispatchable
def generic_multiedge_match(attr: str | Iterable[str], default, op: Callable[[Incomplete, Incomplete], Incomplete]): ...
