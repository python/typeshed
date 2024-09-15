from _typeshed import SupportsRead, SupportsWrite
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from collections.abc import Iterable, MutableSequence
from typing import IO, Any, Final, Self, TypeVar, overload
from typing_extensions import TypeAlias

from .docinfo import Version

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

_ReadStream: TypeAlias = str | bytes | SupportsRead[str] | SupportsRead[bytes]
_WriteStream: TypeAlias = SupportsWrite[str] | SupportsWrite[bytes]

StreamType: TypeAlias = _WriteStream
StreamTextType: TypeAlias = _ReadStream
VersionType: TypeAlias = str | tuple[int, int] | list[int] | Version | None

class ordereddict(OrderedDict[_KT, _VT]):
    def insert(self, pos: int, key: _KT, value: _VT) -> None: ...

builtins_module: Final = "builtins"

def with_metaclass(meta, *bases): ...

DBG_TOKEN: Final = 1
DBG_EVENT: Final = 2
DBG_NODE: Final = 4

def dbg(val: int | None = None) -> int: ...

class Nprint:
    def __init__(self, file_name: str | None = None) -> None: ...
    def __call__(self, *args, **kw) -> None: ...
    def set_max_print(self, i: int) -> None: ...
    def fp(self, mode: str = "a") -> IO[Any]: ...

nprint: Nprint
nprintf: Nprint

def check_namespace_char(ch: str) -> bool: ...
def check_anchorname_char(ch: str) -> bool: ...
def version_tnf(t1: tuple[int, ...], t2: tuple[int, ...] | None = None) -> bool | None: ...

class MutableSliceableSequence(MutableSequence[_T], metaclass=ABCMeta):
    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> Self: ...
    @overload
    def __setitem__(self, index: int, value: _T) -> None: ...
    @overload
    def __setitem__(self, index: slice, value: Iterable[_T]) -> None: ...
    @overload
    def __delitem__(self, index: int) -> None: ...
    @overload
    def __delitem__(self, index: slice) -> None: ...
    @abstractmethod
    def __getsingleitem__(self, index: int) -> _T: ...
    @abstractmethod
    def __setsingleitem__(self, index: int, value: _T) -> None: ...
    @abstractmethod
    def __delsingleitem__(self, index: int) -> None: ...
