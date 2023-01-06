from _typeshed import Incomplete
from collections.abc import Sequence
from typing_extensions import Literal

DEFAULT_STRATEGY: Literal[0]
FILTERED: Literal[1]
HUFFMAN_ONLY: Literal[2]
RLE: Literal[3]
FIXED: Literal[4]

class PixelAccess:
    # As well as the C extension source, this is also documented at
    # Pillow's docs/reference/PixelAccess.rst, e.g.
    # https://github.com/python-pillow/Pillow/blob/main/docs/reference/PixelAccess.rst
    def __getattr__(self, item: str) -> Incomplete: ...

class _Path:
    def __getattr__(self, item: str) -> Incomplete: ...

def path(__x: Sequence[tuple[float, float]] | Sequence[float]) -> _Path: ...
def __getattr__(__name: str) -> Incomplete: ...
