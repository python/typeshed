# Stubs for copy

from typing import TypeVar

_T = TypeVar('_T')

# Note: deepcopy has other kwargs but they are only meant to be used internally.
def deepcopy(x: _T) -> _T: ...
def copy(x: _T) -> _T: ...
class Error(Exception): ...
error = Error