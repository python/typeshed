from collections.abc import Callable
from typing import Any, Type, TypeVar, overload
from typing_extensions import Literal

_F = TypeVar("_F", bound=Callable[..., Any])
_Actions = Literal["default", "error", "ignore", "always", "module", "once"]

class ClassicAdapter:
    reason: str
    version: str
    action: _Actions | None
    category: Type[Warning]
    def __init__(
        self, reason: str = ..., version: str = ..., action: _Actions | None = ..., category: Type[Warning] = ...
    ) -> None: ...
    def get_deprecated_msg(self, wrapped: Callable[..., Any], instance: object) -> str: ...
    def __call__(self, wrapped: _F) -> Callable[[_F], _F]: ...

@overload
def deprecated(__wrapped: _F) -> _F: ...
@overload
def deprecated(
    reason: str = ..., *, version: str = ..., action: _Actions | None = ..., category: Type[Warning] | None = ...
) -> Callable[[_F], _F]: ...
