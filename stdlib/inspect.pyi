import dis
import enum
import sys
import types
from _typeshed import StrPath
from collections import OrderedDict
from collections.abc import AsyncGenerator, Awaitable, Callable, Coroutine, Generator, Mapping, Sequence, Set as AbstractSet
from types import (
    AsyncGeneratorType,
    BuiltinFunctionType,
    BuiltinMethodType,
    ClassMethodDescriptorType,
    CodeType,
    CoroutineType,
    FrameType,
    FunctionType,
    GeneratorType,
    GetSetDescriptorType,
    LambdaType,
    MemberDescriptorType,
    MethodDescriptorType,
    MethodType,
    MethodWrapperType,
    ModuleType,
    TracebackType,
    WrapperDescriptorType,
)
from typing import Any, ClassVar, Literal, NamedTuple, Protocol, TypeVar, overload
from typing_extensions import ParamSpec, Self, TypeAlias, TypeGuard

if sys.version_info >= (3, 11):
    __all__ = [
        "ArgInfo",
        "Arguments",
        "Attribute",
        "BlockFinder",
        "BoundArguments",
        "CORO_CLOSED",
        "CORO_CREATED",
        "CORO_RUNNING",
        "CORO_SUSPENDED",
        "CO_ASYNC_GENERATOR",
        "CO_COROUTINE",
        "CO_GENERATOR",
        "CO_ITERABLE_COROUTINE",
        "CO_NESTED",
        "CO_NEWLOCALS",
        "CO_NOFREE",
        "CO_OPTIMIZED",
        "CO_VARARGS",
        "CO_VARKEYWORDS",
        "ClassFoundException",
        "ClosureVars",
        "EndOfBlock",
        "FrameInfo",
        "FullArgSpec",
        "GEN_CLOSED",
        "GEN_CREATED",
        "GEN_RUNNING",
        "GEN_SUSPENDED",
        "Parameter",
        "Signature",
        "TPFLAGS_IS_ABSTRACT",
        "Traceback",
        "classify_class_attrs",
        "cleandoc",
        "currentframe",
        "findsource",
        "formatannotation",
        "formatannotationrelativeto",
        "formatargvalues",
        "get_annotations",
        "getabsfile",
        "getargs",
        "getargvalues",
        "getattr_static",
        "getblock",
        "getcallargs",
        "getclasstree",
        "getclosurevars",
        "getcomments",
        "getcoroutinelocals",
        "getcoroutinestate",
        "getdoc",
        "getfile",
        "getframeinfo",
        "getfullargspec",
        "getgeneratorlocals",
        "getgeneratorstate",
        "getinnerframes",
        "getlineno",
        "getmembers",
        "getmembers_static",
        "getmodule",
        "getmodulename",
        "getmro",
        "getouterframes",
        "getsource",
        "getsourcefile",
        "getsourcelines",
        "indentsize",
        "isabstract",
        "isasyncgen",
        "isasyncgenfunction",
        "isawaitable",
        "isbuiltin",
        "isclass",
        "iscode",
        "iscoroutine",
        "iscoroutinefunction",
        "isdatadescriptor",
        "isframe",
        "isfunction",
        "isgenerator",
        "isgeneratorfunction",
        "isgetsetdescriptor",
        "ismemberdescriptor",
        "ismethod",
        "ismethoddescriptor",
        "ismethodwrapper",
        "ismodule",
        "isroutine",
        "istraceback",
        "signature",
        "stack",
        "trace",
        "unwrap",
        "walktree",
    ]

    if sys.version_info >= (3, 12):
        __all__ += [
            "markcoroutinefunction",
            "AGEN_CLOSED",
            "AGEN_CREATED",
            "AGEN_RUNNING",
            "AGEN_SUSPENDED",
            "getasyncgenlocals",
            "getasyncgenstate",
            "BufferFlags",
        ]

_P = ParamSpec("_P")
_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_T_cont = TypeVar("_T_cont", contravariant=True)
_V_cont = TypeVar("_V_cont", contravariant=True)

#
# Types and members
#
class EndOfBlock(Exception): ...

class BlockFinder:
    indent: int
    islambda: bool
    started: bool
    passline: bool
    indecorator: bool
    decoratorhasargs: bool
    last: int
    def tokeneater(self, type: int, token: str, srowcol: tuple[int, int], erowcol: tuple[int, int], line: str) -> None: ...

