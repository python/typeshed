from _typeshed import FloatInt
from typing import NamedTuple, TypeAlias

_Quadruple: TypeAlias = tuple[FloatInt, FloatInt, FloatInt, FloatInt]

class BoundingBox(NamedTuple):
    left: FloatInt
    bottom: FloatInt
    right: FloatInt
    top: FloatInt

def disjoint_bounds(bounds1: BoundingBox | _Quadruple, bounds2: BoundingBox | _Quadruple) -> bool: ...
