from lib2to3 import fixer_base
from typing import ClassVar
from typing_extensions import Literal, LiteralString

class FixItertoolsImports(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[LiteralString]
    def transform(self, node, results): ...
