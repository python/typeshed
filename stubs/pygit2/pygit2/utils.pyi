import types
from _typeshed import AnyStr_co
from os import PathLike
from typing import Generic, TypeVar
from typing_extensions import TypeAlias

from _cffi_backend import _CDataBase

def maybe_string(ptr: _CDataBase) -> str | None: ...
def to_bytes(
    s: _CDataBase | PathLike[AnyStr_co] | bytes | str | None, encoding: str = "utf-8", errors: str = "strict"
) -> _CDataBase | bytes: ...
def to_str(s: PathLike[AnyStr_co] | str | bytes) -> str: ...
def ptr_to_bytes(ptr_cdata: _CDataBase) -> bytes: ...
def strarray_to_strings(arr: _GitStrArray) -> list[str]: ...

# Actual type: _cffi_backend.__CDataOwn <cdata 'struct git_strarray *'>
# This is not a real subclassing. Just ensuring type-checkers sees this type as compatible with _CDataBase
# pyright has no error code for subclassing final
class _GitStrArray(_CDataBase):  # type: ignore[misc]  # pyright: ignore
    count: int
    strings: _CDataBase  # <cdata 'char * *'>

_StrOrPath: TypeAlias = str | PathLike[AnyStr_co]
_IntoStrArray: TypeAlias = list[_StrOrPath[AnyStr_co]] | tuple[_StrOrPath[AnyStr_co]] | None

class StrArray:
    array: _CDataBase | _GitStrArray
    def __init__(self, l: _IntoStrArray[AnyStr_co]) -> None: ...
    def __enter__(self) -> _CDataBase: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...

_T = TypeVar("_T")

class _GenericContainer(Generic[_T]):
    def __len__(self) -> int: ...
    def __getitem__(self, idx: int) -> _T: ...

class GenericIterator(Generic[_T]):
    container: _GenericContainer[_T]
    length: int
    idx: int
    def __init__(self, container: _GenericContainer[_T]) -> None: ...
    def next(self) -> _T: ...
    def __next__(self) -> _T: ...
