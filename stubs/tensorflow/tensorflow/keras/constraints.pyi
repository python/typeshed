from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, overload
from typing_extensions import TypeAlias

from tensorflow import Tensor

class Constraint:
    def get_config(self) -> dict[str, Any]: ...
    def __call__(self, __w: Tensor) -> Tensor: ...

_Constraint: TypeAlias = str | dict[str, Any] | Constraint | None  # noqa: Y047

@overload
def get(identifier: None) -> None: ...
@overload
def get(identifier: str | dict[str, Any] | Constraint) -> Constraint: ...
@overload
def get(identifier: Callable[[Tensor], Tensor]) -> Callable[[Tensor], Tensor]: ...
def __getattr__(name: str) -> Incomplete: ...
