from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixFilter(fixer_base.ConditionalFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    skip_on: ClassVar[Literal["future_builtins.filter"]]
    def transform(self, node, results): ...
