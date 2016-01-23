# TODO incomplete
from typing import Any, List, Tuple, NamedTuple

def isgenerator(object: Any) -> bool: ...

class _Frame:
    ...
_FrameRecord = Tuple[_Frame, str, int, str, List[str], int]

def currentframe() -> _FrameRecord: ...
def stack(context: int = ...) -> List[_FrameRecord]: ...

ArgSpec = NamedTuple('ArgSpec', [('args', List[str]),
                                 ('varargs', str),
                                 ('keywords', str),
                                 ('defaults', tuple),
                                 ])

def getargspec(func: object) -> ArgSpec: ...
