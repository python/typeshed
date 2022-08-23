import sys
from _typeshed import SupportsKeysAndGetItem
from collections.abc import (
    AsyncGenerator,
    Awaitable,
    Callable,
    Coroutine,
    Generator,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    MutableSequence,
    ValuesView,
)
from importlib.machinery import ModuleSpec

# pytype crashes if types.MappingProxyType inherits from collections.abc.Mapping instead of typing.Mapping
from typing import Any, ClassVar, Generic, Mapping, Protocol, TypeVar, overload  # noqa: Y027
from typing_extensions import Literal, ParamSpec, final

__all__ = [
    "FunctionType",
    "LambdaType",
    "CodeType",
    "MappingProxyType",
    "SimpleNamespace",
    "GeneratorType",
    "CoroutineType",
    "AsyncGeneratorType",
    "MethodType",
    "BuiltinFunctionType",
    "ModuleType",
    "TracebackType",
    "FrameType",
    "GetSetDescriptorType",
    "MemberDescriptorType",
    "new_class",
    "prepare_class",
    "DynamicClassAttribute",
    "coroutine",
    "BuiltinMethodType",
    "ClassMethodDescriptorType",
    "MethodDescriptorType",
    "MethodWrapperType",
    "WrapperDescriptorType",
    "resolve_bases",
]

if sys.version_info >= (3, 8):
    __all__ += ["CellType"]

if sys.version_info >= (3, 9):
    __all__ += ["GenericAlias"]

if sys.version_info >= (3, 10):
    __all__ += ["EllipsisType", "NoneType", "NotImplementedType", "UnionType"]

# Note, all classes "defined" here require special handling.

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)
_KT = TypeVar("_KT")
_VT_co = TypeVar("_VT_co", covariant=True)
_V_co = TypeVar("_V_co", covariant=True)

@final
class _Cell:
    __hash__: ClassVar[None]  # type: ignore[assignment]
    cell_contents: Any

