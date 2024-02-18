from collections.abc import Callable
from typing import Any, TypeVar, overload
from typing_extensions import ParamSpec

from tensorflow.autograph.experimental import Feature

_Param = ParamSpec("_Param")
_RetType = TypeVar("_RetType")
_Type = TypeVar("_Type")

def set_verbosity(level: int, alsologtostdout: bool = False) -> None: ...
def to_code(
    entity: Callable[_Param, Any] | type,
    recursive: bool = True,
    experimental_optional_features: None | Feature | tuple[Feature, ...] = None,
) -> str: ...
@overload
def to_graph(
    entity: Callable[_Param, _RetType],
    recursive: bool = True,
    experimental_optional_features: None | Feature | tuple[Feature, ...] = None,
) -> Callable[_Param, _RetType]: ...
@overload
def to_graph(
    entity: _Type, recursive: bool = True, experimental_optional_features: None | Feature | tuple[Feature, ...] = None
) -> _Type: ...
def trace(*args: Any) -> None: ...
