from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixThrow(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results) -> None: ...
