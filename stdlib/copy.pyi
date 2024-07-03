import sys
from typing import Any, TypeVar

__all__ = ["Error", "copy", "deepcopy"]

_T = TypeVar("_T")

# None in CPython but non-None in Jython
PyStringMap: Any

# Note: memo and _nil are internal kwargs.
def deepcopy(x: _T, memo: dict[int, Any] | None = None, _nil: Any = []) -> _T: ...
def copy(x: _T) -> _T: ...

if sys.version_info >= (3, 13):
    def replace(obj: _T, /, **changes: Any) -> _T: ...

class Error(Exception): ...

error = Error
