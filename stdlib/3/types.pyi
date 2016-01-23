# Stubs for types
# Note, all classes "defined" here require special handling.

# TODO parts of this should be conditional on version

from typing import Any, Callable, Dict, Iterator, Optional, Tuple, TypeVar, Union, overload

_T = TypeVar('_T')

class _Cell:
    cell_contents = ...  # type: Any

class FunctionType:
    __closure__ = ...  # type: Optional[Tuple[_Cell, ...]]
    __code__ = ...  # type: CodeType
    __defaults__ = ...  # type: Optional[Tuple[Any, ...]]
    __dict__ = ...  # type: Dict[str, Any]
    __doc__ = ...  # type: Optional[str]
    __globals__ = ...  # type: Dict[str, Any]
    __name__ = ...  # type: str
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, obj: Optional[object], type: Optional[type]) -> 'MethodType': ...
LambdaType = FunctionType

class CodeType:
    """Create a code object.  Not for the faint of heart."""
    co_argcount = ... # type: int
    co_kwonlyargcount = ... # type: int
    co_nlocals = ... # type: int
    co_stacksize = ... # type: int
    co_flags = ... # type: int
    co_code = ... # type: bytes
    co_consts = ... # type: Tuple[Any, ...]
    co_names = ... # type: Tuple[str, ...]
    co_varnames = ... # type: Tuple[str, ...]
    co_filename = ... # type: Optional[str]
    co_name = ... # type: str
    co_firstlineno = ... # type: int
    co_lnotab = ... # type: bytes
    co_freevars = ... # type: Tuple[str, ...]
    co_cellvars = ... # type: Tuple[str, ...]
    def __init__(self,
            argcount: int,
            kwonlyargcount: int,
            nlocals: int,
            stacksize: int,
            flags: int,
            codestring: bytes,
            constants: Tuple[Any, ...],
            names: Tuple[str, ...],
            varnames: Tuple[str, ...],
            filename: str,
            name: str,
            firstlineno: int,
            lnotab: bytes,
            freevars: Tuple[str, ...] = ...,
            cellvars: Tuple[str, ...] = ...,
    ) -> None: ...

class MappingProxyType:
    def copy(self) -> dict: ...
    def get(self, key: str, default: _T = ...) -> Union[Any, _T]: ...
    def items(self) -> Iterator[Tuple[str, Any]]: ...
    def keys(self) -> Iterator[str]: ...
    def values(self) -> Iterator[Any]: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
class SimpleNamespace(Any): ...

class GeneratorType:
    gi_code = ...  # type: CodeType
    gi_frame = ...  # type: FrameType
    gi_running = ...  # type: bool
    gi_yieldfrom = ...  # type: Optional[GeneratorType]
    def __iter__(self) -> 'GeneratorType': ...
    def __next__(self) -> Any: ...
    def close(self) -> None: ...
    def send(self, arg: Any) -> Any: ...
    @overload
    def throw(self, val: BaseException) -> Any: ...
    @overload
    def throw(self, typ: type, val: BaseException = ..., tb: 'TracebackType' = ...) -> Any: ...

class CoroutineType:
    cr_await = ...  # type: Optional[Any]
    cr_code = ...  # type: CodeType
    cr_frame = ...  # type: FrameType
    cr_running = ...  # type: bool
    def close(self) -> None: ...
    def send(self, arg: Any) -> Any: ...
    @overload
    def throw(self, val: BaseException) -> Any: ...
    @overload
    def throw(self, typ: type, val: BaseException = ..., tb: 'TracebackType' = ...) -> Any: ...

class MethodType:
    __func__ = ...  # type: FunctionType
    __self__ = ...  # type: object
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
class BuiltinFunctionType:
    __self__ = ...  # type: Union[object, ModuleType]
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
BuiltinMethodType = BuiltinFunctionType

class ModuleType:
    __name__ = ... # type: str
    __file__ = ... # type: str
    def __init__(self, name: str, doc: Any) -> None: ...

class TracebackType:
    tb_frame = ... # type: FrameType
    tb_lasti = ... # type: int
    tb_lineno = ... # type: int
    tb_next = ... # type: TracebackType

class FrameType:
    f_back = ... # type: FrameType
    f_builtins = ... # type: Dict[str, Any]
    f_code = ... # type: CodeType
    f_globals = ... # type: Dict[str, Any]
    f_lasti = ... # type: int
    f_lineno = ... # type: int
    f_locals = ... # type: Dict[str, Any]
    f_trace = ... # type: Callable[[], None]

    def clear(self) -> None: pass

class GetSetDescriptorType:
    __name__ = ...  # type: str
    __objclass__ = ...  # type: type
    def __get__(self, obj: Any, type: type = ...) -> Any: ...
    def __set__(self, obj: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...
class MemberDescriptorType:
    __name__ = ...  # type: str
    __objclass__ = ...  # type: type
    def __get__(self, obj: Any, type: type = ...) -> Any: ...
    def __set__(self, obj: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...

def new_class(name: str, bases: Tuple[type, ...] = ..., kwds: Dict[str, Any] = ..., exec_body: Callable[[Dict[str, Any]], None] = ...) -> type: ...
def prepare_class(name: str, bases: Tuple[type, ...] = ..., kwds: Dict[str, Any] = ...) -> Tuple[type, Dict[str, Any], Dict[str, Any]]: ...

# Actually a different type, but `property` is special and we want that too.
DynamicClassAttribute = property

def coroutine(f: Callable[..., Any]) -> CoroutineType: ...
