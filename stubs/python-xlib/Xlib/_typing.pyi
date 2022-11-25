from _typeshed import StrOrBytesPath, SupportsDunderGT, SupportsDunderLT
from array import array
from collections.abc import Callable
from mmap import mmap
from typing import Any, Optional, Protocol, TypeVar, Union
from typing_extensions import TypeAlias

from Xlib.error import XError
from Xlib.protocol.rq import Request

_T = TypeVar("_T")
ErrorHandler: TypeAlias = Callable[[XError, Optional[Request]], _T]
SliceableBuffer: TypeAlias = bytes | bytearray | memoryview | array[Any] | mmap
Unused: TypeAlias = object
OpenFile: TypeAlias = StrOrBytesPath | int
Address: TypeAlias = Union[tuple[Any, ...], str]

class SupportsDunderEQ(Protocol):
    def __eq__(self, __other: object) -> bool: ...

class SupportsComparisons(SupportsDunderLT[object], SupportsDunderGT[object], SupportsDunderEQ, Protocol): ...
