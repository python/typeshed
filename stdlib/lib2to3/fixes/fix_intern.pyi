from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixIntern(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    order: ClassVar[Literal["pre"]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
