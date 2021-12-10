from typing import Any

from pyasn1.type.univ import Integer, OctetString, Sequence

MAXINT: Any
rangeInt0ToMaxConstraint: Any

class Integer0ToMax(Integer):
    subtypeSpec: Any

class Size(Integer0ToMax): ...
class Cookie(OctetString): ...

class RealSearchControlValue(Sequence):
    componentType: Any

def paged_search_control(criticality: bool = ..., size: int = ..., cookie: Any | None = ...): ...
