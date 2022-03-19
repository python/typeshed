from types import CodeType, FrameType, FunctionType, MethodType, ModuleType, TracebackType
from typing import Any, AnyStr, Callable, NamedTuple, Sequence, Union

# Types and members
class EndOfBlock(Exception): ...

class BlockFinder:
    indent: int
    islambda: bool
    started: bool
    passline: bool
    last: int
    def tokeneater(
        self, type: int, token: AnyStr, srow_scol: tuple[int, int], erow_ecol: tuple[int, int], line: AnyStr
    ) -> None: ...

CO_GENERATOR: int
CO_NESTED: int
CO_NEWLOCALS: int
CO_NOFREE: int
CO_OPTIMIZED: int
CO_VARARGS: int
CO_VARKEYWORDS: int
TPFLAGS_IS_ABSTRACT: int

class ModuleInfo(NamedTuple):
    name: str
    suffix: str
    mode: str
    module_type: int

def getmembers(object: object, predicate: Callable[[Any], bool] | None = ...) -> list[tuple[str, Any]]: ...
def getmoduleinfo(path: str | unicode) -> ModuleInfo | None: ...
def getmodulename(path: AnyStr) -> AnyStr | None: ...
def ismodule(object: object) -> bool: ...
def isclass(object: object) -> bool: ...
def ismethod(object: object) -> bool: ...
def isfunction(object: object) -> bool: ...
def isgeneratorfunction(object: object) -> bool: ...
def isgenerator(object: object) -> bool: ...
def istraceback(object: object) -> bool: ...
def isframe(object: object) -> bool: ...
def iscode(object: object) -> bool: ...
def isbuiltin(object: object) -> bool: ...
def isroutine(object: object) -> bool: ...
def isabstract(object: object) -> bool: ...
def ismethoddescriptor(object: object) -> bool: ...
def isdatadescriptor(object: object) -> bool: ...
def isgetsetdescriptor(object: object) -> bool: ...
def ismemberdescriptor(object: object) -> bool: ...

# Retrieving source code
_SourceObjectType = Union[ModuleType, type[Any], MethodType, FunctionType, TracebackType, FrameType, CodeType, Callable[..., Any]]

def findsource(object: _SourceObjectType) -> tuple[list[str], int]: ...
def getabsfile(object: _SourceObjectType) -> str: ...
def getblock(lines: Sequence[AnyStr]) -> Sequence[AnyStr]: ...
def getdoc(object: object) -> str | None: ...
def getcomments(object: object) -> str | None: ...
def getfile(object: _SourceObjectType) -> str: ...
def getmodule(object: object) -> ModuleType | None: ...
def getsourcefile(object: _SourceObjectType) -> str | None: ...
def getsourcelines(object: _SourceObjectType) -> tuple[list[str], int]: ...
def getsource(object: _SourceObjectType) -> str: ...
def cleandoc(doc: AnyStr) -> AnyStr: ...
def indentsize(line: str | unicode) -> int: ...

# Classes and functions
def getclasstree(classes: list[type], unique: bool = ...) -> list[tuple[type, tuple[type, ...]] | list[Any]]: ...

class ArgSpec(NamedTuple):
    args: list[str]
    varargs: str | None
    keywords: str | None
    defaults: tuple[Any, ...]

class ArgInfo(NamedTuple):
    args: list[str]
    varargs: str | None
    keywords: str | None
    locals: dict[str, Any]

class Arguments(NamedTuple):
    args: list[str | list[Any]]
    varargs: str | None
    keywords: str | None

def getargs(co: CodeType) -> Arguments: ...
def getargspec(func: object) -> ArgSpec: ...
def getargvalues(frame: FrameType) -> ArgInfo: ...
def formatargspec(
    args, varargs=..., varkw=..., defaults=..., formatarg=..., formatvarargs=..., formatvarkw=..., formatvalue=..., join=...
) -> str: ...
def formatargvalues(
    args, varargs=..., varkw=..., defaults=..., formatarg=..., formatvarargs=..., formatvarkw=..., formatvalue=..., join=...
) -> str: ...
def getmro(cls: type) -> tuple[type, ...]: ...
def getcallargs(func, *args, **kwds) -> dict[str, Any]: ...

# The interpreter stack

class Traceback(NamedTuple):
    filename: str
    lineno: int
    function: str
    code_context: list[str] | None
    index: int | None  # type: ignore

_FrameInfo = tuple[FrameType, str, int, str, list[str] | None, int | None]

def getouterframes(frame: FrameType, context: int = ...) -> list[_FrameInfo]: ...
def getframeinfo(frame: FrameType | TracebackType, context: int = ...) -> Traceback: ...
def getinnerframes(traceback: TracebackType, context: int = ...) -> list[_FrameInfo]: ...
def getlineno(frame: FrameType) -> int: ...
def currentframe(depth: int = ...) -> FrameType: ...
def stack(context: int = ...) -> list[_FrameInfo]: ...
def trace(context: int = ...) -> list[_FrameInfo]: ...

# Create private type alias to avoid conflict with symbol of same
# name created in Attribute class.
_Object = object

class Attribute(NamedTuple):
    name: str
    kind: str
    defining_class: type
    object: _Object

def classify_class_attrs(cls: type) -> list[Attribute]: ...
