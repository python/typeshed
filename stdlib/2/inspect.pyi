from types import TracebackType, FrameType, ModuleType
from typing import Any, Dict, Callable, List, Optional, Tuple, Union, NamedTuple, Type

# Types and members
ModuleInfo = NamedTuple('ModuleInfo', [('name', str),
                                       ('suffix', str),
                                       ('mode', str),
                                       ('module_type', int),
                                       ])
def getmembers(
    object: object,
    predicate: Callable[[Any], bool] = ...
) -> List[Tuple[str, Any]]: ...
def getmoduleinfo(path: str) -> Optional[ModuleInfo]: ...
def getmodulename(path: str) -> Optional[str]: ...

def ismodule(object: object) -> bool: ...
def isclass(object: object) -> bool: ...
def ismethod(object: object) -> bool: ...
def isfunction(object: object) -> bool: ...
def isisgeneratorfunction(object: object) -> bool: ...
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
def getdoc(object: object) -> str: ...
def getcomments(object: object) -> str: ...
def getfile(object: object) -> str: ...
def getmodule(object: object) -> ModuleType: ...
def getsourcefile(object: object) -> str: ...
# TODO restrict to "module, class, method, function, traceback, frame,
# or code object"
def getsourcelines(object: object) -> Tuple[List[str], int]: ...
# TODO restrict to "a module, class, method, function, traceback, frame,
# or code object"
def getsource(object: object) -> str: ...
def cleandoc(doc: str) -> str: ...

# Classes and functions
def getclasstree(classes: List[type], unique: bool = ...) -> List[
    Union[Tuple[type, Tuple[type, ...]], list]]: ...

ArgSpec = NamedTuple('ArgSpec', [('args', List[str]),
                                 ('varargs', Optional[str]),
                                 ('keywords', Optional[str]),
                                 ('defaults', tuple),
                                 ])

def getargspec(func: object) -> ArgSpec: ...
def getargvalues(frame: FrameType) -> ArgSpec: ...
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
        ('code_context', List[str]),
        ('index', int),
    ]
)

_FrameRecord = Tuple[FrameType, str, int, str, List[str], int]

def getouterframes(frame: FrameType, context: int = ...) -> List[FrameType]: ...
def getframeinfo(frame: Union[FrameType, TracebackType], context: int = ...) -> Traceback: ...
def getinnerframes(traceback: TracebackType, context: int = ...) -> List[FrameType]: ...

def currentframe(depth: int = ...) -> FrameType: ...
def stack(context: int = ...) -> List[_FrameRecord]: ...
def trace(context: int = ...) -> List[_FrameRecord]: ...
