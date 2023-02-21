from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

iter_exempt: set[str]

class FixDict(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
    P1: ClassVar[LiteralString]
    p1: ClassVar[Incomplete]
    P2: ClassVar[LiteralString]
    p2: ClassVar[Incomplete]
    def in_special_context(self, node, isiter): ...