# Make sure this class definition stays roughly in line with `builtins.function`
@final
class FunctionType:
    @property
    def __closure__(self) -> tuple[_Cell, ...] | None: ...
    __code__: CodeType
    __defaults__: tuple[Any, ...] | None
    __dict__: dict[str, Any]
    @property
    def __globals__(self) -> dict[str, Any]: ...
    __name__: str
    __qualname__: str
    __annotations__: dict[str, Any]
    __kwdefaults__: dict[str, Any]
    if sys.version_info >= (3, 10):
        @property
        def __builtins__(self) -> dict[str, Any]: ...

    __module__: str
    def __init__(
        self,
        code: CodeType,
        globals: dict[str, Any],
        name: str | None = ...,
        argdefs: tuple[object, ...] | None = ...,
        closure: tuple[_Cell, ...] | None = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    @overload
    def __get__(self, obj: None, type: type) -> FunctionType: ...
    @overload
    def __get__(self, obj: object, type: type | None = ...) -> MethodType: ...

LambdaType = FunctionType

@final
class CodeType:
    @property
    def co_argcount(self) -> int: ...
    if sys.version_info >= (3, 8):
        @property
        def co_posonlyargcount(self) -> int: ...

    @property
    def co_kwonlyargcount(self) -> int: ...
    @property
    def co_nlocals(self) -> int: ...
    @property
    def co_stacksize(self) -> int: ...
    @property
    def co_flags(self) -> int: ...
    @property
    def co_code(self) -> bytes: ...
    @property
    def co_consts(self) -> tuple[Any, ...]: ...
    @property
    def co_names(self) -> tuple[str, ...]: ...
    @property
    def co_varnames(self) -> tuple[str, ...]: ...
    @property
    def co_filename(self) -> str: ...
    @property
    def co_name(self) -> str: ...
    @property
    def co_firstlineno(self) -> int: ...
    @property
    def co_lnotab(self) -> bytes: ...
    @property
    def co_freevars(self) -> tuple[str, ...]: ...
    @property
    def co_cellvars(self) -> tuple[str, ...]: ...
    if sys.version_info >= (3, 10):
        @property
        def co_linetable(self) -> bytes: ...
        def co_lines(self) -> Iterator[tuple[int, int, int | None]]: ...
    if sys.version_info >= (3, 11):
        @property
        def co_exceptiontable(self) -> bytes: ...
        @property
        def co_qualname(self) -> str: ...
        def co_positions(self) -> Iterable[tuple[int | None, int | None, int | None, int | None]]: ...

    if sys.version_info >= (3, 11):
        def __init__(
            self,
            __argcount: int,
            __posonlyargcount: int,
            __kwonlyargcount: int,
            __nlocals: int,
            __stacksize: int,
            __flags: int,
            __codestring: bytes,
            __constants: tuple[object, ...],
            __names: tuple[str, ...],
            __varnames: tuple[str, ...],
            __filename: str,
            __name: str,
            __qualname: str,
            __firstlineno: int,
            __linetable: bytes,
            __exceptiontable: bytes,
            __freevars: tuple[str, ...] = ...,
            __cellvars: tuple[str, ...] = ...,
        ) -> None: ...
    elif sys.version_info >= (3, 10):
        def __init__(
            self,
            __argcount: int,
            __posonlyargcount: int,
            __kwonlyargcount: int,
            __nlocals: int,
            __stacksize: int,
            __flags: int,
            __codestring: bytes,
            __constants: tuple[object, ...],
            __names: tuple[str, ...],
            __varnames: tuple[str, ...],
            __filename: str,
            __name: str,
            __firstlineno: int,
            __linetable: bytes,
            __freevars: tuple[str, ...] = ...,
            __cellvars: tuple[str, ...] = ...,
        ) -> None: ...
    elif sys.version_info >= (3, 8):
        def __init__(
            self,
            __argcount: int,
            __posonlyargcount: int,
            __kwonlyargcount: int,
            __nlocals: int,
            __stacksize: int,
            __flags: int,
            __codestring: bytes,
            __constants: tuple[object, ...],
            __names: tuple[str, ...],
            __varnames: tuple[str, ...],
            __filename: str,
            __name: str,
            __firstlineno: int,
            __lnotab: bytes,
            __freevars: tuple[str, ...] = ...,
            __cellvars: tuple[str, ...] = ...,
        ) -> None: ...
    else:
        def __init__(
            self,
            __argcount: int,
            __kwonlyargcount: int,
            __nlocals: int,
            __stacksize: int,
            __flags: int,
            __codestring: bytes,
            __constants: tuple[object, ...],
            __names: tuple[str, ...],
            __varnames: tuple[str, ...],
            __filename: str,
            __name: str,
            __firstlineno: int,
            __lnotab: bytes,
            __freevars: tuple[str, ...] = ...,
            __cellvars: tuple[str, ...] = ...,
        ) -> None: ...
    if sys.version_info >= (3, 11):
        def replace(
            self,
            *,
            co_argcount: int = ...,
            co_posonlyargcount: int = ...,
            co_kwonlyargcount: int = ...,
            co_nlocals: int = ...,
            co_stacksize: int = ...,
            co_flags: int = ...,
            co_firstlineno: int = ...,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_qualname: str = ...,
            co_linetable: bytes = ...,
            co_exceptiontable: bytes = ...,
        ) -> CodeType: ...
    elif sys.version_info >= (3, 10):
        def replace(
            self,
            *,
            co_argcount: int = ...,
            co_posonlyargcount: int = ...,
            co_kwonlyargcount: int = ...,
            co_nlocals: int = ...,
            co_stacksize: int = ...,
            co_flags: int = ...,
            co_firstlineno: int = ...,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_linetable: bytes = ...,
        ) -> CodeType: ...
    elif sys.version_info >= (3, 8):
        def replace(
            self,
            *,
            co_argcount: int = ...,
            co_posonlyargcount: int = ...,
            co_kwonlyargcount: int = ...,
            co_nlocals: int = ...,
            co_stacksize: int = ...,
            co_flags: int = ...,
            co_firstlineno: int = ...,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_lnotab: bytes = ...,
        ) -> CodeType: ...

@final
class MappingProxyType(Mapping[_KT, _VT_co], Generic[_KT, _VT_co]):
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __init__(self, mapping: SupportsKeysAndGetItem[_KT, _VT_co]) -> None: ...
    def __getitem__(self, __k: _KT) -> _VT_co: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...
    def copy(self) -> dict[_KT, _VT_co]: ...
    def keys(self) -> KeysView[_KT]: ...
    def values(self) -> ValuesView[_VT_co]: ...
    def items(self) -> ItemsView[_KT, _VT_co]: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...
        def __reversed__(self) -> Iterator[_KT]: ...
        def __or__(self, __value: Mapping[_T1, _T2]) -> dict[_KT | _T1, _VT_co | _T2]: ...
        def __ror__(self, __value: Mapping[_T1, _T2]) -> dict[_KT | _T1, _VT_co | _T2]: ...

class SimpleNamespace:
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __init__(self, **kwargs: Any) -> None: ...
    def __getattribute__(self, __name: str) -> Any: ...
    def __setattr__(self, __name: str, __value: Any) -> None: ...
    def __delattr__(self, __name: str) -> None: ...

class _LoaderProtocol(Protocol):
    def load_module(self, fullname: str) -> ModuleType: ...

class ModuleType:
    __name__: str
    __file__: str | None
    @property
    def __dict__(self) -> dict[str, Any]: ...  # type: ignore[override]
    __loader__: _LoaderProtocol | None
    __package__: str | None
    __path__: MutableSequence[str]
    __spec__: ModuleSpec | None
    def __init__(self, name: str, doc: str | None = ...) -> None: ...
    # __getattr__ doesn't exist at runtime,
    # but having it here in typeshed makes dynamic imports
    # using `builtins.__import__` or `importlib.import_module` less painful
    def __getattr__(self, name: str) -> Any: ...

@final
class GeneratorType(Generator[_T_co, _T_contra, _V_co]):
    @property
    def gi_code(self) -> CodeType: ...
    @property
    def gi_frame(self) -> FrameType: ...
    @property
    def gi_running(self) -> bool: ...
    @property
    def gi_yieldfrom(self) -> GeneratorType[_T_co, _T_contra, Any] | None: ...
    if sys.version_info >= (3, 11):
        @property
        def gi_suspended(self) -> bool: ...
    __name__: str
    __qualname__: str
    def __iter__(self) -> GeneratorType[_T_co, _T_contra, _V_co]: ...
    def __next__(self) -> _T_co: ...
    def close(self) -> None: ...
    def send(self, __arg: _T_contra) -> _T_co: ...
    @overload
    def throw(
        self, __typ: type[BaseException], __val: BaseException | object = ..., __tb: TracebackType | None = ...
    ) -> _T_co: ...
    @overload
    def throw(self, __typ: BaseException, __val: None = ..., __tb: TracebackType | None = ...) -> _T_co: ...

@final
class AsyncGeneratorType(AsyncGenerator[_T_co, _T_contra]):
    @property
    def ag_await(self) -> Awaitable[Any] | None: ...
    @property
    def ag_frame(self) -> FrameType: ...
    @property
    def ag_running(self) -> bool: ...
    @property
    def ag_code(self) -> CodeType: ...
    __name__: str
    __qualname__: str
    def __aiter__(self) -> AsyncGeneratorType[_T_co, _T_contra]: ...
    def __anext__(self) -> Coroutine[Any, Any, _T_co]: ...
    def asend(self, __val: _T_contra) -> Coroutine[Any, Any, _T_co]: ...
    @overload
    async def athrow(
        self, __typ: type[BaseException], __val: BaseException | object = ..., __tb: TracebackType | None = ...
    ) -> _T_co: ...
    @overload
    async def athrow(self, __typ: BaseException, __val: None = ..., __tb: TracebackType | None = ...) -> _T_co: ...
    def aclose(self) -> Coroutine[Any, Any, None]: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, __item: Any) -> GenericAlias: ...

