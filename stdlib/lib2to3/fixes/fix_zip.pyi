from typing import ClassVar
from typing_extensions import Literal, LiteralString

from .. import fixer_base

class FixZip(fixer_base.ConditionalFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    skip_on: ClassVar[Literal["future_builtins.zip"]]
    def transform(self, node, results): ...
