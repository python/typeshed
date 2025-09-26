import sys
from typing import Any, Protocol, TypeVar, type_check_only
from typing_extensions import Self

__all__ = ["Error", "copy", "deepcopy"]

_T = TypeVar("_T")
_SR = TypeVar("_SR", bound=_SupportsReplace)

@type_check_only
class _SupportsReplace(Protocol):
    # Usually there are *some* kwargs, but there's no great way to express this.
    def __replace__(self, /) -> Self: ...

# None in CPython but non-None in Jython
PyStringMap: Any

# Note: memo and _nil are internal kwargs.
def deepcopy(x: _T, memo: dict[int, Any] | None = None, _nil: Any = []) -> _T: ...
def copy(x: _T) -> _T: ...

if sys.version_info >= (3, 13):
    __all__ += ["replace"]
    def replace(obj: _SR, /, **changes: Any) -> _SR: ...

class Error(Exception): ...

error = Error