@final
class CoroutineType(Coroutine[_T_co, _T_contra, _V_co]):
    __name__: str
    __qualname__: str
    @property
    def cr_await(self) -> Any | None: ...
    @property
    def cr_code(self) -> CodeType: ...
    @property
    def cr_frame(self) -> FrameType: ...
    @property
    def cr_running(self) -> bool: ...
    @property
    def cr_origin(self) -> tuple[tuple[str, int, str], ...] | None: ...
    if sys.version_info >= (3, 11):
        @property
        def cr_suspended(self) -> bool: ...

    def close(self) -> None: ...
    def __await__(self) -> Generator[Any, None, _V_co]: ...
    def send(self, __arg: _T_contra) -> _T_co: ...
    @overload
    def throw(
        self, __typ: type[BaseException], __val: BaseException | object = ..., __tb: TracebackType | None = ...
    ) -> _T_co: ...
    @overload
    def throw(self, __typ: BaseException, __val: None = ..., __tb: TracebackType | None = ...) -> _T_co: ...

class _StaticFunctionType:
    # Fictional type to correct the type of MethodType.__func__.
    # FunctionType is a descriptor, so mypy follows the descriptor protocol and
    # converts MethodType.__func__ back to MethodType (the return type of
    # FunctionType.__get__). But this is actually a special case; MethodType is
    # implemented in C and its attribute access doesn't go through
    # __getattribute__.
    # By wrapping FunctionType in _StaticFunctionType, we get the right result;
    # similar to wrapping a function in staticmethod() at runtime to prevent it
    # being bound as a method.
    def __get__(self, obj: object | None, type: type | None) -> FunctionType: ...

@final
class MethodType:
    @property
    def __closure__(self) -> tuple[_Cell, ...] | None: ...  # inherited from the added function
    @property
    def __defaults__(self) -> tuple[Any, ...] | None: ...  # inherited from the added function
    @property
    def __func__(self) -> _StaticFunctionType: ...
    @property
    def __self__(self) -> object: ...
    @property
    def __name__(self) -> str: ...  # inherited from the added function
    @property
    def __qualname__(self) -> str: ...  # inherited from the added function
    def __init__(self, __func: Callable[..., Any], __obj: object) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

