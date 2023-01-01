import datetime
from _typeshed import Incomplete

from pyasn1.type import char

class ObjectDescriptor(char.GraphicString):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete

class TimeMixIn:
    class FixedOffset(datetime.tzinfo):
        def __init__(self, offset: int = ..., name: str = ...) -> None: ...
        def utcoffset(self, dt): ...
        def tzname(self, dt): ...
        def dst(self, dt): ...
    UTC: Incomplete
    @property
    def asDateTime(self): ...
    @classmethod
    def fromDateTime(cls, dt): ...

class GeneralizedTime(char.VisibleString, TimeMixIn):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete

class UTCTime(char.VisibleString, TimeMixIn):
    __doc__: Incomplete
    tagSet: Incomplete
    typeId: Incomplete
