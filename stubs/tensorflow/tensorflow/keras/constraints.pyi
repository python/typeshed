from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, overload
from typing_extensions import TypeAlias

from tensorflow import Tensor

class Constraint:
    def get_config(self) -> dict[str, Any]: ...
    def __call__(self, w: Tensor, /) -> Tensor: ...

_Constraint: TypeAlias = str | dict[str, Any] | Constraint | None

@overload
def get(identifer: None) -> None: ...
@overload
def get(identifer: Callable[[Tensor], Tensor]) -> Callable[[Tensor], Tensor]: ...
@overload
def get(identifer: str | dict[str, Any]) -> Constraint: ...
@overload
def get(identifer: _Constraint) -> Constraint | Callable[[Tensor], Tensor] | None: ...
def __getattr__(name: str) -> Incomplete: ...
