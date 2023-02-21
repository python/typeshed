from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base
from ..pytree import Leaf

class FixWsComma(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[False]]
    explicit: bool
    PATTERN: ClassVar[LiteralString]
    COMMA: Leaf
    COLON: Leaf
    SEPS: tuple[Leaf, Leaf]
    def transform(self, node, results): ...
