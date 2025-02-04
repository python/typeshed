from _ctypes import Structure
from _typeshed import Incomplete
from ctypes import CDLL, _CFunctionType
from typing import Any, ClassVar

C_EMPTY: type[_CFunctionType]
C_INT: type[_CFunctionType]
C_LONG: type[_CFunctionType]
C_LONGLONG: type[_CFunctionType]
C_DOUBLE: type[_CFunctionType]
C_STR: type[_CFunctionType]
YAJL_OK: int
YAJL_CANCELLED: int
YAJL_INSUFFICIENT_DATA: int
YAJL_ERROR: int

class _CallbacksStructure(Structure):
    _fields_: ClassVar[list[tuple[str, type[_CFunctionType]]]]

def get_yajl(version: int) -> CDLL: ...
def make_callbaks(send: Any, use_float: bool, yajl_version: int) -> _CallbacksStructure: ...
def yajl_get_error(yajl: Any, handle: Incomplete, buffer: Incomplete) -> str | bytes | None: ...
