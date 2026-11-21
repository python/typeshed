from _typeshed import FloatInt
from typing import Final

__version__: Final[str]
inch: Final[FloatInt]
cm: Final[FloatInt]
mm: Final[FloatInt]
pica: Final[FloatInt]

def toLength(s: str) -> float: ...