CO_OPTIMIZED: Literal[1]
CO_NEWLOCALS: Literal[2]
CO_VARARGS: Literal[4]
CO_VARKEYWORDS: Literal[8]
CO_NESTED: Literal[16]
CO_GENERATOR: Literal[32]
CO_NOFREE: Literal[64]
CO_COROUTINE: Literal[128]
CO_ITERABLE_COROUTINE: Literal[256]
CO_ASYNC_GENERATOR: Literal[512]
TPFLAGS_IS_ABSTRACT: Literal[1048576]

modulesbyfile: dict[str, Any]

_GetMembersPredicateTypeGuard: TypeAlias = Callable[[Any], TypeGuard[_T]]
_GetMembersPredicate: TypeAlias = Callable[[Any], bool]
_GetMembersReturnTypeGuard: TypeAlias = list[tuple[str, _T]]
_GetMembersReturn: TypeAlias = list[tuple[str, Any]]

@overload
def getmembers(object: object, predicate: _GetMembersPredicateTypeGuard[_T]) -> _GetMembersReturnTypeGuard[_T]: ...
@overload
def getmembers(object: object, predicate: _GetMembersPredicate | None = None) -> _GetMembersReturn: ...

if sys.version_info >= (3, 11):
    @overload
    def getmembers_static(object: object, predicate: _GetMembersPredicateTypeGuard[_T]) -> _GetMembersReturnTypeGuard[_T]: ...
    @overload
    def getmembers_static(object: object, predicate: _GetMembersPredicate | None = None) -> _GetMembersReturn: ...

def getmodulename(path: StrPath) -> str | None: ...
def ismodule(object: object) -> TypeGuard[ModuleType]: ...
def isclass(object: object) -> TypeGuard[type[Any]]: ...
def ismethod(object: object) -> TypeGuard[MethodType]: ...
def isfunction(object: object) -> TypeGuard[FunctionType]: ...

if sys.version_info >= (3, 12):
    def markcoroutinefunction(func: _F) -> _F: ...

@overload
def isgeneratorfunction(obj: Callable[..., Generator[Any, Any, Any]]) -> bool: ...
@overload
def isgeneratorfunction(obj: Callable[_P, Any]) -> TypeGuard[Callable[_P, GeneratorType[Any, Any, Any]]]: ...
@overload
def isgeneratorfunction(obj: object) -> TypeGuard[Callable[..., GeneratorType[Any, Any, Any]]]: ...
@overload
def iscoroutinefunction(obj: Callable[..., Coroutine[Any, Any, Any]]) -> bool: ...
@overload
def iscoroutinefunction(obj: Callable[_P, Awaitable[_T]]) -> TypeGuard[Callable[_P, CoroutineType[Any, Any, _T]]]: ...
@overload
def iscoroutinefunction(obj: Callable[_P, object]) -> TypeGuard[Callable[_P, CoroutineType[Any, Any, Any]]]: ...
@overload
def iscoroutinefunction(obj: object) -> TypeGuard[Callable[..., CoroutineType[Any, Any, Any]]]: ...
def isgenerator(object: object) -> TypeGuard[GeneratorType[Any, Any, Any]]: ...
def iscoroutine(object: object) -> TypeGuard[CoroutineType[Any, Any, Any]]: ...
def isawaitable(object: object) -> TypeGuard[Awaitable[Any]]: ...
@overload
def isasyncgenfunction(obj: Callable[..., AsyncGenerator[Any, Any]]) -> bool: ...
@overload
def isasyncgenfunction(obj: Callable[_P, Any]) -> TypeGuard[Callable[_P, AsyncGeneratorType[Any, Any]]]: ...
@overload
def isasyncgenfunction(obj: object) -> TypeGuard[Callable[..., AsyncGeneratorType[Any, Any]]]: ...

class _SupportsSet(Protocol[_T_cont, _V_cont]):
    def __set__(self, instance: _T_cont, value: _V_cont, /) -> None: ...

class _SupportsDelete(Protocol[_T_cont]):
    def __delete__(self, instance: _T_cont, /) -> None: ...

def isasyncgen(object: object) -> TypeGuard[AsyncGeneratorType[Any, Any]]: ...
def istraceback(object: object) -> TypeGuard[TracebackType]: ...
def isframe(object: object) -> TypeGuard[FrameType]: ...
def iscode(object: object) -> TypeGuard[CodeType]: ...
def isbuiltin(object: object) -> TypeGuard[BuiltinFunctionType]: ...

if sys.version_info >= (3, 11):
    def ismethodwrapper(object: object) -> TypeGuard[MethodWrapperType]: ...

