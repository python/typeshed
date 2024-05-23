from typing import Final

__version__: str
inch: Final[float]
cm: Final[float]
mm: Final[float]
pica: Final[float]

def toLength(s: str) -> float: ...
