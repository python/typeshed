import sys
from typing import Any, Callable, Protocol, TypeVar
from typing_extensions import Self

__all__ = ["Error", "copy", "deepcopy"]

_T = TypeVar("_T")
_SR = TypeVar("_SR", bound=_SupportsReplace)

class _SupportsReplace(Protocol):
    __replace__: Callable[..., Self]

# None in CPython but non-None in Jython
PyStringMap: Any

# Note: memo and _nil are internal kwargs.
def deepcopy(x: _T, memo: dict[int, Any] | None = None, _nil: Any = []) -> _T: ...
def copy(x: _T) -> _T: ...

if sys.version_info >= (3, 13):
    def replace(obj: _SR, /, **kwargs: Any) -> _SR: ...

class Error(Exception): ...

error = Error