def isroutine(
    object: object,
) -> TypeGuard[
    FunctionType
    | LambdaType
    | MethodType
    | BuiltinFunctionType
    | BuiltinMethodType
    | WrapperDescriptorType
    | MethodDescriptorType
    | ClassMethodDescriptorType
]: ...
def ismethoddescriptor(object: object) -> TypeGuard[MethodDescriptorType]: ...
def ismemberdescriptor(object: object) -> TypeGuard[MemberDescriptorType]: ...
def isabstract(object: object) -> bool: ...
def isgetsetdescriptor(object: object) -> TypeGuard[GetSetDescriptorType]: ...
def isdatadescriptor(object: object) -> TypeGuard[_SupportsSet[Any, Any] | _SupportsDelete[Any]]: ...

#
# Retrieving source code
#
_SourceObjectType: TypeAlias = (
    ModuleType | type[Any] | MethodType | FunctionType | TracebackType | FrameType | CodeType | Callable[..., Any]
)

def findsource(object: _SourceObjectType) -> tuple[list[str], int]: ...
def getabsfile(object: _SourceObjectType, _filename: str | None = None) -> str: ...

# Special-case the two most common input types here
# to avoid the annoyingly vague `Sequence[str]` return type
@overload
def getblock(lines: list[str]) -> list[str]: ...
@overload
def getblock(lines: tuple[str, ...]) -> tuple[str, ...]: ...
@overload
def getblock(lines: Sequence[str]) -> Sequence[str]: ...
def getdoc(object: object) -> str | None: ...
def getcomments(object: object) -> str | None: ...
def getfile(object: _SourceObjectType) -> str: ...
def getmodule(object: object, _filename: str | None = None) -> ModuleType | None: ...
def getsourcefile(object: _SourceObjectType) -> str | None: ...
def getsourcelines(object: _SourceObjectType) -> tuple[list[str], int]: ...
def getsource(object: _SourceObjectType) -> str: ...
def cleandoc(doc: str) -> str: ...
def indentsize(line: str) -> int: ...

_IntrospectableCallable: TypeAlias = Callable[..., Any]

#
# Introspecting callables with the Signature object
#
if sys.version_info >= (3, 10):
    def signature(
        obj: _IntrospectableCallable,
        *,
        follow_wrapped: bool = True,
        globals: Mapping[str, Any] | None = None,
        locals: Mapping[str, Any] | None = None,
        eval_str: bool = False,
    ) -> Signature: ...

else:
    def signature(obj: _IntrospectableCallable, *, follow_wrapped: bool = True) -> Signature: ...

class _void: ...
class _empty: ...

class Signature:
    def __init__(
        self, parameters: Sequence[Parameter] | None = None, *, return_annotation: Any = ..., __validate_parameters__: bool = True
    ) -> None: ...
    empty = _empty
    @property
    def parameters(self) -> types.MappingProxyType[str, Parameter]: ...
    @property
    def return_annotation(self) -> Any: ...
    def bind(self, *args: Any, **kwargs: Any) -> BoundArguments: ...
    def bind_partial(self, *args: Any, **kwargs: Any) -> BoundArguments: ...
    def replace(self, *, parameters: Sequence[Parameter] | type[_void] | None = ..., return_annotation: Any = ...) -> Self: ...
    if sys.version_info >= (3, 10):
        @classmethod
        def from_callable(
            cls,
            obj: _IntrospectableCallable,
            *,
            follow_wrapped: bool = True,
            globals: Mapping[str, Any] | None = None,
            locals: Mapping[str, Any] | None = None,
            eval_str: bool = False,
        ) -> Self: ...
    else:
        @classmethod
        def from_callable(cls, obj: _IntrospectableCallable, *, follow_wrapped: bool = True) -> Self: ...

    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

if sys.version_info >= (3, 10):
    def get_annotations(
        obj: Callable[..., object] | type[Any] | ModuleType,
        *,
        globals: Mapping[str, Any] | None = None,
        locals: Mapping[str, Any] | None = None,
        eval_str: bool = False,
    ) -> dict[str, Any]: ...

# The name is the same as the enum's name in CPython
class _ParameterKind(enum.IntEnum):
    POSITIONAL_ONLY: int
    POSITIONAL_OR_KEYWORD: int
    VAR_POSITIONAL: int
    KEYWORD_ONLY: int
    VAR_KEYWORD: int

    @property
    def description(self) -> str: ...

if sys.version_info >= (3, 12):
    AGEN_CREATED: Literal["AGEN_CREATED"]
    AGEN_RUNNING: Literal["AGEN_RUNNING"]
    AGEN_SUSPENDED: Literal["AGEN_SUSPENDED"]
    AGEN_CLOSED: Literal["AGEN_CLOSED"]

    def getasyncgenstate(
        agen: AsyncGenerator[Any, Any],
    ) -> Literal["AGEN_CREATED", "AGEN_RUNNING", "AGEN_SUSPENDED", "AGEN_CLOSED"]: ...
    def getasyncgenlocals(agen: AsyncGeneratorType[Any, Any]) -> dict[str, Any]: ...

