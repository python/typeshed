from types import CodeType, TracebackType, FrameType, FunctionType, MethodType, ModuleType
from typing import Any, Dict, Callable, List, NamedTuple, Optional, Sequence, Tuple, Type, Union

# Types and members
class EndOfBlock(Exception): ...

class BlockFinder:
    indent: int
    islambda: bool
    started: bool
    passline: bool
    last: int
    def tokeneater(self, type: int, token: str, srow_scol: Tuple[int, int],
                   erow_ecol: Tuple[int, int], line: str) -> None: ...

CO_GENERATOR: int
CO_NESTED: int
CO_NEWLOCALS: int
CO_NOFREE: int
CO_OPTIMIZED: int
CO_VARARGS: int
CO_VARKEYWORDS: int
TPFLAGS_IS_ABSTRACT: int

ModuleInfo = NamedTuple('ModuleInfo', [('name', str),
                                       ('suffix', str),
                                       ('mode', str),
                                       ('module_type', int),
                                       ])
def getmembers(
    object: object,
    predicate: Optional[Callable[[Any], bool]] = ...
) -> List[Tuple[str, Any]]: ...
def getmoduleinfo(path: str) -> Optional[ModuleInfo]: ...
def getmodulename(path: str) -> Optional[str]: ...

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
_SourceObjectType = Union[ModuleType, Type, MethodType, FunctionType,
                          TracebackType, FrameType, CodeType]

def findsource(object: _SourceObjectType) -> Tuple[List[str], int]: ...
def getabsfile(object: _SourceObjectType) -> str: ...
def getblock(lines: Sequence[str]) -> Sequence[str]: ...
def getdoc(object: object) -> Optional[str]: ...
def getcomments(object: object) -> Optional[str]: ...
def getfile(object: _SourceObjectType) -> str: ...
def getmodule(object: object) -> Optional[ModuleType]: ...
def getsourcefile(object: _SourceObjectType) -> Optional[str]: ...
def getsourcelines(object: _SourceObjectType) -> Tuple[List[str], int]: ...
def getsource(object: _SourceObjectType) -> str: ...
def cleandoc(doc: str) -> str: ...
def indentsize(line: str) -> int: ...

# Classes and functions
def getclasstree(classes: List[type], unique: bool = ...) -> List[
    Union[Tuple[type, Tuple[type, ...]], list]]: ...

ArgSpec = NamedTuple('ArgSpec', [('args', List[str]),
                                 ('varargs', Optional[str]),
                                 ('keywords', Optional[str]),
                                 ('defaults', tuple),
                                 ])

ArgInfo = NamedTuple('ArgInfo', [('args', List[str]),
                                 ('varargs', Optional[str]),
                                 ('keywords', Optional[str]),
                                 ('locals', Dict[str, Any]),
                                 ])

Arguments = NamedTuple('Arguments', [('args', List[Union[str, List[Any]]]),
                                     ('varargs', Optional[str]),
                                     ('keywords', Optional[str]),
                                     ])

def getargs(co: CodeType) -> Arguments: ...
def getargspec(func: object) -> ArgSpec: ...
def getargvalues(frame: FrameType) -> ArgInfo: ...
def formatargspec(args, varargs=..., varkw=..., defaults=...,
                  formatarg=..., formatvarargs=..., formatvarkw=..., formatvalue=...,
                  join=...) -> str: ...
def formatargvalues(args, varargs=..., varkw=..., defaults=...,
                    formatarg=..., formatvarargs=..., formatvarkw=..., formatvalue=...,
                    join=...) -> str: ...
def getmro(cls: type) -> Tuple[type, ...]: ...
def getcallargs(func, *args, **kwds) -> Dict[str, Any]: ...

# The interpreter stack

Traceback = NamedTuple(
    'Traceback',
    [
        ('filename', str),
        ('lineno', int),
        ('function', str),
        ('code_context', Optional[List[str]]),
        ('index', Optional[int]),
    ]
)

_FrameInfo = Tuple[FrameType, str, int, str, Optional[List[str]], Optional[int]]

def getouterframes(frame: FrameType, context: int = ...) -> List[_FrameInfo]: ...
def getframeinfo(frame: Union[FrameType, TracebackType], context: int = ...) -> Traceback: ...
def getinnerframes(traceback: TracebackType, context: int = ...) -> List[_FrameInfo]: ...
def getlineno(frame: FrameType) -> int: ...

def currentframe(depth: int = ...) -> FrameType: ...
def stack(context: int = ...) -> List[_FrameInfo]: ...
def trace(context: int = ...) -> List[_FrameInfo]: ...

Attribute = NamedTuple('Attribute', [('name', str),
                                     ('kind', str),
                                     ('defining_class', type),
                                     ('object', object),
                                     ])

def classify_class_attrs(cls: type) -> List[Attribute]: ...
