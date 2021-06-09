from typing import Any
from typing_extensions import Literal

DEFAULT_STRATEGY: Literal[0]
FILTERED: Literal[1]
HUFFMAN_ONLY: Literal[2]
RLE: Literal[3]
FIXED: Literal[4]

def __getattr__(__name: str) -> Any: ...  # incomplete
