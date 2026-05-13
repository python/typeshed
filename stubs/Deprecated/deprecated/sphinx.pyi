from collections.abc import Callable
from typing import Any, Literal, TypeVar, overload

from .classic import ClassicAdapter, _Actions

_F = TypeVar("_F", bound=Callable[..., Any])

class SphinxAdapter(ClassicAdapter):
    directive: Literal["versionadded", "versionchanged", "deprecated"]
    reason: str
    version: str
    action: _Actions | None
    category: type[Warning]
    def __init__(
        self,
        directive: Literal["versionadded", "versionchanged", "deprecated"],
        reason: str = "",
        version: str = "",
        action: _Actions | None = None,
        category: type[Warning] = DeprecationWarning,
        extra_stacklevel: int = 0,
        line_length: int = 70,
    ) -> None: ...
    @overload
    def __call__(self, wrapped: _F) -> _F: ...
    @overload
    def __call__(self, wrapped: _F) -> Callable[[_F], _F]: ...
    """
        :param wrapped: Wrapped class or function.

        :return: the decorated class or function.
    """
    def get_deprecated_msg(self, wrapped: _F, instance: Any) -> str: ...
    """
        :param wrapped: Wrapped class or function.

        :param instance: The object to which the wrapped function was bound when it was called.
    """

def versionadded(reason: str = "", version: str = "", line_length: int = 70) -> Callable[[_F], _F]: ...
def versionchanged(reason: str = "", version: str = "", line_length: int = 70) -> Callable[[_F], _F]: ...
def deprecated(
    reason: str = "",
    version: str = "",
    line_length: int = 70,
    *,
    action: _Actions | None = ...,
    category: type[Warning] | None = ...,
    extra_stacklevel: int = 0,
) -> Callable[[_F], _F]: ...