class Parameter:
    def __init__(self, name: str, kind: _ParameterKind, *, default: Any = ..., annotation: Any = ...) -> None: ...
    empty = _empty

    POSITIONAL_ONLY: ClassVar[Literal[_ParameterKind.POSITIONAL_ONLY]]
    POSITIONAL_OR_KEYWORD: ClassVar[Literal[_ParameterKind.POSITIONAL_OR_KEYWORD]]
    VAR_POSITIONAL: ClassVar[Literal[_ParameterKind.VAR_POSITIONAL]]
    KEYWORD_ONLY: ClassVar[Literal[_ParameterKind.KEYWORD_ONLY]]
    VAR_KEYWORD: ClassVar[Literal[_ParameterKind.VAR_KEYWORD]]
    @property
    def name(self) -> str: ...
    @property
    def default(self) -> Any: ...
    @property
    def kind(self) -> _ParameterKind: ...
    @property
    def annotation(self) -> Any: ...
    def replace(
        self,
        *,
        name: str | type[_void] = ...,
        kind: _ParameterKind | type[_void] = ...,
        default: Any = ...,
        annotation: Any = ...,
    ) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class BoundArguments:
    arguments: OrderedDict[str, Any]
    @property
    def args(self) -> tuple[Any, ...]: ...
    @property
    def kwargs(self) -> dict[str, Any]: ...
    @property
    def signature(self) -> Signature: ...
    def __init__(self, signature: Signature, arguments: OrderedDict[str, Any]) -> None: ...
    def apply_defaults(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...

#
# Classes and functions
#

# TODO: The actual return type should be list[_ClassTreeItem] but mypy doesn't
# seem to be supporting this at the moment:
# _ClassTreeItem = list[_ClassTreeItem] | Tuple[type, Tuple[type, ...]]
def getclasstree(classes: list[type], unique: bool = False) -> list[Any]: ...
def walktree(classes: list[type], children: Mapping[type[Any], list[type]], parent: type[Any] | None) -> list[Any]: ...

class Arguments(NamedTuple):
    args: list[str]
    varargs: str | None
    varkw: str | None

def getargs(co: CodeType) -> Arguments: ...

if sys.version_info < (3, 11):
    class ArgSpec(NamedTuple):
        args: list[str]
        varargs: str | None
        keywords: str | None
        defaults: tuple[Any, ...]

    def getargspec(func: object) -> ArgSpec: ...

class FullArgSpec(NamedTuple):
    args: list[str]
    varargs: str | None
    varkw: str | None
    defaults: tuple[Any, ...] | None
    kwonlyargs: list[str]
    kwonlydefaults: dict[str, Any] | None
    annotations: dict[str, Any]

def getfullargspec(func: object) -> FullArgSpec: ...

class ArgInfo(NamedTuple):
    args: list[str]
    varargs: str | None
    keywords: str | None
    locals: dict[str, Any]

def getargvalues(frame: FrameType) -> ArgInfo: ...
def formatannotation(annotation: object, base_module: str | None = None) -> str: ...
def formatannotationrelativeto(object: object) -> Callable[[object], str]: ...

if sys.version_info < (3, 11):
    def formatargspec(
        args: list[str],
        varargs: str | None = None,
        varkw: str | None = None,
        defaults: tuple[Any, ...] | None = None,
        kwonlyargs: Sequence[str] | None = (),
        kwonlydefaults: Mapping[str, Any] | None = {},
        annotations: Mapping[str, Any] = {},
        formatarg: Callable[[str], str] = ...,
        formatvarargs: Callable[[str], str] = ...,
        formatvarkw: Callable[[str], str] = ...,
        formatvalue: Callable[[Any], str] = ...,
        formatreturns: Callable[[Any], str] = ...,
        formatannotation: Callable[[Any], str] = ...,
    ) -> str: ...

def formatargvalues(
    args: list[str],
    varargs: str | None,
    varkw: str | None,
    locals: Mapping[str, Any] | None,
    formatarg: Callable[[str], str] | None = ...,
    formatvarargs: Callable[[str], str] | None = ...,
    formatvarkw: Callable[[str], str] | None = ...,
    formatvalue: Callable[[Any], str] | None = ...,
) -> str: ...
def getmro(cls: type) -> tuple[type, ...]: ...
def getcallargs(func: Callable[_P, Any], /, *args: _P.args, **kwds: _P.kwargs) -> dict[str, Any]: ...

class ClosureVars(NamedTuple):
    nonlocals: Mapping[str, Any]
    globals: Mapping[str, Any]
    builtins: Mapping[str, Any]
    unbound: AbstractSet[str]

def getclosurevars(func: _IntrospectableCallable) -> ClosureVars: ...
def unwrap(func: Callable[..., Any], *, stop: Callable[[Callable[..., Any]], Any] | None = None) -> Any: ...

#
# The interpreter stack
#

if sys.version_info >= (3, 11):
    class _Traceback(NamedTuple):
        filename: str
        lineno: int
        function: str
        code_context: list[str] | None
        index: int | None  # type: ignore[assignment]

    class Traceback(_Traceback):
        positions: dis.Positions | None
        def __new__(
            cls,
            filename: str,
            lineno: int,
            function: str,
            code_context: list[str] | None,
            index: int | None,
            *,
            positions: dis.Positions | None = None,
        ) -> Self: ...

    class _FrameInfo(NamedTuple):
        frame: FrameType
        filename: str
        lineno: int
        function: str
        code_context: list[str] | None
        index: int | None  # type: ignore[assignment]

    class FrameInfo(_FrameInfo):
        positions: dis.Positions | None
        def __new__(
            cls,
            frame: FrameType,
            filename: str,
            lineno: int,
            function: str,
            code_context: list[str] | None,
            index: int | None,
            *,
            positions: dis.Positions | None = None,
        ) -> Self: ...

else:
    class Traceback(NamedTuple):
        filename: str
        lineno: int
        function: str
        code_context: list[str] | None
        index: int | None  # type: ignore[assignment]

    class FrameInfo(NamedTuple):
        frame: FrameType
        filename: str
        lineno: int
        function: str
        code_context: list[str] | None
        index: int | None  # type: ignore[assignment]

def getframeinfo(frame: FrameType | TracebackType, context: int = 1) -> Traceback: ...
def getouterframes(frame: Any, context: int = 1) -> list[FrameInfo]: ...
def getinnerframes(tb: TracebackType, context: int = 1) -> list[FrameInfo]: ...
def getlineno(frame: FrameType) -> int: ...
def currentframe() -> FrameType | None: ...
def stack(context: int = 1) -> list[FrameInfo]: ...
def trace(context: int = 1) -> list[FrameInfo]: ...

#
# Fetching attributes statically
#

def getattr_static(obj: object, attr: str, default: Any | None = ...) -> Any: ...

#
# Current State of Generators and Coroutines
#

GEN_CREATED: Literal["GEN_CREATED"]
GEN_RUNNING: Literal["GEN_RUNNING"]
GEN_SUSPENDED: Literal["GEN_SUSPENDED"]
GEN_CLOSED: Literal["GEN_CLOSED"]

def getgeneratorstate(
    generator: Generator[Any, Any, Any],
) -> Literal["GEN_CREATED", "GEN_RUNNING", "GEN_SUSPENDED", "GEN_CLOSED"]: ...

CORO_CREATED: Literal["CORO_CREATED"]
CORO_RUNNING: Literal["CORO_RUNNING"]
CORO_SUSPENDED: Literal["CORO_SUSPENDED"]
CORO_CLOSED: Literal["CORO_CLOSED"]

def getcoroutinestate(
    coroutine: Coroutine[Any, Any, Any],
) -> Literal["CORO_CREATED", "CORO_RUNNING", "CORO_SUSPENDED", "CORO_CLOSED"]: ...
def getgeneratorlocals(generator: Generator[Any, Any, Any]) -> dict[str, Any]: ...
def getcoroutinelocals(coroutine: Coroutine[Any, Any, Any]) -> dict[str, Any]: ...

# Create private type alias to avoid conflict with symbol of same
# name created in Attribute class.
_Object: TypeAlias = object

class Attribute(NamedTuple):
    name: str
    kind: Literal["class method", "static method", "property", "method", "data"]
    defining_class: type
    object: _Object

def classify_class_attrs(cls: type) -> list[Attribute]: ...

if sys.version_info >= (3, 9):
    class ClassFoundException(Exception): ...

if sys.version_info >= (3, 12):
    class BufferFlags(enum.IntFlag):
        SIMPLE: int
        WRITABLE: int
        FORMAT: int
        ND: int
        STRIDES: int
        C_CONTIGUOUS: int
        F_CONTIGUOUS: int
        ANY_CONTIGUOUS: int
        INDIRECT: int
        CONTIG: int
        CONTIG_RO: int
        STRIDED: int
        STRIDED_RO: int
        RECORDS: int
        RECORDS_RO: int
        FULL: int
        FULL_RO: int
        READ: int
        WRITE: int
