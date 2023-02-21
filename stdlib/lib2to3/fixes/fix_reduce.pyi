from lib2to3 import fixer_base
from typing import ClassVar
from typing_extensions import Literal, LiteralString

class FixReduce(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    order: ClassVar[Literal["pre"]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results) -> None: ...
