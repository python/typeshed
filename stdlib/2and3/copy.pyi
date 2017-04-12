# Stubs for copy

from typing import TypeVar, Optional, Dict, Any

_T = TypeVar('_T')

# Note: memo and _nil are internal kwargs.
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil: Any = ...) -> _T: ...
def copy(x: _T) -> _T: ...
class Error(Exception): ...
error = Error
