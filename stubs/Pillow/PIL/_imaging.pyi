from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any
from typing_extensions import Literal

DEFAULT_STRATEGY: Literal[0]
FILTERED: Literal[1]
HUFFMAN_ONLY: Literal[2]
RLE: Literal[3]
FIXED: Literal[4]

class _PixelAccess:
    # As well as the C extension source, this is also documented at
    # Pillow's docs/reference/PixelAccess.rst, e.g.
    # https://github.com/python-pillow/Pillow/blob/main/docs/reference/PixelAccess.rst
    # The name is prefixed here with an underscore as PixelAccess is not
    # runtime-importable.

    def __setitem__(self, xy, color) -> None: ...
    def __getitem__(self, xy) -> Any: ...
    def putpixel(self, xy, color) -> None: ...
    def getpixel(self, xy) -> Any: ...

class _Path:
    def __getattr__(self, item: str) -> Incomplete: ...

def path(__x: Sequence[tuple[float, float]] | Sequence[float]) -> _Path: ...
def __getattr__(__name: str) -> Incomplete: ...
