from typing import (overload, Any, ContextManager, Generic,
                    Optional, Sequence, Tuple, Type, TypeVar, Union)
import ctypes

from .context import BaseContext
from .synchronize import _LockLike

_CData = Union[ctypes._SimpleCData, ctypes.Array, ctypes.Structure]
_T = TypeVar("_T", bound=_CData)

@overload
def RawValue(typecode_or_type: Type[_T], *args: Any) -> _T: ...
@overload
def RawValue(typecode_or_type: str, *args: Any) -> ctypes._SimpleCData: ...

# TODO: return ctypes.Array[_T] instead
def RawArray(typecode_or_type: Union[Type, str], size_or_initializer: Union[int, Sequence]) -> ctypes.Array: ...

@overload
def Value(typecode_or_type: _T, *args: Any, lock: bool = ...,
          ctx: Optional[BaseContext] = ...) -> SynchronizedBase[_T]: ...
@overload
def Value(typecode_or_type: str, *args: Any, lock: bool = ...,
          ctx: Optional[BaseContext] = ...) -> SynchronizedBase: ...

def Array(typecode_or_type: Union[Type, str],
          size_or_initializer: Union[int, Sequence],
          *, lock: bool = ..., ctx: Optional[BaseContext] = ...) -> SynchronizedArray[ctypes.Array]: ...

# synchronization
class SynchronizedBase(ContextManager[bool], Generic[_T]):
    def __init__(self, obj: _T, lock: Optional[_LockLike] = ..., ctx: Optional[BaseContext] = ...) -> None: ...
    def get_obj(self) -> _T: ...
    def get_lock(self) -> _LockLike: ...
    def __repr__(self) -> str: ...

class Synchronized(SynchronizedBase):
    def get_value(self) -> Any: ...
    def set_value(self, value: Any) -> None: ...
    value = property(get_value, set_value)

class SynchronizedArray(SynchronizedBase, Sequence):
    pass
