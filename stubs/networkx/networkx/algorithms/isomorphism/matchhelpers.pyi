from _typeshed import Incomplete
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
def allclose(x, y, rtol: float = 1.0000000000000001e-05, atol: float = 1e-08) -> bool: ...
@_dispatchable
def categorical_node_match(attr: str | list[Incomplete], default: Incomplete | list[Incomplete]) -> Callable[..., Incomplete]: ...

categorical_edge_match: Incomplete

@_dispatchable
def categorical_multiedge_match(
    attr: str | list[Incomplete], default: Incomplete | list[Incomplete]
) -> Callable[..., Incomplete]: ...
@_dispatchable
def numerical_node_match(
    attr: str | list[Incomplete], default: Incomplete | list[Incomplete], rtol: float = 1e-05, atol: float = 1e-08
) -> Callable[..., Incomplete]: ...

numerical_edge_match: Incomplete

@_dispatchable
def numerical_multiedge_match(
    attr: str | list[Incomplete], default: Incomplete | list[Incomplete], rtol: float = 1e-05, atol: float = 1e-08
) -> Callable[..., Incomplete]: ...
@_dispatchable
def generic_node_match(
    attr: str | list[Incomplete], default: Incomplete | list[Incomplete], op: Callable[..., Incomplete] | list[Incomplete]
) -> Callable[..., Incomplete]: ...

generic_edge_match: Incomplete

@_dispatchable
def generic_multiedge_match(
    attr: str | list[Incomplete], default: Incomplete | list[Incomplete], op: Callable[..., Incomplete] | list[Incomplete]
) -> Callable[..., Incomplete]: ...