@final
class BuiltinFunctionType:
    @property
    def __self__(self) -> object | ModuleType: ...
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

BuiltinMethodType = BuiltinFunctionType

@final
class WrapperDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, __obj: Any, __type: type = ...) -> Any: ...

@final
class MethodWrapperType:
    @property
    def __self__(self) -> object: ...
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...

@final
class MethodDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, obj: Any, type: type = ...) -> Any: ...

@final
class ClassMethodDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __get__(self, obj: Any, type: type = ...) -> Any: ...

@final
class TracebackType:
    def __init__(self, tb_next: TracebackType | None, tb_frame: FrameType, tb_lasti: int, tb_lineno: int) -> None: ...
    tb_next: TracebackType | None
    # the rest are read-only even in 3.7
    @property
    def tb_frame(self) -> FrameType: ...
    @property
    def tb_lasti(self) -> int: ...
    @property
    def tb_lineno(self) -> int: ...

@final
class FrameType:
    @property
    def f_back(self) -> FrameType | None: ...
    @property
    def f_builtins(self) -> dict[str, Any]: ...
    @property
    def f_code(self) -> CodeType: ...
    @property
    def f_globals(self) -> dict[str, Any]: ...
    @property
    def f_lasti(self) -> int: ...
    # see discussion in #6769: f_lineno *can* sometimes be None,
    # but you should probably file a bug report with CPython if you encounter it being None in the wild.
    # An `int | None` annotation here causes too many false-positive errors.
    @property
    def f_lineno(self) -> int | Any: ...
    @property
    def f_locals(self) -> dict[str, Any]: ...
    f_trace: Callable[[FrameType, str, Any], Any] | None
    f_trace_lines: bool
    f_trace_opcodes: bool
    def clear(self) -> None: ...

@final
class GetSetDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __get__(self, __obj: Any, __type: type = ...) -> Any: ...
    def __set__(self, __instance: Any, __value: Any) -> None: ...
    def __delete__(self, __obj: Any) -> None: ...

@final
class MemberDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __get__(self, __obj: Any, __type: type = ...) -> Any: ...
    def __set__(self, __instance: Any, __value: Any) -> None: ...
    def __delete__(self, __obj: Any) -> None: ...

def new_class(
    name: str,
    bases: Iterable[object] = ...,
    kwds: dict[str, Any] | None = ...,
    exec_body: Callable[[dict[str, Any]], object] | None = ...,
) -> type: ...
def resolve_bases(bases: Iterable[object]) -> tuple[Any, ...]: ...
def prepare_class(
    name: str, bases: tuple[type, ...] = ..., kwds: dict[str, Any] | None = ...
) -> tuple[type, dict[str, Any], dict[str, Any]]: ...

# Actually a different type, but `property` is special and we want that too.
DynamicClassAttribute = property

_Fn = TypeVar("_Fn", bound=Callable[..., object])
_R = TypeVar("_R")
_P = ParamSpec("_P")

# it's not really an Awaitable, but can be used in an await expression. Real type: Generator & Awaitable
# The type: ignore is due to overlapping overloads, not the use of ParamSpec
@overload
def coroutine(func: Callable[_P, Generator[_R, Any, Any]]) -> Callable[_P, Awaitable[_R]]: ...  # type: ignore[misc]
@overload
def coroutine(func: _Fn) -> _Fn: ...

if sys.version_info >= (3, 8):
    CellType = _Cell

if sys.version_info >= (3, 9):
    class GenericAlias:
        @property
        def __origin__(self) -> type: ...
        @property
        def __args__(self) -> tuple[Any, ...]: ...
        @property
        def __parameters__(self) -> tuple[Any, ...]: ...
        def __init__(self, origin: type, args: Any) -> None: ...
        if sys.version_info >= (3, 11):
            @property
            def __unpacked__(self) -> bool: ...
            @property
            def __typing_unpacked_tuple_args__(self) -> tuple[Any, ...] | None: ...

        def __getattr__(self, name: str) -> Any: ...  # incomplete

if sys.version_info >= (3, 10):
    @final
    class NoneType:
        def __bool__(self) -> Literal[False]: ...
    EllipsisType = ellipsis  # noqa: F821 from builtins
    from builtins import _NotImplementedType

    NotImplementedType = _NotImplementedType
    @final
    class UnionType:
        @property
        def __args__(self) -> tuple[Any, ...]: ...
        def __or__(self, __obj: Any) -> UnionType: ...
        def __ror__(self, __obj: Any) -> UnionType: ...
