from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixBuffer(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    explicit: bool
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results) -> None: ...
