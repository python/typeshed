from _typeshed import Unused
from collections.abc import Sequence

from matplotlib.typing import ColorType

__all__ = ["dogplot", "palplot"]

def palplot(pal: Sequence[ColorType], size: int = 1) -> None: ...
def dogplot(*_: Unused, **__: Unused) -> None: ...
