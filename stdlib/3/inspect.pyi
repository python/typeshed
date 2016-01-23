# Stubs for inspect

from typing import Any, Tuple, List, Dict, Callable, NamedTuple
from types import FrameType

_object = object

def getmembers(obj: object, predicate: Callable[[Any], bool]) -> List[Tuple[str, object]]: ...

def isclass(obj: object) -> bool: ...

# namedtuple('Attribute', 'name kind defining_class object')
class Attribute(tuple):
    name = ...  # type: str
    kind = ...  # type: str
    defining_class = ...  # type: type
    object = ...  # type: _object

def classify_class_attrs(cls: type) -> List[Attribute]: ...

def cleandoc(doc: str) -> str: ...

def getsourcelines(obj: object) -> Tuple[List[str], int]: ...

ArgSpec = NamedTuple('ArgSpec', [('args', List[str]),
                                 ('varargs', str),
                                 ('keywords', str),
                                 ('defaults', tuple),
                                 ])

def getargspec(func: object) -> ArgSpec: ...

FullArgSpec = NamedTuple('FullArgSpec', [('args', List[str]),
                                         ('varargs', str),
                                         ('varkw', str),
                                         ('defaults', tuple),
                                         ('kwonlyargs', List[str]),
                                         ('kwonlydefaults', Dict[str, Any]),
                                         ('annotations', Dict[str, Any]),
                                         ])

def getfullargspec(func: object) -> FullArgSpec: ...

def stack() -> List[Tuple[FrameType, str, int, str, List[str], int]]: ...
