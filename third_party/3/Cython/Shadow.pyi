from builtins import (int as py_int, float as py_float,
                      bool as py_bool, str as py_str)
from typing import (Union, Dict, Any, Sequence, Optional,
                    List, TypeVar, Type, Generic)

int = py_int
long = py_int
longlong = py_int
short = py_int
char = py_int
sint = py_int
slong = py_int
slonglong = py_int
sshort = py_int
schar = py_int
uint = py_int
ulong = py_int
ulonglong = py_int
ushort = py_int
uchar = py_int
size_t = py_int
Py_ssize_t = py_int
float = py_float
double = py_float
longdouble = py_float
bint = py_bool
void = Union[None]
basestring = py_str

gs: Dict[str, Any]  # Should match the return type of globals()

T = TypeVar('T')

class _ArrayType(object, Generic[T]):
    is_array: bool
    subtypes: Sequence[str]
    dtype: T
    ndim: int
    is_c_contig: bool
    is_f_contig: bool
    inner_contig: bool
    broadcasting: Any

    # broadcasting is not used, so it's not clear about its type
    def __init__(self, dtype: T, ndim: int, is_c_contig: bool = ...,
                 is_f_contig: bool = ..., inner_contig: bool = ...,
                 broadcasting: Any = ...) -> None: ...
    def __repr__(self) -> str: ...

class CythonTypeObject(object):
    ...

class CythonType(CythonTypeObject):
    ...

class PointerType(CythonType, Generic[T]):
    def __init__(
        self,
        value: Optional[Union[ArrayType[T],
                              PointerType[T], List[T], int]] = ...
    ) -> None: ...
    def __getitem__(self, ix: int) -> T: ...
    def __setitem__(self, ix: int, value: T) -> None: ...
    def __eq__(self, value: object) -> bool: ...
    def __repr__(self) -> str: ...

class ArrayType(PointerType[T]):
    def __init__(self) -> None: ...

def index_type(
    base_type: T, item: Union[tuple, slice, int]) -> _ArrayType[T]: ...

def pointer(basetype: T) -> Type[PointerType[T]]: ...

def array(basetype: T, n: int) -> Type[ArrayType[T]]: ...

class typedef(CythonType, Generic[T]):
    name: str

    def __init__(self, type: T, name: Optional[str] = ...) -> None: ...
    def __call__(self, *arg) -> T: ...
    def __repr__(self) -> str: ...
    __getitem__ = index_type
