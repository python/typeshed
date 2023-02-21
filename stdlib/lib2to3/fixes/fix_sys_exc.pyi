from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixSysExc(fixer_base.BaseFix):
    exc_info: ClassVar[list[str]]
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
