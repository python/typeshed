from _typeshed import Incomplete

unicode = str
long = int
xrange = range
bytechr: Incomplete

class CTypesType(type): ...

class CTypesData:
    __metaclass__: Incomplete
    __name__: str
    def __init__(self, *args) -> None: ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self) -> int: ...
    def __repr__(self, c_name: str | None = ...): ...

class CTypesGenericPrimitive(CTypesData):
    def __hash__(self) -> int: ...

class CTypesGenericArray(CTypesData):
    def __iter__(self): ...

class CTypesGenericPtr(CTypesData):
    kind: str
    def __nonzero__(self): ...
    def __bool__(self) -> bool: ...

class CTypesBaseStructOrUnion(CTypesData): ...

class CTypesBackend:
    PRIMITIVE_TYPES: Incomplete
    RTLD_LAZY: int
    RTLD_NOW: int
    RTLD_GLOBAL: Incomplete
    RTLD_LOCAL: Incomplete
    def __init__(self) -> None: ...
    ffi: Incomplete
    def set_ffi(self, ffi) -> None: ...
    def load_library(self, path, flags: int = ...): ...
    def new_void_type(self): ...
    def new_primitive_type(self, name): ...
    def new_pointer_type(self, BItem): ...
    def new_array_type(self, CTypesPtr, length): ...
    def new_struct_type(self, name): ...
    def new_union_type(self, name): ...
    def complete_struct_or_union(
        self, CTypesStructOrUnion, fields, tp, totalsize: int = ..., totalalignment: int = ..., sflags: int = ..., pack: int = ...
    ): ...
    def new_function_type(self, BArgs, BResult, has_varargs): ...
    def new_enum_type(self, name, enumerators, enumvalues, CTypesInt): ...
    def get_errno(self): ...
    def set_errno(self, value) -> None: ...
    def string(self, b, maxlen: int = ...): ...
    def buffer(self, bptr, size: int = ...) -> None: ...
    def sizeof(self, cdata_or_BType): ...
    def alignof(self, BType): ...
    def newp(self, BType, source): ...
    def cast(self, BType, source): ...
    def callback(self, BType, source, error, onerror): ...
    def gcp(self, cdata, destructor, size: int = ...): ...
    typeof: Incomplete
    def getcname(self, BType, replace_with): ...
    def typeoffsetof(self, BType, fieldname, num: int = ...): ...
    def rawaddressof(self, BTypePtr, cdata, offset: Incomplete | None = ...): ...

class CTypesLibrary:
    backend: Incomplete
    cdll: Incomplete
    def __init__(self, backend, cdll) -> None: ...
    def load_function(self, BType, name): ...
    def read_variable(self, BType, name): ...
    def write_variable(self, BType, name, value) -> None: ...
